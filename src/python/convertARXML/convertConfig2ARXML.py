import os
import string
import sys
from lxml import etree as etree_
from . import autosar_config_api as supermod_config
from . import autosar_all_api as supermod_all
from . import utils4ParseARXML 
#import autosar_config_api0519 as supermod_config
#import autosar_all_api as supermod_all
#import utils4ParseARXML 
import uuid
import re as re_
import copy
from datetime import datetime
Tag_pattern_ = re_.compile(r'({.*})?(.*)')

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc



#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True
id_name_maps_config={

}
name_id_maps_config={

}

irv_wirte_runnable_maps_config={

}
irv_read_runnable_maps_config={

}

idport_period_maps_config={}
idport_portname_interfacename_elementname_maps_config={}
name_swcComponent_global=""
internal_behavior_qualified_name_global=""
package_global=""
datatype_package_global=""
interface_package_global=""


def get_root_tag(node):
    tag = supermod_config.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod_config.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod_config, tag):
        rootClass = getattr(supermod_config, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod_config.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj



path2AR_Package={}


namespaces = {'ns': 'http://autosar_configuration.wumbuk'}

#如果path以“/”开头，则去掉
def defiltePath(path):
    if path[0]=='/':
        path=path[1:]
    return path

#创建包，同时更新path2AR_Package这个字典
def createPackageIter(rootNode,rootNodePath,pathList):
    global path2AR_Package
    if len(pathList)==0:
        return
    else:
        path=pathList[0]
        pathList.pop(0)
        path=rootNodePath+path
        if path not in path2AR_Package:
            AR_PACKAGES=rootNode.get_AR_PACKAGES()
            if AR_PACKAGES is None:
                AR_PACKAGES=supermod_all.AR_PACKAGESType.factory()
                rootNode.set_AR_PACKAGES(AR_PACKAGES)

            AR_PACKAGE=supermod_all.AR_PACKAGE.factory()
            shortName=supermod_all.IDENTIFIER.factory()
            shortName.set_valueOf_(path.split("/")[-1])
            AR_PACKAGE.set_SHORT_NAME(shortName)
            AR_PACKAGES.add_AR_PACKAGE(AR_PACKAGE)
            path2AR_Package[path]=AR_PACKAGE
            createPackageIter(AR_PACKAGE,path+"/",pathList)
        else:
            createPackageIter(path2AR_Package[path],path+"/",pathList)


#先初始化path2AR_Package
def init_path2AR_Package(rootNode):
    #每次调用，手动将path2AR_Package中的值置空
    global path2AR_Package
    path2AR_Package={}
    packageList=[]
    #packageList.append("/DataTypes/SwBaseTypes")
    packageList.append("/Timing")
    senderReceiverInterfaces=rootNode.xpath('//ns:Sender-Receiver-Interface',namespaces=namespaces)
    for senderReceiverInterface in senderReceiverInterfaces:
        temp=senderReceiverInterface.attrib["PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
    swAddrMethodPrototypes=rootNode.xpath('//ns:SwAddrMethod-Prototype',namespaces=namespaces)
    for swAddrMethodPrototype in swAddrMethodPrototypes:
        temp=swAddrMethodPrototype.attrib["PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
    packagePaths=rootNode.xpath('//ns:Package-Paths',namespaces=namespaces)
    for packagePath in packagePaths:
        temp=packagePath.attrib["INTERFACE-PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
        temp=packagePath.attrib["DATATYPE-PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
    additionalPackages=rootNode.xpath('//ns:Additional-Packages',namespaces=namespaces)
    for additionalPackage in additionalPackages:
        temp=additionalPackage.attrib["SWBASETYPE-PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
        temp=additionalPackage.attrib["CONSTANT-SPECIFICATION-PACKAGE"]
        if temp not in packageList:
            packageList.append(temp)
    componentXMLOptions=rootNode.xpath('//ns:Component-XML-Options',namespaces=namespaces)
    for componentXMLOption in componentXMLOptions:
        temp=componentXMLOption.attrib["Package"]
        if temp not in packageList:
            packageList.append(temp)
        temp=componentXMLOption.attrib["Implementation-Qualified-Name"]
        temp="/".join(temp.split("/"))
        if temp not in packageList:
            packageList.append(temp)
        internal_behavior=componentXMLOption.attrib["Internal-Behavior-Qualified-Name"]
        temp=internal_behavior
        if len(temp.split("/"))>2:
            temp="/".join(temp.split("/")[:-2])
        if temp not in packageList:
            packageList.append(temp)
    AUTOSAR=supermod_all.AUTOSAR.factory()
    path2AR_Package["/"]=AUTOSAR
    for packagePath in packageList:
        pathSplit=defiltePath(packagePath).split("/")
        createPackageIter(AUTOSAR,"/",pathSplit)
    if len(internal_behavior.split("/"))>2:
        application_name=internal_behavior.split("/")[-2]
        internal_name=internal_behavior.split("/")[-1]
        ar_package_internal=path2AR_Package["/".join(internal_behavior.split("/")[:-2])]
        if ar_package_internal.get_ELEMENTS() is None:
            ar_package_internal.set_ELEMENTS(supermod_all.ELEMENTSType.factory())
        application_sw_component_all=supermod_all.APPLICATION_SW_COMPONENT_TYPE.factory()
        application_sw_component_all.set_UUID(str(uuid.uuid4()))
        ar_package_internal.get_ELEMENTS().add_APPLICATION_SW_COMPONENT_TYPE(application_sw_component_all)
        path2AR_Package["/".join(internal_behavior.split("/")[:-1])]=application_sw_component_all
        short_name_all=supermod_all.IDENTIFIER.factory()    
        short_name_all.set_valueOf_(application_name)
        application_sw_component_all.set_SHORT_NAME(short_name_all)







id2NodeMap={}

#初始化本地配置文件中的id_name的映射关系，source为传入的文件
#初始化两个字典，一个是id_name_maps_config，另一个是name_id_maps_config
#还有一个是 id2NodeMap
def init_id_name_mappings(node):
    attrs=node.attrib
    ID=attrs.get("ID")
    NAME=attrs.get("NAME")
    if ID and NAME:
        id_name_maps_config[ID]=NAME
        name_id_maps_config[NAME]=ID
        id2NodeMap[ID]=node
    UUID=attrs.get("UUID")
    if UUID:
        id2NodeMap[UUID]=node
    for child in node:
        init_id_name_mappings(child)

#初始化idport_period_mappings中的值
def init_idport_period_mappings(node):
    name_node=Tag_pattern_.match(node.tag).groups()[-1]
    if name_node!="ReceiverPort-Prototype":
        for child in node:
            init_idport_period_mappings(child)
    else:
        id=supermod_config.find_attr_value_("ID",node)
        for child_ReceiverPort_Prototype in node:
            name_child_ReceiverPort_Prototype=Tag_pattern_.match(child_ReceiverPort_Prototype.tag).groups()[-1]
            if name_child_ReceiverPort_Prototype=="Period":
                period=supermod_config.get_all_text_(child_ReceiverPort_Prototype)
                idport_period_maps_config[id]=period

#初始化idport_portname_interfacename_elementname_maps_config的值
def init_idport_portname_interfacename_elementname_mappings(node):
    name_node=Tag_pattern_.match(node.tag).groups()[-1]
    if name_node=="ReceiverPort-Prototype":
        for child_receiverPort_prototye in node:
            name_child_receiverPort_prototye=Tag_pattern_.match(child_receiverPort_prototye.tag).groups()[-1]
            if name_child_receiverPort_prototye=="ReceiverPort-Specs":
                id_port=supermod_config.find_attr_value_("ID",node)
                name_port=supermod_config.find_attr_value_("NAME",node)
                interface_ref_id=supermod_config.find_attr_value_("INTERFACE-REF-ID",node)
                name_interface=id_name_maps_config[interface_ref_id]
                name_element_list=[]
                for child_receiverport_specs in child_receiverPort_prototye:
                    name_child_receiverport_specs=Tag_pattern_.match(child_receiverport_specs.tag).groups()[-1]
                    if name_child_receiverport_specs=="Nonqueued-Receiver-Com-Spec":
                        element_ref_id=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_receiverport_specs)
                        name_element=id_name_maps_config[element_ref_id]
                        name_element_list.append(name_element)
                idport_portname_interfacename_elementname_maps_config[id_port]=(name_port,name_interface,name_element_list)
    elif name_node=="SenderPort-Prototype":
        for child_senderPort_prototype in node:
            name_child_senderPort_prototype=Tag_pattern_.match(child_senderPort_prototype.tag).groups()[-1]
            if name_child_senderPort_prototype=="SenderPort-Specs":
                id_port=supermod_config.find_attr_value_("ID",node)
                name_port=supermod_config.find_attr_value_("NAME",node)
                interface_ref_id=supermod_config.find_attr_value_("INTERFACE-REF-ID",node)
                name_interface=id_name_maps_config[interface_ref_id]
                name_element_list=[]
                for child_senderPort_specs in child_senderPort_prototype:
                    name_child_senderPort_specs=Tag_pattern_.match(child_senderPort_specs.tag).groups()[-1]
                    if name_child_senderPort_specs=="Nonqueued-Sender-Com-Spec":
                        element_ref_id=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_senderPort_specs)
                        name_element=id_name_maps_config[element_ref_id]
                        name_element_list.append(name_element)
                idport_portname_interfacename_elementname_maps_config[id_port]=(name_port,name_interface,name_element_list)
    else:
        for child in node:
            init_idport_portname_interfacename_elementname_mappings(child)

#初始化Package-Paths中的DATATYPE-PACKAGE和INTERFACE-PACKAGE
def init_package_paths(node):
    global datatype_package_global
    global interface_package_global
    name_node=Tag_pattern_.match(node.tag).groups()[-1]
    if name_node!="Package-Paths":
        for child in node:
            init_package_paths(child)
    else:
        datatype_package_global=supermod_config.find_attr_value_("DATATYPE-PACKAGE",node)  #不一定能不能改到
        interface_package_global=supermod_config.find_attr_value_("INTERFACE-PACKAGE",node)

def init_swc_component_config(node):
    global name_swcComponent_global
    global internal_behavior_qualified_name_global
    global package_global
    name_node=Tag_pattern_.match(node.tag).groups()[-1]
    if name_node=="SwcComponent":
        name_swcComponent_global=supermod_config.find_attr_value_("NAME",node)
        for child in node:                  #不能找到SwcComponent后就不能再往后了
            init_swc_component_config(child)
    elif name_node=="Component-XML-Options":
        internal_behavior_qualified_name_global=supermod_config.find_attr_value_("Internal-Behavior-Qualified-Name",node)
        if (internal_behavior_qualified_name_global[0]=='/'):
            internal_behavior_qualified_name_global=internal_behavior_qualified_name_global[1:]
        package_global=supermod_config.find_attr_value_("Package",node)
        if (package_global[0]=='/'):
            package_global=package_global[1:]
    else:
        for child in node:
            init_swc_component_config(child)



#从config文件转换为相对应的dataType文件
#sourceFile表示本地的配置文件，targetFile表示要写的目标文件
#主要就是处理的SwAddrMethods的内容，将其中的软件地址计算方法转到ARXML文件中
def convertConfig2DataType(sourceFile,targetFile):
    parser = None
    doc = parsexml_(sourceFile, parser)
    source=doc.getroot()
    #root_obj_all=supermod_all.AUTOSAR.factory()
    #ar_packages_all=supermod_all.AR_PACKAGESType.factory()
    #root_obj_all.set_AR_PACKAGES(ar_packages_all)
    #ar_package_all=supermod_all.AR_PACKAGE.factory()
    #ar_packages_all.add_AR_PACKAGE(ar_package_all)


    swBaseTypePackage="/DataTypes/SwBaseTypes"
    additionalPaths=source.xpath('//ns:Additional-Packages',namespaces=namespaces)
    for additionalPath in additionalPaths:
        swBaseTypePackage=additionalPath.attrib["SWBASETYPE-PACKAGE"]
    #1.处理IMPLEMENTATION-DATA-TYPE标签
    datatype_package_path="/DataTypes"
    temp=source.xpath('//ns:Package-Paths',namespaces=namespaces)[0].attrib["DATATYPE-PACKAGE"]
    if temp!="":
        datatype_package_path=temp
    datatype_package=path2AR_Package[datatype_package_path]
    elements_all_1=supermod_all.ELEMENTSType.factory()
    datatype_package.set_ELEMENTS(elements_all_1)
    #implementation_data_type_all=supermod_all.IMPLEMENTATION_DATA_TYPE.factory()
    #implementation_data_type_all.set_UUID(str(uuid.uuid4()))
    
    implementation_data_type_list=source.xpath('//ns:IMPLEMENTATION-DATA-TYPE',namespaces=namespaces)
    for implementation_data_type in implementation_data_type_list:
        implementation_data_type_all=supermod_all.IMPLEMENTATION_DATA_TYPE.factory()
        implementation_data_type_all.build(implementation_data_type)
        
        base_type_ref_list_config=implementation_data_type.xpath('.//ns:BASE-TYPE-REF',namespaces=namespaces)
        implementation_data_type_ref_list_config=implementation_data_type.xpath('.//ns:IMPLEMENTATION-DATA-TYPE-REF',namespaces=namespaces)
        if len(base_type_ref_list_config):
            base_type_ref_all=base_type_ref_list_config[0]
            base_type_ref_value_config=base_type_ref_all.text
            base_type_ref_all=implementation_data_type_all.get_SW_DATA_DEF_PROPS().get_SW_DATA_DEF_PROPS_VARIANTS().get_SW_DATA_DEF_PROPS_CONDITIONAL()[0].get_BASE_TYPE_REF()
            base_type_ref_all.set_valueOf_(swBaseTypePackage+"/"+base_type_ref_value_config.split("/")[-1])
        
        elif len(implementation_data_type_ref_list_config):
            #implementation_data_type_all.get_SUB_ELEMENTS().get_IMPLEMENTATION_DATA_TYPE_ELEMENT()[0].get_ARRAY_SIZE().set_valueOf_(0)
            implementation_data_type_ref_all=implementation_data_type_ref_list_config[0]
            implementation_data_type_ref_value_config=implementation_data_type_ref_all.text
            implementation_data_type_ref_all=implementation_data_type_all.get_SUB_ELEMENTS().get_IMPLEMENTATION_DATA_TYPE_ELEMENT()[0].get_SW_DATA_DEF_PROPS().get_SW_DATA_DEF_PROPS_VARIANTS().get_SW_DATA_DEF_PROPS_CONDITIONAL()[0].get_IMPLEMENTATION_DATA_TYPE_REF()
            implementation_data_type_ref_all.set_valueOf_(datatype_package_path+"/"+implementation_data_type_ref_value_config.split("/")[-1])
        
        elements_all_1.add_IMPLEMENTATION_DATA_TYPE(implementation_data_type_all)



    #2.处理CONSTANT-SPECIFICATIONS标签
    constant_specification_package_path="/DataTypes/Constant-Specifications"
    temp=source.xpath('//ns:Additional-Packages',namespaces=namespaces)[0].attrib["CONSTANT-SPECIFICATION-PACKAGE"]
    if temp!=constant_specification_package_path:
        constant_specification_package_path=temp
    constant_specification_package=path2AR_Package[constant_specification_package_path]
    elements_all_2=supermod_all.ELEMENTSType.factory()
    constant_specification_package.set_ELEMENTS(elements_all_2)
    constant_specification_list=source.xpath('.//ns:CONSTANT-SPECIFICATION',namespaces=namespaces)
    for constant_specification in constant_specification_list:
        constant_specification_all=supermod_all.CONSTANT_SPECIFICATION.factory()
        constant_specification_all.build(constant_specification)
        constant_ref_list_config=constant_specification.xpath('.//ns:CONSTANT-REF',namespaces=namespaces)
        if len(constant_ref_list_config):
            for i,constant_ref in enumerate(constant_ref_list_config):
                constant_ref_value_config=constant_ref.text
                constant_ref_all=constant_specification_all.get_VALUE_SPEC().get_ARRAY_VALUE_SPECIFICATION().get_ELEMENTS().get_CONSTANT_REFERENCE()[i].get_CONSTANT_REF()
                constant_ref_all.set_valueOf_(constant_specification_package_path+"/"+constant_ref_value_config.split("/")[-1])
        elements_all_2.add_CONSTANT_SPECIFICATION(constant_specification_all)

    #3.处理SW-BASE-TYPE标签


    swBaseTypePackage=path2AR_Package[swBaseTypePackage]
    elements=swBaseTypePackage.get_ELEMENTS()
    if elements is None:
        elements=supermod_all.ELEMENTSType.factory()
        swBaseTypePackage.set_ELEMENTS(elements)
    sw_base_type_list=source.xpath('//ns:SW-BASE-TYPE',namespaces=namespaces)
    for sw_base_type in sw_base_type_list:
        sw_base_type_all=supermod_all.SW_BASE_TYPE.factory()
        sw_base_type_all.build(sw_base_type)
        elements.add_SW_BASE_TYPE(sw_base_type_all)
    

    #ar_package_all_3=supermod_all.AR_PACKAGE.factory()
    #ar_packages_all_2.add_AR_PACKAGE(ar_package_all_3)
    #short_name_all_5=supermod_all.IDENTIFIER.factory()   #SwBaseTypes的SHORT-NAME
    #short_name_all_5.set_valueOf_("SwBaseTypes")
    #ar_package_all_3.set_SHORT_NAME(short_name_all_5)
    #ar_elements_all_3=supermod_all.ELEMENTSType.factory()
    #ar_package_all_3.set_ELEMENTS(ar_elements_all_3)
    '''
    ar_sw_base_type_all=supermod_all.SW_BASE_TYPE.factory()
    ar_sw_base_type_all.set_UUID(str(uuid.uuid4()))
    elements.add_SW_BASE_TYPE(ar_sw_base_type_all)
    short_name_all_6=supermod_all.IDENTIFIER.factory()
    short_name_all_6.set_valueOf_("float64")
    ar_sw_base_type_all.set_SHORT_NAME(short_name_all_6)
    category_all_2=supermod_all.CATEGORY_STRING.factory()
    category_all_2.set_valueOf_("FIXED_LENGTH")
    ar_sw_base_type_all.set_CATEGORY(category_all_2)
    base_type_size_all=supermod_all.POSITIVE_INTEGER.factory()
    base_type_size_all.set_valueOf_(64)
    ar_sw_base_type_all.set_BASE_TYPE_SIZE(base_type_size_all)
    base_type_encoding_all=supermod_all.BASE_TYPE_ENCODING_STRING.factory()
    base_type_encoding_all.set_valueOf_("IEEE754")
    ar_sw_base_type_all.set_BASE_TYPE_ENCODING(base_type_encoding_all)
    native_declaration_all=supermod_all.NATIVE_DECLARATION_STRING.factory()
    native_declaration_all.set_valueOf_("float64")
    ar_sw_base_type_all.set_NATIVE_DECLARATION(native_declaration_all)
    '''
    #1. <AR-PACKAGE>-><SHORT-NAME>
    #short_name_all_1=supermod_all.IDENTIFIER.factory() #最上层的SHORT-NAME
    #short_name_all_1.set_valueOf_(defiltePath(datatype_package_path))
    #datatype_package.set_SHORT_NAME(short_name_all_1)


    #2. <AR-PACKAGE>-><ELEMENTS>



    '''
    short_name_all_2=supermod_all.IDENTIFIER.factory() #第二个SHORT-NAME
    short_name_all_2.set_valueOf_("Double")
    implementation_data_type_all.set_SHORT_NAME(short_name_all_2)
    category_all_1=supermod_all.CATEGORY_STRING.factory()
    category_all_1.set_valueOf_("VALUE")
    implementation_data_type_all.set_CATEGORY(category_all_1)
    sw_data_def_props_all=supermod_all.SW_DATA_DEF_PROPS.factory()
    implementation_data_type_all.set_SW_DATA_DEF_PROPS(sw_data_def_props_all)
    sw_data_def_props_variants_all=supermod_all.SW_DATA_DEF_PROPS_VARIANTSType.factory()
    sw_data_def_props_all.set_SW_DATA_DEF_PROPS_VARIANTS(sw_data_def_props_variants_all)
    sw_data_def_props_conditional_all=supermod_all.SW_DATA_DEF_PROPS_CONDITIONAL.factory()
    sw_data_def_props_variants_all.add_SW_DATA_DEF_PROPS_CONDITIONAL(sw_data_def_props_conditional_all)
    base_type_ref_all=supermod_all.BASE_TYPE_REFType.factory()

    base_type_ref_value="/DataTypes/SwBaseTypes/float64"
    additionalPaths=source.xpath('//ns:Additional-Packages',namespaces=namespaces)
    for additionalPath in additionalPaths:
        swBaseTypePackage=additionalPath.attrib["SWBASETYPE-PACKAGE"]
        base_type_ref_value=swBaseTypePackage+"/float64"
        
    base_type_ref_all.set_valueOf_(base_type_ref_value)
    base_type_ref_all.set_DEST(supermod_all.SW_BASE_TYPE__SUBTYPES_ENUM.SWBASETYPE)
    sw_data_def_props_conditional_all.set_BASE_TYPE_REF(base_type_ref_all)
    '''     
    #return datatype_package


    #3. <AR-PACKAGE>-><AR-PACKAGES>
    #ar_packages_all_2=supermod_all.AR_PACKAGESType.factory()
    #datatype_package.set_AR_PACKAGES(ar_packages_all_2)
    #ar_package_all_2=supermod_all.AR_PACKAGE.factory()
    #ar_packages_all_2.add_AR_PACKAGE(ar_package_all_2)
    #short_name_all_3=supermod_all.IDENTIFIER.factory()
    #short_name_all_3.set_valueOf_("SwAddrMethods")
    #ar_package_all_2.set_SHORT_NAME(short_name_all_3)


    #elements_all_2=supermod_all.ELEMENTSType.factory()
    #ar_package_all_2.set_ELEMENTS(elements_all_2)
    #4 循环着对组件计算方法进行设置
    for child_autosar in source:
        name_child_autosar=Tag_pattern_.match(child_autosar.tag).groups()[-1]
        if name_child_autosar=="AUTOSAR-Dictionary":
            for autosar_dictionary_child in child_autosar:
                name_autosar_dictionary=Tag_pattern_.match(autosar_dictionary_child.tag).groups()[-1]
                if name_autosar_dictionary == 'Methods':
                    for child_methods in autosar_dictionary_child:
                        name_child_methods=Tag_pattern_.match(child_methods.tag).groups()[-1]
                        if name_child_methods=='SwAddrMethods':
                            for child_swAddrMethods in child_methods:
                                name=supermod_all.find_attr_value_('NAME',child_swAddrMethods)
                                section_type=supermod_all.find_attr_value_('SECTION-TYPE',child_swAddrMethods)
                                export_xml_file=supermod_all.find_attr_value_('EXPORT-XML-FILE',child_swAddrMethods) #这一块，需要看看怎么利用
                                package=supermod_all.find_attr_value_('PACKAGE',child_swAddrMethods)
                                swAddrMethodPackage=path2AR_Package[package]
                                elements=swAddrMethodPackage.get_ELEMENTS()
                                if elements is None:
                                    elements=supermod_all.ELEMENTSType.factory()
                                    swAddrMethodPackage.set_ELEMENTS(elements)
                                
                                sw_addr_method_all=supermod_all.SW_ADDR_METHOD.factory()
                                sw_addr_method_all.set_UUID(str(uuid.uuid4()))
                                short_name_all_4=supermod_all.IDENTIFIER.factory()
                                short_name_all_4.set_valueOf_(name)
                                sw_addr_method_all.set_SHORT_NAME(short_name_all_4)
                                section_type_all=supermod_all.MEMORY_SECTION_TYPE.factory()
                                section_type_all.set_valueOf_(section_type)
                                sw_addr_method_all.set_SECTION_TYPE(section_type_all)
                                elements.add_SW_ADDR_METHOD(sw_addr_method_all)
    #return datatype_package


    return datatype_package














#从config文件转换为相对应的interface文件
#source表示的是本地的配置文件，target表示要写的目标interface文件
def convertConfig2Interface(sourceFile,targetFile):
    parser = None
    doc = parsexml_(sourceFile, parser)
    source=doc.getroot()
    #root_obj_all=supermod_all.AUTOSAR.factory()
    #ar_packages_all=supermod_all.AR_PACKAGESType.factory()
    #root_obj_all.set_AR_PACKAGES(ar_packages_all)
    #ar_package_all=supermod_all.AR_PACKAGE.factory()
    #ar_packages_all.add_AR_PACKAGE(ar_package_all)

    interface_package_path="/Interfaces"
    temp=source.xpath('//ns:Package-Paths',namespaces=namespaces)[0].attrib["INTERFACE-PACKAGE"]
    if temp!="":
        interface_package_path=temp
    interface_package=path2AR_Package[interface_package_path]
    #return interface_package
    #1. <AR-PACKAGE>-><SHORT-NAME>
    #short_name_all_1=supermod_all.IDENTIFIER.factory() #最上层的SHORT-NAME
    #short_name_all_1.set_valueOf_("Interfaces")
    #ar_package_all.set_SHORT_NAME(short_name_all_1)

    #2. <AR-PACKAGE>-><ELEMENTS>
    #elements_all=supermod_all.ELEMENTSType.factory()
    #2.1 做sender-receiver-interface的设置
    sender_receiver_interface_list_all=[]
    for child_autosar in source:
        name_child_autosar=Tag_pattern_.match(child_autosar.tag).groups()[-1]
        if name_child_autosar=="AUTOSAR-Dictionary":
            for child_autosar_dictionary in child_autosar:
                name_child_autosar_dictionary=Tag_pattern_.match(child_autosar_dictionary.tag).groups()[-1]
                if name_child_autosar_dictionary=="Interfaces":
                    for child_interfaces in child_autosar_dictionary:
                        name_child_interfaces=Tag_pattern_.match(child_interfaces.tag).groups()[-1]
                        if name_child_interfaces=="S-R-Interfaces":
                            for child_s_r_interfaces in child_interfaces:
                                name_child_s_r_interfaces=Tag_pattern_.match(child_s_r_interfaces.tag).groups()[-1]
                                if name_child_s_r_interfaces=="Sender-Receiver-Interface":  #虽然s_r下面的都是这个类型，但是我们为了保证可扩展性，依然加上
                                    sender_receiver_interface_all=supermod_all.SENDER_RECEIVER_INTERFACE.factory()
                                    package_config=supermod_config.find_attr_value_('PACKAGE',child_s_r_interfaces)
                                    package_ar=path2AR_Package[package_config]
                                    elements_ar=package_ar.get_ELEMENTS()
                                    if elements_ar is None:
                                        elements_ar=supermod_all.ELEMENTSType.factory()
                                        package_ar.set_ELEMENTS(elements_ar)
                                    elements_ar.add_SENDER_RECEIVER_INTERFACE(sender_receiver_interface_all)
                                    sender_receiver_interface_all.set_UUID(str(uuid.uuid4()))
                                    name_attr_config=supermod_config.find_attr_value_('NAME',child_s_r_interfaces)
                                    short_name_all_2=supermod_all.IDENTIFIER.factory()
                                    short_name_all_2.set_valueOf_(name_attr_config)
                                    sender_receiver_interface_all.set_SHORT_NAME(short_name_all_2)
                                    is_service_all=supermod_all.BOOLEAN.factory()
                                    is_service_config=supermod_config.find_attr_value_('IS-SERVICE',child_s_r_interfaces)
                                    is_service_all.set_valueOf_(is_service_config) 
                                    sender_receiver_interface_all.set_IS_SERVICE(is_service_all)
                                    data_elements_all=supermod_all.DATA_ELEMENTSType.factory()
                                    variable_data_prototype_all_list=[]
                                    for child_sender_receiver_interface in child_s_r_interfaces:
                                        name_child_sender_receiver_interface=Tag_pattern_.match(child_sender_receiver_interface.tag).groups()[-1]
                                        if name_child_sender_receiver_interface=="Data-Elements":
                                            for child_data_elements in child_sender_receiver_interface:
                                                name_child_data_elements=Tag_pattern_.match(child_data_elements.tag).groups()[-1]
                                                if name_child_data_elements=="Variable-Data-Prototype":
                                                    variable_data_prototype_all=supermod_all.VARIABLE_DATA_PROTOTYPE.factory()
                                                    variable_data_prototype_all.set_UUID(str(uuid.uuid4()))
                                                    short_name_all_3=supermod_all.IDENTIFIER.factory()
                                                    name_variable_data_prototype_config=supermod_config.find_attr_value_('NAME',child_data_elements)
                                                    short_name_all_3.set_valueOf_(name_variable_data_prototype_config)
                                                    variable_data_prototype_all.set_SHORT_NAME(short_name_all_3)
                                                    category_all=supermod_all.CATEGORY_STRING.factory()
                                                    category_all.set_valueOf_("VALUE")
                                                    variable_data_prototype_all.set_CATEGORY(category_all)
                                                    sw_data_def_props_all=supermod_all.SW_DATA_DEF_PROPS.factory()
                                                    variable_data_prototype_all.set_SW_DATA_DEF_PROPS(sw_data_def_props_all)
                                                    sw_data_def_props_variants_all=supermod_all.SW_DATA_DEF_PROPS_VARIANTSType.factory()
                                                    sw_data_def_props_conditional_all_list=[]
                                                    sw_data_def_props_conditional_all=supermod_all.SW_DATA_DEF_PROPS_CONDITIONAL.factory()  
                                                    for child_variable_data_prototype in child_data_elements:
                                                        name_child_variable_data_prototype=Tag_pattern_.match(child_variable_data_prototype.tag).groups()[-1]
                                                        if name_child_variable_data_prototype=="Sw-Calibration-Access":
                                                            value_sw_calibration_access_config=supermod_config.get_all_text_(child_variable_data_prototype)
                                                            if value_sw_calibration_access_config=="ReadOnly":
                                                                value_sw_calibration_access_config="READ-ONLY"
                                                    
                                                            sw_calibration_access_all=supermod_all.SW_CALIBRATION_ACCESS_ENUM.factory()
                                                            sw_calibration_access_all.set_valueOf_(value_sw_calibration_access_config)
                                                            sw_data_def_props_conditional_all.set_SW_CALIBRATION_ACCESS(sw_calibration_access_all)
                                                        elif name_child_variable_data_prototype=="Type-Tref":
                                                            type_tref_all=supermod_all.TYPE_TREFType.factory()
                                                            type_tref_all.set_DEST(child_variable_data_prototype.attrib["DEST"])
                                                            value_type_tref_all=child_variable_data_prototype.text
                                                            type_tref_all.set_valueOf_(value_type_tref_all)
                                                            variable_data_prototype_all.set_TYPE_TREF(type_tref_all)
                                                        sw_impl_policy_all=supermod_all.SW_IMPL_POLICY_ENUM.factory()
                                                        sw_impl_policy_all.set_valueOf_("STANDARD")
                                                        sw_data_def_props_conditional_all.set_SW_IMPL_POLICY(sw_impl_policy_all)
                                                        
                                                    sw_data_def_props_conditional_all_list.append(sw_data_def_props_conditional_all)

                                                    sw_data_def_props_variants_all.set_SW_DATA_DEF_PROPS_CONDITIONAL(sw_data_def_props_conditional_all_list)
                                                    sw_data_def_props_all.set_SW_DATA_DEF_PROPS_VARIANTS(sw_data_def_props_variants_all)
                                                    
                                                    
                                                    
                                                    #temp=source.xpath('//ns:Package-Paths',namespaces=namespaces)[0].attrib["DATATYPE-PACKAGE"]
                                                    #if temp!="":
                                                    #    value_type_tref_all_prefix=temp
                                                    #value_type_tref_all_prefix=getDataTypePackage_fromConfig(source)
                                                    #value_type_tref_all=value_type_tref_all_prefix+"/Double"
                                                    
                                                    variable_data_prototype_all_list.append(variable_data_prototype_all)
                                    data_elements_all.set_VARIABLE_DATA_PROTOTYPE(variable_data_prototype_all_list)
                                    sender_receiver_interface_all.set_DATA_ELEMENTS(data_elements_all)
                                    #sender_receiver_interface_list_all.append(sender_receiver_interface_all)
   # elements_all.set_SENDER_RECEIVER_INTERFACE(sender_receiver_interface_list_all)
   # ar_package_all.set_ELEMENTS(elements_all)
    return interface_package






                                                                                      
                                                                                    


#从config文件转换为对应的component文件
def convertConfig2Component(sourceFile,targetFile):
    parser = None
    doc = parsexml_(sourceFile, parser)
    source=doc.getroot()
    #root_obj_all=supermod_all.AUTOSAR.factory()
    #ar_packages_all=supermod_all.AR_PACKAGESType.factory()
    #root_obj_all.set_AR_PACKAGES(ar_packages_all)
    #ar_package_all=supermod_all.AR_PACKAGE.factory()
    #ar_packages_all.add_AR_PACKAGE(ar_package_all)
    component_package_path="/Components"
    temp=source.xpath('//ns:Component-XML-Options',namespaces=namespaces)[0].attrib["Internal-Behavior-Qualified-Name"]
    temp="/".join(temp.split("/")[:-2])
    if temp!="":
        component_package_path=temp
    component_package=path2AR_Package[component_package_path]
    #component_package=copy.deepcopy(component_package)
    #component_package.set_AR_PACKAGES(None)
    #return component_package

    #1. <AR-PACKAGE>-><SHORT-NAME>
    #short_name_all_1=supermod_all.IDENTIFIER.factory() #最上层的SHORT-NAME
    #short_name_all_1.set_valueOf_("Components")
    #ar_package_all.set_SHORT_NAME(short_name_all_1)

    #2. <AR-PACKAGE>-><ELEMENTS>
    if component_package.get_ELEMENTS() is None:
        elements_all=supermod_all.ELEMENTSType.factory()
        component_package.set_ELEMENTS(elements_all)
    else:
        elements_all=component_package.get_ELEMENTS()
    if elements_all.get_APPLICATION_SW_COMPONENT_TYPE() is None:
        application_sw_component_type_all=supermod_all.APPLICATION_SW_COMPONENT_TYPE.factory()
        elements_all.add_APPLICATION_SW_COMPONENT_TYPE(application_sw_component_type_all)
        application_sw_component_type_all.set_UUID(str(uuid.uuid4()))
    else:
        application_sw_component_type_all=elements_all.get_APPLICATION_SW_COMPONENT_TYPE()[0]
    internal_behaviors_all=supermod_all.INTERNAL_BEHAVIORSType.factory()
    application_sw_component_type_all.set_INTERNAL_BEHAVIORS(internal_behaviors_all)
    swc_internal_behavior=supermod_all.SWC_INTERNAL_BEHAVIOR.factory()
    internal_behaviors_all.add_SWC_INTERNAL_BEHAVIOR(swc_internal_behavior)
    swc_internal_behavior.set_UUID(str(uuid.uuid4()))
    #return component_package
    #2.1 接下来进行遍历赋值
    for child_autosar in source:
        name_child_autosar=Tag_pattern_.match(child_autosar.tag).groups()[-1]
        if name_child_autosar=="AUTOSAR-Dictionary":
            for child_autosar_dictionary in child_autosar:
                name_child_autosar_dictionary=Tag_pattern_.match(child_autosar_dictionary.tag).groups()[-1]
                if name_child_autosar_dictionary=="AtomicComponents":
                    for child_atomicComponents in child_autosar_dictionary:
                        name_child_atomicComponents=Tag_pattern_.match(child_atomicComponents.tag).groups()[-1]
                        if name_child_atomicComponents=="SwcComponent":
                            value_swc_component_name=supermod_config.find_attr_value_("NAME",child_atomicComponents)
                            name_swcComponent_global=value_swc_component_name
                            short_name_all_2=supermod_all.IDENTIFIER.factory()
                            short_name_all_2.set_valueOf_(value_swc_component_name)
                            application_sw_component_type_all.set_SHORT_NAME(short_name_all_2)
                            for child_swc_component_config in child_atomicComponents:
                                name_child_swc_component_config=Tag_pattern_.match(child_swc_component_config.tag).groups()[-1]
                                if name_child_swc_component_config=="Component-XML-Options": #配置INTERNAL-BEHAVIORS中的SWC-INTERNAL-BEHAVIOR，新建立一个
                                    package_global=supermod_config.find_attr_value_("Package",child_swc_component_config)
                                    if (package_global[0]=='/'):
                                        package_global=package_global[1:]
                                    internal_behavior_qualified_name_config=supermod_config.find_attr_value_("Internal-Behavior-Qualified-Name",child_swc_component_config)
                                    internal_behavior_qualified_name_global=internal_behavior_qualified_name_config
                                    name_swc_internal_behavior_all=internal_behavior_qualified_name_config.split("/")[-1]
                                    short_name_all_5=supermod_all.IDENTIFIER.factory()
                                    short_name_all_5.set_valueOf_(name_swc_internal_behavior_all)
                                    swc_internal_behavior.set_SHORT_NAME(short_name_all_5)
                                    events_all=supermod_all.EVENTSType.factory()
                                    swc_internal_behavior.set_EVENTS(events_all) #EVENTS也写了，只能写在这里，要不在Runnable那边写的话，会重复定义
                                    handle_termination_and_restart=supermod_all.HANDLE_TERMINATION_AND_RESTART_ENUM.factory()      #把无关的先给写死
                                    swc_internal_behavior.set_HANDLE_TERMINATION_AND_RESTART(handle_termination_and_restart)
                                    handle_termination_and_restart.set_valueOf_("NO-SUPPORT")                                
                                    supports_multiple_instantiation_all=supermod_all.BOOLEAN.factory()
                                    supports_multiple_instantiation_all.set_valueOf_("false")                                           #把无关的先给写死
                                    swc_internal_behavior.set_SUPPORTS_MULTIPLE_INSTANTIATION(supports_multiple_instantiation_all)

                                elif name_child_swc_component_config=="Ports":  ##写PORTS这部分
                                    ports_all=supermod_all.PORTSType.factory()
                                    ports_all.set_R_PORT_PROTOTYPE([])
                                    ports_all.set_P_PORT_PROTOTYPE([])
                                    application_sw_component_type_all.set_PORTS(ports_all)
                                    for child_ports in child_swc_component_config:
                                        name_child_ports=Tag_pattern_.match(child_ports.tag).groups()[-1]
                                        if name_child_ports=="ReceiverPorts": #表示的是配置文件中的ReceiverPorts
                                            for child_receiverPorts_config in child_ports:
                                                name_child_receiverPorts_config=Tag_pattern_.match(child_receiverPorts_config.tag).groups()[-1]
                                                if name_child_receiverPorts_config=="ReceiverPort-Prototype":
                                                    r_port_prototype_all=supermod_all.R_PORT_PROTOTYPE.factory()
                                                    ports_all.add_R_PORT_PROTOTYPE(r_port_prototype_all)
                                                    r_port_prototype_all.set_UUID(str(uuid.uuid4()))
                                                    short_name_all_3=supermod_all.IDENTIFIER.factory()
                                                    short_name_all_3.set_valueOf_(supermod_config.find_attr_value_("NAME",child_receiverPorts_config))
                                                    r_port_prototype_all.set_SHORT_NAME(short_name_all_3)
                                                    required_interface_tref_all=supermod_all.REQUIRED_INTERFACE_TREFType.factory() #这的顺序和arxml中先REQUIRED-COM-SPECS,后REQUIRED-INTERFACE-TREF的顺序不一样，这里反过来，为了获得接口的内容
                                                    r_port_prototype_all.set_REQUIRED_INTERFACE_TREF(required_interface_tref_all)
                                                    required_interface_tref_all.set_DEST("SENDER-RECEIVER-INTERFACE")
                                                    interfaceNode=id2NodeMap[child_receiverPorts_config.attrib["INTERFACE-REF-ID"]]
                                                    interface_package_config=interfaceNode.attrib["PACKAGE"]
                                                    #interface_package_config=getInterfacePackage_fromConfig(source)
                                                    attr_interface_ref_id_config=supermod_config.find_attr_value_("INTERFACE-REF-ID",child_receiverPorts_config)
                                                    name_interface_config=id_name_maps_config.get(attr_interface_ref_id_config)
                                                    name_interface_config=name_interface_config if name_interface_config is not None else "None"
                                                    value_interface_all=interface_package_config+"/"+name_interface_config
                                                    required_interface_tref_all.set_valueOf_(value_interface_all)

                                                    required_com_specs_all=supermod_all.REQUIRED_COM_SPECSType.factory()
                                                    r_port_prototype_all.set_REQUIRED_COM_SPECS(required_com_specs_all)
                                                    required_com_specs_all.set_NONQUEUED_RECEIVER_COM_SPEC([])
                                                   
                                                    for child_receiverPort_Prototype_config in child_receiverPorts_config:
                                                        name_child_receiverPort_Prototype_config=Tag_pattern_.match(child_receiverPort_Prototype_config.tag).groups()[-1]
                                                        if name_child_receiverPort_Prototype_config=="ReceiverPort-Specs":
                                                            for child_receiverPort_Specs_config in child_receiverPort_Prototype_config:
                                                                name_child_receiverPort_Specs_config=Tag_pattern_.match(child_receiverPort_Specs_config.tag).groups()[-1]
                                                                if name_child_receiverPort_Specs_config=="Nonqueued-Receiver-Com-Spec":
                                                                    nonqueued_receiver_com_spec_all=supermod_all.NONQUEUED_RECEIVER_COM_SPEC.factory()
                                                                    required_com_specs_all.add_NONQUEUED_RECEIVER_COM_SPEC(nonqueued_receiver_com_spec_all) 
                                                                    element_ref_id_config=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_receiverPort_Specs_config)
                                                                    name_element=id_name_maps_config.get(element_ref_id_config)
                                                                    data_elements_ref_all=supermod_all.DATA_ELEMENT_REFType.factory()
                                                                    nonqueued_receiver_com_spec_all.set_DATA_ELEMENT_REF(data_elements_ref_all)
                                                                    data_elements_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    value_element_all=value_interface_all+"/"+name_element
                                                                    data_elements_ref_all.set_valueOf_(value_element_all)
                                                                    handle_out_of_range_all=supermod_all.HANDLE_OUT_OF_RANGE_ENUM.factory()
                                                                    handle_out_of_range_all.set_valueOf_("NONE")
                                                                    nonqueued_receiver_com_spec_all.set_HANDLE_OUT_OF_RANGE(handle_out_of_range_all)
                                                                    uses_end_to_end_protection_all=supermod_all.BOOLEAN_VALUE_VARIATION_POINT.factory()
                                                                    nonqueued_receiver_com_spec_all.set_USES_END_TO_END_PROTECTION(uses_end_to_end_protection_all)
                                                                    uses_end_to_end_protection_all.set_valueOf_("false")
                                                                    enable_update_all=supermod_all.BOOLEAN.factory()   #顺序和之前不太一样
                                                                    nonqueued_receiver_com_spec_all.set_ENABLE_UPDATE(enable_update_all)
                                                                    enable_update_all.set_valueOf_("false")
                                                                    handle_timeout_type_all=supermod_all.HANDLE_TIMEOUT_ENUM.factory()
                                                                    nonqueued_receiver_com_spec_all.set_HANDLE_TIMEOUT_TYPE(handle_timeout_type_all)
                                                                    handle_timeout_type_all.set_valueOf_("NONE")
                                                                    for child_nonqueued_receiver_com_spec in child_receiverPort_Specs_config:
                                                                        name_child_nonqueued_receiver_com_spec=Tag_pattern_.match(child_nonqueued_receiver_com_spec.tag).groups()[-1]
                                                                        if name_child_nonqueued_receiver_com_spec=="Alive-Timeout":
                                                                            alive_timeout_all=supermod_all.TIME_VALUE.factory()
                                                                            nonqueued_receiver_com_spec_all.set_ALIVE_TIMEOUT(alive_timeout_all)
                                                                            alive_timeout_all.set_valueOf_(supermod_config.get_all_text_(child_nonqueued_receiver_com_spec))
                                                                        elif name_child_nonqueued_receiver_com_spec=="Handle-Nerver-Received":
                                                                            handle_never_received_all=supermod_all.BOOLEAN.factory()
                                                                            nonqueued_receiver_com_spec_all.set_HANDLE_NEVER_RECEIVED(handle_never_received_all)
                                                                            handle_never_received_all.set_valueOf_(supermod_config.get_all_text_(child_nonqueued_receiver_com_spec))
                                                                        elif name_child_nonqueued_receiver_com_spec=="Init-Value":
                                                                            init_value_all=supermod_all.INIT_VALUEType35.factory()
                                                                            nonqueued_receiver_com_spec_all.set_INIT_VALUE(init_value_all)
                                                                            for child_init_value in child_nonqueued_receiver_com_spec:
                                                                                name_child_init_value=Tag_pattern_.match(child_init_value.tag).groups()[-1]
                                                                                if name_child_init_value=="NUMERICAL-VALUE-SPECIFICATION":

                                                                                    numerical_value_specification_all=supermod_all.NUMERICAL_VALUE_SPECIFICATION.factory()
                                                                                    init_value_all.set_NUMERICAL_VALUE_SPECIFICATION(numerical_value_specification_all)
                                                                                    short_label=supermod_all.IDENTIFIER.factory()
                                                                                    numerical_value_specification_all.set_SHORT_LABEL(short_label)
                                                                                    short_label.set_valueOf_("DefaultInitValue_Double")
                                                                                    value_all=supermod_all.NUMERICAL_VALUE_VARIATION_POINT.factory()
                                                                                    numerical_value_specification_all.set_VALUE(value_all)
                                                                                    value_all.set_valueOf_(child_init_value.xpath('.//ns:VALUE',namespaces=namespaces)[0].text)
                                                                                elif name_child_init_value=="Constant-Reference":
                                                                                    constant_specification_ref_id=supermod_config.find_attr_value_("CONSTANT-SPECIFICATION-REF-ID",child_init_value)
                                                                                    if constant_specification_ref_id!="":
                                                                                        constant_specification_node=id2NodeMap[constant_specification_ref_id]
                                                                                        constant_reference_all=supermod_all.CONSTANT_REFERENCE.factory()
                                                                                        init_value_all.set_CONSTANT_REFERENCE(constant_reference_all)
                                                                                        short_label_all=supermod_all.IDENTIFIER.factory()
                                                                                        short_label_all.set_valueOf_(constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)
                                                                                        constant_reference_all.set_SHORT_LABEL(short_label_all)
                                                                                        constant_ref_all=supermod_all.CONSTANT_REFType.factory()
                                                                                        constant_reference_all.set_CONSTANT_REF(constant_ref_all)
                                                                                        constant_ref_all.set_DEST("CONSTANT-SPECIFICATION")
                                                                                        constant_specification_package_path="/DataTypes/Constant-Specifications"
                                                                                        temp=source.xpath('//ns:Additional-Packages',namespaces=namespaces)[0].attrib["CONSTANT-SPECIFICATION-PACKAGE"]
                                                                                        if temp!=constant_specification_package_path:
                                                                                            constant_specification_package_path=temp
                                                                                        constant_ref_all.set_valueOf_(constant_specification_package_path+"/"+constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)


                                        elif name_child_ports=="SenderPorts":#表示的是配置文件中的SenderPorts
                                            for child_senderports_config in child_ports:
                                                name_child_senderports_config=Tag_pattern_.match(child_senderports_config.tag).groups()[-1]
                                                if name_child_senderports_config=="SenderPort-Prototype":
                                                    p_port_prototype_all=supermod_all.P_PORT_PROTOTYPE.factory()
                                                    ports_all.add_P_PORT_PROTOTYPE(p_port_prototype_all)
                                                    p_port_prototype_all.set_UUID(str(uuid.uuid4()))
                                                    short_name_all_4=supermod_all.IDENTIFIER.factory()
                                                    p_port_prototype_all.set_SHORT_NAME(short_name_all_4)
                                                    short_name_all_4.set_valueOf_(supermod_config.find_attr_value_("NAME",child_senderports_config))

                                                    provide_interface_tref=supermod_all.PROVIDED_INTERFACE_TREFType.factory()  #先做的下面一块的定义
                                                    p_port_prototype_all.set_PROVIDED_INTERFACE_TREF(provide_interface_tref)
                                                    provide_interface_tref.set_DEST("SENDER-RECEIVER-INTERFACE")
                                                    interfaceNode=id2NodeMap[child_receiverPorts_config.attrib["INTERFACE-REF-ID"]]
                                                    interface_package_config=interfaceNode.attrib["PACKAGE"]
                                                    attr_interface_ref_id_config=supermod_config.find_attr_value_("INTERFACE-REF-ID",child_senderports_config)
                                                    name_interface_config=id_name_maps_config.get(attr_interface_ref_id_config)
                                                    name_interface_config= name_interface_config if name_interface_config is not None else "NONE"
                                                    value_interface_all=interface_package_config+"/"+name_interface_config
                                                    provide_interface_tref.set_valueOf_(value_interface_all)

                                                    #进行all中PROVIDED-COM-SPECS的定义
                                                    provided_com_specs_all=supermod_all.PROVIDED_COM_SPECSType.factory()
                                                    p_port_prototype_all.set_PROVIDED_COM_SPECS(provided_com_specs_all)

                                                    for child_senderport_prototype in child_senderports_config:
                                                        name_child_senderport_prototype=Tag_pattern_.match(child_senderport_prototype.tag).groups()[-1]
                                                        if name_child_senderport_prototype=="SenderPort-Specs":
                                                            for child_senderport_specs in child_senderport_prototype:
                                                                name_child_senderport_specs=Tag_pattern_.match(child_senderport_specs.tag).groups()[-1]
                                                                if name_child_senderport_specs=="Nonqueued-Sender-Com-Spec":
                                                                    nonqueued_sender_com_spec=supermod_all.NONQUEUED_SENDER_COM_SPEC.factory()
                                                                    provided_com_specs_all.add_NONQUEUED_SENDER_COM_SPEC(nonqueued_sender_com_spec)
                                                                    handle_out_of_range_all=supermod_all.HANDLE_OUT_OF_RANGE_ENUM.factory()
                                                                    nonqueued_sender_com_spec.set_HANDLE_OUT_OF_RANGE(handle_out_of_range_all)
                                                                    handle_out_of_range_all.set_valueOf_("NONE")
                                                                    uses_end_to_end_protection_all=supermod_all.BOOLEAN.factory()
                                                                    uses_end_to_end_protection_all.set_valueOf_("false")
                                                                    nonqueued_sender_com_spec.set_USES_END_TO_END_PROTECTION(uses_end_to_end_protection_all)
                                                                    element_ref_id_config=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_senderport_specs)
                                                                    name_element=id_name_maps_config.get(element_ref_id_config)
                                                                    name_element=name_element if name_element is not None else "NONE"
                                                                    value_data_element_ref_config=value_interface_all+"/"+name_element
                                                                    data_elements_ref_all=supermod_all.DATA_ELEMENT_REFType.factory()
                                                                    nonqueued_sender_com_spec.set_DATA_ELEMENT_REF(data_elements_ref_all)
                                                                    data_elements_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    data_elements_ref_all.set_valueOf_(value_data_element_ref_config)
                                                                    for child_nonqueued_sender_com_spec in child_senderport_specs:
                                                                        name_child_nonqueued_sender_com_spec=Tag_pattern_.match(child_nonqueued_sender_com_spec.tag).groups()[-1]
                                                                        if name_child_nonqueued_sender_com_spec=="Init-Value":
                                                                            init_value_all=supermod_all.INIT_VALUEType35.factory()
                                                                            nonqueued_sender_com_spec.set_INIT_VALUE(init_value_all)
                                                                            for child_init_value in child_nonqueued_sender_com_spec:
                                                                                name_child_init_value=Tag_pattern_.match(child_init_value.tag).groups()[-1]
                                                                                if name_child_init_value=="NUMERICAL-VALUE-SPECIFICATION":

                                                                                    numerical_value_specification_all=supermod_all.NUMERICAL_VALUE_SPECIFICATION.factory()
                                                                                    init_value_all.set_NUMERICAL_VALUE_SPECIFICATION(numerical_value_specification_all)
                                                                                    short_label=supermod_all.IDENTIFIER.factory()
                                                                                    numerical_value_specification_all.set_SHORT_LABEL(short_label)
                                                                                    short_label.set_valueOf_("DefaultInitValue_Double")
                                                                                    value_all=supermod_all.NUMERICAL_VALUE_VARIATION_POINT.factory()
                                                                                    numerical_value_specification_all.set_VALUE(value_all)
                                                                                    value_all.set_valueOf_(child_init_value.xpath('.//ns:VALUE',namespaces=namespaces)[0].text)
                                                                                elif name_child_init_value=="Constant-Reference":
                                                                                    constant_specification_ref_id=supermod_config.find_attr_value_("CONSTANT-SPECIFICATION-REF-ID",child_init_value)
                                                                                    constant_specification_node=id2NodeMap[constant_specification_ref_id]
                                                                                    constant_reference_all=supermod_all.CONSTANT_REFERENCE.factory()
                                                                                    init_value_all.set_CONSTANT_REFERENCE(constant_reference_all)
                                                                                    short_label_all=supermod_all.IDENTIFIER.factory()
                                                                                    short_label_all.set_valueOf_(constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)
                                                                                    constant_reference_all.set_SHORT_LABEL(short_label_all)
                                                                                    constant_ref_all=supermod_all.CONSTANT_REFType.factory()
                                                                                    constant_reference_all.set_CONSTANT_REF(constant_ref_all)
                                                                                    constant_ref_all.set_DEST("CONSTANT-SPECIFICATION")
                                                                                    constant_specification_package_path="/DataTypes/Constant-Specifications"
                                                                                    temp=source.xpath('//ns:Additional-Packages',namespaces=namespaces)[0].attrib["CONSTANT-SPECIFICATION-PACKAGE"]
                                                                                    if temp!=constant_specification_package_path:
                                                                                        constant_specification_package_path=temp
                                                                                    constant_ref_all.set_valueOf_(constant_specification_package_path+"/"+constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)
                                                                    
                                elif name_child_swc_component_config=="Runnables": ##遍历Runnables，填写SW-INTERNAL-BEHAVIOR中的内容
                                    runnables_all=supermod_all.RUNNABLESType.factory()
                                    swc_internal_behavior.set_RUNNABLES(runnables_all)
                                    for child_Runnables_config in child_swc_component_config:
                                        name_child_Runnables_config=Tag_pattern_.match(child_Runnables_config.tag).groups()[-1]
                                        if name_child_Runnables_config=="Runnable-Entity":
                                            runnable_entity_all=supermod_all.RUNNABLE_ENTITY.factory()
                                            runnables_all.add_RUNNABLE_ENTITY(runnable_entity_all)
                                            runnable_entity_all.set_UUID(str(uuid.uuid4()))
                                            short_name_all_8=supermod_all.IDENTIFIER.factory()
                                            runnable_entity_all.set_SHORT_NAME(short_name_all_8)
                                            short_name_all_8.set_valueOf_(supermod_config.find_attr_value_("NAME",child_Runnables_config))
                                            minimum_start_interval=supermod_all.TIME_VALUE.factory()
                                            minimum_start_interval.set_valueOf_("0")
                                            runnable_entity_all.set_MINIMUM_START_INTERVAL(minimum_start_interval)
                                            
                                            for child_runnable_entity_config in child_Runnables_config:
                                                name_child_runnable_entity_config=Tag_pattern_.match(child_runnable_entity_config.tag).groups()[-1]
                                                if name_child_runnable_entity_config=="Can-Be-Invoked-Concurrently":
                                                    can_be_invoked_concurrently_all=supermod_all.BOOLEAN.factory()
                                                    runnable_entity_all.set_CAN_BE_INVOKED_CONCURRENTLY(can_be_invoked_concurrently_all)
                                                    can_be_invoked_concurrently_all.set_valueOf_(supermod_config.get_all_text_(child_runnable_entity_config))

                                                elif name_child_runnable_entity_config=="Events":
                                                    for child_events in child_runnable_entity_config:
                                                        name_child_events=Tag_pattern_.match(child_events.tag).groups()[-1]
                                                        if name_child_events=="Event-Prototype":
                                                            swc_internal_behavior=internal_behaviors_all.get_SWC_INTERNAL_BEHAVIOR()[-1] 
                                                            events_all=swc_internal_behavior.get_EVENTS()
                                                            value_Event_type_config=""
                                                            value_Event_Name=""
                                                            for child_Event_Prototype in child_events:
                                                                name_child_Event_Prototype=Tag_pattern_.match(child_Event_Prototype.tag).groups()[-1]
                                                                if name_child_Event_Prototype=="Event-Type":
                                                                    value_Event_type_config=supermod_config.get_all_text_(child_Event_Prototype)
                                                                elif name_child_Event_Prototype=="Event-Name":
                                                                    value_Event_Name=supermod_config.get_all_text_(child_Event_Prototype)
                                                            if value_Event_type_config=="TimingEvent":
                                                                timing_event_all=supermod_all.TIMING_EVENT.factory()
                                                                events_all.add_TIMING_EVENT(timing_event_all)
                                                                timing_event_all.set_UUID(str(uuid.uuid4()))
                                                                short_name_all_6=supermod_all.IDENTIFIER.factory()
                                                                timing_event_all.set_SHORT_NAME(short_name_all_6)
                                                                short_name_all_6.set_valueOf_(value_Event_Name)
                                                                start_on_event_ref=supermod_all.START_ON_EVENT_REFType.factory()
                                                                timing_event_all.set_START_ON_EVENT_REF(start_on_event_ref)
                                                                start_on_event_ref.set_DEST("RUNNABLE_ENTITY")
                                                                name_runnable_entity_config=supermod_config.find_attr_value_("NAME",child_Runnables_config)
                                                                value_start_on_event_ref=internal_behavior_qualified_name_global+"/"+name_runnable_entity_config
                                                                start_on_event_ref.set_valueOf_(value_start_on_event_ref)
                                                                period_all=supermod_all.TIME_VALUE.factory()
                                                                timing_event_all.set_PERIOD(period_all)
                                                                period_all.set_valueOf_(child_events.xpath('.//ns:Period',namespaces=namespaces)[0].text)
                                                elif name_child_runnable_entity_config=="Data-Read-Access":
                                                    data_read_access_all=supermod_all.DATA_READ_ACCESSSType.factory()
                                                    runnable_entity_all.set_DATA_READ_ACCESSS(data_read_access_all)

                                                    for child_data_read_access in child_runnable_entity_config:
                                                        name_child_data_read_access=Tag_pattern_.match(child_data_read_access.tag).groups()[-1]
                                                        if name_child_data_read_access=="Variable-Access":
                                                            for child_variable_access in child_data_read_access:
                                                                name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_variable_access=="Port-Prototype-Ref":
                                                                    port_ref_id_config=supermod_config.find_attr_value_("PORT-REF-ID",child_variable_access)
                                                                    #period_config=idport_period_maps_config.get(port_ref_id_config)
                                                                    #period_all=supermod_all.TIME_VALUE.factory()
                                                                    #period_all.set_valueOf_(period_config)
                                                                    #timing_event_all=swc_internal_behavior.get_EVENTS().get_TIMING_EVENT()[-1]
                                                                    #timing_event_all.set_PERIOD(period_all)
                                                                    name_port,name_interface,name_element_list=idport_portname_interfacename_elementname_maps_config[port_ref_id_config]
                                                                    #原来的element有误，现在改正
                                                                    element_ref_id_config=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_variable_access)
                                                                    #println("name_element",element_ref_id_config)
                                                                    #print("id_name_maps_config",id_name_maps_config)
                                                                    #print("element_ref_id_config",element_ref_id_config)
                                                                    name_element=id_name_maps_config.get(element_ref_id_config)
                                                                    #for name_element in name_element_list:
                                                                    variable_access_all=supermod_all.VARIABLE_ACCESS.factory()
                                                                    data_read_access_all.add_VARIABLE_ACCESS(variable_access_all)
                                                                    variable_access_all.set_UUID(str(uuid.uuid4()))
                                                                    short_name_all_9=supermod_all.IDENTIFIER.factory()
                                                                    variable_access_all.set_SHORT_NAME(short_name_all_9)
                                                                    #print("name_port",name_port)
                                                                    #print("name_element",name_element)
                                                                    short_name_all_9.set_valueOf_("IN_"+name_port+"_"+name_element)
                                                                    accessed_varaible_all=supermod_all.AUTOSAR_VARIABLE_REF.factory()
                                                                    variable_access_all.set_ACCESSED_VARIABLE(accessed_varaible_all)
                                                                    autosar_variable_iref=supermod_all.VARIABLE_IN_ATOMIC_SWC_TYPE_INSTANCE_REF.factory()
                                                                    accessed_varaible_all.set_AUTOSAR_VARIABLE_IREF(autosar_variable_iref)
                                                                    port_prototype_ref=supermod_all.PORT_PROTOTYPE_REFType.factory()
                                                                    autosar_variable_iref.set_PORT_PROTOTYPE_REF(port_prototype_ref)
                                                                    port_prototype_ref.set_DEST("R-PORT-PROTOTYPE")
                                                                    #print("name_swcComponent_global",name_swcComponent_global)
                                                                    port_prototype_ref.set_valueOf_(internal_behavior_qualified_name_global.split("/")[1]+"/"+name_swcComponent_global+"/"+name_port)
                                                                    target_data_prototype_ref_all=supermod_all.TARGET_DATA_PROTOTYPE_REFType.factory()
                                                                    autosar_variable_iref.set_TARGET_DATA_PROTOTYPE_REF(target_data_prototype_ref_all)
                                                                    target_data_prototype_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    port_temp=id2NodeMap[port_ref_id_config]
                                                                    interfaceIdRef=port_temp.attrib["INTERFACE-REF-ID"]
                                                                    interfaceTemp=id2NodeMap[interfaceIdRef]
                                                                    interface_package_config=interfaceTemp.attrib["PACKAGE"]
                                                                    target_data_prototype_ref_all.set_valueOf_(interface_package_config+"/"+name_interface+"/"+name_element)
                                                elif name_child_runnable_entity_config=="Data-Write-Access":
                                                    data_write_access_all=supermod_all.DATA_WRITE_ACCESSSType.factory()
                                                    runnable_entity_all.set_DATA_WRITE_ACCESSS(data_write_access_all)
                                                    for child_data_write_access in child_runnable_entity_config:
                                                        name_child_data_write_access=Tag_pattern_.match(child_data_write_access.tag).groups()[-1]
                                                        if name_child_data_write_access=="Variable-Access":

                                                            for child_variable_access in child_data_write_access:
                                                                name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_variable_access=="Port-Prototype-Ref":
                                                                    port_ref_id_config=supermod_config.find_attr_value_("PORT-REF-ID",child_variable_access)
                                                                    name_port,name_interface,name_element_list=idport_portname_interfacename_elementname_maps_config[port_ref_id_config]
                                                                    element_ref_id_config=supermod_config.find_attr_value_("ELEMENT-REF-ID",child_variable_access)
                                                                    name_element=id_name_maps_config.get(element_ref_id_config)
                                                                    
                                                                    variable_access_all=supermod_all.VARIABLE_ACCESS.factory()
                                                                    data_write_access_all.add_VARIABLE_ACCESS(variable_access_all)
                                                                    variable_access_all.set_UUID(str(uuid.uuid4()))
                                                                    short_name_all_10=supermod_all.IDENTIFIER.factory()
                                                                    variable_access_all.set_SHORT_NAME(short_name_all_10)
                                                                    short_name_all_10.set_valueOf_("OUT_"+name_port+"_"+name_element)
                                                                    accessed_varaible_all=supermod_all.AUTOSAR_VARIABLE_REF.factory()
                                                                    variable_access_all.set_ACCESSED_VARIABLE(accessed_varaible_all)
                                                                    autosar_variable_iref=supermod_all.VARIABLE_IN_ATOMIC_SWC_TYPE_INSTANCE_REF.factory()
                                                                    accessed_varaible_all.set_AUTOSAR_VARIABLE_IREF(autosar_variable_iref)
                                                                    port_prototype_ref=supermod_all.PORT_PROTOTYPE_REFType.factory()
                                                                    autosar_variable_iref.set_PORT_PROTOTYPE_REF(port_prototype_ref)
                                                                    port_prototype_ref.set_DEST("P-PORT-PROTOTYPE")
                                                                    port_prototype_ref.set_valueOf_(internal_behavior_qualified_name_global.split("/")[1]+"/"+name_swcComponent_global+"/"+name_port)
                                                                    target_data_prototype_ref_all=supermod_all.TARGET_DATA_PROTOTYPE_REFType.factory()
                                                                    autosar_variable_iref.set_TARGET_DATA_PROTOTYPE_REF(target_data_prototype_ref_all)
                                                                    target_data_prototype_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    port_temp=id2NodeMap[port_ref_id_config]
                                                                    interfaceIdRef=port_temp.attrib["INTERFACE-REF-ID"]
                                                                    interfaceTemp=id2NodeMap[interfaceIdRef]
                                                                    interface_package_config=interfaceTemp.attrib["PACKAGE"]
                                                                    target_data_prototype_ref_all.set_valueOf_(interface_package_config+"/"+name_interface+"/"+name_element)
                                                elif name_child_runnable_entity_config=="Read-Local-Access":
                                                    read_local_variables_all=supermod_all.READ_LOCAL_VARIABLESType.factory()
                                                    runnable_entity_all.set_READ_LOCAL_VARIABLES(read_local_variables_all)
                                                    for child_read_local_access in child_runnable_entity_config:
                                                        name_child_read_local_access=Tag_pattern_.match(child_read_local_access.tag).groups()[-1]
                                                        if name_child_read_local_access=="Variable-Access":
                                                            variable_access_all=supermod_all.VARIABLE_ACCESS.factory()
                                                            read_local_variables_all.add_VARIABLE_ACCESS(variable_access_all)
                                                            variable_access_all.set_UUID(str(uuid.uuid4()))
                                                            for child_variable_access in child_read_local_access:
                                                                name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_variable_access=="Local-Prototype-Ref":
                                                                    attr_local_ref_id=supermod_config.find_attr_value_("LOCAL-REF-ID",child_variable_access)
                                                                    name_local_ref_irv=id_name_maps_config.get(attr_local_ref_id)
                                                                    short_name_all_11=supermod_all.IDENTIFIER.factory()
                                                                    variable_access_all.set_SHORT_NAME(short_name_all_11)
                                                                    short_name_all_11.set_valueOf_("RV_"+name_local_ref_irv)
                                                                    accessed_varaible_all=supermod_all.AUTOSAR_VARIABLE_REF.factory()
                                                                    variable_access_all.set_ACCESSED_VARIABLE(accessed_varaible_all)
                                                                    local_variable_ref_all=supermod_all.LOCAL_VARIABLE_REFType.factory()
                                                                    accessed_varaible_all.set_LOCAL_VARIABLE_REF(local_variable_ref_all)
                                                                    local_variable_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    local_variable_ref_all.set_valueOf_(internal_behavior_qualified_name_global.split("/")[1]+"/"+name_swcComponent_global+"/"+internal_behavior_qualified_name_global.split("/")[-1]+"/"+name_local_ref_irv)
                                                elif name_child_runnable_entity_config=="Write-Local-Access":
                                                    written_local_variables=supermod_all.WRITTEN_LOCAL_VARIABLESType.factory()
                                                    runnable_entity_all.set_WRITTEN_LOCAL_VARIABLES(written_local_variables)
                                                    for child_write_local_access in child_runnable_entity_config:
                                                        name_child_write_local_access=Tag_pattern_.match(child_write_local_access.tag).groups()[-1]
                                                        if name_child_write_local_access=="Variable-Access":
                                                            variable_access_all=supermod_all.VARIABLE_ACCESS.factory()
                                                            written_local_variables.add_VARIABLE_ACCESS(variable_access_all)
                                                            variable_access_all.set_UUID(str(uuid.uuid4()))
                                                            for child_variable_access in child_write_local_access:
                                                                name_child_varialble_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_varialble_access=="Local-Prototype-Ref":
                                                                    attr_local_ref_id=supermod_config.find_attr_value_("LOCAL-REF-ID",child_variable_access)
                                                                    name_local_ref_irv=id_name_maps_config.get(attr_local_ref_id)
                                                                    short_name_all_12=supermod_all.IDENTIFIER.factory()
                                                                    variable_access_all.set_SHORT_NAME(short_name_all_12)
                                                                    short_name_all_12.set_valueOf_("WV_"+name_local_ref_irv)
                                                                    accessed_varaible_all=supermod_all.AUTOSAR_VARIABLE_REF.factory()
                                                                    variable_access_all.set_ACCESSED_VARIABLE(accessed_varaible_all)
                                                                    local_varaible_ref_all=supermod_all.LOCAL_VARIABLE_REFType.factory()
                                                                    accessed_varaible_all.set_LOCAL_VARIABLE_REF(local_varaible_ref_all)
                                                                    local_varaible_ref_all.set_DEST("VARIABLE-DATA-PROTOTYPE")
                                                                    local_varaible_ref_all.set_valueOf_(internal_behavior_qualified_name_global.split("/")[1]+"/"+name_swcComponent_global+"/"+internal_behavior_qualified_name_global.split("/")[-1]+"/"+name_local_ref_irv)                                                          
                                                elif name_child_runnable_entity_config=="Symbol":
                                                    symbol_all=supermod_all.C_IDENTIFIER.factory()
                                                    runnable_entity_all.set_SYMBOL(symbol_all)
                                                    symbol_all.set_valueOf_(supermod_all.get_all_text_(child_runnable_entity_config))

                                elif name_child_swc_component_config=="IRV":
                                    for child_irv in child_swc_component_config:
                                        name_child_irv=Tag_pattern_.match(child_irv.tag).groups()[-1]
                                        if name_child_irv=="IRVS":
                                            implicit_inter_runnable_variables_all=supermod_all.IMPLICIT_INTER_RUNNABLE_VARIABLESType.factory()
                                            swc_internal_behavior.set_IMPLICIT_INTER_RUNNABLE_VARIABLES(implicit_inter_runnable_variables_all)
                                            for child_irvs in child_irv:
                                                name_child_irvs=Tag_pattern_.match(child_irvs.tag).groups()[-1]
                                                if name_child_irvs=="Variable-Data-Prototype":
                                                    name_irv=supermod_config.find_attr_value_("NAME",child_irvs)
                                                    variable_data_prototype_all=supermod_all.VARIABLE_DATA_PROTOTYPE.factory()
                                                    variable_data_prototype_all.set_UUID(str(uuid.uuid4()))
                                                    implicit_inter_runnable_variables_all.add_VARIABLE_DATA_PROTOTYPE(variable_data_prototype_all)
                                                    short_name_all_7=supermod_all.IDENTIFIER.factory()
                                                    short_name_all_7.set_valueOf_(name_irv)
                                                    variable_data_prototype_all.set_SHORT_NAME(short_name_all_7)
                                                    category_all=supermod_all.CATEGORY_STRING.factory()
                                                    variable_data_prototype_all.set_CATEGORY(category_all)
                                                    category_all.set_valueOf_("VALUE")
                                                    for child_variable_data_prototype in child_irvs:
                                                        name_child_variable_data_prototype=Tag_pattern_.match(child_variable_data_prototype.tag).groups()[-1]
                                                        if name_child_variable_data_prototype=="Sw-Calibration-Access":
                                                            value_sw_calibration_access=supermod_config.get_all_text_(child_variable_data_prototype)
                                                            value_sw_calibration_access="READ-ONLY" if value_sw_calibration_access=="ReadOnly" else "None"
                                                            sw_data_def_props=supermod_all.SW_DATA_DEF_PROPS.factory()
                                                            variable_data_prototype_all.set_SW_DATA_DEF_PROPS(sw_data_def_props)
                                                            sw_data_def_props_variants=supermod_all.SW_DATA_DEF_PROPS_VARIANTSType.factory()
                                                            sw_data_def_props.set_SW_DATA_DEF_PROPS_VARIANTS(sw_data_def_props_variants)
                                                            sw_data_def_props_conditional_all=supermod_all.SW_DATA_DEF_PROPS_CONDITIONAL.factory()
                                                            sw_data_def_props_variants.add_SW_DATA_DEF_PROPS_CONDITIONAL(sw_data_def_props_conditional_all)
                                                            sw_calibration_access_all=supermod_all.SW_CALIBRATION_ACCESS_ENUM.factory()
                                                            sw_data_def_props_conditional_all.set_SW_CALIBRATION_ACCESS(sw_calibration_access_all)
                                                            sw_calibration_access_all.set_valueOf_(value_sw_calibration_access)
                                                            sw_impl_policy_all=supermod_all.SW_IMPL_POLICY_ENUM.factory()
                                                            sw_data_def_props_conditional_all.set_SW_IMPL_POLICY(sw_impl_policy_all)
                                                            sw_impl_policy_all.set_valueOf_("STANDARD")
                                                        elif name_child_variable_data_prototype=="Init-Value":
                                                            init_value_all_1=supermod_all.INIT_VALUEType35.factory()
                                                            variable_data_prototype_all.set_INIT_VALUE(init_value_all_1)
                                                            constant_reference_config_list=child_variable_data_prototype.xpath('.//ns:Constant-Reference',namespaces=namespaces)
                                                            if len(constant_reference_config_list)!=0:
                                                                constant_reference_config=constant_reference_config_list[0]
                                                                constant_specification_ref_id=supermod_config.find_attr_value_("CONSTANT-SPECIFICATION-REF-ID",constant_reference_config)
                                                                if constant_specification_ref_id!="":
                                                                    constant_specification_node=id2NodeMap[constant_specification_ref_id]
                                                                    constant_reference_all=supermod_all.CONSTANT_REFERENCE.factory()
                                                                    init_value_all_1.set_CONSTANT_REFERENCE(constant_reference_all)
                                                                    short_label_all=supermod_all.IDENTIFIER.factory()
                                                                    short_label_all.set_valueOf_(constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)
                                                                    constant_reference_all.set_SHORT_LABEL(short_label_all)
                                                                    constant_ref_all=supermod_all.CONSTANT_REFType.factory()
                                                                    constant_reference_all.set_CONSTANT_REF(constant_ref_all)
                                                                    constant_ref_all.set_DEST("CONSTANT-SPECIFICATION")
                                                                    constant_specification_package_path="/DataTypes/Constant-Specifications"
                                                                    temp=source.xpath('//ns:Additional-Packages',namespaces=namespaces)[0].attrib["CONSTANT-SPECIFICATION-PACKAGE"]
                                                                    if temp!=constant_specification_package_path:
                                                                        constant_specification_package_path=temp
                                                                    constant_ref_all.set_valueOf_(constant_specification_package_path+"/"+constant_specification_node.xpath('.//ns:SHORT-NAME',namespaces=namespaces)[0].text)
                                                            else:
                                                                numerical_value_specification_all_1=supermod_all.NUMERICAL_VALUE_SPECIFICATION.factory()
                                                                init_value_all_1.set_NUMERICAL_VALUE_SPECIFICATION(numerical_value_specification_all_1)
                                                                short_label_all_1=supermod_all.IDENTIFIER.factory()
                                                                numerical_value_specification_all_1.set_SHORT_LABEL(short_label_all_1)
                                                                short_label_all_1.set_valueOf_("DefaultInitValue_Double")
                                                                #numerical_value_specification_all.set_SHORT_LABEL(short_label_all_1)
                                                                value_all_2=supermod_all.NUMERICAL_VALUE_VARIATION_POINT.factory()
                                                                value_all_2.set_valueOf_("0")
                                                                numerical_value_specification_all_1.set_VALUE(value_all_2)


                                                    type_tref_all=supermod_all.TYPE_TREFType.factory()     
                                                    type_tref_all.set_DEST("IMPLEMENTATION-DATA-TYPE")
                                                    type_tref_all.set_valueOf_(datatype_package_global+"/Double")
                                                    variable_data_prototype_all.set_TYPE_TREF(type_tref_all)


                                                    
                                                    

    

    return component_package
                                                    
                                        

    
    



#从config文件转换为对应的implemetation文件
def convertConfig2Implementation(sourceFile,targetFile,modelName):
    parser = None
    doc = parsexml_(sourceFile, parser)
    source=doc.getroot()
    componentPath="/Components"
    implementationPath="/Components/SwcImplementation"
    componentXMLOptions=source.xpath('//ns:Component-XML-Options',namespaces=namespaces)
    for componentXMLOption in componentXMLOptions:
        temp=componentXMLOption.attrib["Implementation-Qualified-Name"]
        implementationPath="/".join(temp.split("/")[:-1])
        temp2=componentXMLOption.attrib["Package"]
        if temp2!="":
            componentPath=temp2

    package_implementation=path2AR_Package[implementationPath]

    package_component=path2AR_Package[componentPath]
            

    name_package_top,name_package_middle,name_swc_implementation="UNDEFINED","UNDEFINED","UNDEFINED"
    name_swcComponent="UNDEFINED"
    for child_autosar in source:
        name_child_autosar_all=Tag_pattern_.match(child_autosar.tag).groups()[-1]
        if name_child_autosar_all=="AUTOSAR-Dictionary":
            for child_autosar_dictionary in child_autosar:
                name_child_autosar_dictionary=Tag_pattern_.match(child_autosar_dictionary.tag).groups()[-1]
                if name_child_autosar_dictionary=="AtomicComponents":
                    for child_atomicComponents in child_autosar_dictionary:
                        name_child_atomicComponents=Tag_pattern_.match(child_atomicComponents.tag).groups()[-1]
                        if name_child_atomicComponents=="SwcComponent":
                            name_swcComponent=supermod_config.find_attr_value_("NAME",child_atomicComponents)
                            for child_swc_component in child_atomicComponents:
                                name_child_swc_component=Tag_pattern_.match(child_swc_component.tag).groups()[-1]
                                if name_child_swc_component=="Component-XML-Options":
                                    #package_config=supermod_config.find_attr_value_("Package",child_swc_component)
                                    #name_package_top,name_package_middle,name_swc_implementation=supermod_config.find_attr_value_("Implementation-Qualified-Name",child_swc_component).split("/")[1:]
                                    parts = supermod_config.find_attr_value_("Implementation-Qualified-Name", child_swc_component).split("/")[1:]

                                    if len(parts) >= 3:
                                        name_package_top = parts[0]
                                        name_package_middle = parts[1]
                                        name_swc_implementation = "/".join(parts[2:])
                                    elif len(parts) == 2:
                                        name_package_top = parts[0]
                                        name_package_middle = parts[1]
                                        name_swc_implementation = "UNDEFINED"
                                    elif len(parts) == 1:
                                        name_package_top = parts[0]
                                        name_package_middle = "UNDEFINED"
                                        name_swc_implementation = "UNDEFINED"
                                    else:
                                        # 为空或者格式不符合，全部赋默认值
                                        name_package_top = "UNDEFINED"
                                        name_package_middle = "UNDEFINED"
                                        name_swc_implementation = "UNDEFINED"
                                    
                                    #下面进行all的Implementation元素的编辑

    elements_all=supermod_all.ELEMENTSType.factory()
    package_implementation.set_ELEMENTS(elements_all)
    swc_implementation_all=supermod_all.SWC_IMPLEMENTATION.factory()
    elements_all.add_SWC_IMPLEMENTATION(swc_implementation_all)
    swc_implementation_all.set_UUID(str(uuid.uuid4()))
    short_name_all_3=supermod_all.IDENTIFIER.factory()
    short_name_all_3.set_valueOf_(name_swc_implementation)
    swc_implementation_all.set_SHORT_NAME(short_name_all_3)

    code_descriptors_all=supermod_all.CODE_DESCRIPTORSType.factory()
    swc_implementation_all.set_CODE_DESCRIPTORS(code_descriptors_all)
    code_all=supermod_all.CODE.factory()
    code_descriptors_all.add_CODE(code_all)
    short_name_all_4=supermod_all.IDENTIFIER.factory()
    code_all.set_SHORT_NAME(short_name_all_4)
    short_name_all_4.set_valueOf_("Code")
    artifact_descriptors=supermod_all.ARTIFACT_DESCRIPTORSType.factory()
    code_all.set_ARTIFACT_DESCRIPTORS(artifact_descriptors)
    autosar_engineering_object=supermod_all.AUTOSAR_ENGINEERING_OBJECT.factory()
    artifact_descriptors.add_AUTOSAR_ENGINEERING_OBJECT(autosar_engineering_object)
    short_label_1=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object.set_SHORT_LABEL(short_label_1)
    short_label_1.set_valueOf_(modelName+"_c")
    category_all=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object.set_CATEGORY(category_all)
    category_all.set_valueOf_("SWSRC")

    autosar_engineering_object_2=supermod_all.AUTOSAR_ENGINEERING_OBJECT.factory()
    artifact_descriptors.add_AUTOSAR_ENGINEERING_OBJECT(autosar_engineering_object_2)
    short_label_2=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object_2.set_SHORT_LABEL(short_label_2)
    short_label_2.set_valueOf_("rtwtypes_h")
    catagory_all_2=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object_2.set_CATEGORY(catagory_all_2)
    catagory_all_2.set_valueOf_("SWHDR")

    autosar_engineering_object_3=supermod_all.AUTOSAR_ENGINEERING_OBJECT.factory()
    artifact_descriptors.add_AUTOSAR_ENGINEERING_OBJECT(autosar_engineering_object_3)
    short_label_3=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object_3.set_SHORT_LABEL(short_label_3)
    short_label_3.set_valueOf_(modelName+"_h")
    category_all_3=supermod_all.NMTOKEN_STRING.factory()
    autosar_engineering_object_3.set_CATEGORY(category_all_3)
    category_all_3.set_valueOf_("SWHDR")

    programming_language_all=supermod_all.PROGRAMMINGLANGUAGE_ENUM.factory()
    swc_implementation_all.set_PROGRAMMING_LANGUAGE(programming_language_all)
    programming_language_all.set_valueOf_("C")
    resource_consumption_all=supermod_all.RESOURCE_CONSUMPTION.factory()
    swc_implementation_all.set_RESOURCE_CONSUMPTION(resource_consumption_all)
    short_name_all=supermod_all.IDENTIFIER.factory()
    resource_consumption_all.set_SHORT_NAME(short_name_all)
    short_name_all.set_valueOf_("RsrcCons_"+modelName)
    sw_version_all=supermod_all.REVISION_LABEL_STRING.factory()
    swc_implementation_all.set_SW_VERSION(sw_version_all)
    sw_version_all.set_valueOf_("1.27.1")
    used_code_generator_all=supermod_all.STRING.factory()
    swc_implementation_all.set_USED_CODE_GENERATOR(used_code_generator_all)
    used_code_generator_all.set_valueOf_("ARXML Coder Generator 1.0 (Wumbuk) 04-OCT-2023")
    vendor_id_all=supermod_all.POSITIVE_INTEGER.factory()
    swc_implementation_all.set_VENDOR_ID(vendor_id_all)
    vendor_id_all.set_valueOf_(0)
    behavior_ref_all=supermod_all.BEHAVIOR_REFType.factory()
    swc_implementation_all.set_BEHAVIOR_REF(behavior_ref_all)
    behavior_ref_all.set_DEST("SWC-INTERNAL-BEHAVIOR")
    behavior_ref_all.set_valueOf_(utils4ParseARXML.filtePath(internal_behavior_qualified_name_global))
    return package_component

                            


                                

#从config文件转换为对应的Timing文件
def convertConfig2Timing(sourceFile,targetFile):
    parser = None
    doc = parsexml_(sourceFile, parser)
    source=doc.getroot()
    timing_package=path2AR_Package["/Timing"]


    elements_all=supermod_all.ELEMENTSType.factory()

    timing_package.set_ELEMENTS(elements_all)
    swc_timing_all=supermod_all.SWC_TIMING.factory()
    elements_all.add_SWC_TIMING(swc_timing_all)
    swc_timing_all.set_UUID(str(uuid.uuid4()))
    name_package_top,name_package_middle,name_swc_implementation="UNDEFINED","UNDEFINED","UNDEFINED"
    name_swcComponent="UNDEFINED"

    for child_autosar in source:
        name_child_autosar_all=Tag_pattern_.match(child_autosar.tag).groups()[-1]
        if name_child_autosar_all=="AUTOSAR-Dictionary":
            for child_autosar_dictionary in child_autosar:
                name_child_autosar_dictionary=Tag_pattern_.match(child_autosar_dictionary.tag).groups()[-1]
                if name_child_autosar_dictionary=="AtomicComponents":
                    for child_atomicComponents in child_autosar_dictionary:
                        name_child_atomicComponents=Tag_pattern_.match(child_atomicComponents.tag).groups()[-1]
                        if name_child_atomicComponents=="SwcComponent":
                            name_swcComponent=supermod_config.find_attr_value_("NAME",child_atomicComponents)
                            short_name_all_2=supermod_all.IDENTIFIER.factory()
                            short_name_all_2.set_valueOf_(name_swcComponent+"_timing")
                            swc_timing_all.set_SHORT_NAME(short_name_all_2)
                            timing_requirements_all=supermod_all.TIMING_REQUIREMENTSType.factory()
                            swc_timing_all.set_TIMING_REQUIREMENTS(timing_requirements_all)
                            execution_order_constraint_all=supermod_all.EXECUTION_ORDER_CONSTRAINT.factory()
                            timing_requirements_all.add_EXECUTION_ORDER_CONSTRAINT(execution_order_constraint_all)
                            execution_order_constraint_all.set_UUID(str(uuid.uuid4()))
                            short_name_all_3=supermod_all.IDENTIFIER.factory()
                            execution_order_constraint_all.set_SHORT_NAME(short_name_all_3)
                            short_name_all_3.set_valueOf_("EOC")
                            ordered_elements_all=supermod_all.ORDERED_ELEMENTSType.factory()
                            execution_order_constraint_all.set_ORDERED_ELEMENTS(ordered_elements_all)



                            for child_swcComponent in child_atomicComponents:
                                name_child_swcComponent=Tag_pattern_.match(child_swcComponent.tag).groups()[-1]
                                
                                #这个If先弄一下local-write
                                if name_child_swcComponent=="Runnables":
                                    for child_runnables in child_swcComponent:
                                        name_child_runnables=Tag_pattern_.match(child_runnables.tag).groups()[-1]
                                        if name_child_runnables=="Runnable-Entity":
                                            for child_runnable_entity in child_runnables:
                                                name_child_runnable_entity=Tag_pattern_.match(child_runnable_entity.tag).groups()[-1]
                                                if name_child_runnable_entity=="Write-Local-Access":
                                                    for child_write_local_access in child_runnable_entity:
                                                        name_child_write_local_access=Tag_pattern_.match(child_write_local_access.tag).groups()[-1]
                                                        if name_child_write_local_access=="Variable-Access":
                                                            for child_variable_access in child_write_local_access:
                                                                name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_variable_access=="Local-Prototype-Ref":
                                                                    irv_wirte_runnable_maps_config[supermod_config.find_attr_value_("LOCAL-REF-ID",child_variable_access)]=supermod_all.find_attr_value_("NAME",child_runnables)                                
                                                elif name_child_runnable_entity=="Read-Local-Access":
                                                    for child_write_local_access in child_runnable_entity:
                                                        name_child_write_local_access=Tag_pattern_.match(child_write_local_access.tag).groups()[-1]
                                                        if name_child_write_local_access=="Variable-Access":
                                                            for child_variable_access in child_write_local_access:
                                                                name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                if name_child_variable_access=="Local-Prototype-Ref":
                                                                    irv_read_runnable_maps_config[supermod_config.find_attr_value_("LOCAL-REF-ID",child_variable_access)]=supermod_all.find_attr_value_("NAME",child_runnables)                                
                                if name_child_swcComponent=="Component-XML-Options":
                                    internal_behavior_qualified_name_all=supermod_config.find_attr_value_("Internal-Behavior-Qualified-Name",child_swcComponent)
                                    list_internal_behavior_qualified_name=internal_behavior_qualified_name_all.split("/")
                                    #list_internal_behavior_qualified_name[2]=name_swcComponent
                                    value_behavior_ref="/".join(list_internal_behavior_qualified_name)
                                    # if(value_behavior_ref[0]=="/"):
                                        # value_behavior_ref=value_behavior_ref[1:]
                                    behavior_ref=supermod_all.BEHAVIOR_REFType.factory()
                                    swc_timing_all.set_BEHAVIOR_REF(behavior_ref)
                                    behavior_ref.set_DEST("SWC-INTERNAL-BEHAVIOR")
                                    behavior_ref.set_valueOf_(value_behavior_ref)


                                elif name_child_swcComponent=="Runnables":
                                    for child_runnables in child_swcComponent:
                                        name_child_runnables=Tag_pattern_.match(child_runnables.tag).groups()[-1]
                                        if name_child_runnables=="Runnable-Entity":
                                            value_name_RunnableEntity=supermod_config.find_attr_value_("NAME",child_runnables)
                                            if "Init" not in value_name_RunnableEntity:
                                                eoc_executable_entity_ref_all=supermod_all.EOC_EXECUTABLE_ENTITY_REF.factory()
                                                ordered_elements_all.add_EOC_EXECUTABLE_ENTITY_REF(eoc_executable_entity_ref_all)
                                                eoc_executable_entity_ref_all.set_UUID(str(uuid.uuid4()))
                                                short_name_all_4=supermod_all.IDENTIFIER.factory()
                                                eoc_executable_entity_ref_all.set_SHORT_NAME(short_name_all_4)
                                                
                                                short_name_all_4.set_valueOf_(value_name_RunnableEntity)
                                                executable_ref_all=supermod_all.EXECUTABLE_REFType.factory()
                                                eoc_executable_entity_ref_all.set_EXECUTABLE_REF(executable_ref_all)
                                                executable_ref_all.set_DEST("RUNNABLE-ENTITY")
                                                executable_ref_all.set_valueOf_(value_behavior_ref+"/"+value_name_RunnableEntity)

                                                for child_runnable_entity in child_runnables:
                                                    name_child_runnable_entity=Tag_pattern_.match(child_runnable_entity.tag).groups()[-1]
                                                    if name_child_runnable_entity=="Write-Local-Access":
                                                        successor_refs_all=supermod_all.SUCCESSOR_REFSType.factory()
                                                        eoc_executable_entity_ref_all.set_SUCCESSOR_REFS(successor_refs_all)
                                                        for child_read_local_access in child_runnable_entity:
                                                            name_child_read_local_access=Tag_pattern_.match(child_read_local_access.tag).groups()[-1]
                                                            if name_child_read_local_access=="Variable-Access":
                                                                for child_variable_access in child_read_local_access:
                                                                    name_child_variable_access=Tag_pattern_.match(child_variable_access.tag).groups()[-1]
                                                                    if name_child_variable_access=="Local-Prototype-Ref":
                                                                        id_local_ref_read=supermod_config.find_attr_value_("LOCAL-REF-ID",child_variable_access)
                                                                        name_local_ref_read=irv_read_runnable_maps_config.get(id_local_ref_read)
                                                                        successor_ref_all=supermod_all.SUCCESSOR_REFType.factory()
                                                                        eoc_executable_entity_ref_all.get_SUCCESSOR_REFS().add_SUCCESSOR_REF(successor_ref_all)
                                                                        successor_ref_all.set_DEST("EOC-EXECUTABLE-ENTITY-REF")
                                                                        successor_ref_all.set_valueOf_("/Timing/"+name_swcComponent+"_timing/EOC/"+name_local_ref_read)

    return timing_package



USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    '''
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    '''
    inFilename = "autosar_config_codegen.xml"
    parser = None
    doc = parsexml_(inFilename, parser)
    source=doc.getroot()   
    init_id_name_mappings(source)
    init_idport_period_mappings(source)
    init_package_paths(source)
    init_idport_portname_interfacename_elementname_mappings(source)
    init_swc_component_config(source)
    convertConfig2Timing(inFilename,"test_autogen_timing.xml")


"""
import xml.etree.ElementTree as ET
import uuid

def convert_variable_data_prototype_to_arxml(vdp_element: ET.Element) -> ET.Element:
    param_proto = ET.Element('PARAMETER-DATA-PROTOTYPE')
    param_proto.set('UUID', str(uuid.uuid4()))  # 应该是从vdp_element获得ID的值
    

    short_name = ET.SubElement(param_proto, 'SHORT-NAME')
    short_name.text = vdp_element.attrib.get('NAME', 'UnknownName')

    category = ET.SubElement(param_proto, 'CATEGORY')
    category.text = 'CURVE'

    sw_data_def_props = ET.SubElement(param_proto, 'SW-DATA-DEF-PROPS')
    sw_data_def_props_variants = ET.SubElement(sw_data_def_props, 'SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional = ET.SubElement(sw_data_def_props_variants, 'SW-DATA-DEF-PROPS-CONDITIONAL')

    sw_cal_access = ET.SubElement(sw_data_def_props_conditional, 'SW-CALIBRATION-ACCESS')
    val = vdp_element.findtext('Sw-Calibration-Access', default='ReadWrite').upper().replace('READWRITE', 'READ-WRITE')
    sw_cal_access.text = val

    sw_impl_policy = ET.SubElement(sw_data_def_props_conditional, 'SW-IMPL-POLICY')
    sw_impl_policy.text = 'STANDARD'

    type_tref = ET.SubElement(param_proto, 'TYPE-TREF')
    type_tref.set('DEST', 'APPLICATION-PRIMITIVE-DATA-TYPE')
    type_tref.text = f"/AUTOSAR_Platform/ImplementationDataTypes/ApplDataTypes/Appl_{short_name.text}"

    init_value = ET.SubElement(param_proto, 'INIT-VALUE')
    constant_ref = ET.SubElement(init_value, 'CONSTANT-REFERENCE')

    short_label = ET.SubElement(constant_ref, 'SHORT-LABEL')
    short_label.text = short_name.text

    constant_ref_ref = ET.SubElement(constant_ref, 'CONSTANT-REF')
    constant_ref_ref.set('DEST', 'CONSTANT-SPECIFICATION')
    constant_ref_ref.text = f"/AUTOSAR_Platform/ImplementationDataTypes/Ground/{short_name.text}"

    return param_proto
"""


import logging
import xml.etree.ElementTree as ET
import uuid

# 配置日志写入 i:\test.log
logging.basicConfig(
    filename=r'i:\test2.log',  # 注意路径前加 r 防止转义
    filemode='w',             # 'w' 每次覆盖，'a' 追加
    level=logging.DEBUG,      # 记录所有调试及以上级别信息
    format='%(asctime)s %(levelname)s: %(message)s',
)

def convert_variable_data_prototype_to_arxml(vdp_element: ET.Element) -> ET.Element:
    """
    把自定义XML的 <Variable-Data-Prototype> 转换为ARXML格式的 <PARAMETER-DATA-PROTOTYPE> 节点
    """
    ns_uri = "http://autosar.org/schema/r4.0"

    # UUID 从 vdp_element 读取 ID 属性，没有就生成一个新的
    uuid_value = vdp_element.attrib.get('ID', str(uuid.uuid4()))
    param_proto = ET.Element(f'{{{ns_uri}}}PARAMETER-DATA-PROTOTYPE')
    param_proto.set('UUID', uuid_value)

    # SHORT-NAME
    short_name_value = vdp_element.attrib.get('NAME', 'UnknownName')
    short_name = ET.SubElement(param_proto, f'{{{ns_uri}}}SHORT-NAME')
    short_name.text = short_name_value

    # CATEGORY
    category = ET.SubElement(param_proto, f'{{{ns_uri}}}CATEGORY')
    category.text = 'CURVE'

    # SW-DATA-DEF-PROPS
    sw_data_def_props = ET.SubElement(param_proto, f'{{{ns_uri}}}SW-DATA-DEF-PROPS')
    sw_data_def_props_variants = ET.SubElement(sw_data_def_props, f'{{{ns_uri}}}SW-DATA-DEF-PROPS-VARIANTS')
    sw_data_def_props_conditional = ET.SubElement(sw_data_def_props_variants, f'{{{ns_uri}}}SW-DATA-DEF-PROPS-CONDITIONAL')

    # SW-CALIBRATION-ACCESS
    sw_cal_access = ET.SubElement(sw_data_def_props_conditional, f'{{{ns_uri}}}SW-CALIBRATION-ACCESS')
    val = vdp_element.findtext('Sw-Calibration-Access', default='ReadWrite').upper().replace('READWRITE', 'READ-WRITE')
    sw_cal_access.text = val

    # SW-IMPL-POLICY
    sw_impl_policy = ET.SubElement(sw_data_def_props_conditional, f'{{{ns_uri}}}SW-IMPL-POLICY')
    sw_impl_policy.text = 'STANDARD'

    # TYPE-TREF
    type_tref = ET.SubElement(param_proto, f'{{{ns_uri}}}TYPE-TREF')
    type_tref.set('DEST', 'APPLICATION-PRIMITIVE-DATA-TYPE')
    type_tref.text = f"/AUTOSAR_Platform/ImplementationDataTypes/ApplDataTypes/Appl_{short_name_value}"

    # INIT-VALUE
    init_value = ET.SubElement(param_proto, f'{{{ns_uri}}}INIT-VALUE')
    constant_ref = ET.SubElement(init_value, f'{{{ns_uri}}}CONSTANT-REFERENCE')

    short_label = ET.SubElement(constant_ref, f'{{{ns_uri}}}SHORT-LABEL')
    short_label.text = short_name_value

    constant_ref_ref = ET.SubElement(constant_ref, f'{{{ns_uri}}}CONSTANT-REF')
    constant_ref_ref.set('DEST', 'CONSTANT-SPECIFICATION')
    constant_ref_ref.text = f"/AUTOSAR_Platform/ImplementationDataTypes/Ground/{short_name_value}"

    return param_proto

import xml.etree.ElementTree as ET
import xml.dom.minidom

def pretty_xml(element, indent="  "):
    """使用 minidom 格式化 XML，去掉多余空行"""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_str = reparsed.toprettyxml(indent=indent)

    # 去掉空行
    lines = [line for line in pretty_str.split('\n') if line.strip()]
    if lines and lines[0].startswith('<?xml'):
        lines = lines[1:]
    return '\n'.join(lines)
    
    
def add_per_instance_parameters(xmlConfigPath: str, targetPath: str):
    logging.info(f"Start processing config XML: {xmlConfigPath}, target ARXML: {targetPath}")
    # 读取自定义XML
    custom_tree = ET.parse(xmlConfigPath)
    custom_root = custom_tree.getroot()

    # 尝试查找无命名空间的 Parameters
    parameters_node = custom_root.find('.//Parameters')
    if parameters_node is None:
        # 尝试带命名空间查找
        nsmap = {k if k else 'ns': v for k, v in custom_root.attrib.items()}
        # 如果根节点声明了命名空间，从根 tag 提取
        if custom_root.tag.startswith("{"):
            uri = custom_root.tag.split("}")[0][1:]
            nsmap['ns'] = uri
            parameters_node = custom_root.find('.//ns:Parameters', nsmap)

    if parameters_node is None:
        logging.info(f"add_per_instance_parameters_finished")
        return 
    #    raise ValueError("Custom XML does not contain <Parameters> node")

    variable_data_prototypes = parameters_node.findall('ns:Variable-Data-Prototype',nsmap)
    if not variable_data_prototypes:  # 防止空
        variable_data_prototypes = parameters_node.findall('.//ns:Variable-Data-Prototype',nsmap)

    # 读取目标ARXML
    ET.register_namespace('', "http://autosar.org/schema/r4.0")
    arxml_tree = ET.parse(targetPath)
    arxml_root = arxml_tree.getroot()

    ns = {'ns': 'http://autosar.org/schema/r4.0'}

    swc_internal_behavior = arxml_root.find('.//ns:SWC-INTERNAL-BEHAVIOR', ns)
    if swc_internal_behavior is None:
        raise ValueError("ARXML does not contain <SWC-INTERNAL-BEHAVIOR> node")

    per_instance_params = swc_internal_behavior.find('ns:PER-INSTANCE-PARAMETERS', ns)
    if per_instance_params is None:
        per_instance_params = ET.Element('{http://autosar.org/schema/r4.0}PER-INSTANCE-PARAMETERS')
        swc_internal_behavior.append(per_instance_params)
        logging.info(f"Created new <PER-INSTANCE-PARAMETERS> node")

    for vdp in variable_data_prototypes:
        # 这里用转换函数生成符合ARXML格式的节点
        logging.info(f"Processing Variable-Data-Prototype with ID: {vdp.attrib.get('ID')} NAME: {vdp.attrib.get('NAME')}")
        new_param = convert_variable_data_prototype_to_arxml(vdp)
        per_instance_params.append(new_param)

    # 输出 XML 时加上头部和注释
    pretty_str = pretty_xml(arxml_root, indent="    ")
    now = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    header = f'''<?xml version="1.0" encoding="UTF-8"?>
<!--
    Auto generated XML Component Description for model 
    Model version                : 1.42                
    Author                       : wumbuk              
    XML source code generated on : {now}
    -->\n'''
    
    with open(targetPath, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(pretty_str)

    logging.info(f"add_per_instance_parameters_finished")
   # print(f"ARXML file {targetPath} updated with new PER-INSTANCE-PARAMETERS")
    
    
    
"""

def convertConfigXml2ARXMLFiles(xmlConfigPath:string,targetPath:string,modelName):
    parser=None
    doc=parsexml_(xmlConfigPath,parser)
    source=doc.getroot()
    if modelName=="":
        modelName=source.xpath('//ns:SwcComponent',namespaces=namespaces)[0].attrib["NAME"]

    #print("modelName:",modelName)
    init_path2AR_Package(source)
    init_id_name_mappings(source)
    init_idport_period_mappings(source)
    init_package_paths(source)
    init_idport_portname_interfacename_elementname_mappings(source)
    init_swc_component_config(source)
    exportedXmlFilePackaging=source.xpath('//ns:Packaging-Options',namespaces=namespaces)[0].attrib["EXPORTED-XML-FILE-PACKAGING"]

    suffixList=["_datatype.arxml","_interface.arxml","_component.arxml","_implementation.arxml","_timing.arxml"]
    if exportedXmlFilePackaging=="Modular":
        AUTOSAR=supermod_all.AUTOSAR.factory()
        arPackages=supermod_all.AR_PACKAGESType.factory()
        AUTOSAR.set_AR_PACKAGES(arPackages)
        for i,suffix in enumerate(suffixList):
            if i==0:
                arPackages.set_AR_PACKAGE([])
                datatypePackage=convertConfig2DataType(xmlConfigPath,os.path.join(targetPath,"test_datatype_test.arxml"))
                arPackages.add_AR_PACKAGE(datatypePackage)
            elif i==1:
                arPackages.set_AR_PACKAGE([])
                interfacePackage=convertConfig2Interface(xmlConfigPath,os.path.join(targetPath,"test_interface_test.arxml"))
                arPackages.add_AR_PACKAGE(interfacePackage)
            elif i==2:
                arPackages.set_AR_PACKAGE([])
                componentPackage=convertConfig2Component(xmlConfigPath,os.path.join(targetPath,"test_component_test.arxml"))
                temp=copy.deepcopy(componentPackage)
                temp.set_AR_PACKAGES(None)
                arPackages.add_AR_PACKAGE(temp)
            elif i==3:
                arPackages.set_AR_PACKAGE([])
                implementationPackage=convertConfig2Implementation(xmlConfigPath,os.path.join(targetPath,"test_implementation_test.arxml"),modelName)
                temp=copy.deepcopy(implementationPackage)
                temp.set_ELEMENTS(None)
                arPackages.add_AR_PACKAGE(temp)
            else:
                arPackages.set_AR_PACKAGE([])
                timingPackage=convertConfig2Timing(xmlConfigPath,os.path.join(targetPath,"test_timing_test.arxml"))
                arPackages.add_AR_PACKAGE(timingPackage)

            f=open(os.path.join(targetPath,modelName+suffix),'w')
            sys.stdout=f
            sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            now=datetime.now()
            date_time=now.strftime("%Y-%m-%d,%H:%M:%S")
            sys.stdout.write('''<!--
        Auto generated XML Component Description for model 
        Model version                : 1.42                
        Author                       : wumbuk              
        XML source code generated on : {0}
        -->\n'''.format(date_time))
            rootTag = 'AUTOSAR'
            AUTOSAR.export(
                sys.stdout, 0, name_=rootTag,
                namespacedef_='',
                pretty_print=True)
            f.close()  
            if i==2:
                add_per_instance_parameters(xmlConfigPath,os.path.join(targetPath,modelName+"_component.arxml"))


    else:
        convertConfig2DataType(xmlConfigPath,os.path.join(targetPath,"test_datatype_test.arxml"))
        convertConfig2Interface(xmlConfigPath,os.path.join(targetPath,"test_interface_test.arxml"))
        convertConfig2Component(xmlConfigPath,os.path.join(targetPath,"test_component_test.arxml"))
        convertConfig2Implementation(xmlConfigPath,os.path.join(targetPath,"test_implementation_test.arxml"),modelName)
        convertConfig2Timing(xmlConfigPath,os.path.join(targetPath,"test_timing_test.arxml"))
        f=open(os.path.join(targetPath,modelName+".arxml"),'w')
        sys.stdout=f
        sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        now=datetime.now()
        date_time=now.strftime("%Y-%m-%d,%H:%M:%S")
        sys.stdout.write('''<!--
    Auto generated XML Component Description for model 
    Model version                : 1.42                
    Author                       : wumbuk              
    XML source code generated on : {0}
    -->\n'''.format(date_time))
        rootTag = 'AUTOSAR'
        AUTOSAR=path2AR_Package["/"]
        AUTOSAR.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
        f.close()  
     

        add_per_instance_parameters(xmlConfigPath,os.path.join(targetPath,modelName+".arxml"))

"""


import traceback
import sys
import os
from datetime import datetime

def convertConfigXml2ARXMLFiles(xmlConfigPath: str, targetPath: str, modelName):
    log_file_path = r"I:\log.txt"

    try:
        parser = None
        doc = parsexml_(xmlConfigPath, parser)
        source = doc.getroot()
        if modelName == "":
            modelName = source.xpath('//ns:SwcComponent', namespaces=namespaces)[0].attrib["NAME"]

        init_path2AR_Package(source)
        init_id_name_mappings(source)
        init_idport_period_mappings(source)
        init_package_paths(source)
        init_idport_portname_interfacename_elementname_mappings(source)
        init_swc_component_config(source)
        exportedXmlFilePackaging = source.xpath('//ns:Packaging-Options', namespaces=namespaces)[0].attrib["EXPORTED-XML-FILE-PACKAGING"]

        suffixList = ["_datatype.arxml", "_interface.arxml", "_component.arxml", "_implementation.arxml", "_timing.arxml"]
        if exportedXmlFilePackaging == "Modular":
            AUTOSAR = supermod_all.AUTOSAR.factory()
            arPackages = supermod_all.AR_PACKAGESType.factory()
            AUTOSAR.set_AR_PACKAGES(arPackages)

            for i, suffix in enumerate(suffixList):
                try:
                    if i == 0:
                        arPackages.set_AR_PACKAGE([])
                        datatypePackage = convertConfig2DataType(xmlConfigPath, os.path.join(targetPath, "test_datatype_test.arxml"))
                        arPackages.add_AR_PACKAGE(datatypePackage)
                    elif i == 1:
                        arPackages.set_AR_PACKAGE([])
                        interfacePackage = convertConfig2Interface(xmlConfigPath, os.path.join(targetPath, "test_interface_test.arxml"))
                        arPackages.add_AR_PACKAGE(interfacePackage)
                    elif i == 2:
                        arPackages.set_AR_PACKAGE([])
                        componentPackage = convertConfig2Component(xmlConfigPath, os.path.join(targetPath, "test_component_test.arxml"))
                        temp = copy.deepcopy(componentPackage)
                        temp.set_AR_PACKAGES(None)
                        arPackages.add_AR_PACKAGE(temp)
                    elif i == 3:
                        arPackages.set_AR_PACKAGE([])
                        implementationPackage = convertConfig2Implementation(xmlConfigPath, os.path.join(targetPath, "test_implementation_test.arxml"), modelName)
                        temp = copy.deepcopy(implementationPackage)
                        temp.set_ELEMENTS(None)
                        arPackages.add_AR_PACKAGE(temp)
                    else:
                        arPackages.set_AR_PACKAGE([])
                        timingPackage = convertConfig2Timing(xmlConfigPath, os.path.join(targetPath, "test_timing_test.arxml"))
                        arPackages.add_AR_PACKAGE(timingPackage)

                    with open(os.path.join(targetPath, modelName + suffix), 'w', encoding='utf-8') as f:
                        sys.stdout = f
                        sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                        now = datetime.now()
                        date_time = now.strftime("%Y-%m-%d,%H:%M:%S")
                        sys.stdout.write(f'''<!--
        Auto generated XML Component Description for model 
        Model version                : 1.42                
        Author                       : wumbuk              
        XML source code generated on : {date_time}
        -->\n''')
                        rootTag = 'AUTOSAR'
                        AUTOSAR.export(
                            sys.stdout, 0, name_=rootTag,
                            namespacedef_='',
                            pretty_print=True)
                    
                    if i == 2:
                        add_per_instance_parameters(xmlConfigPath, os.path.join(targetPath, modelName + "_component.arxml"))

                except Exception as e:
                    with open(log_file_path, 'a', encoding='utf-8') as log:
                        log.write(f"\n[Error in file generation: {modelName + suffix}]\n")
                        traceback.print_exc(file=log)

        else:
            convertConfig2DataType(xmlConfigPath, os.path.join(targetPath, "test_datatype_test.arxml"))
            convertConfig2Interface(xmlConfigPath, os.path.join(targetPath, "test_interface_test.arxml"))
            convertConfig2Component(xmlConfigPath, os.path.join(targetPath, "test_component_test.arxml"))
            convertConfig2Implementation(xmlConfigPath, os.path.join(targetPath, "test_implementation_test.arxml"), modelName)
            convertConfig2Timing(xmlConfigPath, os.path.join(targetPath, "test_timing_test.arxml"))

            with open(os.path.join(targetPath, modelName + ".arxml"), 'w', encoding='utf-8') as f:
                sys.stdout = f
                sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d,%H:%M:%S")
                sys.stdout.write(f'''<!--
    Auto generated XML Component Description for model 
    Model version                : 1.42                
    Author                       : wumbuk              
    XML source code generated on : {date_time}
    -->\n''')
                rootTag = 'AUTOSAR'
                AUTOSAR = path2AR_Package["/"]
                AUTOSAR.export(
                    sys.stdout, 0, name_=rootTag,
                    namespacedef_='',
                    pretty_print=True)

            add_per_instance_parameters(xmlConfigPath, os.path.join(targetPath, modelName + ".arxml"))

    except Exception as e:
        with open(log_file_path, 'a', encoding='utf-8') as log:
            log.write(f"\n[Critical error in convertConfigXml2ARXMLFiles: {modelName}]\n")
            traceback.print_exc(file=log)



if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    #main()
    
    xmlConfigPath="I:\\testM\\test_configuration.xml"
    aRXMLFilesPathList=["I:\\testM\ARXMLS\\test_component.arxml",
                        "I:\\testM\ARXMLS\\test_datatype.arxml",
                        "I:\\testM\ARXMLS\\test_implementation.arxml",
                        "I:\\testM\ARXMLS\\test_interface.arxml",
                        "I:\\testM\ARXMLS\\test_timing.arxml"]
    
   
    xmlConfigPath="I:\\testM\\test_configuration.xml"
    targetPath="I:\\testM\\testGenerate"
    convertConfigXml2ARXMLFiles(xmlConfigPath,targetPath)