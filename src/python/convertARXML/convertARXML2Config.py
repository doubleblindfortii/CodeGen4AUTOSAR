import os
import string
import sys
from lxml import etree as etree_
#import autosar_config_api as supermod_config
#import autosar_all_api as supermod_all
#import utils4ParseARXML 
from . import autosar_config_api as supermod_config
from . import autosar_all_api as supermod_all
from . import utils4ParseARXML 
import uuid
import re as re_
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


path2Nodemap={}
nodemap2Path={}
id2Config={}

namespaces = {'ar': 'http://autosar.org/schema/r4.0','ns': 'http://autosar_configuration.wumbuk'}


"""
该函数用来匹配路径，返回匹配的路径。
参数：path，需要匹配的路径
        path2Nodemap，路径到节点的映射
比如，path=DataTypes/Double/1，path2Nodemap中有DataTypes,DataTypes/Double,DataTypes/Double/2，DataTypes/Double/3，DataTypes/Double/4
则返回DataTypes/Double
如果不匹配，返回None
"""
def get_longest_matched_path(path,path2Nodemap):
    path_list=path.split('/')
    for i in range(len(path_list),0,-1):
        path_temp="/".join(path_list[:i])
        if path_temp in path2Nodemap.keys():
            return path_temp
    return None

    
def extract_short_names(rootNode,parent_names=[],res={}):
    short_name_elements=rootNode.xpath('ar:SHORT-NAME', namespaces=namespaces)
    flag=False
    if len(short_name_elements)==1:
        parent_names.append(short_name_elements[0].text)
        pathAbs="/".join(parent_names)
        if pathAbs not in path2Nodemap.keys():
            path2Nodemap[pathAbs]=rootNode
            nodemap2Path[rootNode]=pathAbs
        
        res[pathAbs]=rootNode
        flag=True
    for child in rootNode:
        extract_short_names(child,parent_names,res)
    if flag==True:
        parent_names.pop()
    
    
def intergrate2Nodes(rootNode1,rootNode2):
    tempOld=path2Nodemap.copy()
    tempNew={}
    extract_short_names(rootNode2,res=tempNew)
    record=[]
    for key in tempNew.keys():
        if key not in tempOld.keys():
            matched_path=get_longest_matched_path(key,tempOld)
            if matched_path:
                parts=key.split('/')
                index_temp=parts.index(matched_path.split('/')[0])
                result_path="/".join(parts[:index_temp+len(matched_path.split('/'))+1])
                if result_path not in record:
                    #f=open("I:\\testM\\test_configuration_testhaha2Pre.xml",'w')
                    #print(etree_.tostring(tempOld[matched_path], pretty_print=True).decode('utf-8'),file=f)
                    record.append(result_path)
                    arPackages=etree_.SubElement(tempOld[matched_path],"AR-PACKAGES")
                    arPackages.append(tempNew[result_path])

                    #f=open("I:\\testM\\test_configuration_testhaha2.xml",'w')
                    #print(etree_.tostring(path2Nodemap[matched_path], pretty_print=True).decode('utf-8'),file=f)
            else:
                result_path=key.split('/')[0]
                if result_path not in record:
                    record.append(result_path)
                    rootNode1[0].append(tempNew[result_path])
  #  f=open("I:\\testM\\test_configuration_testhaha.xml",'w')
  #  print(etree_.tostring(rootNode1, pretty_print=True).decode('utf-8'),file=f)
    return rootNode1


#写一个函数，将fileList中标明的arxml做合并，返回根节点
#注意这是lxml的根节点
def integrateNodes2One(fileList):
    if len(fileList)>0:
        parser = None
        doc = parsexml_(fileList[0], parser)
        #print(etree_.tostring(doc, pretty_print=True, encoding='unicode'))
        rootNodeTemp = doc.getroot()
        extract_short_names(rootNodeTemp)
    if len(fileList)>1:
        for file in fileList[1:]:
            parser = None
            doc = parsexml_(file, parser)
            rootNode = doc.getroot()

            implementationDataTypes=rootNode.xpath('//ar:IMPLEMENTATION-DATA-TYPE', namespaces=namespaces)
            #if len(implementationDataTypes)>0:
            #    for implementationDataType in implementationDataTypes:
            #       test=implementationDataType.getparent().getparent().getparent()
                

            rootNodeTemp=intergrate2Nodes(rootNodeTemp,rootNode)
    #print(etree_.tostring(doc, pretty_print=True, encoding='unicode'))
    return rootNodeTemp

def convertSwAddrMethod2ConfigAPI(swAddrmethod,swAddrMethodPkg,swAddrMethod_config):
    swAddrMethod_config.set_ID(swAddrmethod.attrib.get('UUID'))
    name=swAddrmethod.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    section_type=swAddrmethod.xpath('ar:SECTION-TYPE', namespaces=namespaces)[0].text
    swAddrMethod_config.set_NAME(name)
    swAddrMethod_config.set_SECTION_TYPE(section_type)
    swAddrMethod_config.set_EXPORT_XML_FILE("$ModelName_datatype.arxml")
    swAddrMethod_config.set_PACKAGE(utils4ParseARXML.filtePath(swAddrMethodPkg))

