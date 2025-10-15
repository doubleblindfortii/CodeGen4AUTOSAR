#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           code_header_emit.py
#  @brief          C代码头文件输出
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/6/15
# 
#**************************************************************************

import os
import logging

class CodeHeaderEmit():
    """
    C代码头文件输出
    """
    
    def __init__(self, buffer, options, filename):
        """
        构造函数
        @param[in]buffer        输出缓冲
        @param[in]options       选项
        @param[in]filename      文件名
        @note 
        """
        self.buffer = buffer
        self.options = options
        self.file_name = os.path.join(options["code path"], filename)

    def notify_template_finished(self):
        """
        通知模板已经完成
        """
        #logging.debug(self.buffer.getvalue())
        with open(self.file_name, 'a') as file_obj:
            file_obj.write(self.buffer.getvalue())
        self.buffer.clear()
        
    def notify_finished(self):
        """
        通知已经完成
        """
        with open(self.file_name, 'a') as file_obj:
            file_obj.write(self.buffer.getvalue())
            # 增加一个空行，避免C语言文件末尾没有
            file_obj.write('\n')
        self.buffer.clear()

        