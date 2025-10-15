
import os
import string
import sys
from lxml import etree as etree_
from . import autosar_config_api as supermod_config
from . import autosar_all_api as supermod_all
#import autosar_config_api as supermod_config
#import autosar_all_api as supermod_all
import uuid
import re as re_
from datetime import datetime

path2Nodemap={}  #ARXML文件中的所有节点的路径信息，是一个字典，key是节点的路径，value是节点的对象
nodemap2Path={}   #ARXML文件中的所有节点的对象，是一个字典，key是节点的对象，value是节点的路径
namespaces = {'ar': 'http://autosar.org/schema/r4.0'}
#如果path不是以“/”开头，则在path前面加上“/”
def filtePath(path):
    if path[0]!='/':
        path='/'+path
    return path
#如果path以“/”开头，则去掉
def defiltePath(path):
    if path[0]=='/':
        path=path[1:]
    return path

#根据ARXML文件中的SW-BASE-TYPE定义，得到有关的SW-BASE-TYPE的包路径信息
#输入：swBaseTypes，ARXML文件中的SW-BASE-TYPE定义，是通过xpath得到的一个列表
#输出：所有的SW-BASE-TYPE的包路径信息，是一个列表
def parseSWBASETYPE(swBaseTypes):
    swBaseTypePkgList = []
    for swBaseType in swBaseTypes:
        swBaseTypePkg=nodemap2Path[swBaseType.getparent().getparent()]
        if swBaseTypePkg not in swBaseTypePkgList:
            swBaseTypePkgList.append(swBaseTypePkg)
    return swBaseTypePkgList

def parseSWADDRMETHOD(swAddrMethods):
    swAddrMethodPkgList = []
    for swAddrMethod in swAddrMethods:
        swAddrMethodPkg=nodemap2Path[swAddrMethod.getparent().getparent()]
        swAddrMethodPkgList.append(swAddrMethodPkg)
    return swAddrMethodPkgList

def parseImplementationDataType(implementationDataTypes):
    implementationDataTypePkgList = []
    for implementationDataType in implementationDataTypes:
       # test1=implementationDataType.getparent()
        #test2=implementationDataType.getparent().getparent()
        #test3=implementationDataType.getparent().getparent().getparent()
        implementationDataTypePkg=nodemap2Path[implementationDataType.getparent().getparent()]
        if implementationDataTypePkg not in implementationDataTypePkgList:
            implementationDataTypePkgList.append(implementationDataTypePkg)
    return implementationDataTypePkgList
def parseConstantSpecification(constantSpecifications):
    constantSpecificationPkgList = []
    for constantSpecification in constantSpecifications:
        constantSpecificationPkg=nodemap2Path[constantSpecification.getparent().getparent()]
        if constantSpecificationPkg not in constantSpecificationPkgList:
            constantSpecificationPkgList.append(constantSpecificationPkg)
    return constantSpecificationPkgList

#根据ARXML文件中的Sender-Receiver-Interface定义，得到有关的Sender-Receiver-Interface的包路径信息和DataElements的信息
#输入：senderReceiverInterfaces，ARXML文件中的Sender-Receiver-Interface定义，是通过xpath得到的一个列表
#返回：senderReceiverInterfacePkgList，dataElementList
def parseSenderReceiverInterface(senderReceiverInterfaces):
    senderReceiverInterfacePkgList = []
    dataElementList = []
    for senderReceiverInterface in senderReceiverInterfaces:
        senderReceiverInterfacePkg=nodemap2Path[senderReceiverInterface.getparent().getparent()]
        senderReceiverInterfacePkgList.append(senderReceiverInterfacePkg)

        dataElementList.append(senderReceiverInterface.xpath('.//ar:VARIABLE-DATA-PROTOTYPE', namespaces=namespaces))
    return senderReceiverInterfacePkgList,dataElementList