def convertSenderReceiverInterface2ConfigAPI(senderReceiverInterface,senderReceiverInterfacePkg,dataElement,senderReceiverInterfaceConfig):
    senderReceiverInterfaceConfig.set_ID(senderReceiverInterface.attrib.get('UUID'))
    name=senderReceiverInterface.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    is_service=senderReceiverInterface.xpath('ar:IS-SERVICE', namespaces=namespaces)[0].text
    senderReceiverInterfaceConfig.set_IS_SERVICE(is_service)
    senderReceiverInterfaceConfig.set_NAME(name)
    senderReceiverInterfaceConfig.set_PACKAGE(utils4ParseARXML.filtePath(senderReceiverInterfacePkg))
    dataElementConfigList=[]
    for dataElementTemp in dataElement:
        dataElementConfig=supermod_config.Variable_Data_Prototype_Type()
        dataElementConfig.set_ID(dataElementTemp.attrib.get('UUID'))
        name=dataElementTemp.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
        dataElementConfig.set_NAME(name)
        dataElementConfig.set_DISPLAY_FORMAT("")
        swCalibrationAccess=dataElementTemp.xpath('.//ar:SW-CALIBRATION-ACCESS', namespaces=namespaces)
        swCalibrationAccessConfig="ReadOnly" if swCalibrationAccess[0].text=="READ-ONLY" else "NONE"
        dataElementConfig.set_Sw_Calibration_Access(swCalibrationAccessConfig)
        dataElementConfig.set_Sw_AddrMethod("None")
        typeTrefConfig=supermod_config.Type_TrefType()
        if len(dataElementTemp.xpath('ar:TYPE-TREF', namespaces=namespaces)):
            typeTrefConfig.set_DEST(dataElementTemp.xpath('ar:TYPE-TREF', namespaces=namespaces)[0].attrib.get('DEST'))
            typeTrefConfig.set_valueOf_(dataElementTemp.xpath('ar:TYPE-TREF', namespaces=namespaces)[0].text)
        else:
            typeTrefConfig.set_DEST("IMPLEMENTATION-DATA-TYPE")
            typeTrefConfig.set_valueOf_("/DataTypes/Double")
        dataElementConfig.set_Type_Tref(typeTrefConfig)
        dataElementConfigList.append(dataElementConfig)
    dataElements=supermod_config.Data_Elements_Type()
    dataElements.set_Variable_Data_Prototype(dataElementConfigList)
    senderReceiverInterfaceConfig.set_Data_Elements(dataElements)

def convertReceiverPortPrototype2ConfigAPI(rPortPrototype,receiverPortPrototypeConfig):
    receiverPortPrototypeConfig.set_ID(rPortPrototype.attrib.get('UUID'))
    id2Config[rPortPrototype.attrib.get('UUID')]=receiverPortPrototypeConfig
    name=rPortPrototype.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    receiverPortPrototypeConfig.set_NAME(name) 
    interfaceRef=rPortPrototype.xpath('ar:REQUIRED-INTERFACE-TREF', namespaces=namespaces)[0].text
    interfaceRef=path2Nodemap[utils4ParseARXML.defiltePath(interfaceRef)]
    idInterfaceRef=interfaceRef.attrib.get('UUID')
    receiverPortPrototypeConfig.set_INTERFACE_REF_ID(idInterfaceRef)
    nonqueuedRececeiverComSpecs=rPortPrototype.xpath('ar:REQUIRED-COM-SPECS/ar:NONQUEUED-RECEIVER-COM-SPEC', namespaces=namespaces)
# nonqueuedRececeiverComSpecsList=[]
    receiverPortSpecsConfig=supermod_config.ReceiverPort_Specs_Type()
    if (len(nonqueuedRececeiverComSpecs)>=1):
        for nonqueuedRececeiverComSpec in nonqueuedRececeiverComSpecs:
            nonqueuedRececeiverComSpecsConfig=supermod_config.Nonqueued_Receiver_Com_Spec_Type()
            dataElementRef=nonqueuedRececeiverComSpec.xpath('ar:DATA-ELEMENT-REF', namespaces=namespaces)[0].text
            dataElementRef=path2Nodemap[utils4ParseARXML.defiltePath(dataElementRef)]
            idDataElementRef=dataElementRef.attrib.get('UUID')
            nonqueuedRececeiverComSpecsConfig.set_ELEMENT_REF_ID(idDataElementRef)
            
            aliveTimeout=nonqueuedRececeiverComSpec.xpath('ar:ALIVE-TIMEOUT', namespaces=namespaces)[0].text
            handleNeverReceived=nonqueuedRececeiverComSpec.xpath('ar:HANDLE-NEVER-RECEIVED', namespaces=namespaces)[0].text
            init_Value_all_list=nonqueuedRececeiverComSpec.xpath('ar:INIT-VALUE', namespaces=namespaces)
            if len(init_Value_all_list)==1:
                init_value_config=supermod_config.Init_Value_Type()
                initValue_all=init_Value_all_list[0]
                constant_reference_all=initValue_all.xpath('ar:CONSTANT-REFERENCE', namespaces=namespaces)
                numeriacal_value_specification_all=initValue_all.xpath('ar:NUMERICAL-VALUE-SPECIFICATION', namespaces=namespaces)
                if len(constant_reference_all)==1:
                    constant_reference_config=supermod_config.Constant_Reference_Type()
                    init_value_config.set_Constant_Reference(constant_reference_config)
                    constant_ref_path=constant_reference_all[0].xpath('ar:CONSTANT-REF', namespaces=namespaces)[0].text
                    constant_node=path2Nodemap[utils4ParseARXML.defiltePath(constant_ref_path)]
                    constant_id=constant_node.attrib.get('UUID')
                    constant_reference_config.set_CONSTANT_SPECIFICATION_REF_ID(constant_id)
                elif len(numeriacal_value_specification_all)==1:
                    numeraical_value_specification_config=supermod_config.NUMERICAL_VALUE_SPECIFICATION_Type()
                    init_value_config.set_NUMERICAL_VALUE_SPECIFICATION(numeraical_value_specification_config)
                    numeraical_value_specification_config.build(numeriacal_value_specification_all[0])
                nonqueuedRececeiverComSpecsConfig.set_Init_Value(init_value_config)

            #else:
            #    initValue="0"
            nonqueuedRececeiverComSpecsConfig.set_Alive_Timeout(aliveTimeout)
            nonqueuedRececeiverComSpecsConfig.set_Handle_Nerver_Received(handleNeverReceived)
            
        # nonqueuedRececeiverComSpecsList.append(nonqueuedRececeiverComSpecsConfig)
            receiverPortSpecsConfig.add_Nonqueued_Receiver_Com_Spec(nonqueuedRececeiverComSpecsConfig)
    else:
        print("ReceiverPort的REQUIRED-COM-SPECS个数为0")
    receiverPortPrototypeConfig.set_ReceiverPort_Specs(receiverPortSpecsConfig)

