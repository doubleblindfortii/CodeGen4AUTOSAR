

import os
import re
import sys
import traceback
import logging
from itertools import zip_longest

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import FileSystemBytecodeCache

#import MwPyModelData
#from .model_var import ModelVariables 
#from .cvt2code_model import ConvertToCodeInModel
#from .cvt2code_func import ConvertToCodeInFunc
from .code_env import CodeEnvironment
'''
from autosar_code_gen.model_var import ModelVariables 
from autosar_code_gen.cvt2code_model import ConvertToCodeInModel
from autosar_code_gen.cvt2code_func import ConvertToCodeInFunc
from autosar_code_gen.code_env import CodeEnvironment
import re
'''

def getIntegratorInit(idIntegrator,options,model_data):
    """
    根据idIntegrator获取在Init函数中应该具有的语句
    """
    res=[]
    modelicaName=options["states"][idIntegrator]["Source"]
    lefts=options["state_interface"][idIntegrator]
    for left in lefts:
        if "discrete" in left:
            continue
        fullModelicaName=modelicaName.strip()+".k"
        if fullModelicaName in model_data.param_dict.keys():
            right=model_data.param_dict[fullModelicaName]
            if '.' in right and 'f' not in right:
                right=right+'f'
            else:
                right=right+'.0f'
        else :
            right='1.0f'
        right=right+";\n"
        res.append(left+" = "+right)
    return res



def replace_data_init_custormer(statement,options):
    """
    将语句中的用户自定义的给替换
    """
    parts=re.split("[+]|[-]|[*]|[/]",statement)
    operators=[]
    operators_set={"+","-","*","/"}
    for s in statement:
        if s in operators_set:
            operators.append(s)
    
    for i,part in enumerate(parts):
        if part.strip() in options["dict_non_array_data_initial"].keys():
            parts[i]=options["dict_non_array_data_initial"][part.strip()]
    result_list = [item for pair in zip_longest(parts, operators) for item in pair if item is not None]
    res="".join(result_list)
    return res
    

def replace_integrator_y(statement,options):
    """
    将语句中的integrator进行替换
    """
    for id_state,state in options["states"].items():
        modelicaSource=state["Source"]
        be_replaced="_".join(modelicaSource.strip().split("."))+"_y"
        target=options["state_interface"][id_state]
        statement=statement.replace(be_replaced,target)
    return statement

def state_have_integrator(statement,options):
    """
    句子statement中是否含有和积分器有关的语句
    """
    for id_state,state in options["states"].items():
        modelicaSource=state["Source"]
        if "_".join(modelicaSource.strip().split(".")) in statement:
            return True
    return False

def getIntegratorExpression(statement,idIntegrator,Runnable,options):
    '''
    返回求积分的算数
    '''    
    res=[]
    left,right=statement.split("=")
    left_express_list=options["state_interface"][idIntegrator]
    for left_express in left_express_list:
        if "Delay" in left_express:
            right_parts=re.split(r'[*,/]',right)
            operators=re.findall(r'[*/]', right)
            for i,right_part in enumerate(right_parts):
                runnableModelica=options["runnableAutosarKeyDict"][Runnable]
                if runnableModelica in right_part:
                    right_parts[i]=left_express
            right_express= ''.join([num + op for num, op in zip(right_parts, operators)] + [right_parts[-1]])
        else:
            right_express=right.strip().replace(".","_")
            right_express = re.sub(r'(\d+)(?=[+*/-]|$)', r'\g<1>.0f', right_express)
        sample_time="1"
        if "Delay" not in left_express:
            if "dataReadAccess" in options["runnableEntitiesRte"][Runnable].keys():
                sample_time=options["runnableSampleTimes"][Runnable]
            right_express=sample_time+" * "+right_express+";\n"
        else:
            right_express=right_express+";\n"
        if "Delay" in left_express:
            res.append(left_express+"="+right_express)
        else:
            res.append(left_express+"+="+right_express)
    return res

