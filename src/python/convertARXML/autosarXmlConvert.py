#import convertARXML2Config
#import convertConfig2ARXML
from . import convertARXML2Config
from . import convertConfig2ARXML
import string

def convertARXMLFiles2ConfigXml(xmlConfigPath:string,aRXMLFilesPathlist:[]):

    rootNode=convertARXML2Config.integrateNodes2One(aRXMLFilesPathlist)
    convertARXML2Config.convertARXML2Config(rootNode,xmlConfigPath)


def convertConfigXml2ARXMLFiles(xmlConfigPath:string,targetPath:string,modelName:str=""):
    convertConfig2ARXML.convertConfigXml2ARXMLFiles(xmlConfigPath,targetPath,modelName)
                    




if __name__ == '__main__':

    
    xmlConfigPath="I:\\testM\\autosar_swc_configuration.xml"
    #xmlConfigPath="I:\\testM\\Swc_Expfcns_configuration.xml"
    '''
    aRXMLFilesPathList=["I:\\testM\ARXMLS\\test_component.arxml",
                        "I:\\testM\ARXMLS\\test_datatype.arxml",
                        "I:\\testM\ARXMLS\\test_implementation.arxml",
                        "I:\\testM\ARXMLS\\test_interface.arxml",
                        "I:\\testM\ARXMLS\\test_timing.arxml"]
    '''
    aRXMLFilesPathList=["I:\\testM\\testGenerate\\autosar_swc.arxml"]
    #aRXMLFilesPathList=["I:\\testM\\autosar_swc_expfcns.arxml"]
    #aRXMLFilesPathList=["I:\\testM\\autosar_swc_expfcns.arxml"]
    
    #aRXMLFilesPathList=["I:\\testM\\testGenerate\\autosar_swc_expfcns.arxml"]
    convertARXMLFiles2ConfigXml(xmlConfigPath,aRXMLFilesPathList)
    
    #xmlConfigPath="I:\\testM\\test_configuration.xml"
    targetPath="I:\\testM\\testGenerate"
    model_name="autosar_swc_expfcns"
    #model_name="autosar_swc"
    #convertConfigXml2ARXMLFiles(xmlConfigPath,targetPath,model_name)