def convertSenderPortPrototype2ConfigAPI(pPortPrototype,senderPortPrototypeConfig):
    senderPortPrototypeConfig.set_ID(pPortPrototype.attrib.get('UUID'))
    id2Config[pPortPrototype.attrib.get('UUID')]=senderPortPrototypeConfig
    
    name=pPortPrototype.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    senderPortPrototypeConfig.set_NAME(name) 
    interfaceRef=pPortPrototype.xpath('ar:PROVIDED-INTERFACE-TREF', namespaces=namespaces)[0].text
    interfaceRef=path2Nodemap[utils4ParseARXML.defiltePath(interfaceRef)]
    idInterfaceRef=interfaceRef.attrib.get('UUID')
    senderPortPrototypeConfig.set_INTERFACE_REF_ID(idInterfaceRef)
    nonqueuedSenderComSpecs=pPortPrototype.xpath('ar:PROVIDED-COM-SPECS/ar:NONQUEUED-SENDER-COM-SPEC', namespaces=namespaces)
# nonqueuedRececeiverComSpecsList=[]
    senderPortSpecsConfig=supermod_config.SenderPort_Specs_Type()
    if (len(nonqueuedSenderComSpecs)>=1):
        for nonqueuedSenderComSpec in nonqueuedSenderComSpecs:
            nonqueuedSenderComSpecsConfig=supermod_config.Nonqueued_Sender_Com_Spec_Type()
            dataElementRef=nonqueuedSenderComSpec.xpath('ar:DATA-ELEMENT-REF', namespaces=namespaces)[0].text
            dataElementRef=path2Nodemap[utils4ParseARXML.defiltePath(dataElementRef)]
            idDataElementRef=dataElementRef.attrib.get('UUID')
            nonqueuedSenderComSpecsConfig.set_ELEMENT_REF_ID(idDataElementRef)
            init_Value_all_list=nonqueuedSenderComSpec.xpath('ar:INIT-VALUE', namespaces=namespaces)
            if len(init_Value_all_list)==1:
                init_value_config=supermod_config.Init_Value_Type()
                initValue_all=init_Value_all_list[0]
                constant_reference_all=initValue_all.xpath('ar:CONSTANT-REFERENCE', namespaces=namespaces)
                numeriacal_value_specification_all=initValue_all.xpath('ar:NUMERICAL-VALUE-SPECIFICATION', namespaces=namespaces)
                if len(constant_reference_all)==1:
                    constant_reference_config=supermod_config.Constant_Reference_Type()
                    init_value_config.set_Constant_Reference(constant_reference_config)
                    constant_ref_path=constant_reference_all[0].xpath('ar:CONSTANT-REF', namespaces=namespaces)[0].text
                    constant_node=path2Nodemap[utils4ParseARXML.defiltePath(constant_ref_path)]
                    constant_id=constant_node.attrib.get('UUID')
                    constant_reference_config.set_CONSTANT_SPECIFICATION_REF_ID(constant_id)
                elif len(numeriacal_value_specification_all)==1:
                    numeraical_value_specification_config=supermod_config.NUMERICAL_VALUE_SPECIFICATION_Type()
                    init_value_config.set_NUMERICAL_VALUE_SPECIFICATION(numeraical_value_specification_config)
                    numeraical_value_specification_config.build(numeriacal_value_specification_all[0])
                nonqueuedSenderComSpecsConfig.set_Init_Value(init_value_config)
            
        # nonqueuedRececeiverComSpecsList.append(nonqueuedRececeiverComSpecsConfig)
            
            senderPortSpecsConfig.add_Nonqueued_Sender_Com_Spec(nonqueuedSenderComSpecsConfig)
            
    else:
        print("SenderPort的PROVIDED-COM-SPECS为0")
    senderPortPrototypeConfig.set_SenderPort_Specs(senderPortSpecsConfig)

def convertVariableDataPrototype2ConfigAPI(variableDataPrototype,variableDataPrototypeConfig):
    variableDataPrototypeConfig.set_ID(variableDataPrototype.attrib.get('UUID'))
    name=variableDataPrototype.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    variableDataPrototypeConfig.set_NAME(name)
    variableDataPrototypeConfig.set_DISPLAY_FORMAT("")
    swCalibrationAccess=variableDataPrototype.xpath('.//ar:SW-CALIBRATION-ACCESS', namespaces=namespaces)
    swCalibrationAccessConfig="ReadOnly" if swCalibrationAccess[0].text=="READ-ONLY" else "NONE"
    variableDataPrototypeConfig.set_Sw_Calibration_Access(swCalibrationAccessConfig)
    variableDataPrototypeConfig.set_Sw_AddrMethod("None")
    typeTrefConfig=supermod_config.Type_TrefType()
    typeTrefConfig.set_DEST(variableDataPrototype.xpath('ar:TYPE-TREF', namespaces=namespaces)[0].attrib.get('DEST'))
    typeTrefConfig.set_valueOf_(variableDataPrototype.xpath('ar:TYPE-TREF', namespaces=namespaces)[0].text)
    variableDataPrototypeConfig.set_Type_Tref(typeTrefConfig)
    init_value_list_all=variableDataPrototype.xpath('ar:INIT-VALUE', namespaces=namespaces)
    if len(init_value_list_all)==1:
        init_value_all=init_value_list_all[0]
        init_value_config=supermod_config.Init_Value_Type()
        variableDataPrototypeConfig.set_Init_Value(init_value_config)
        constant_reference_all=init_value_all.xpath('ar:CONSTANT-REFERENCE', namespaces=namespaces)
        numeriacal_value_specification_all=init_value_all.xpath('ar:NUMERICAL-VALUE-SPECIFICATION', namespaces=namespaces)
        if len(constant_reference_all)==1:
            constant_reference_config=supermod_config.Constant_Reference_Type()
            init_value_config.set_Constant_Reference(constant_reference_config)
            constant_ref_path=constant_reference_all[0].xpath('ar:CONSTANT-REF', namespaces=namespaces)[0].text
            constant_node=path2Nodemap[utils4ParseARXML.defiltePath(constant_ref_path)]
            constant_id=constant_node.attrib.get('UUID')
            constant_reference_config.set_CONSTANT_SPECIFICATION_REF_ID(constant_id)
        elif len(numeriacal_value_specification_all)==1:
            numeraical_value_specification_config=supermod_config.NUMERICAL_VALUE_SPECIFICATION_Type()
            init_value_config.set_NUMERICAL_VALUE_SPECIFICATION(numeraical_value_specification_config)
            numeraical_value_specification_config.build(numeriacal_value_specification_all[0])

