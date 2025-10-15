#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           code_buffer.py
#  @brief          代码缓存
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/1/15
# 
#**************************************************************************

import logging
from io import StringIO

class CodeAutoWrap():
    """
    自动换行
    """
    
    def __init__(self):
        self.start = 0
        
    # 进行自动换行    
    def do(self, s):
        return s#.rstrip()

#class CodeStringIO(StringIO):
class CodeStringIO:
    """
    模板输出的缓冲，同时具备自动换行和行数统计功能
    """
    
    def __init__(self):
        #super().__init__()
        self.num_lines = 0
        self.wraper = CodeAutoWrap()
        self.text = ""
        
    def write(self, s):
        #logging.debug("write '{0}'".format(s))
        # 先进行自动换行
        s = self.wraper.do(s)
        # 统计行数
        self.num_lines += s.count("\n",0)
        self.text += s
        #super().write(s)
    
    def clear(self):
        """
        清除缓冲内容
        """
        self.num_lines = 0
        self.text = ""
        #super().truncate(0)
        
    def get_line_count(self):
        """
        获取行数
        """
        return self.num_lines

    def getvalue(self):
        """
        获取内容
        """
        return self.text