import subprocess
import os
import re
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import winreg


import traceback
output_log_file_path="i:\\output.log"


from .script import code_generator as code_generator
#import script.code_generator as code_generator
file_created = False

def needs_generate_equations(mo_file_path: str, equations_file_path: str) -> bool:
    """判断是否需要重新生成 equations 文件"""
    # 如果 equations 文件不存在，必须生成
    if not os.path.exists(equations_file_path):
        return True
    
    # 获取 modelica 文件的修改时间
    mo_mtime = os.path.getmtime(mo_file_path)
    # 获取 equations 文件的修改时间
    eq_mtime = os.path.getmtime(equations_file_path)
    
    # 如果模型文件比 equations 文件新，说明改过，需要重新生成
    return mo_mtime > eq_mtime

def getEquations(path_Oshell:str,path_observed:str,model_path:str): 
    # 定义观察者和事件处理器类
    class MyHandler(FileSystemEventHandler):
        def __init__(self,process):
            super().__init__()
            self.process = process
        def check_last_line(self, filepath):
            with open(filepath, 'r') as file:
                lines = file.readlines()
                if lines and lines[-1].strip() == "endflag":
                    return True
                else:
                    return False
        def on_created(self, event):
            global file_created
            if event.src_path.endswith("equations.txt"):
                #print("New equations.txt file created. Terminating Python program.")
                file_created = True
                while not self.check_last_line(event.src_path):
                    time.sleep(0.1)  # 每次循环等待0.1秒
                self.process.terminate()  # 终止外部进程
                
    # 假设你的C++可执行文件为 OMShell.exe
    executable_path = path_Oshell
    #print(model_path)
    # 传递给可执行文件的命令行参数
    argv = ['cd("'+path_observed+'")',"translateModel("+model_path+")"]  # 替换成你实际的命令行参数列表
    # 使用subprocess模块启动外部进程
    #process = subprocess.Popen([executable_path] + argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    with open(output_log_file_path, "a", encoding="utf-8") as f:
        f.write("executable_path is "+executable_path+"\n")
        f.write("argv is")
        f.write(argv[0]+"\n")
        f.write(argv[1]+"\n")
        f.write("\n")
    process = subprocess.Popen([executable_path] + argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # 启动观察者和事件处理器
    event_handler = MyHandler(process)
    observer = Observer()
    observer.schedule(event_handler, path=path_observed, recursive=False)
    observer.start()
    # 获取进程的输出和错误信息
    stdout, stderr = process.communicate()
    #print(stdout)
    #print(stderr)
    process.wait()  # 等待进程结束
    observer.stop()  # 停止观察者
    return file_created
#    return True

#根据解析的mo文件获取顶层项目路径
def getModelicaProjectPath(mo_file_path:str):
    # 获取目录路径
    directory = os.path.dirname(mo_file_path)
    
    # 初始化顶层目录
    top_directory = directory
    
    # 逐级向上查找，直到根目录
    while directory != "/" and directory != "":
        # 检查当前目录是否存在 package.mo 文件
        if os.path.exists(os.path.join(directory, "package.mo")):
            # 更新顶层目录为当前目录
            top_directory = directory
            # 定位到上一级目录
            directory = os.path.dirname(directory)
        else:
            break
    return top_directory
#获得库文件目录
def get_openmodelica_library_path():
    # 获取用户名
    username = os.getenv('USERNAME')
    # 构建路径
    library_path = os.path.join('C:\\', 'Users', username, 'Documents', 'AR','libraries')
        # 设置环境变量 OPENMODELICALIBRARY
    current_path = os.getenv('OPENMODELICALIBRARY')
    #if current_path is not None and current_path == library_path:
    if current_path is not None:
        return current_path
    else:
        os.environ['OPENMODELICALIBRARY'] = library_path
        
        # 打开注册表
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)
        
        # 将 OPENMODELICALIBRARY 写入注册表
        winreg.SetValueEx(key, "OPENMODELICALIBRARY", 0, winreg.REG_SZ, library_path)
        
        # 关闭注册表
        winreg.CloseKey(key)
        return library_path