def convertVariableAccessDataRead2ConfigAPI(variableAccess,variableAccessConfig):
    variableAccessConfig.set_ID(variableAccess.attrib.get('UUID'))
    portPrototypeRef=variableAccess.xpath('.//ar:PORT-PROTOTYPE-REF', namespaces=namespaces)[0].text
    #print(path2Nodemap)
    portPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(portPrototypeRef)]
    idPortPrototypeRef=portPrototypeRef.attrib.get('UUID')
    portPrototypeRefConfig=supermod_config.Port_Prototype_Ref_Type()
    portPrototypeRefConfig.set_PORT_REF_ID(idPortPrototypeRef)
    targetDataPrototypeRef=variableAccess.xpath('.//ar:TARGET-DATA-PROTOTYPE-REF', namespaces=namespaces)[0].text
    targetDataPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(targetDataPrototypeRef)]
    idTargetDataPrototypeRef=targetDataPrototypeRef.attrib.get('UUID')
    portPrototypeRefConfig.set_ELEMENT_REF_ID(idTargetDataPrototypeRef)
    variableAccessConfig.set_Port_Prototype_Ref(portPrototypeRefConfig)

def convertVariableAccessDataWrite2ConfigAPI(variableAccess,variableAccessConfig):
    variableAccessConfig.set_ID(variableAccess.attrib.get('UUID'))
    portPrototypeRef=variableAccess.xpath('.//ar:PORT-PROTOTYPE-REF', namespaces=namespaces)[0].text
    portPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(portPrototypeRef)]
    idPortPrototypeRef=portPrototypeRef.attrib.get('UUID')
    portPrototypeRefConfig=supermod_config.Port_Prototype_Ref_Type()
    portPrototypeRefConfig.set_PORT_REF_ID(idPortPrototypeRef)
    targetDataPrototypeRef=variableAccess.xpath('.//ar:TARGET-DATA-PROTOTYPE-REF', namespaces=namespaces)[0].text
    targetDataPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(targetDataPrototypeRef)]
    idTargetDataPrototypeRef=targetDataPrototypeRef.attrib.get('UUID')
    portPrototypeRefConfig.set_ELEMENT_REF_ID(idTargetDataPrototypeRef)
    variableAccessConfig.set_Port_Prototype_Ref(portPrototypeRefConfig)


def convertVariableAccessReadLocal2ConfigAPI(variableAccess,variableAccessConfig):
    variableAccessConfig.set_ID(variableAccess.attrib.get('UUID'))
    portPrototypeRef=variableAccess.xpath('.//ar:LOCAL-VARIABLE-REF', namespaces=namespaces)[0].text
    portPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(portPrototypeRef)]
    idPortPrototypeRef=portPrototypeRef.attrib.get('UUID')
    localPrototypeRefConfig=supermod_config.Local_Prototype_Ref_Type()
    localPrototypeRefConfig.set_LOCAL_REF_ID(idPortPrototypeRef)
    variableAccessConfig.set_Local_Prototype_Ref(localPrototypeRefConfig)

def convertVariableAccessWriteLocal2ConfigAPI(variableAccess,variableAccessConfig):
    variableAccessConfig.set_ID(variableAccess.attrib.get('UUID'))
    portPrototypeRef=variableAccess.xpath('.//ar:LOCAL-VARIABLE-REF', namespaces=namespaces)[0].text
    portPrototypeRef=path2Nodemap[utils4ParseARXML.defiltePath(portPrototypeRef)]
    idPortPrototypeRef=portPrototypeRef.attrib.get('UUID')
    localPrototypeRefConfig=supermod_config.Local_Prototype_Ref_Type()
    localPrototypeRefConfig.set_LOCAL_REF_ID(idPortPrototypeRef)
    variableAccessConfig.set_Local_Prototype_Ref(localPrototypeRefConfig)

