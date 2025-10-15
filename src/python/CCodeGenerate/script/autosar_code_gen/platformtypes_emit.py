#**************************************************************************
# 
#  Copyright (c) 2023, Wumbuk
#  All rights reserved.
# 
#  @file           platformtypes_emit.py
#  @brief          AUTOSAR平台类型文件
# 
#  @version        v1.0
#  @author         杨培豪
#  @date           2023/7/30
# 
#**************************************************************************

import logging
import os

class PlatformTypes():
    """
    AUTOSAR Platform_Types文件代码生成
    """
    
    def __init__(self, code_engine):
        self.engine = code_engine
      
    def emit(self, splitter):
        """
        输出求解器方程代码
        @param[in]equ_splitter             模型方程函数代码拆分器
        """
        self.engine.run_template(template_filename = "autosar/Platform_Types.tpl", splitter = splitter)
        

        splitter.notify_finished()