def get_pre_integrator_statements(runnableEntity,idIntegrator,options,model_data):
    pre_pports=[]
    pre_irv=[]
    intergrator_y_express=options["states"][idIntegrator]["Source"]+".y"
    delay_path=".".join(options["states"][idIntegrator]["Path"].strip().split(".")[1:])
    state_full_path=options["states"][idIntegrator]["Path"]+"."+options["states"][idIntegrator]["Source"]
    for equation in model_data.NormalEquations:
        left,right = re.split(r'\s*=\s*', equation, maxsplit=1)
        left=left.strip()
        right=right.strip()
        if intergrator_y_express in right and delay_path in right:
            for pport_mo in options['pPortSet']:
                if pport_mo in left:
                    for pport in options["runnableEntitiesRte"][runnableEntity]["dataWriteAccess"]:
                        if options["pPortAutosarDict"][pport]==pport_mo:
                            pre_pports.append(options["autosar_interface"][pport][0]+"("+options["state_nameList"][state_full_path][1]+");")
                            #for state_interface in options["state_interface"][idIntegrator]:
                            #    pre_pports.append(options["autosar_interface"][pport][0]+"("+state_interface+");")
                            #pre_pports.append(options["autosar_interface"][pport]+"("+options["state_interface"][idIntegrator][0]+");") #
            for irv_mo in options['irvSet']:
                if irv_mo in left:
                    for irv in options["runnableEntitiesRte"][runnableEntity]["writeLocalAccess"]:
                        if options["iRVAutosarDict"][irv]==irv_mo:
                            pre_irv.append(options["autosar_interface"][irv+"_write"][0]+"("+options["state_nameList"][state_full_path][1]+");")
                            #for state_interface in options["state_interface"][idIntegrator]:
                            #    pre_irv.append(options["autosar_interface"][irv+"_write"][0]+"("+state_interface+");")
                            #pre_irv.append(options["autosar_interface"][irv+"_write"]+"("+options["state_interface"][idIntegrator][0]+");")
    '''                     
    if "dataWriteAccess" in options["runnableEntitiesRte"][runnableEntity].keys():
        
            nameIntegrator=options["state_interface"][idIntegrator]
            pre_pports.append(options["autosar_interface"][pport]+"("+nameIntegrator+");")
    if "writeLocalAccess" in options["runnableEntitiesRte"][runnableEntity].keys():
        for writeLocal in options["runnableEntitiesRte"][runnableEntity]["writeLocalAccess"]:
            nameIntegrator=options["state_interface"][idIntegrator]
            pre_irv.append(options["autosar_interface"][writeLocal+"_write"]+"("+nameIntegrator+");")
    '''
    return pre_pports,pre_irv

def queryHaveIntegrators(value,options):
    #print(value)
    res_states=[]
   # if value in options["runnableAutosarKeyDict"].keys():
    modelicaRunnable=options["runnableAutosarKeyDict"][value]
    #print("modelicaRunnable",modelicaRunnable)
    #print("options[states]",options["states"])
    for id_state,state in options["states"].items():
        source=state["Source"]
        path=state["Path"]
        if modelicaRunnable in source.strip().split(".") or modelicaRunnable in path.strip().split("."):
            res_states.append(id_state)
    #print("res_states",res_states)
    return len(res_states)>0,res_states

def have_occured(value,options):
    if value in options["record"]["statement"].keys():
        options["record"]["statement"][value]+=1
        return True
    else:
        options["record"]["statement"][value]=1
        return False
def save_autosar_interface(value,autosar_item,options,_type):
    """
    保存mwOptions中的autosar_interface的东西
    """
    options["autosar_interface"][autosar_item]=(value,_type)
    return "";
def save_autosar_interface_ErrorStatus(value,autosar_item,options,_type):
    options["autosar_interface_ErrorStatus"]={}
    options["autosar_interface_ErrorStatus"][autosar_item]=(value,_type)
    