#将moProPath的文件或者文件夹复制到library_path
def copy_to_library(moProPath, library_path):
    # 如果 moProPath 是文件夹，则递归复制整个文件夹
    if os.path.isdir(moProPath):
        shutil.copytree(moProPath, os.path.join(library_path, os.path.basename(moProPath)))
    # 如果 moProPath 是文件，则直接复制文件
    elif os.path.isfile(moProPath):
        shutil.copy(moProPath, library_path)


class MwModelDataContext:
    def __init__(self):
        self.TemplatePaths=[]
        self.WorkPath=""
        self.ModelName=""   #模型文件名
        self.RuntimeDebugEnabled=False
        self.InstallPath=""
        self.TempPath=""
        self.XMLName=""
        self.ComponentName="" #组件名

class MwModelData:
    def __init__(self):
        self.NormalEquations=[]
        self.OrdinaryNormalEquations=[]
        self.param_dict={}
        self.ModelName=None
    def loadEquations(self,filePath,mwOptions):
        initParamPath=os.path.join(filePath,"initParam.txt")
        with open(initParamPath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                left,right=line.split("=")
                left=left.strip()
                right=right.strip()
                #print("left: ",left)
                #print("right: ",right)
                if not right.strip():
                    continue
                if right[0]=="+":
                    right=right[1:]
                elif right[0]=="-":
                    right="("+right+")"
                self.param_dict[left]=right
        #equation_name= self.ModelName+"_equations.txt"
        equation_name="equations.txt"
        equationsPath=os.path.join(filePath,equation_name)
        #equationsPath=os.path.join(filePath,"equations.txt")

        with open(equationsPath, 'r') as file:
            lines = file.readlines()
            pport_replace_set={}
            left_set=set()
            for index,line in enumerate(lines):
                line=line.strip()
                #print(line)
                pre_process_flag=False
                for rPortModelica in mwOptions["rPortSet"]:
                    if rPortModelica in line and "if" in line and ">=" in line and index+1<len(lines):
                        next_line=lines[index+1].strip()
                        if rPortModelica not in next_line:
                            if ":=" in next_line:
                                left,right=next_line.split(":=")
                            else:
                                left,right = re.split(r'\s*=\s*', next_line, maxsplit=1)
                            left=left.strip()
                            right=rPortModelica+".y_"
                            left_set.add(left)
                            self.NormalEquations.append(left+" = "+right)
                            pre_process_flag=True
                if pre_process_flag:
                    continue
                        
                if "$START" in line or "$when" in line or "pre(" in line or "sample_time" in line or  ("temp" in line and "$DER." not in line)  or "flag" in line or len(line)==0 or "<=" in line or ">=" in line or "==" in line:
                    continue
                if not ("=" in line or ":=" in line):
                    continue
                if ":=" in line:
                    left,right=line.split(":=")
                else:
                    #print(re.split(r'\s*=\s*(?![^<])', line))
                    left,right = re.split(r'\s*=\s*', line, maxsplit=1)
                left=left.strip()
                if "$DER." in left: 
                    left=left.replace("$DER.","")
                right=right.strip()
                if right[-1]==";":  
                    right=right[:-1]
                #如果right部分表示整型或者浮点型常量
                if right.isdigit() or right.replace(".","").isdigit():
                    continue
                

                
                #将right中的参数替换为具体的值
                right_parts=re.split(r'[+,-,*,/]',right)
                for i,right_part in  enumerate(right_parts):
                    right_part=right_part.strip()
                    if right_part in self.param_dict:
                        right_parts[i]=self.param_dict[right_part]
                    elif right_part in pport_replace_set:
                        right_parts[i]="("+pport_replace_set[right_part]+")"
                operators = re.findall(r'[-+*/]', right)
                right = ''.join([num + op for num, op in zip(right_parts, operators)] + [right_parts[-1]])
                if left in mwOptions["pPortSet"]:
                    pport_replace_set[left]=right
                if left.split(".")[0] in mwOptions["rPortSet"]:
                    left_first=left.split(".")[0]+".u"
                    right_first=right
                    express_first=left_first+" = "+right_first
                    left_second=left
                    right_second=left_first
                    express_second=left_second+" = "+right_second
                    if express_first not in self.NormalEquations:
                        self.NormalEquations.append(express_first)
                    if express_second not in self.NormalEquations:
                        self.NormalEquations.append(express_second)
                    continue
                if left.split(".")[0] in mwOptions["irvSet"]:
                    left_first=left.split(".")[0]+".u"
                    right_first=right
                    express_first=left_first+" = "+right_first
                    left_second=left
                    right_second=left_first
                    express_second=left_second+" = "+right_second
                    if express_first not in self.NormalEquations:
                        self.NormalEquations.append(express_first)
                    if express_second not in self.NormalEquations:
                        self.NormalEquations.append(express_second)
                    continue
                equation_express=left+" = "+right
                if equation_express not in self.NormalEquations and left not in left_set:
                    self.NormalEquations.append(equation_express)
        #print("NormalEquations: ",self.NormalEquations)
        #for equation in self.NormalEquations:
        #    print(equation)

    def loadOrdinaryNormalEquations(self,filePath,mwOptions):
        
        #equation_name= self.ModelName+"_equations.txt"
        equation_name="equations.txt"
        equationsPath=os.path.join(filePath,equation_name)

        with open(equationsPath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line=line.strip()
                if "$START" in line or "$when" in line or "pre(" in line or "sample_time" in line or  "temp" in line  or "flag" in line or len(line)==0:
                    continue
                if not ("=" in line or ":=" in line):
                    continue
                if ":=" in line:
                    left,right=line.split(":=")
                else:
                    left,right = re.split(r'\s*=\s*', line, maxsplit=1)
                left=left.strip()
                if "$DER." in left: 
                    left=left.replace("$DER.","")
                right=right.strip()
                if right[-1]==";":  
                    right=right[:-1]
                equation_express=left+" = "+right
                if equation_express not in self.OrdinaryNormalEquations:
                    self.OrdinaryNormalEquations.append(equation_express)

#目标C代码生成的函数
#1. 调用OMC生成等式，在
def c_code_gen(xml_name: str, mo_file_path: str, model_path: str, sysplore_path: str, target_path: str):
    # 获取日志文件路径（和 util4ConfigXML 那边一致）
    username = os.getenv('USERNAME')
    workPath = os.path.join('C:\\', 'Users', username, 'Documents', 'MWORKS')
    log_dir = os.path.join(workPath, "..", "AR", "temp")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    #log_file_path = os.path.join(log_dir, f"{model_path.split('.')[-1]}_log.txt")
    error_log_file_path = os.path.join(log_dir, f"{model_path.split('.')[-1]}_error.txt")
    

    try:
        moProPath = getModelicaProjectPath(mo_file_path)
        moProPathName = os.path.basename(moProPath)

        library_path = get_openmodelica_library_path()
        moFullPath = os.path.join(library_path, moProPathName)

        if os.path.exists(moFullPath):
            shutil.rmtree(moFullPath)

        copy_to_library(moProPath, library_path)

        path_Oshell = sysplore_path + "/Tools/omshellTool/bin/OMShell.exe"
        path_observed = os.path.join(library_path, "..", "temp")
        if not os.path.exists(path_observed):
            os.makedirs(path_observed)

        equations_file = os.path.join(path_observed, f"flag_equations_{model_path.split('.')[-1]}.txt")

        if needs_generate_equations(mo_file_path, equations_file):
            with open(output_log_file_path, "a", encoding="utf-8") as f:
                f.write("need generate equation is true")
                f.write("\n")
            #print("Equations file missing or outdated, regenerating...")
            equation_txt_path = os.path.join(path_observed, "equation.txt")
            if os.path.exists(equation_txt_path):
                os.remove(equation_txt_path)
            is_generate = getEquations(path_Oshell, path_observed, model_path)
            with open(output_log_file_path, "a", encoding="utf-8") as f:
                f.write("is_generate is "+str(is_generate))
                f.write("\n")
        else:
            #print("Equations file is up to date, skipping generation.")
            is_generate = True
            
        if not os.path.exists(equations_file):
            with open(equations_file, "w", encoding="utf-8") as f:
                f.write("")  # 创建一个空文件

        # 创建调用对象
        mwOptions = {}
        mwModelData = MwModelData()
        mwOptions["code path"] = target_path
        mwModelDataContext = MwModelDataContext()
        mwModelDataContext.WorkPath = workPath
        mwModelDataContext.TemplatePaths.append(sysplore_path + "/Tools/autosar_template")
        mwModelDataContext.ModelName = model_path.split(".")[-1]
        mwModelDataContext.RuntimeDebugEnabled = True
        mwModelDataContext.InstallPath = sysplore_path
        mwModelDataContext.TempPath = path_observed
        mwModelDataContext.XMLName = xml_name
        
        mwModelData.ModelName = model_path.split(".")[-1]

        code_generator.generateCcode(mwOptions, mwModelDataContext, mwModelData)

    except Exception as e:
        # 记录错误到日志文件
        with open(error_log_file_path, "a", encoding="utf-8") as f:
            f.write("=== Exception occurred in c_code_gen ===\n")
            f.write(traceback.format_exc())
            f.write("\n")
        print(f"[ERROR] 发生异常，已写入日志文件: {error_log_file_path}")





#主函数
if __name__ == '__main__':
    c_code_gen("autosar_swc_configuration.xml","C:/Users/ASUS/Desktop/test/M2/Examples","M2.Examples.autosar_swc_Example.autosar_swc","D:/Program Files/MWORKS/Sysplorer 2023b","C:/Users/ASUS/Desktop/target/c")
    #c_code_gen("Swc_Expfcns_configuration.xml","C:/Users/ASUS/Desktop/test/M2/Examples","M2.Examples.Swc_Expfcns_Example.Swc_Expfcns","D:/Program Files/MWORKS/Sysplorer 2023b","C:/Users/ASUS/Desktop/test/autosar_swc_Expfcns")
    '''
    mo_file_path="C:/Users/ASUS/Desktop/test/M2/Examples"
    moProPath=getModelicaProjectPath(mo_file_path)
    model_path="M2.Examples.autosar_swc_Example.autosar_swc"
    print(moProPath)
    #获得moProPath的文件夹名
    moProPathName=os.path.basename(moProPath)
    print(moProPathName)
    library_path=get_openmodelica_library_path()
    print(library_path)
    moFullPath=os.path.join(library_path,moProPathName)
    print("test: ",moFullPath)
    #判断library_path是否含有名为moProPathName的文件或者文件夹，有的话则删除
    if os.path.exists(moFullPath):
        print("存在")
        shutil.rmtree(moFullPath)
    #将名为moProPath的文件或者文件夹复制到library_path
    copy_to_library(moProPath, library_path)   

    sysplore_path="D:/Program Files/MWORKS/Sysplorer 2023b"
    path_Oshell=sysplore_path+"/Tools/omshellTool/bin/OMShell.exe"
    path_observed=library_path+"/../temp"
    if not os.path.exists(path_observed):
        os.makedirs(path_observed)
    is_generate=getEquations(path_Oshell,path_observed)
    print(is_generate)
    #创建调用对象
    mwOptions={}
    mwModelData=MwModelData()
    target_path="C:/Users/ASUS/Desktop/test"
    mwOptions["code path"]=target_path
    mwModelDataContext=MwModelDataContext()
    username = os.getenv('USERNAME')
    # 构建路径
    workPath = os.path.join('C:\\', 'Users', username, 'Documents', 'MWORKS')
    mwModelDataContext.WorkPath=workPath
    mwModelDataContext.TemplatePaths.append(sysplore_path+"/Tools/autosar_template")
    mwModelDataContext.ModelName=model_path.split(".")[-1]
    mwModelDataContext.RuntimeDebugEnabled=True
    mwModelDataContext.InstallPath=sysplore_path
    mwModelDataContext.TempPath=path_observed

    #mwModelData.loadEquations(path_observed)
    code_generator.generateCcode(mwOptions,mwModelDataContext,mwModelData)

    

    
  #  xml_file = "test.xml"
    
  #  mo_file_path = "test.mo"
  #  model_path = "test.c"
  #  c_code_gen(xml_file,mo_file_path,model_path)
  #  print("C code generation end")


    '''
