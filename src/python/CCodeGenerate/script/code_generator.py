import os
import sys 
import struct
import platform
import subprocess
import logging
import traceback
import json
from datetime import date
from datetime import datetime
import shutil
import re
import glob


from jinja2 import TemplateError,TemplateSyntaxError,TemplateRuntimeError,TemplateNotFound,UndefinedError

from .autosar_code_gen.platformtypes_emit import PlatformTypes
from .autosar_code_gen.memmap_emit import MemMap
from .autosar_code_gen.rteproject_emit import RteProject
from .autosar_code_gen.projecthead_emit import ProjectHead
from .autosar_code_gen.projectbody_emit import ProjectBody
from .autosar_code_gen.rte_types_emit import Rte_Types
from .autosar_code_gen.code_buffer import CodeStringIO 
from .autosar_code_gen.code_split import CodeSplit 
from .autosar_code_gen.code_engine import CodeGeneratorEngine 
#from .autosar_code_gen.solver_model_data import SolverModelData
#from .autosar_code_gen.equ_emit import ModelEquations 

'''
from autosar_code_gen.platformtypes_emit import PlatformTypes
from autosar_code_gen.memmap_emit import MemMap
from autosar_code_gen.rteproject_emit import RteProject
from autosar_code_gen.projecthead_emit import ProjectHead
from autosar_code_gen.projectbody_emit import ProjectBody

from autosar_code_gen.code_buffer import CodeStringIO 
from autosar_code_gen.code_split import CodeSplit 
from autosar_code_gen.code_engine import CodeGeneratorEngine 
from autosar_code_gen.solver_model_data import SolverModelData
from autosar_code_gen.equ_emit import ModelEquations 
'''

from .autosar_configuration.autosar_config_app import *

# from MwPyModelData import *

#from mw_code_gen.func_emit import FunctionEmit 
#from mw_code_gen.record_emit import RecordEmit
#from mw_code_gen.code_emit import CodeEmit
#from mw_code_gen.code_header_emit import CodeHeaderEmit
#from mw_code_gen.scheduler_emit import SchedulerEmit
#from mw_code_gen.make_emit import MakefileEmit



def init_state_interface(options):
    for id_state,state in options["states"].items():
        options["state_interface"][id_state]="rtDW."+state["Source"].split(".")[-1]+"_DSTATE"

#YPH:运行Clang指令，我觉得这里就是将C语言代码格式化
def RunCommand(cmd):
    try:
        ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", timeout=None, check=True)
        if ret.returncode == 0:
            return ""
        else:
            return str(ret)
    except BaseException as e:
        return e.message

    


