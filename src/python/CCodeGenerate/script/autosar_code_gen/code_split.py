#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           code_split.py
#  @brief          代码拆分的类
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/5/19
# 
#**************************************************************************

import os
import logging

class CodeSplit():
    """
    代码拆分，计算是否需要进行函数或文件拆分
    """
    
    def __init__(self, buffer, options, filename_base, filename_ext):
        """
        构造函数
        @param[in]buffer        输出缓冲
        @param[in]options       选项
        @param[in]filename_base 文件名基本部分
        @param[in]filename_ext  文件名扩展名
        @note 辅助进行函数拆分或文件拆分，基本流程如下:
                1.调用enter_function。
                2.输出代码，若完成则转8。
                3.调用is_need_split_function，若为False则转2，否则拆分函数。
                4.调用is_need_split_file，若为False则转2，否则拆分文件。
                5.调用notify_splited。
                6.调用is_file_splited，若为True则在新的文件输出。
                7.转2.
                8.调用exit_function。
                
        """
        self.buffer = buffer
        self.options = options
        self.file_base = filename_base
        self.file_ext = filename_ext
        self.num_func = 0
        self.func_count = [1]
        self.file_count = 0
        
    def enter_function(self, function_name):
        """
        进入生成函数的过程。
        @param[in]function_name 函数名
        """
        self.num_func += 1
        self.func_count.append(1)
        
    def exit_function(self):
        """
        退出处理函数的过程。
        """
        self.num_func -= 1
        self.func_count.pop()

    def get_splited_number(self):
        """
        拆分的函数个数。
        """
        return  self.func_count[self.num_func]

    def get_function_postfix(self):
        """
        拆分的函数名字的后缀。
        拆分的第一个函数调用第二个函数，第二个函数中依次调用后续函数。
        """
        if self.func_count[self.num_func] > 1:
            return "%d" % self.func_count[self.num_func]
        return  ""
    
    def get_previous_function_postfix(self):
        """
        前一次拆分的函数名字的后缀。
        """
        if self.func_count[self.num_func] > 2:
            return "%d" % (self.func_count[self.num_func] - 1)
        return  ""

    def is_need_split_function(self):
        """
        是否需要进行拆分(函数)
        """
        return False

    def is_need_split_file(self):
        """
        是否需要进行文件拆分
        若返回真则is_need_split_function必定返回真
        """
        return False
        
    def is_file_splited(self):
        """
        是否进行了拆分(文件)
        """
        return False
        
    def notify_splited(self):
        """
        通知已进行了拆分
        """
        pass
        
    def notify_template_finished(self):
        """
        通知模板已经完成
        """
        #logging.debug(self.buffer.getvalue())
        file_name = os.path.join(self.options["code path"], self.file_base)
        file_name += self.get_function_postfix() + self.file_ext
        with open(file_name, 'a') as file_obj:
            file_obj.write(self.buffer.getvalue())
        self.buffer.clear()
        #logging.debug(self.buffer.getvalue())
        
    def notify_finished(self):
        """
        通知已经完成
        """
     #   logging.debug(self.buffer.getvalue())
        file_name = os.path.join(self.options["code path"], self.file_base)
        file_name += self.get_function_postfix() + self.file_ext
        with open(file_name, 'a') as file_obj:
            file_obj.write(self.buffer.getvalue())
            # 增加一个空行，避免C语言文件末尾没有
            file_obj.write('\n')
        self.buffer.clear()
     #   logging.debug(self.buffer.getvalue())
        