#将ARXML文件中的IMPLEMENTATION-DATA-TYPE转换成config中的对应元素列表
def parseIMPLEMENTATION_DATA_Type_all_list(implementationDataTypeList):
    implementationDataTypeList_config = []
    for implementationDataType_all in implementationDataTypeList:
        implementationDataType_config=supermod_config.IMPLEMENTATION_DATA_TYPE_Type()
        implementationDataType_config.set_UUID(implementationDataType_all.attrib.get('UUID'))
        implementationDataType_config.set_SHORT_NAME(implementationDataType_all.xpath('ar:SHORT-NAME',namespaces=namespaces)[0].text)
        implementationDataType_config.set_CATEGORY(implementationDataType_all.xpath('ar:CATEGORY',namespaces=namespaces)[0].text)
        subelements_all_list=implementationDataType_all.xpath('ar:SUB-ELEMENTS',namespaces=namespaces)
        if len(subelements_all_list) ==1:
            subelements_all=subelements_all_list[0]
            sub_elements_config=supermod_config.SUB_ELEMENTS_Type()
            implementationDataType_config.set_SUB_ELEMENTS(sub_elements_config)
            implementation_data_type_element_all_list=subelements_all.xpath('ar:IMPLEMENTATION-DATA-TYPE-ELEMENT',namespaces=namespaces)
            for implementation_data_type_element_all in implementation_data_type_element_all_list:
                implementation_data_type_element_config=supermod_config.IMPLEMENTATION_DATA_TYPE_ELEMENT_Type()
                implementation_data_type_element_config.set_UUID(implementation_data_type_element_all.attrib.get('UUID'))
                implementation_data_type_element_config.set_SHORT_NAME(implementation_data_type_element_all.xpath('ar:SHORT-NAME',namespaces=namespaces)[0].text)
                implementation_data_type_element_config.set_CATEGORY(implementation_data_type_element_all.xpath('ar:CATEGORY',namespaces=namespaces)[0].text)
                array_size=implementation_data_type_element_all.xpath('ar:ARRAY-SIZE',namespaces=namespaces)[0].text
                implementation_data_type_element_config.set_ARRAY_SIZE(array_size)
                implementation_data_type_element_config.set_ARRAY_SIZE_SEMANTICS(implementation_data_type_element_all.xpath('ar:ARRAY-SIZE-SEMANTICS',namespaces=namespaces)[0].text)
                sw_data_def_props_config=supermod_config.SW_DATA_DEF_PROPS_Type()
                implementation_data_type_element_config.set_SW_DATA_DEF_PROPS(sw_data_def_props_config)
                sw_data_def_props_variants_config=supermod_config.SW_DATA_DEF_PROPS_VARIANTS_Type()
                sw_data_def_props_config.set_SW_DATA_DEF_PROPS_VARIANTS(sw_data_def_props_variants_config)
                sw_data_def_props_conditional_all_list=implementation_data_type_element_all.xpath('ar:SW-DATA-DEF-PROPS/ar:SW-DATA-DEF-PROPS-VARIANTS/ar:SW-DATA-DEF-PROPS-CONDITIONAL',namespaces=namespaces)
                
                for sw_data_def_props_conditional_all in sw_data_def_props_conditional_all_list:
                    sw_data_def_props_conditional_config=supermod_config.SW_DATA_DEF_PROPS_CONDITIONAL_Type()
                    implementation_data_type_ref_config=supermod_config.IMPLEMENTATION_DATA_TYPE_REFType()
                    sw_data_def_props_conditional_config.set_IMPLEMENTATION_DATA_TYPE_REF(implementation_data_type_ref_config)
                    implementation_data_type_ref_all=sw_data_def_props_conditional_all.xpath('ar:IMPLEMENTATION-DATA-TYPE-REF',namespaces=namespaces)[0]
                    implementation_data_type_ref_config.set_DEST(implementation_data_type_ref_all.attrib.get('DEST'))
                    implementation_data_type_ref_config.set_valueOf_(sw_data_def_props_conditional_all.xpath('ar:IMPLEMENTATION-DATA-TYPE-REF',namespaces=namespaces)[0].text)
                    sw_data_def_props_variants_config.add_SW_DATA_DEF_PROPS_CONDITIONAL(sw_data_def_props_conditional_config)
                
                sub_elements_config.add_IMPLEMENTATION_DATA_TYPE_ELEMENT(implementation_data_type_element_config)
        sw_data_def_props_list_all=implementationDataType_all.xpath('ar:SW-DATA-DEF-PROPS',namespaces=namespaces) 
        if len(sw_data_def_props_list_all) ==1:
            sw_data_def_props_all=sw_data_def_props_list_all[0]
            sw_data_def_props_config=supermod_config.SW_DATA_DEF_PROPS_Type()
            implementationDataType_config.set_SW_DATA_DEF_PROPS(sw_data_def_props_config)
            sw_data_def_props_variants_config=supermod_config.SW_DATA_DEF_PROPS_VARIANTS_Type()
            sw_data_def_props_config.set_SW_DATA_DEF_PROPS_VARIANTS(sw_data_def_props_variants_config)
            sw_data_def_props_conditional_all_list=sw_data_def_props_all.xpath('ar:SW-DATA-DEF-PROPS-VARIANTS/ar:SW-DATA-DEF-PROPS-CONDITIONAL',namespaces=namespaces)
            for sw_data_def_props_conditional_all in sw_data_def_props_conditional_all_list:
                sw_data_def_props_conditional_config=supermod_config.SW_DATA_DEF_PROPS_CONDITIONAL_Type()
                base_type_ref_config=supermod_config.BASE_TYPE_REFType()
                sw_data_def_props_conditional_config.set_BASE_TYPE_REF(base_type_ref_config)
                base_type_ref_all=sw_data_def_props_conditional_all.xpath('ar:BASE-TYPE-REF',namespaces=namespaces)[0]
                base_type_ref_config.set_DEST(base_type_ref_all.attrib.get('DEST'))
                base_type_ref_config.set_valueOf_(sw_data_def_props_conditional_all.xpath('ar:BASE-TYPE-REF',namespaces=namespaces)[0].text)
                sw_data_def_props_variants_config.add_SW_DATA_DEF_PROPS_CONDITIONAL(sw_data_def_props_conditional_config)
        
        
        implementationDataTypeList_config.append(implementationDataType_config)
    
    return implementationDataTypeList_config      