def convertRunnableEntity2ConfigAPI(runnableEntity,runnableEntityConfig):
    #3.3.1 进行常规的转换
    runnableEntityConfig.set_ID(runnableEntity.attrib.get('UUID'))
    id2Config[runnableEntity.attrib.get('UUID')]=runnableEntityConfig
    name=runnableEntity.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
    runnableEntityConfig.set_NAME(name)
    canBeInvokedConcurrently=runnableEntity.xpath('ar:CAN-BE-INVOKED-CONCURRENTLY', namespaces=namespaces)[0].text
    runnableEntityConfig.set_Can_Be_Invoked_Concurrently(canBeInvokedConcurrently)
    symbol=runnableEntity.xpath('ar:SYMBOL', namespaces=namespaces)[0].text
    runnableEntityConfig.set_Symbol(symbol)
    eventsConfig=supermod_config.Events_Type()
    runnableEntityConfig.set_Events(eventsConfig)
    #3.3.2 进行Data-Read-Access的转换
    dataReadAccess=runnableEntity.xpath('ar:DATA-READ-ACCESSS', namespaces=namespaces)
    if len(dataReadAccess)>0:
        variableAccessList=[]
        variableAccesses=dataReadAccess[0].xpath('ar:VARIABLE-ACCESS', namespaces=namespaces)
        for variableAccess in variableAccesses:
            variableAccessConfig=supermod_config.Variable_Access_Type()
            convertVariableAccessDataRead2ConfigAPI(variableAccess,variableAccessConfig)

            variableAccessList.append(variableAccessConfig)
        dataReadAccessConfig=supermod_config.Data_Read_Access_Type()
        dataReadAccessConfig.set_Variable_Access(variableAccessList)
        runnableEntityConfig.set_Data_Read_Access(dataReadAccessConfig)
    
    #3.3.3 进行Data-Write-Access的转换
    dataWriteAccess=runnableEntity.xpath('ar:DATA-WRITE-ACCESSS', namespaces=namespaces)
    if len(dataWriteAccess)>0:
        variableAccessList=[]
        variableAccesses=dataWriteAccess[0].xpath('ar:VARIABLE-ACCESS', namespaces=namespaces)
        for variableAccess in variableAccesses:
            variableAccessConfig=supermod_config.Variable_Access_Type()
            convertVariableAccessDataWrite2ConfigAPI(variableAccess,variableAccessConfig)
            variableAccessList.append(variableAccessConfig)
        dataWriteAccessConfig=supermod_config.Data_Write_Access_Type()
        dataWriteAccessConfig.set_Variable_Access(variableAccessList)
        runnableEntityConfig.set_Data_Write_Access(dataWriteAccessConfig)
# runnableEntityList.append(runnableEntityConfig)

    #3.3.4 进行Read-Local-Variables的转换
    readLocalVariables=runnableEntity.xpath('ar:READ-LOCAL-VARIABLES', namespaces=namespaces)
    if len(readLocalVariables)>0:
        variableAccessList=[]
        variableAccesses=readLocalVariables[0].xpath('ar:VARIABLE-ACCESS', namespaces=namespaces)
        for variableAccess in variableAccesses:
            variableAccessConfig=supermod_config.Variable_Access_Type()
            convertVariableAccessReadLocal2ConfigAPI(variableAccess,variableAccessConfig)
            
            variableAccessList.append(variableAccessConfig)
        readLocalVariablesConfig=supermod_config.Read_Local_Access_Type()
        readLocalVariablesConfig.set_Variable_Access(variableAccessList)
        runnableEntityConfig.set_Read_Local_Access(readLocalVariablesConfig)

    #3.3.5 进行Write-Local-Variables的转换
    writeLocalVariables=runnableEntity.xpath('ar:WRITTEN-LOCAL-VARIABLES', namespaces=namespaces)
    if len(writeLocalVariables)>0:
        variableAccessList=[]
        variableAccesses=writeLocalVariables[0].xpath('ar:VARIABLE-ACCESS', namespaces=namespaces)
        for variableAccess in variableAccesses:
            variableAccessConfig=supermod_config.Variable_Access_Type()
            convertVariableAccessWriteLocal2ConfigAPI(variableAccess,variableAccessConfig)
            variableAccessList.append(variableAccessConfig)
        writeLocalVariablesConfig=supermod_config.Write_Local_Access_Type()
        writeLocalVariablesConfig.set_Variable_Access(variableAccessList)
        runnableEntityConfig.set_Write_Local_Access(writeLocalVariablesConfig)

def convertEventPrototype2ConfigAPI(timingEvent,eventPrototypeConfig):
        eventPrototypeConfig.set_ID(timingEvent.attrib.get('UUID'))
        name=timingEvent.xpath('ar:SHORT-NAME', namespaces=namespaces)[0].text
        eventPrototypeConfig.set_Event_Type("TimingEvent")
        eventPrototypeConfig.set_Event_Name(name)
        period=timingEvent.xpath('ar:PERIOD', namespaces=namespaces)[0].text
        eventPrototypeConfig.set_Period(period)