def get_left_post_statements(left_statement,options,dictAccess):
    post_statements_pport=[]
    post_statements_irv=[]
    left_statement=left_statement.strip()
    if "dataWriteAccess" in dictAccess.keys():
        for dataWrite in dictAccess["dataWriteAccess"]:
            modelicaName=options["pPortAutosarDict"][dataWrite].strip()
            if left_statement==modelicaName and not modelicaName in options["record"]:
                post_statements_pport.append(options["autosar_interface"][dataWrite][0]+"("+get_variable_name(left_statement.split("."))+");\n")
                options["record"].add(modelicaName)
    if "writeLocalAccess" in dictAccess.keys():
        for writeLocal in dictAccess["writeLocalAccess"]:
            modelicaName=options["iRVAutosarDict"][writeLocal].strip()
            modelicaName=modelicaName+"_u"
            if left_statement==modelicaName and not modelicaName in options["record"]:
                post_statements_irv.append(options["autosar_interface"][writeLocal+"_write"][0]+"("+get_variable_name(left_statement.split("."))+");\n")
                options["record"].add(modelicaName)       
    return post_statements_pport,post_statements_irv
 
import re
import os

def get_block_signals(model_data, options):
    ordinaryNormalEquations = model_data.OrdinaryNormalEquations
    res = {}  # 键是模型元素名，值是结构体中的信号名
    enableSystem_set = {}  # 键值为使能子系统的名字，值为其字符部分所在的索引

    log_path = "i://signal.log"

    # 确保目录存在（对于 i:// 可能是映射盘，不一定需要）
    log_dir = os.path.dirname(log_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    with open(log_path, "w", encoding="utf-8") as log_file:
        for equation in ordinaryNormalEquations:
            log_file.write(f"[EQUATION] {equation}\n")

            left, right = re.split(r'\s*=\s*', equation, maxsplit=1)
            right_parts = re.split(r'[+,\-,*,/]', right)

            for right_part in right_parts:
                right_part = right_part.strip()
                if "EnableSubsystem" in right_part:
                    parts_right_part = right_part.split(".")
                    for i, part_right_part in enumerate(parts_right_part):
                        if "EnableSubsystem" in part_right_part:
                            enableSystem = ".".join(parts_right_part[:i+1])
                            enableSystem_set[enableSystem] = i
                            log_file.write(f"  Found EnableSubsystem: {enableSystem} (index {i})\n")

            for right_part in right_parts:
                right_part = right_part.strip()
                for enableSystem in enableSystem_set.keys():
                    if enableSystem in right_part and "booleanToReal" not in right_part:
                        parts_right_part = right_part.split(".")
                        signal_name = parts_right_part[enableSystem_set[enableSystem] + 1]
                        res[enableSystem] = signal_name
                        log_file.write(f"  Mapped: {enableSystem} -> {signal_name}\n")

        options["enableSystem2signal"] = res
        log_file.write("\n[FINAL MAPPING]\n")
        for k, v in res.items():
            log_file.write(f"{k} => {v}\n")

    return res

 
'''
#返回使能模块的信号，键是模型元素名，值是结构体中的信号名  
def get_block_signals(model_data,options):
    ordinaryNormalEquations=model_data.OrdinaryNormalEquations
    res={} #键是模型元素名，值是结构体中的信号名
    res_set=set()
    enableSystem_set={} #键值为使能子系统的名字，值为其字符部分所在的索引
    count=1
    for equation in ordinaryNormalEquations:
        left,right = re.split(r'\s*=\s*', equation, maxsplit=1)
        right_parts=re.split(r'[+,-,*,/]',right)
        for right_part in right_parts:
            right_part=right_part.strip()
            if "EnableSubsystem" in right_part:
                parts_right_part=right_part.split(".")
                #第一个part表示.拆分后的，第二个part表示操作符拆分后的
                for i,part_right_part in enumerate(parts_right_part):
                    if "EnableSubsystem" in part_right_part:
                        enableSystem=".".join(parts_right_part[:i+1])
                        enableSystem_set[enableSystem]=i
        for right_part in right_parts:
            right_part=right_part.strip()
            for enableSystem in enableSystem_set.keys():
                if enableSystem in right_part and "booleanToReal" not in right_part:
                    parts_right_part=right_part.split(".")
                    signal_name=parts_right_part[enableSystem_set[enableSystem]+1]
                    res[enableSystem]=signal_name
        options["enableSystem2signal"]=res
    return res
'''

#被getStates调用                   
def getArrayStateElementDeclare(state_path,model_data,options):
    isArray=False
    arraySize=0
    for ordinaraEquation in model_data.OrdinaryNormalEquations:
        left,right = re.split(r'\s*=\s*', ordinaraEquation, maxsplit=1)
        left=left.strip()
        right=right.strip()
        if state_path in right:
            for pport in options["pPortSet"]:
                if pport==left:
                    portRefName=options["portInfoDict"][pport][0]
                    elementRefName=options["portInfoDict"][pport][1]
                    element_type=options["element_type_map"][portRefName+"_"+elementRefName]
                    if element_type in options["autosar_array_types"].keys():
                        isArray=True
                        arraySize=options["autosar_array_types"].get(element_type)[1]
    return isArray,arraySize

            
    
def getStates(options,model_data):
    """
    返回所有的状态
    """
    if len(options["states"].keys())==1:
        res="DW","rtDW"
    else:
        res="D_Work","rtDWork"
    options["state_nameList"]={}
    source_record=set()
    count_single=0
    count_array=0
    for id_state,state in options["states"].items():
        source=state["Source"]
        path=state["Path"]
        key=path.strip()+"."+source.strip()
        temp=[]
        state_path=state["Path"].strip().split(".")[-1]+"."+state["Source"].strip()
        isArray,arraySize=getArrayStateElementDeclare(state_path,model_data,options) 
        source=source+"_DSTATE"
        source_use_temp=source
        if source in source_record:
            if not isArray:
                source=source+"_"+chr(ord("a")+count_single)
                options["state_interface"][id_state]=[res[1]+"."+source]
                count_single+=1
                source_record.add(source)
            else:
                source=source+"_"+chr(ord("m")+count_array)
                source_record.add(source)
                temp_state_interface=[]
                arraySize=int(arraySize)
                for i in range(arraySize):
                    temp_state_interface.append(res[1]+"."+source+"["+str(i)+"]")
                options["state_interface"][id_state]=temp_state_interface
                source_use_temp=source
                source=source+"["+str(arraySize)+"]"
                count_array+=1
        else:
            source_record.add(source)
            options["state_interface"][id_state]=[res[1]+"."+source]
        temp.append(source)
        if len(options["states"].keys())==1:
            temp.append("rtDW"+"."+source_use_temp)
        else:
            temp.append("rtDWork"+"."+source_use_temp)
        options["state_nameList"][key]=temp
    return res





def get_num_from_str(input_string,pattern):

    # 定义正则表达式模式，匹配括号内或括号外的数字字符，忽略空格
    

    # 使用正则表达式进行匹配
    match = pattern.search(input_string)

    # 如果匹配成功，打印匹配的数字字符
    if match:
        number = match.group(1)
        return number
        
    else:
        return ''
        
def isRunnableOccurRight(modelicaRunnableEntity,statement):
    left,right=statement.split("=")
    left=left.strip()
    right=right.strip()
    right_parts_comp=re.split(r'[+,-,*,/]',right)
    for i,right_part in enumerate(right_parts_comp):
        right_parts_comp[i]=right_part.strip()
        right_parts=right_parts_comp[i].split(".")
        for j,right_part_unit in enumerate(right_parts):
            right_parts[j]=right_part_unit.strip()
            if modelicaRunnableEntity in right_parts[j]:
                return True
    return False



def get_right_statements(right,options,dictAccess):
    """
    获得右侧语句
    """
    res=""
    pre_statements_rport=[]
    pre_statements_irv=[]
    right_parts=re.split(r'[+,-,*,/]',right)
    operators = re.findall(r'[-+*/]', right)
    index_flag_unmodify=len(right_parts)
    for i,right_part_unit in enumerate(right_parts):
        right_part_unit=right_part_unit.strip()
        if "dataReadAccess" in dictAccess.keys():
            for dataRead in dictAccess["dataReadAccess"]:
                modelicaName=options["rPortAutosarDict"][dataRead].strip()
                if right_part_unit==modelicaName+".y_" and right_part_unit not in options["record"]:
                    left_var=modelicaName+"_y_"
                    _type=options["autosar_interface"][dataRead][1]
                    options["var2type"][left_var]=_type
                    pre_statements_rport.append(_type+" "+left_var+" = "+options["autosar_interface"][dataRead][0]+"();\n")
                    options["record"].add(right_part_unit) 
        if "readLocalAccess" in dictAccess.keys():
            for readLocal in dictAccess["readLocalAccess"]:
                modelicaName=options["iRVAutosarDict"][readLocal].strip()
                if right_part_unit==modelicaName+".y_" and right_part_unit not in options["record"]:
                    left_var=modelicaName+"_y_"
                    _type=options["autosar_interface"][readLocal+"_read"][1]
                    options["var2type"][left_var]=_type
                    pre_statements_irv.append(_type+" "+left_var+" = "+options["autosar_interface"][readLocal+"_read"][0]+"();\n")
                    options["record"].add(right_part_unit) 
        if "booleanToReal.y" in right_part_unit:
            right_parts[i]="1"
        for enableSystem,signal in options["enableSystem2signal"].items():
            if enableSystem+"."+signal in right_part_unit:
                right_parts[i]="rtB."+signal
                index_flag_unmodify=i
    rights_standard=[]
    for i,right_part in enumerate(right_parts):
        if i!=index_flag_unmodify:
            rights_standard.append(get_variable_name(right_part.split(".")))
        else:
            rights_standard.append(right_part)        
    res= ''.join([num + op for num, op in zip(rights_standard, operators)] + [rights_standard[-1]])+";\n"           
    return pre_statements_rport,pre_statements_irv,res

def get_type(prototypeName,options):
    """
    根据prototypeName获取类型
    """
    if prototypeName in options["element_type_map"].keys():
        type=options["element_type_map"][prototypeName]
        if type in options["autosar_array_types"].keys():
            #print(options["typeMap"][type])
            return options["autosar_array_types"][type][0]
        else:
            #print(type)
            return type
    return "void"

def get_parts_split(value,keys):
    """
    根据keys，将value给分割
    """
    return re.split(keys,value)
def get_operators_split(value,operators):
    """
    根据operators，将value的符号给压栈
    """
    res=[]
    for s in value:
        if s in operators:
            res.append(s)
    return res

def get_statement_type(left_stament,right_stament,options):
    right_parts=re.split(r'[+,-]',right_stament)
    left_stament=left_stament.strip()
    res="float64"
    weight={"sint8":0,"float64":1,"Double":2}
    for right_part in right_parts:
        for var,_type in options["var2type"].items():
            if var in right_part:
                if weight[_type]>weight[res]:
                    res=_type
                    #if res=="Double":
                    #    res="float64"
    options["var2type"][left_stament]=res
    return res
def get_conditional_express(condition_var,model_data,options):
    res=""
    for ordinaraEquation in model_data.OrdinaryNormalEquations:
        left,right = re.split(r'\s*=\s*', ordinaraEquation, maxsplit=1)
        left=left.strip()
        right=right.strip()
        if condition_var in left and "==" in right:
            right_parts=re.split(r'==',right)
            operators=re.findall(r'==', right)
            for i,right_part in enumerate(right_parts):
                right_part=right_part.strip()
                if right_part in model_data.param_dict.keys():
                    right_parts[i]=model_data.param_dict[right_part]
                for portModelicaName,port_and_element in options["portInfoDict"].items():
                    if portModelicaName in right_part:
                        interface_name=port_and_element[0]+"_"+port_and_element[1]
                        if interface_name in options["autosar_interface_ErrorStatus"].keys():
                            right_parts[i]=options["autosar_interface_ErrorStatus"][interface_name][0]+"()"
                        elif interface_name in options["autosar_interface"].keys():
                            right_parts[i]=options["autosar_interface"][interface_name][0]+"()"
            

            
            res= ''.join([num + op for num, op in zip(right_parts, operators)] + [right_parts[-1]])
    return res
                    
                
def fileter(parts,options,model_data):
    
    for i,part in enumerate(parts):
        part=part.strip()
        #先替换参数
        if part in model_data.param_dict.keys():
            parts[i]=model_data.param_dict[part]
        #再替换接口
        #首先，替换port接口
        for portModelicaName,port_and_element in options["portInfoDict"].items():
            if portModelicaName in part:
                interface_name=port_and_element[0]+"_"+port_and_element[1]
                if interface_name in options["autosar_interface_ErrorStatus"].keys():
                    parts[i]=options["autosar_interface_ErrorStatus"][interface_name][0]+"()"
                elif interface_name in options["autosar_interface"].keys():
                    parts[i]=options["autosar_interface"][interface_name][0]+"()"
        #再替换irv接口
        for irvName,irvModelicaName in options["iRVAutosarDict"].items():
            if irvModelicaName+".y_" in part:
                interface_name=irvName+"_read"
                if interface_name in options["autosar_interface"].keys():
                    parts[i]=options["autosar_interface"][interface_name][0]+"()"  
    return parts 


        
def getEnableStatements(modelicaRunnableEntity,options,model_data):
    res=[]
    if_content=[]
    endFlag=False
    for ordinaraEquation in model_data.OrdinaryNormalEquations:
        left,right = re.split(r'\s*=\s*', ordinaraEquation, maxsplit=1)
        right_parts=re.split(r'[+,-,*,/]',right)
        operators = re.findall(r'[-+*/]', right)
        if modelicaRunnableEntity in left and "EnableSubsystem.booleanToReal.y" in left and "if" in right and "then" in right:
            pattern = r'if\s+(.*?)\s+then'
            matches=re.search(pattern,right)
            if matches:
                conditional_var=matches.group(1)
                conditional_express=get_conditional_express(conditional_var,model_data,options)
                res.append("if( "+conditional_express+" ){\n")
                endFlag=True
        elif modelicaRunnableEntity in left and "EnableSubsystem"in left:
            for enableSystem,signal in options["enableSystem2signal"].items():
                if enableSystem+"."+signal in left:
                    left="rtB."+signal
            right_parts=fileter(right_parts,options,model_data)
            right_standard= ''.join([num + op for num, op in zip(right_parts, operators)] + [right_parts[-1]])
            if_content.append(left+" = "+right_standard+";\n")
    res.extend(if_content)
    if endFlag:
        res.append("}\n")
    return res
def get_variable_name(var_list):
    """
    返回合法的var_list的变量命名
    """
    return "_".join(var_list)


def mw_name_filter(value, code_env):
    """
    名字过滤器
    """
    return code_env.get_truncate_name(value)

def mw_cur_indent_filter(value, code_env):
    """
    当前缩进的过滤器
    """
    return code_env.get_cur_indent() + value

def mw_remove_if_stat_filter(value, if_stat):
    """
    移除if语句（过滤器）
    """
    # 删除if语句
    if_len = len(if_stat)
    res_str = ""
    pre_pos = 0
    pos = value.find(if_stat)
    while pos != -1:
        res_str += value[pre_pos:pos]
        pre_pos = pos + if_len

        brace_left_count = 1
        brace_right_count = 0
        # {必定存在
        brace_left_pos = value.find("{", pre_pos)
        pre_pos = brace_left_pos + 1
        quote_sym = False
        while pre_pos < len(value):
            if not quote_sym:
                if value[pre_pos] == '"':
                    quote_sym = True
                elif value[pre_pos] == '}':
                    brace_right_count += 1
                    if brace_left_count == brace_right_count:
                        pre_pos += 1
                        break
                elif value[pre_pos] == '{':
                    brace_left_count += 1
            else:
                if value[pre_pos] == '"' and value[pre_pos - 1] != '\\':
                    quote_sym = False
            pre_pos += 1
            
        pos = value.find(if_stat, pre_pos)
    if pre_pos < len(value):
        res_str += value[pre_pos:len(value)]
    return res_str

def mw_to_integrator_calc_filter(value, old_name, new_name, if_stat):
    """
    计算函数转为积分计算的简化函数（过滤器）
    """
    # 修改函数名
    new_value = value.replace(old_name, new_name)
    # 删除if语句
    return mw_remove_if_stat_filter(new_value,if_stat)

def mw_to_integrator_completed_calc_filter(value, if_stat):
    """
    计算函数转为积分计算完成的简化函数（过滤器）
    """
    return value.replace(if_stat, "/*" + if_stat + "*/")

class CodeGeneratorEngine():
    """
    代码生成引擎
    """
    
    def __init__(self, model_data_context, model_data, options, template_paths):
        """
        构造函数
        @param[in]model_data_context    模型数据环境
        @param[in]model_data            模型数据
        @param[in]options               选项
        @param[in]template_paths        模板路径
        """

        self.code_env = CodeEnvironment(model_data_context = model_data_context, model_data = model_data, 
                                      options = options, code_engine = self)
        
        template_loader = FileSystemLoader(searchpath = template_paths, encoding = 'utf-8')
        byte_code_cache = FileSystemBytecodeCache(directory = os.path.join(self.code_env.model_data_context.TempPath, "mw_embcg_module"), pattern = 'mw_%s.cache')
        self.env = Environment(loader=template_loader, trim_blocks = True, lstrip_blocks = True, line_statement_prefix = '#', line_comment_prefix = '##', autoescape = False, 
            extensions = ['jinja2.ext.do','jinja2.ext.loopcontrols','jinja2.ext.with_', 'jinja2.ext.debug'], auto_reload = True, bytecode_cache = byte_code_cache)
        #作为过滤器提供给模板使用
        self.env.filters["mw_valid_name"] = mw_name_filter
        self.env.filters["mw_cur_indent"] = mw_cur_indent_filter
        #self.env.filters["mw_c_name"] = MwPyModelData.ToCName
        self.env.filters["mw_to_integrator_calc"] = mw_to_integrator_calc_filter
        self.env.filters["mw_to_completed_calc"] = mw_to_integrator_completed_calc_filter
        self.env.filters["mw_remove_if_stat"] = mw_remove_if_stat_filter
        self.env.filters["get_parts_split"]=get_parts_split
        self.env.filters["get_operators_split"]=get_operators_split
        self.env.filters["get_variable_name"]=get_variable_name
        self.env.filters["get_right_statements"]=get_right_statements
        self.env.filters["save_autosar_interface"]=save_autosar_interface
        self.env.filters["get_left_post_statements"]=get_left_post_statements
        self.env.filters["have_occured"]=have_occured
        self.env.filters["queryHaveIntegrators"]=queryHaveIntegrators
        self.env.filters["get_pre_integrator_statements"]=get_pre_integrator_statements
        self.env.filters["getIntegratorExpression"]=getIntegratorExpression
        self.env.filters["state_have_integrator"]=state_have_integrator
        self.env.filters["getIntegratorInit"]=getIntegratorInit
        self.env.filters["isRunnableOccurRight"]=isRunnableOccurRight
        self.env.filters["get_type"]=get_type
        self.env.filters["get_block_signals"]=get_block_signals
        self.env.filters["getStates"]=getStates
        self.env.filters["get_statement_type"]=get_statement_type
        self.env.filters["getEnableStatements"]=getEnableStatements
        self.env.filters["save_autosar_interface_ErrorStatus"]=save_autosar_interface_ErrorStatus
        #self.env.tests = test
        #self.env.globals = {'model_data' : self.model_data, 'splitter' : splitter, 'options' : self.options}
        
        # 模型变量    
        #self.model_vars = ModelVariables(code_env = self.code_env)
        #f2=open("E:\\log_model_var.txt","w");   
        #print("Time name is '{0}'",file=f2);
        
        #f2.close();  

        #self.code_env.set_model_variables(self.model_vars)

        # 模型代码转换
      #  self.model_converter = ConvertToCodeInModel(code_env = self.code_env)
        # 函数代码转换
      #  self.func_converter = ConvertToCodeInFunc(code_env = self.code_env)
        # 代码转换(根据所处的环境切换)
      #  self.converter = self.model_converter
        

    def run_template(self, template_filename, splitter, **kwdata):
        """
        运行模板
        @param[in]template_filename 模板名
        @param[in]splitter          代码分割器
        @param[in]kwdata            数据
        """
        
        try:
        #    temp_globals = {'model_data' : self.code_env.model_data, 'splitter' : splitter, 'options' : self.code_env.options, 
        #                    'code_engine' : self, 'code_env' : self.code_env, 'MwPyModelData':MwPyModelData}
            temp_globals = {'model_data' : self.code_env.model_data, 'splitter' : splitter, 'options' : self.code_env.options, 
                            'code_engine' : self, 'code_env' : self.code_env}
            template = self.env.get_template(name = template_filename, globals = temp_globals)
            stream = template.stream(kwdata)
            stream.disable_buffering()
            while True:
                try:
                    splitter.buffer.write(next(stream))
                    
                except StopIteration:
                    # 模板输出完成
                    splitter.notify_template_finished()
                    break
        
        except Exception as e:
            raise

    def run_header_template(self, template_filename, header_emitter, **kwdata):
        """
        运行模板
        @param[in]template_filename 模板名
        @param[in]header_emitter    头文件生成器
        @param[in]kwdata            数据
        """
        
        try:
   #         temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
   #                         'code_env' : self.code_env, 'MwPyModelData':MwPyModelData}
            temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
                            'code_env' : self.code_env}
            template = self.env.get_template(name = template_filename, globals = temp_globals)
            stream = template.stream(kwdata)
            stream.disable_buffering()
            while True:
                try:
                    header_emitter.buffer.write(next(stream))
                    
                except StopIteration:
                    # 模板输出完成
                    header_emitter.notify_template_finished()
                    break
        
        except Exception as e:
            raise

    def run_piece_template(self, template_filename, **kwdata):
        """
        运行小段模板，返回模板执行后的结果
        @param[in]template_filename 模板名
        @param[in]kwdata            数据
        """

        try:
            #temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
            #                'code_env' : self.code_env, 'MwPyModelData':MwPyModelData}
            temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
                            'code_env' : self.code_env}
            template = self.env.get_template(name = template_filename, globals = temp_globals)
            result = template.render(kwdata)
            return result        
        except Exception as e:
            raise 

    def run_string_template(self, template_string, **kwdata):
        """
        运行字符串模板，返回模板执行后的结果
        @param[in]template_string   模板字符串
        @param[in]kwdata            数据
        """

        try:
           # temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
           #                 'code_env' : self.code_env, 'MwPyModelData':MwPyModelData}
            temp_globals = {'model_data' : self.code_env.model_data, 'options' : self.code_env.options, 'code_engine' : self,
                            'code_env' : self.code_env}
            template = self.env.from_string(source = template_string, globals = temp_globals)
            result = template.render(kwdata)
            return result        
        except Exception as e:
            raise

    def switch_to_func_converter(self):
        """
        切换为函数转换
        """
        self.converter = self.func_converter

    def switch_to_model_converter(self):
        """
        切换为模型转换
        """
        self.converter = self.model_converter