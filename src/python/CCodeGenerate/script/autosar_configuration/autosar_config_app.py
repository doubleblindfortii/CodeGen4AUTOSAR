#!/usr/bin/env python


import os
import sys
from lxml import etree as etree_
from . import autosar_config_api as supermod
#import autosar_configuration.autosar_config_api as supermod
#import autosar_config_api as supermod
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

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
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


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from autosar_config_api import *\n\n')
        sys.stdout.write('import autosar_config_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj

#获取模型中的所有的Functions的绑定信息，返回列表[[Modelica模型中的源文件的名字,[有关的AUTOSAR信息，RunnableEntity的名字]]]
def getRunnableEntities(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res=[]
    runnableEntityDict={}
    autosar_Dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_Dictionary in autosar_Dictionary_list:
        runnableEntityList=autosar_Dictionary.get_AtomicComponents().get_SwcComponent().get_Runnables().get_Runnable_Entity()
        for runnableEntity in runnableEntityList:
            id=runnableEntity.get_ID()
            name=runnableEntity.get_NAME()
            runnableEntityDict[id]=name
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        functionPrototypeList=code_mapping.get_Functions().get_Function_Prototype()
        for functionPrototype in functionPrototypeList:
            temp_tuple=[functionPrototype.get_Source(),[runnableEntityDict[functionPrototype.get_RUNNABLE_ENTITY_REF_ID()]]]
            res.append(temp_tuple)
    return res



#获取模型中的所有的Inports的绑定信息，返回列表[(Modelica模型中的源文件的名字,即RPORT的名字，Element的名字),...]
def getRPorts(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res=[]
    inportsDict={}
    dataElementDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        inportsList=autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().get_ReceiverPort_Prototype()
        #inportsList = rootObj.get_AUTOSAR_Dictionary().get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().get_ReceiverPort_Prototype()

        for inport in inportsList:
            id=inport.get_ID()
            name=inport.get_NAME()
            interfaceRefId=inport.get_INTERFACE_REF_ID()
            #elementRefId=inport.get_ReceiverPort_Specs().get_Nonqueued_Receiver_Com_Spec().get_ELEMENT_REF_ID()
            elementRefIdList=[]
            for nonqueued_Receiver_Com_Spec in inport.get_ReceiverPort_Specs().get_Nonqueued_Receiver_Com_Spec():
                elementRefIdList.append(nonqueued_Receiver_Com_Spec.get_ELEMENT_REF_ID())
            
            inportsDict[id]=[name,interfaceRefId,elementRefIdList]
        
        senderReceiverInterfaceList=autosar_dictionary.get_Interfaces().get_S_R_Interfaces().get_Sender_Receiver_Interface()
        for senderReceiverInterface in senderReceiverInterfaceList:
            id=senderReceiverInterface.get_ID()
            name=senderReceiverInterface.get_NAME()
            variableDataPrototypeList=senderReceiverInterface.get_Data_Elements().get_Variable_Data_Prototype()
            for variableDataPrototype in variableDataPrototypeList:
                id_element=variableDataPrototype.get_ID()
                name_element=variableDataPrototype.get_NAME()
                dataElementDict[id_element]=name_element
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        inportPrototypeList=code_mapping.get_Inports().get_Inport_Prototype()
        for inportPrototype in inportPrototypeList:
            element=dataElementDict[inportPrototype.get_ELEMENT_REF_ID()]
            temp_tuple=(inportPrototype.get_Source(),inportsDict[inportPrototype.get_RECEIVE_PORT_REF_ID()][0],element)
            res.append(temp_tuple)
    return res




#获取模型中的所有的Outports的绑定信息，返回列表[(Modelica模型中的源文件的名字,即PPORT的名字，里面有效的Element的名字),...]
def getPPorts(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res=[]
    outPortsDict={}
    dataElementDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        outPortsList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_SenderPorts().get_SenderPort_Prototype()
    
        for outPort in outPortsList:
            id=outPort.get_ID()
            name=outPort.get_NAME()
            interfaceRefId=outPort.get_INTERFACE_REF_ID()
            elementRefIdList=[]
            for nonqueued_Sender_Com_Spec in outPort.get_SenderPort_Specs().get_Nonqueued_Sender_Com_Spec():
                elementRefIdList.append(nonqueued_Sender_Com_Spec.get_ELEMENT_REF_ID())
            outPortsDict[id]=[name,interfaceRefId,elementRefIdList]
    
        senderReceiverInterfaceList=autosar_dictionary.get_Interfaces().get_S_R_Interfaces().get_Sender_Receiver_Interface()
        for senderReceiverInterface in senderReceiverInterfaceList:
            id=senderReceiverInterface.get_ID()
            name=senderReceiverInterface.get_NAME()
            variableDataPrototypeList=senderReceiverInterface.get_Data_Elements().get_Variable_Data_Prototype()
            for variableDataPrototype in variableDataPrototypeList:
                id_element=variableDataPrototype.get_ID()
                name_element=variableDataPrototype.get_NAME()
                dataElementDict[id_element]=name_element
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        outPortPrototypeList=code_mapping.get_Outports().get_Outport_Prototype()
        for outPortPrototype in outPortPrototypeList:
            element_name=dataElementDict[outPortPrototype.get_ELEMENT_REF_ID()]
            temp_tuple=(outPortPrototype.get_Source(),outPortsDict[outPortPrototype.get_SENDER_PORT_REF_ID()][0],element_name)
            res.append(temp_tuple)
    return res


#获取模型中的所有的IRV的绑定信息，返回列表[(Modelica模型中的源文件的名字,[有关的AUTOSAR信息，IRV的名字]]
def getIRV(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res=[]
    iRVSDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        variableDataPrototypeList=autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_IRV().get_IRVS().get_Variable_Data_Prototype()
        for variableDataPrototype in variableDataPrototypeList:
            id=variableDataPrototype.get_ID()
            name=variableDataPrototype.get_NAME()
            iRVSDict[id]=name
    
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        dataTransferPrototypeList=code_mapping.get_Data_Transfers().get_Data_Transfer_Prototype()
        for dataTransferPrototype in dataTransferPrototypeList:
            temp_tuple=[dataTransferPrototype.get_Source(),[iRVSDict[dataTransferPrototype.get_IRV_REF_ID()]]]
            res.append(temp_tuple)
    return res


#获得与RunnableEntity绑定的RTE的内容，res的结构为{"运行实体名":
#                                                {"ImplicitReceive":{"dateReadAccess":[输入的端口名称_element名称],"dateWriteAccess":[输出的端口名称_element名称],"readLocalAccess":[读的本地变量名称],"writeLocalAccess":[写的本地变量名称]}}
#                                               }
def getRunnableEntitiesRte(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}

    portsDict={}
    iRVSDict={}
    elementsDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        inportsList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().get_ReceiverPort_Prototype()
        for inport in inportsList:
            id=inport.get_ID()
            name=inport.get_NAME()
            portsDict[id]=name
        outPortsList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_SenderPorts().get_SenderPort_Prototype()
        for outPort in outPortsList:
            id=outPort.get_ID()
            name=outPort.get_NAME()
            portsDict[id]=name
        variableDataPrototypeList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_IRV().get_IRVS().get_Variable_Data_Prototype()
        
        for variableDataPrototype in variableDataPrototypeList:
            id=variableDataPrototype.get_ID()
            name=variableDataPrototype.get_NAME()
            iRVSDict[id]=name    
        
        senderReceiverInterfaceList=autosar_dictionary.get_Interfaces().get_S_R_Interfaces().get_Sender_Receiver_Interface()
        for senderReceiverInterface in senderReceiverInterfaceList:
            elementsPrototypes=senderReceiverInterface.get_Data_Elements().get_Variable_Data_Prototype()
            for elementsPrototype in elementsPrototypes:
                id=elementsPrototype.get_ID()
                name=elementsPrototype.get_NAME()
                elementsDict[id]=name


        runnableEntityList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Runnables().get_Runnable_Entity()   
        for runnableEntity in runnableEntityList:
            name=runnableEntity.get_NAME()

            tempDic={}

            #进行dataReadAccess键值的处理
            dataReadList=[]
            dataReadAccess=runnableEntity.get_Data_Read_Access()
            if dataReadAccess is not None:
                dataReadVariableAccessList=dataReadAccess.get_Variable_Access()
                for dataReadVariableAccess in dataReadVariableAccessList:
                    portPrototypeRef=dataReadVariableAccess.get_Port_Prototype_Ref()
                    portRefId=portPrototypeRef.get_PORT_REF_ID()
                    elementRefId=portPrototypeRef.get_ELEMENT_REF_ID()
                    dataReadList.append(portsDict[portRefId]+"_"+elementsDict[elementRefId])
                tempDic["dataReadAccess"]=dataReadList

            #进行dataWriteAccess键值的处理
            dataWriteList=[]
            dataWriteAccess=runnableEntity.get_Data_Write_Access()
            if dataWriteAccess is not None:
                dataWriteVariableAccessList=dataWriteAccess.get_Variable_Access()
                for dataWriteVariableAccess in dataWriteVariableAccessList:
                    portPrototypeRef=dataWriteVariableAccess.get_Port_Prototype_Ref()
                    portRefId=portPrototypeRef.get_PORT_REF_ID()
                    elementRefId=portPrototypeRef.get_ELEMENT_REF_ID()
                    dataWriteList.append(portsDict[portRefId]+"_"+elementsDict[elementRefId])
                tempDic["dataWriteAccess"]=dataWriteList

            #进行readLocalAccess键值的处理
            readLocalList=[]
            readLocalAccess=runnableEntity.get_Read_Local_Access()
            if readLocalAccess is not None:
                readLocalVariableAccessList=readLocalAccess.get_Variable_Access()
                for readLocalVariableAccess in readLocalVariableAccessList:
                    localPrototypeRef=readLocalVariableAccess.get_Local_Prototype_Ref()
                    localRefId=localPrototypeRef.get_LOCAL_REF_ID()
                    readLocalList.append(iRVSDict[localRefId])
                tempDic["readLocalAccess"]=readLocalList
            #进行writeLocalAccess键值的处理
            writeLocalList=[]
            writeLocalAccess=runnableEntity.get_Write_Local_Access()
            if writeLocalAccess is not None:
                writeLocalVariableAccessList=writeLocalAccess.get_Variable_Access()
                for writeLocalVariableAccess in writeLocalVariableAccessList:
                    localPrototypeRef=writeLocalVariableAccess.get_Local_Prototype_Ref()
                    localRefId=localPrototypeRef.get_LOCAL_REF_ID()
                    writeLocalList.append(iRVSDict[localRefId])
                tempDic["writeLocalAccess"]=writeLocalList
            
            res[name]=tempDic
    



    return res



def getRunnableEntitySymbolMap(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}   
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        runnableEntityList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Runnables().get_Runnable_Entity()   
        for runnableEntity in runnableEntityList:
            name=runnableEntity.get_NAME()
            symbolVal=runnableEntity.get_Symbol()
            res[name]=symbolVal
    return res

def getInitRunnableEntityName(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}
    runnableEntitiesDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        runnableEntityList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Runnables().get_Runnable_Entity()   
        for runnableEntity in runnableEntityList:
            name=runnableEntity.get_NAME()
            temp={}
            temp["name"]=name
            temp["symbol"]=runnableEntity.get_Symbol()
            runnableEntitiesDict[runnableEntity.get_ID()]=temp
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        functionPrototypeList = code_mapping.get_Functions().get_Function_Prototype()
        for functionPrototype in functionPrototypeList:
            if functionPrototype.get_Source()=="DataDictionary":
                initRunnableId=functionPrototype.get_RUNNABLE_ENTITY_REF_ID()
                res["name"]= runnableEntitiesDict[initRunnableId]["name"]
                res["symbol"]=runnableEntitiesDict[initRunnableId]["symbol"]
    return res


#获得与States有关的内容，res的结构为{"id":{"Source":源地址,"Mapped-To":映射到的地址,"Path":路径地址}}
def getStates(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}
    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        statesList=code_mapping.get_Signals_States().get_States().get_State_Prototype()
        for state in statesList:
            id=state.get_ID()
            source=state.get_Source()
            mappedTo=state.get_Mapped_To()
            path=state.get_Path()
            temp={}
            temp["Source"]=source
            temp["Mapped-To"]=mappedTo
            temp["Path"]=path
            res[id]=temp
    return res

#获得可运行实体的采样周期，res的结构为{"RunnableEntity名称"："采样周期"}
def getRunnableSampleTime(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        runnableEntityList=autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Runnables().get_Runnable_Entity()
        for runnableEntity in runnableEntityList:
            if len(runnableEntity.get_Events().get_Event_Prototype())>0:
                name=runnableEntity.get_NAME()
                sample_time=runnableEntity.get_Events().get_Event_Prototype()[0].get_Period()
                res[name]=sample_time
    return res



#获得IMPLEMENTATION-DATA-Type的内容，res的结构为{“shortNAME”:{数组大小，实现的类型名字}}
def getImplementationDataType(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}
    IMPLEMENTATION_DATA_TYPE_list=rootObj.get_UnModify().get_IMPLEMENTATION_DATA_TYPE()
    for IMPLEMENTATION_DATA_TYPE in IMPLEMENTATION_DATA_TYPE_list:
        if IMPLEMENTATION_DATA_TYPE.get_SUB_ELEMENTS() is not None:
            shortName=IMPLEMENTATION_DATA_TYPE.get_SHORT_NAME()
            implementation_data_type_element=IMPLEMENTATION_DATA_TYPE.get_SUB_ELEMENTS().get_IMPLEMENTATION_DATA_TYPE_ELEMENT()[0]
            arraySize=implementation_data_type_element.get_ARRAY_SIZE()
            ref_name=implementation_data_type_element.get_SW_DATA_DEF_PROPS().get_SW_DATA_DEF_PROPS_VARIANTS().get_SW_DATA_DEF_PROPS_CONDITIONAL()[0].get_IMPLEMENTATION_DATA_TYPE_REF().get_valueOf_()
            ref_name_last=ref_name.split("/")[-1]
            res[shortName]=(arraySize,ref_name_last)
    return res

#获得组件名
def getComponentName(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res=rootObj.get_AUTOSAR_Dictionary()[0].get_AtomicComponents().get_SwcComponent().get_NAME()
    return res

#获得各种数据的传输方式的集合，res的结构为{"数据获取方式":{端口名_元素名 或者irv名}}
def getAccessMode(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}

    portsDict={}
    iRVSDict={}
    elementsDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        inportsList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().get_ReceiverPort_Prototype()
        for inport in inportsList:
            id=inport.get_ID()
            name=inport.get_NAME()
            portsDict[id]=name
        outPortsList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_SenderPorts().get_SenderPort_Prototype()
        for outPort in outPortsList:
            id=outPort.get_ID()
            name=outPort.get_NAME()
            portsDict[id]=name
        variableDataPrototypeList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_IRV().get_IRVS().get_Variable_Data_Prototype()
        
        for variableDataPrototype in variableDataPrototypeList:
            id=variableDataPrototype.get_ID()
            name=variableDataPrototype.get_NAME()
            iRVSDict[id]=name    
        
        senderReceiverInterfaceList=autosar_dictionary.get_Interfaces().get_S_R_Interfaces().get_Sender_Receiver_Interface()
        for senderReceiverInterface in senderReceiverInterfaceList:
            elementsPrototypes=senderReceiverInterface.get_Data_Elements().get_Variable_Data_Prototype()
            for elementsPrototype in elementsPrototypes:
                id=elementsPrototype.get_ID()
                name=elementsPrototype.get_NAME()
                elementsDict[id]=name

    code_mapping_list=rootObj.get_CODE_Mapping()
    for code_mapping in code_mapping_list:
        errorStatusSet=set()
        inport_PrototypeList=code_mapping.get_Inports().get_Inport_Prototype()
        for inport_Prototype in inport_PrototypeList:
            dataAccessMode=inport_Prototype.get_DataAccessMode()
            if dataAccessMode=="ErrorStatus":
                errorStatusSet.add(portsDict[inport_Prototype.get_RECEIVE_PORT_REF_ID()]+"_"+elementsDict[inport_Prototype.get_ELEMENT_REF_ID()])
        res["ErrorStatusSet"]=errorStatusSet
    return res

#获得数据元素或者irv元素对应的数据类型，res的结构为{"端口名_元素名 或者irv名":数据类型}
def get_element_type(inFilename):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AUTOSAR_Type'
        rootClass = supermod.AUTOSAR_Type
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    res={}

    
    
    elementsDict={}
    idTypeDict={}
    autosar_dictionary_list=rootObj.get_AUTOSAR_Dictionary()
    for autosar_dictionary in autosar_dictionary_list:
        variableDataPrototypeList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_IRV().get_IRVS().get_Variable_Data_Prototype()
        
        for variableDataPrototype in variableDataPrototypeList:
            id=variableDataPrototype.get_ID()
            name=variableDataPrototype.get_NAME()
            if variableDataPrototype.get_Type_Tref() is not None:
                type=variableDataPrototype.get_Type_Tref().get_valueOf_().split("/")[-1]
            else:
                type="/DataTypes/Double"
            res[name]=type   
        
        senderReceiverInterfaceList=autosar_dictionary.get_Interfaces().get_S_R_Interfaces().get_Sender_Receiver_Interface()
        for senderReceiverInterface in senderReceiverInterfaceList:
            elementsPrototypes=senderReceiverInterface.get_Data_Elements().get_Variable_Data_Prototype()
            for elementsPrototype in elementsPrototypes:
                id=elementsPrototype.get_ID()
                name=elementsPrototype.get_NAME()
                elementsDict[id]=name
                if  elementsPrototype.get_Type_Tref() is not None:
                    type=elementsPrototype.get_Type_Tref().get_valueOf_().split("/")[-1]
                    if type.strip()=="None":
                        type="Double"
                else:
                    type="Double"
                idTypeDict[id]=type

        receiverPortPrototypeList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_ReceiverPorts().get_ReceiverPort_Prototype()
        for receiverPortPrototype in receiverPortPrototypeList:
            id=receiverPortPrototype.get_ID()
            name=receiverPortPrototype.get_NAME()
            nonqueued_ReceiverComSpecList=receiverPortPrototype.get_ReceiverPort_Specs().get_Nonqueued_Receiver_Com_Spec()
            for nonqueued_ReceiverComSpec in nonqueued_ReceiverComSpecList:
                elementRefId=nonqueued_ReceiverComSpec.get_ELEMENT_REF_ID()
                res[name+"_"+elementsDict[elementRefId]]=idTypeDict[elementRefId]
            
        senderPortPrototypeList = autosar_dictionary.get_AtomicComponents().get_SwcComponent().get_Ports().get_SenderPorts().get_SenderPort_Prototype()
        for senderPortPrototype in senderPortPrototypeList:
            id=senderPortPrototype.get_ID()
            name=senderPortPrototype.get_NAME()
            nonqueued_SenderComSpecList=senderPortPrototype.get_SenderPort_Specs().get_Nonqueued_Sender_Com_Spec()
            for nonqueued_SenderComSpec in nonqueued_SenderComSpecList:
                elementRefId=nonqueued_SenderComSpec.get_ELEMENT_REF_ID()
                res[name+"_"+elementsDict[elementRefId]]=idTypeDict[elementRefId]
    return res



USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
   # args = sys.argv[1:]
   # if len(args) != 1:
   #     usage()
   # infilename = args[0]
    infilename="autosar_swc_configuration.xml"
    parse(infilename)
    getRunnableEntities(infilename)
    getRPorts(infilename)
    getPPorts(infilename)
    getIRV(infilename)
    getRunnableEntitiesRte(infilename)
    getStates(infilename)
    getRportSampleTime(infilename)
    getRunnableEntitySymbolMap(infilename)
    getInitRunnableEntityName(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