def generateCcode(mwOptions,mwModelDataContext, mwModelData):

    #f=open("E:\\log.txt","w");
    mwOptions["error message"] = ""
    c_autosar_path=mwOptions["code path"]+"//c_autosar";
    if os.path.exists(c_autosar_path):
        shutil.rmtree(c_autosar_path)
    os.mkdir(c_autosar_path)
    
    mwOptions["today"] = date.today()
    mwOptions["now"] = datetime.now()
    
    template_list=[]
    for index,template_path in enumerate(mwModelDataContext.TemplatePaths):
        template_list.append(template_path)


    # 设置日志
    if mwModelDataContext.RuntimeDebugEnabled:
        logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s", datefmt = '%Y-%m-%d %H:%M:%S',
            filename = os.path.join(mwModelDataContext.WorkPath, "py_code_gen.log"), filemode='w')
    else:
    
        logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s", datefmt = '%Y-%m-%d %H:%M:%S',
            filename = os.path.join(mwModelDataContext.WorkPath, "py_code_gen.log"), filemode='w')
    mwOptions["workPath"]=mwModelDataContext.WorkPath
  #  logging.debug("test in 20240328")
  #  logging.debug("Model name is {0}".format(mwModelDataContext.ModelName))
  #  logging.debug("Work directory is {0}".format(mwModelDataContext.WorkPath))
    #logging.debug("Temporary files directory is {0}".format(mwModelDataContext.TempPath))
  #  logging.debug("Template paths are {0}".format(mwModelDataContext.TemplatePaths))


        
    #进行固定的文件的复制
    #Compiler.h文件
    source_autosar_compiler_h=os.path.join(mwModelDataContext.InstallPath,"Tools","autosar_template","autosar","Compiler.h")
    target_autosar_compiler_h=os.path.join(mwOptions["code path"],"c_autosar//Compiler.h")
    shutil.copyfile(source_autosar_compiler_h,target_autosar_compiler_h)
    #rtwtypes.h
    source_autosar_rtwtypes_h=os.path.join(mwModelDataContext.InstallPath,"Tools","autosar_template","autosar","rtwtypes.h")
    target_autosar_rtwtypes_h=os.path.join(mwOptions["code path"],"c_autosar//rtwtypes.h")
    shutil.copyfile(source_autosar_rtwtypes_h,target_autosar_rtwtypes_h)    
    
    #Std_Types.h
    source_autosar_stdtypes_h=os.path.join(mwModelDataContext.InstallPath,"Tools","autosar_template","autosar","Std_Types.h")
    target_autosar_stdtypes_h=os.path.join(mwOptions["code path"],"c_autosar//Std_Types.h")
    shutil.copyfile(source_autosar_stdtypes_h,target_autosar_stdtypes_h)    
    
    #Rte_Type.h
    #source_autosar_rtetype_h=os.path.join(mwModelDataContext.InstallPath,"Tools","autosar_template","autosar","Rte_Type.h")
    #target_autosar_rtetype_h=os.path.join(mwOptions["code path"],"c_autosar//Rte_Type.h")
    #shutil.copyfile(source_autosar_rtetype_h,target_autosar_rtetype_h)  
    try:
        
        # 创建模板缓存文件夹
        temporary_path = os.path.join(mwModelDataContext.TempPath, "mw_embcg_module")
        if not os.path.exists(temporary_path):
            os.mkdir(temporary_path)

        # 用户配置转换为JSON对象
        #config_params = json.loads(mwOptions["configuration parameters"])

        # 读取用户定制内容的模板设置(不使用界面配置定制项而是使用json文件进行配置时打开此处，注释掉上一行)
        #with open(os.path.join(mwModelDataContext.TemplatePaths[1], "user_custom_template.json"), "r", encoding="utf-8") as fp:
        #    config_params = json.load(fp)
    
        # 读取目标平台的模板设置

        # 读取默认的模板设置
        '''
        with open(os.path.join(template_list[1], "default_templates.json"), "r", encoding="utf-8") as fp:
            default_template_map = json.load(fp)
        # 读取默认的内置替换配置
        with open(os.path.join(template_list[1], "default_builtin.json"), "r", encoding="utf-8") as fp:
            default_builtin_map = json.load(fp)
        # 读取默认的用户配置
        with open(os.path.join(template_list[1], "default_config_param.json"), "r", encoding="utf-8") as fp:
            default_config_param = json.load(fp)

        # 合并模板缺省设置
        # 合并内置替换配置
        # # 合并用户配置

        # 收集实验设置
        if "experiment" in config_params:
            if "simulation_interval" in config_params["experiment"]:
                if "start_time" in config_params["experiment"]["simulation_interval"] and config_params["experiment"]["simulation_interval"]["start_time"] != "":
                    default_config_param["experiment"]["simulation_interval"]["start_time"] =config_params["experiment"]["simulation_interval"]["start_time"]
                if "stop_defined" in config_params["experiment"]["simulation_interval"] and config_params["experiment"]["simulation_interval"]["stop_defined"] != "":
                    default_config_param["experiment"]["simulation_interval"]["stop_defined"] =config_params["experiment"]["simulation_interval"]["stop_defined"]
                if "stop_time" in config_params["experiment"]["simulation_interval"] and config_params["experiment"]["simulation_interval"]["stop_time"] != "":
                    default_config_param["experiment"]["simulation_interval"]["stop_time"] =config_params["experiment"]["simulation_interval"]["stop_time"]
            if "integration" in config_params["experiment"]:
                if "algorithm" in config_params["experiment"]["integration"] and config_params["experiment"]["integration"]["algorithm"] != "":
                    default_config_param["experiment"]["integration"]["algorithm"] =config_params["experiment"]["integration"]["algorithm"]
                if "step_size" in config_params["experiment"]["integration"] and config_params["experiment"]["integration"]["step_size"] != "":
                    default_config_param["experiment"]["integration"]["step_size"] =config_params["experiment"]["integration"]["step_size"]

        # 代码优化选项
        if "optimization" in config_params:
            if "code" in config_params["optimization"]:
                default_config_param["optimization"]["code"] = config_params["optimization"]["code"]
            if "inline_integration" in config_params["optimization"]:
                default_config_param["optimization"]["inline_integration"] = config_params["optimization"]["inline_integration"]
            
        # TODO
        # YPH:这里将配置的信息都放到了mwOptions中了
        mwOptions["template map"] = default_template_map
        mwOptions["builtin map"] = default_builtin_map
        mwOptions["configuration parameters"] = default_config_param

        logging.debug("Options are {0}".format(mwOptions))
        

        
        # TODO 增加定制路径，此处临时增加美的模板路径
        all_template_paths = template_list
        #all_template_paths.append(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder", "midea"))
        #all_template_paths.append(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder", "casia"))
        #all_template_paths.append(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder", "get"))

        ## 根据配置选项选择调用的模板，否则调用默认驱动
        tpl_file_list = {"udt_scheduler.tpl":"scheduler"} # 模板名和模板键值的映射，目前只有一项，后续可以增加
        target_name = ""
        if "target" in config_params["hardware_platform"]:
            target_name = config_params["hardware_platform"]["target"]
            if target_name in mwOptions["targets"]:  
                for root,dirs,files in os.walk(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder",mwOptions["targets"][target_name])):
                    for name in files:
                        if name in tpl_file_list:
                            #YPH:运行了这里，配置了main函数的模板文件，和模板的文件路径
                            mwOptions["template map"]["float_point"][tpl_file_list[name]] = mwOptions["targets"][target_name] + "/" + name
                            all_template_paths.append(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder"))
        else:
            mwOptions["template map"]["float_point"]["scheduler"] = "floatpoint/udt_scheduler.tpl"
            target_name = "default"
            all_template_paths.append(os.path.join(mwModelDataContext.InstallPath, "EmbedCoder", target_name))        
        '''      
        all_template_paths = template_list
        code_engine = CodeGeneratorEngine(model_data_context = mwModelDataContext, model_data = mwModelData, options = mwOptions, template_paths = all_template_paths)



    #进行Platform_Types文件生成
        with open(os.path.join(mwModelDataContext.InstallPath,"Tools","autosar_template","autosar","autosar_ecg_configuration.json"), "r", encoding="utf-8") as fp:
            autosar_ecg_map = json.load(fp)   
        mwOptions["autosar ecg"]=autosar_ecg_map
        platform_type=PlatformTypes(code_engine)
        buffer_platform_types=CodeStringIO()
        splitter_platform_types=CodeSplit(buffer_platform_types,mwOptions,"c_autosar//Platform_Types",".h")
        platform_type.emit(splitter=splitter_platform_types)
    #进行“ModelName”MemMap.h文件的生成
        mem_map=MemMap(code_engine)
        buffer_mem_map=CodeStringIO()
        modelname_mem_map=mwModelDataContext.ModelName+"_MemMap"
        splitter_mem_map=CodeSplit(buffer_mem_map,mwOptions,"c_autosar//"+modelname_mem_map,".h")
        mem_map.emit(splitter=splitter_mem_map)



        mwOptions["autosar_interface"]={}
        xmlPath=os.path.join(mwModelDataContext.WorkPath,mwModelDataContext.XMLName)
        if os.path.exists(xmlPath):
            #获取组件名
            mwModelDataContext.ComponentName=getComponentName(xmlPath)
           
           
            #进行Rte_Type文件生成
            accessMode=getAccessMode(xmlPath)
            mwOptions["accessMode"]=accessMode
            element_type_map=get_element_type(xmlPath)
            mwOptions["element_type_map"]=element_type_map
            autosar_array_types_info_xml=getImplementationDataType(xmlPath)
            autosar_array_types={}
            implementationShortName2ArraySize={}
            for array_name,autosar_array_type_info in autosar_array_types_info_xml.items():
                #autosar_array_types[array_name+"["+autosar_array_type_info[0]+"]"]=autosar_array_type_info[1]
                autosar_array_types[array_name]=[autosar_array_type_info[1],autosar_array_type_info[0]]
                implementationShortName2ArraySize[array_name]=autosar_array_type_info[0]
            mwOptions["autosar_array_types"]=autosar_array_types
            #mwOptions["implementationShortName2ArraySize"]=implementationShortName2ArraySize
            
            
            rte_type=Rte_Types(code_engine)
            buffer_rte_type=CodeStringIO()
            splitter_rte_type=CodeSplit(buffer_rte_type,mwOptions,"c_autosar//Rte_Type",".h")
            rte_type.emit(splitter=splitter_rte_type)          
           
            #进行Rte_项目名.h文件的生成
            #mwOptions["typeMap"]={}
            #for key,value in autosar_array_types.items():
            #    key_ordinary=key.split("[")[0].strip()
            #    mwOptions["typeMap"][key_ordinary]=value
            runnableEntitiesRte=getRunnableEntitiesRte(xmlPath)
            #print("runnableEntitiesRte is {0}".format(runnableEntitiesRte),file=f);
            mwOptions["runnableEntitiesRte"]=runnableEntitiesRte
            rPortsInfo=getRPorts(xmlPath)
            pPortsInfo=getPPorts(xmlPath)
            portInfoDict={}
            for rPortInfo in rPortsInfo:
                portInfoDict[rPortInfo[0]]=[rPortInfo[1],rPortInfo[2]]
            for pPortInfo in pPortsInfo:
                portInfoDict[pPortInfo[0]]=[pPortInfo[1],pPortInfo[2]]
            mwOptions["portInfoDict"]=portInfoDict

            #portDict={}
            #for rPortInfo in rPortsInfo:
            #    namePort=rPortInfo[1]
            #    nameElement=rPortInfo[2]
            #    portDict[namePort]=nameElement
            #for pPortInfo in pPortsInfo:
            #    namePort=pPortInfo[1]
            #    nameElement=pPortInfo[2]
            #    portDict[namePort]=nameElement   
            #mwOptions["port_element_info"]=portDict
            rte_project=RteProject(code_engine)
            buffer_rte_project=CodeStringIO()
            modelname_rte_project="Rte_"+mwModelDataContext.ComponentName
            splitter_rte_project=CodeSplit(buffer_rte_project,mwOptions,"c_autosar//"+modelname_rte_project,".h")
            rte_project.emit(splitter=splitter_rte_project)


            states=getStates(xmlPath)
            #print("states is {0}".format(states),file=f);
            mwOptions["states"]=states
            #这里设置mwOptions["rPortSet"]=set(),在进行变量值替换的时候，不进行替换
            mwOptions["rPortSet"]=set()
            for rPortInfo in rPortsInfo:
                mwOptions["rPortSet"].add(rPortInfo[0])
            mwOptions["pPortSet"]=set()
            for pPortInfo in pPortsInfo:
                mwOptions["pPortSet"].add(pPortInfo[0])
            #print("mwOptions[rPortSet] is {0}".format(mwOptions["rPortSet"]),file=f)
            runnableSampleTimes=getRunnableSampleTime(xmlPath)
            mwOptions["runnableSampleTimes"]=runnableSampleTimes
            mwOptions["statements"]=[]
            runnaleEntities=getRunnableEntities(xmlPath)
            runnableAutosarKeyDict={}
            for runnableInfo in runnaleEntities:
                runnableAutosarKeyDict[runnableInfo[1][0]]=runnableInfo[0]
            rPortAutosarDict={}
            for rPortInfo in rPortsInfo:
                rPortAutosarDict[rPortInfo[1]+"_"+rPortInfo[2]]=rPortInfo[0]
            pPortAutosarDict={}
            for pPortInfo in pPortsInfo:
                pPortAutosarDict[pPortInfo[1]+"_"+pPortInfo[2]]=pPortInfo[0]
            iRVs=getIRV(xmlPath)
            iRVAutosarDict={}
            for iRV in iRVs:
                iRVAutosarDict[iRV[1][0]]=iRV[0]

            mwOptions["runnableAutosarKeyDict"]=runnableAutosarKeyDict
            mwOptions["rPortAutosarDict"]=rPortAutosarDict
            mwOptions["pPortAutosarDict"]=pPortAutosarDict
            mwOptions["iRVAutosarDict"]=iRVAutosarDict
            mwOptions["irvSet"]=set()
            for irv in iRVs:
                mwOptions["irvSet"].add(irv[0])

            mwOptions["record"]=set()
            

            mwOptions["state_interface"]={}
            #init_state_interface(mwOptions)
            mwModelData.loadEquations(mwModelDataContext.TempPath,mwOptions)
            mwModelData.loadOrdinaryNormalEquations(mwModelDataContext.TempPath,mwOptions)
        #进行project.h文件的生成

            project_head=ProjectHead(code_engine)
            buffer_project_head=CodeStringIO()
            modelname_project_head=mwModelDataContext.ModelName
            splitter_project_head=CodeSplit(buffer_project_head,mwOptions,"c_autosar//"+modelname_project_head,".h")
            project_head.emit(splitter=splitter_project_head)


        #进行project.c文件的生成

            #print("rPortSampleTimes is {0}".format(rPortSampleTimes),file=f)
            

            
            runnableEntityNameSymbolMap=getRunnableEntitySymbolMap(xmlPath)
            mwOptions["runnableEntityNameSymbolMap"]=runnableEntityNameSymbolMap
            initRunnableEntityDic=getInitRunnableEntityName(xmlPath)
            mwOptions["initRunnableEntityDic"]=initRunnableEntityDic
            
            
            mwOptions["var2type"]={}
                             
            project_body=ProjectBody(code_engine)
            buffer_project_body=CodeStringIO()
            modelname_project_body=mwModelDataContext.ModelName
            splitter_project_body=CodeSplit(buffer_project_body,mwOptions,"c_autosar//"+modelname_project_body,".c")
            project_body.emit(splitter=splitter_project_body)


            
            # 使用clang-format格式化代码
            
            # clang-format程序
            clang_formater = os.path.join(mwModelDataContext.InstallPath, "external")  
            if struct.calcsize("P") == 8:
                clang_formater = os.path.join(clang_formater, "clang-format64")
            else:
                clang_formater = os.path.join(clang_formater, "clang-format")

            if platform.system().lower() == "windows":
                clang_formater = os.path.join(clang_formater, "clang-format.exe")
            else:
                clang_formater = os.path.join(clang_formater, "clang-format")

            src_files = os.path.join(mwOptions["code path"]+"//c_autosar", "*.c")
            h_files = os.path.join(mwOptions["code path"]+"//c_autosar", "*.h")
            clang_format_cmd_pre = "\"" + clang_formater + "\" --style=\"{BasedOnStyle: LLVM, Language: Cpp, IndentWidth: 2, ColumnLimit: 100, BreakBeforeBraces: Allman}\"" 
            
            # 执行clang-format格式化.c文件
            clang_format_cmd = clang_format_cmd_pre + " -i \""  + src_files + "\""
            cmd_ret = RunCommand(clang_format_cmd)
            if cmd_ret != "":
                mwOptions["error message"] = "Run command error: {0} error:{1}.".format(clang_format_cmd, cmd_ret)

            # 执行clang-format格式化.c文件
            clang_format_cmd = clang_format_cmd_pre + " -i \""  + h_files + "\""
            cmd_ret = RunCommand(clang_format_cmd)
            if cmd_ret != "":
                mwOptions["error message"] = "Run command error: {0} error:{1}.".format(clang_format_cmd, cmd_ret)
        
    except Exception as e:
       # print(e)
       # print(traceback.format_exc())
        logging.debug(f"error hapends when jicheng: {e}")
        logging.debug(f"error is : {traceback.format_exc()}")
        logging.error(traceback.format_exc())     