#将ARXML文件中的CONSTANT-SPECIFICATION转换成config中的对应元素列表    
def parseCONSTANT_SPECIFICATION_all_list(constantspecifiationList):
    constant_specifiationList_config = []
    for constant_specifiation_all in constantspecifiationList:
        constant_specifiation_config=supermod_config.CONSTANT_SPECIFICATION_Type()
        constant_specifiation_config.set_UUID(constant_specifiation_all.attrib.get('UUID'))
        constant_specifiation_config.set_SHORT_NAME(constant_specifiation_all.xpath('ar:SHORT-NAME',namespaces=namespaces)[0].text)
        value_spec_config=supermod_config.VALUE_SPEC_Type()
        constant_specifiation_config.set_VALUE_SPEC(value_spec_config)
        numerical_value_specification_list_all=constant_specifiation_all.xpath('ar:VALUE-SPEC/ar:NUMERICAL-VALUE-SPECIFICATION',namespaces=namespaces)
        array_value_specification_list_all=constant_specifiation_all.xpath('ar:VALUE-SPEC/ar:ARRAY-VALUE-SPECIFICATION',namespaces=namespaces)
        if len(numerical_value_specification_list_all)>0:
            for numerial_value_specification_all in numerical_value_specification_list_all:
                numerical_vale_specification_config=supermod_config.NUMERICAL_VALUE_SPECIFICATION_Type()
                numerical_vale_specification_config.set_SHORT_LABEL(numerial_value_specification_all.xpath('ar:SHORT-LABEL',namespaces=namespaces)[0].text)
                numerical_vale_specification_config.set_VALUE(numerial_value_specification_all.xpath('ar:VALUE',namespaces=namespaces)[0].text)
                value_spec_config.add_NUMERICAL_VALUE_SPECIFICATION(numerical_vale_specification_config)
        if len(array_value_specification_list_all)>0:
            for array_value_specification_all in array_value_specification_list_all:
                array_value_specification_config=supermod_config.ARRAY_VALUE_SPECIFICATION_Type()
                array_value_specification_config.set_SHORT_LABEL(array_value_specification_all.xpath('ar:SHORT-LABEL',namespaces=namespaces)[0].text)
                elements_config=supermod_config.ELEMENTS_Type()
                array_value_specification_config.set_ELEMENTS(elements_config)
                constant_reference_list_all=array_value_specification_all.xpath('ar:ELEMENTS/ar:CONSTANT-REFERENCE',namespaces=namespaces)
                for constant_reference_all in constant_reference_list_all:
                    constant_reference_config=supermod_config.CONSTANT_REFERENCE_Type()
                    constant_reference_config.set_SHORT_LABEL(constant_reference_all.xpath('ar:SHORT-LABEL',namespaces=namespaces)[0].text)
                    constant_ref_config=supermod_config.CONSTANT_REFType()
                    constant_ref_all=constant_reference_all.xpath('ar:CONSTANT-REF',namespaces=namespaces)[0]
                    constant_ref_config.set_DEST(constant_ref_all.attrib.get('DEST'))
                    constant_ref_config.set_valueOf_(constant_reference_all.xpath('ar:CONSTANT-REF',namespaces=namespaces)[0].text)
                    constant_reference_config.set_CONSTANT_REF(constant_ref_config)
                    elements_config.add_CONSTANT_REFERENCE(constant_reference_config)
                value_spec_config.add_ARRAY_VALUE_SPECIFICATION(array_value_specification_config)
        constant_specifiationList_config.append(constant_specifiation_config)
    return constant_specifiationList_config

def parseSW_BASE_TYPE_all_list(swBaseTypes_all):
    sw_base_type_config_list = []
    for sw_base_type_all in swBaseTypes_all:
        sw_base_type_config=supermod_config.SW_BASE_TYPE_Type()
        sw_base_type_config.set_UUID(sw_base_type_all.attrib.get('UUID'))
        sw_base_type_config.set_SHORT_NAME(sw_base_type_all.xpath('ar:SHORT-NAME',namespaces=namespaces)[0].text)
        sw_base_type_config.set_CATEGORY(sw_base_type_all.xpath('ar:CATEGORY',namespaces=namespaces)[0].text)
        sw_base_type_config.set_BASE_TYPE_SIZE(sw_base_type_all.xpath('ar:BASE-TYPE-SIZE',namespaces=namespaces)[0].text)
        sw_base_type_config.set_BASE_TYPE_ENCODING(sw_base_type_all.xpath('ar:BASE-TYPE-ENCODING',namespaces=namespaces)[0].text)
        sw_base_type_config.set_NATIVE_DECLARATION(sw_base_type_all.xpath('ar:NATIVE-DECLARATION',namespaces=namespaces)[0].text)
        sw_base_type_config_list.append(sw_base_type_config)
    return sw_base_type_config_list