def convertApplicationSwComponentType2ConfigAPI(applicationSwcComponent,swcComponent_config,atomicComponents_config,autosar_Dictionary_config,xmlOptions_config,rootObj_config,index_component,rootNode):
    swcComponent_config.set_ID(applicationSwcComponent.attrib.get('UUID'))
    ports_config=supermod_config.Ports_Type()
    receiverPorts_config=supermod_config.ReceiverPorts_Type()
    senderPorts_config=supermod_config.SenderPorts_Type()
    ports_config.set_ReceiverPorts(receiverPorts_config)
    ports_config.set_SenderPorts(senderPorts_config)
    swcComponent_config.set_Ports(ports_config)
    atomicComponents_config.set_SwcComponent(swcComponent_config)
    autosar_Dictionary_config.set_AtomicComponents(atomicComponents_config)
    irv_config=supermod_config.IRV_Type()
    irvs_config=supermod_config.IRVS_Type()
    irv_config.set_IRVS(irvs_config)
    swcComponent_config.set_IRV(irv_config)
    runnables_config=supermod_config.Runnables_Type()
    swcComponent_config.set_Runnables(runnables_config)
    xmlOptions_config.get_View_And_Edit_Options().set_XML_OPTIONS_SOURCE("Inlined in this model")
    xmlOptions_config.get_Packaging_Options().set_EXPORTED_XML_FILE_PACKAGING("Single File")
    componentXMLOptions_config=supermod_config.Component_XML_Options_Type()
    swcComponent_config.set_Component_XML_Options(componentXMLOptions_config)
    componentXMLOptions_config.set_Package(utils4ParseARXML.filtePath(nodemap2Path[applicationSwcComponent].split('/')[0]))
    #print("hello")
    swcComponent_config.set_NAME(name_swcComponent_global)
    #print(swcComponent_config.)
    swcComponent_config.set_KIND("Application")
    swcComponent_config.set_EXPORT_XML_FILE("$ModelName_component.arxml")



    rootObj_config.get_AUTOSAR_Dictionary().append(autosar_Dictionary_config)
    #1. 首先进行datatype有关的转换
    #1.1 进行swBaseType有关的转换
    swBaseTypes=rootNode.xpath('//ar:SW-BASE-TYPE', namespaces=namespaces)
    swBaseTypePkgList=utils4ParseARXML.parseSWBASETYPE(swBaseTypes)
    if len(swBaseTypePkgList)==1:
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_XML_Options().get_Additional_Packages().set_SWBASETYPE_PACKAGE(utils4ParseARXML.filtePath(swBaseTypePkgList[0]))
    else:
        print("SW-BASE-TYPE的包路径不唯一，无法进行转换")
    #1.2 进行SW-ADDR-METHOD有关的转换
    swAddrMethods=rootNode.xpath('//ar:SW-ADDR-METHOD', namespaces=namespaces)
    if len(swAddrMethods)>0:
        swAddrMethodPkgList=utils4ParseARXML.parseSWADDRMETHOD(swAddrMethods)
        swAddrMethodList=[]
        for swAddrmethod,swAddrMethodPkg in zip(swAddrMethods,swAddrMethodPkgList):
            swAddrMethod_config=supermod_config.SwAddrMethod_Prototype_Type()
            convertSwAddrMethod2ConfigAPI(swAddrmethod,swAddrMethodPkg,swAddrMethod_config)
            swAddrMethodList.append(swAddrMethod_config)
            autosar_Dictionary_config.get_XML_Options().get_Package_Paths().set_DATATYPE_PACKAGE(utils4ParseARXML.filtePath(swAddrMethodPkg).split("/")[0])
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_Methods().get_SwAddrMethods().set_SwAddrMethod_Prototype(swAddrMethodList)
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_XML_Options().get_Additional_Packages().set_SWADDRESS_METHOD_PACKAGE(utils4ParseARXML.filtePath(swAddrMethodPkgList[0]))
        
    #1.3 进行有关DataType指定的包的转换
    implementationDataType=rootNode.xpath('//ar:IMPLEMENTATION-DATA-TYPE', namespaces=namespaces)
    implementationDataTypePkgList=utils4ParseARXML.parseImplementationDataType(implementationDataType)
    if len(implementationDataTypePkgList)==1:
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_XML_Options().get_Package_Paths().set_DATATYPE_PACKAGE(utils4ParseARXML.filtePath(implementationDataTypePkgList[0]))
    else:
        print("DATATYPE包路径不唯一，无法进行转换")

    #1.4 进行ConstantSpecification Package包的转换
    constantSpecifications=rootNode.xpath('//ar:CONSTANT-SPECIFICATION', namespaces=namespaces)
    constantSpecificationPkgList=utils4ParseARXML.parseConstantSpecification(constantSpecifications)
    if len(constantSpecificationPkgList)==1:
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_XML_Options().get_Additional_Packages().set_CONSTANT_SPECIFICATION_PACKAGE(utils4ParseARXML.filtePath(constantSpecificationPkgList[0]))
    elif len(constantSpecificationPkgList)==0:
        rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_XML_Options().get_Additional_Packages().set_CONSTANT_SPECIFICATION_PACKAGE("/pkg/dt/Ground")
    else:
        print("CONSTANT-SPECIFICATION包路径不唯一，无法进行转换")
    #2. 然后进行interface有关的转换
    #2.1 进行各个Interface的转换
    senderReceiverInterfaces=rootNode.xpath('//ar:SENDER-RECEIVER-INTERFACE', namespaces=namespaces)
    senderReceiverInterfacesPkgList,dataElementList=utils4ParseARXML.parseSenderReceiverInterface(senderReceiverInterfaces)
    senderReceiverInterfaceList=[]
    for senderReceiverInterface,senderReceiverInterfacePkg,dataElement in zip(senderReceiverInterfaces,senderReceiverInterfacesPkgList,dataElementList):
        senderReceiverInterfaceConfig=supermod_config.Sender_Receiver_Interface_Type()
        convertSenderReceiverInterface2ConfigAPI(senderReceiverInterface,senderReceiverInterfacePkg,dataElement,senderReceiverInterfaceConfig)
        senderReceiverInterfaceList.append(senderReceiverInterfaceConfig)
        autosar_Dictionary_config.get_XML_Options().get_Package_Paths().set_INTERFACE_PACKAGE(utils4ParseARXML.filtePath(senderReceiverInterfacePkg))
    rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_Interfaces().get_S_R_Interfaces().set_Sender_Receiver_Interface(senderReceiverInterfaceList)

    #3. 然后进行有关component有关的转换
    #3.1 进行PORTS的转换
    #3.1.1 进行ReceiverPort的转换
    rPortPrototypes=rootNode.xpath('//ar:R-PORT-PROTOTYPE', namespaces=namespaces)
    ReceiverPortPrototypeList=[]
    for rPortPrototype in rPortPrototypes:
        receiverPortPrototypeConfig=supermod_config.ReceiverPort_Prototype_Type()
        convertReceiverPortPrototype2ConfigAPI(rPortPrototype,receiverPortPrototypeConfig)

        ReceiverPortPrototypeList.append(receiverPortPrototypeConfig)
    rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().set_ReceiverPort_Prototype(ReceiverPortPrototypeList)

    #3.1.2 进行SenderPort的转换
    pPortPrototypes=rootNode.xpath('//ar:P-PORT-PROTOTYPE', namespaces=namespaces)
    senderPortPrototypeList=[]
    for pPortPrototype in pPortPrototypes:
        senderPortPrototypeConfig=supermod_config.SenderPort_Prototype_Type()
        convertSenderPortPrototype2ConfigAPI(pPortPrototype,senderPortPrototypeConfig)

        senderPortPrototypeList.append(senderPortPrototypeConfig)
    rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_AtomicComponents().get_SwcComponent().get_Ports().get_SenderPorts().set_SenderPort_Prototype(senderPortPrototypeList)
    

    #3.2进行IRV的转换
    implicitInterRunnableVariables=rootNode.xpath('//ar:IMPLICIT-INTER-RUNNABLE-VARIABLES', namespaces=namespaces)[0]
    variableDataPrototypes=implicitInterRunnableVariables.xpath('ar:VARIABLE-DATA-PROTOTYPE', namespaces=namespaces)
    variableDataPrototypeList=[]
    for variableDataPrototype in variableDataPrototypes:
        variableDataPrototypeConfig=supermod_config.Variable_Data_Prototype_Type()
        convertVariableDataPrototype2ConfigAPI(variableDataPrototype,variableDataPrototypeConfig)
        variableDataPrototypeList.append(variableDataPrototypeConfig)
    rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_AtomicComponents().get_SwcComponent().get_IRV().get_IRVS().set_Variable_Data_Prototype(variableDataPrototypeList)
    
    #3.3 进行RUNNABLE-ENTITY的转换
    runnableEntitys=rootNode.xpath('//ar:RUNNABLE-ENTITY', namespaces=namespaces)
    runnableEntityList=[]
    for runnableEntity in runnableEntitys:
        runnableEntityConfig=supermod_config.Runnable_Entity_Type()
        convertRunnableEntity2ConfigAPI(runnableEntity,runnableEntityConfig)


        runnableEntityList.append(runnableEntityConfig)
    rootObj_config.get_AUTOSAR_Dictionary()[index_component].get_AtomicComponents().get_SwcComponent().get_Runnables().set_Runnable_Entity(runnableEntityList)
    3.4 #进行Event和RPORT的转换
    timingEvents=rootNode.xpath('//ar:TIMING-EVENT', namespaces=namespaces)
    for timingEvent in timingEvents:
        runnableEntityRef=timingEvent.xpath('ar:START-ON-EVENT-REF', namespaces=namespaces)[0].text
        runnableEntityRef=path2Nodemap[utils4ParseARXML.defiltePath(runnableEntityRef)]
        #3.4.1 进行Event的转换
        eventPrototypeConfig=supermod_config.Event_Prototype_Type()
        convertEventPrototype2ConfigAPI(timingEvent,eventPrototypeConfig)

        runnableEntityRefConfig=id2Config[runnableEntityRef.attrib.get('UUID')]
        runnableEntityRefConfig.get_Events().add_Event_Prototype(eventPrototypeConfig)
        #3.4.2 进行RPORT的转换
        #if runnableEntityRefConfig.get_Data_Read_Access() is not None:
            #variableAccessesConfig=runnableEntityRefConfig.get_Data_Read_Access().get_Variable_Access()
            #if len(variableAccessesConfig)>0:
                #idPortRef=variableAccessesConfig[0].get_Port_Prototype_Ref().get_PORT_REF_ID()
                #portPrototypeRef=id2Config[idPortRef]
                #portPrototypeRef.set_Period(timingEvent.xpath('ar:PERIOD', namespaces=namespaces)[0].text)
    #3.5进行Component-XML-Options的转换
    swc_internal_behavior=rootNode.xpath('//ar:SWC-INTERNAL-BEHAVIOR', namespaces=namespaces)
    if len(swc_internal_behavior)>0:
        value_internal_behavior=nodemap2Path[swc_internal_behavior[0]]
        temp_list=value_internal_behavior.split('/')
        #print("temp_list0",temp_list)
        #print(swcComponent_config.get_NAME())
        temp_list[1]=swcComponent_config.get_NAME()
        #print("temp_list1",temp_list)
        componentXMLOptions_config.set_Internal_Behavior_Qualified_Name(utils4ParseARXML.filtePath("/".join(temp_list)))




#4. 然后进行有关timing有关的转换
    #没有
#5. 最后进行有关implementation有关的转换
    swc_implementation=rootNode.xpath('//ar:SWC-IMPLEMENTATION', namespaces=namespaces)
    if len(swc_implementation)>0:
        componentXMLOptions_config.set_Implementation_Qualified_Name(utils4ParseARXML.filtePath(nodemap2Path[swc_implementation[0]]))




#接下来进行armxl到配置文件的转换，以模块为单位，而不是以文件为单位
def convertARXML2Config(rootNode,targetFile):

    parser_config=None
    doc_config=parsexml_(targetFile,parser_config)
    rootNode_config=doc_config.getroot()
    rootTag_config,rootClass_config=get_root_tag(rootNode_config)
    if rootClass_config is None:
        rootTag_config='AUTOSAR_Type'
        rootClass_config=supermod_config.AUTOSAR_Type
    rootObj_config=rootClass_config.factory()
    rootObj_config.build(rootNode_config)

    global path2Nodemap
    global nodemap2Path
    global name_swcComponent_global
    path2Nodemap={}
    nodemap2Path={}
    name_swcComponent_global=rootObj_config.get_AUTOSAR_Dictionary()[0].get_AtomicComponents().get_SwcComponent().get_NAME()
    extract_short_names(rootNode,res=path2Nodemap)
    #将utils4ParseARXML中的path2Nodemap和nodemap2Path进行更新
    utils4ParseARXML.path2Nodemap=path2Nodemap
    utils4ParseARXML.nodemap2Path=nodemap2Path

    #0. 进行没有修改的元素的复制到配置文件中
    unModify=supermod_config.UnModify_Type()
    rootObj_config.set_UnModify(unModify)
    #0.0 进行CODE-MAPPING的复制
    codeMappings=[]
    
    codeMappings_all=rootNode_config.xpath('.//ns:CODE-Mapping', namespaces=namespaces)
    #print("codeMappings_all",codeMappings_all)
    for codeMapping_all in codeMappings_all:
        codeMapping_config=supermod_config.CODE_Mapping_Type()
        codeMapping_config.build(codeMapping_all)
        id_condemapping=codeMapping_all.attrib.get('UUID')
        if id_condemapping is None:
            id_condemapping=str(uuid.uuid4())
            codeMapping_config.set_ID(id_condemapping)
        codeMappings.append(codeMapping_config)
    rootObj_config.set_CODE_Mapping(codeMappings)

    #0.1 进行IMPLEMENTATION-DATA-TYPE的复制
    implementationDataTypes=rootNode.xpath('//ar:IMPLEMENTATION-DATA-TYPE', namespaces=namespaces)
    if len(implementationDataTypes)>0:
        implementationDataTypesListConfig=utils4ParseARXML.parseIMPLEMENTATION_DATA_Type_all_list(implementationDataTypes)
        unModify.set_IMPLEMENTATION_DATA_TYPE(implementationDataTypesListConfig)
    #0.2 进行CONSTANT-SPECIFICATION的复制
    constantSpecifications=rootNode.xpath('//ar:CONSTANT-SPECIFICATION', namespaces=namespaces)
    if len(constantSpecifications)>0:
        constantSpecificationsListConfig=utils4ParseARXML.parseCONSTANT_SPECIFICATION_all_list(constantSpecifications)
        unModify.set_CONSTANT_SPECIFICATION(constantSpecificationsListConfig)
    #0.3 进行SW-BASE-TYPE的复制
    swBaseTypes=rootNode.xpath('//ar:SW-BASE-TYPE', namespaces=namespaces)
    if len(swBaseTypes)>0:
        swBaseTypesListConfig=utils4ParseARXML.parseSW_BASE_TYPE_all_list(swBaseTypes)
        unModify.set_SW_BASE_TYPE(swBaseTypesListConfig)

    
    #找所有COMPONENT
    applicationSwcComponents=rootNode.xpath('//ar:APPLICATION-SW-COMPONENT-TYPE', namespaces=namespaces) 
    for index_component,applicationSwcComponent in enumerate(applicationSwcComponents):
        rootObj_config.set_AUTOSAR_Dictionary([])
        autosar_Dictionary_config=supermod_config.AUTOSAR_Dictionary_Type()
        autosar_Dictionary_config.set_ID(applicationSwcComponent.attrib.get('UUID')+"autosar_dictionary")
        xmlOptions_config=supermod_config.XML_Options_Type()
        autosar_Dictionary_config.set_XML_Options(xmlOptions_config)
        viewAndEditOptions_config=supermod_config.View_And_Edit_Options_Type()
        packagingOptions_config=supermod_config.Packaging_Options_Type()
        packagePaths_config=supermod_config.Package_Paths_Type()
        additionalPackages_config=supermod_config.Additional_Packages_Type()
        additional_options_config=supermod_config.Additional_Options_Type()
        xmlOptions_config.set_View_And_Edit_Options(viewAndEditOptions_config)
        xmlOptions_config.set_Packaging_Options(packagingOptions_config)
        xmlOptions_config.set_Package_Paths(packagePaths_config)
        xmlOptions_config.set_Additional_Packages(additionalPackages_config)
        xmlOptions_config.set_Additional_Options(additional_options_config)
        methods_config=supermod_config.Methods_Type()
        swAddrMethods_config=supermod_config.SwAddrMethods_Type()
        methods_config.set_SwAddrMethods(swAddrMethods_config)
        autosar_Dictionary_config.set_Methods(methods_config)
        interfaces_config=supermod_config.Interfaces_Type()
        s_r_interfaces_config=supermod_config.S_R_Interfaces_Type()
        interfaces_config.set_S_R_Interfaces(s_r_interfaces_config)
        autosar_Dictionary_config.set_Interfaces(interfaces_config)
        if "\\" in targetFile:
            autosar_Dictionary_config.set_MODEL_NAME(targetFile.split("\\")[-1][:-len("_configuration.xml")])
        else:
            autosar_Dictionary_config.set_MODEL_NAME(targetFile.split("/")[-1][:-len("_configuration.xml")])
        atomicComponents_config=supermod_config.AtomicComponents_Type()
        swcComponent_config=supermod_config.SwcComponent_Type()
        convertApplicationSwComponentType2ConfigAPI(applicationSwcComponent,swcComponent_config,atomicComponents_config,autosar_Dictionary_config,xmlOptions_config,rootObj_config,index_component,rootNode)

    
    
    f=open(targetFile,'w',encoding='utf-8')
    sys.stdout=f
    sys.stdout.write('''<?xml version="1.0" encoding="UTF-8"?>
<!--
wumbuk自定义AUTOSAR配置元素信息，包含
1. AUTOSAR 定义信息
2. AUTOSAR 配置信息，即AUTOSAR的配置信息映射到哪部分的Modelica模型中
-->''')
    #接下来把本地配置文件打印输入就行rootObj_config
    rootObj_config.export(
        sys.stdout,0,name_=rootTag_config,
        namespacedef_='',
        pretty_print=True
        )
    f.close()





                                

if __name__ == '__main__':

    
    xmlConfigPath="I:\\testM\\test_configuration.xml"
    # aRXMLFilesPathList=["I:\\testM\ARXMLS\\test_component.arxml",
    #                     "I:\\testM\ARXMLS\\test_datatype.arxml",
    #                     "I:\\testM\ARXMLS\\test_implementation.arxml",
    #                     "I:\\testM\ARXMLS\\test_interface.arxml",
    #                     "I:\\testM\ARXMLS\\test_timing.arxml"]
    
    aRXMLFilesPathList=["I:\\testM\ARXMLS\\autosar_swc.arxml"]
    rootNode=integrateNodes2One(aRXMLFilesPathList)
    f=open("I:\\testM\\test_configuration_test.xml",'w')
    print(etree_.tostring(rootNode, pretty_print=True).decode('utf-8'),file=f)
    convertARXML2Config(rootNode,"I:\\testM\\test_configuration.xml")

