#**************************************************************************
# 
#  Copyright (c) 2023, Wumbuk
#  All rights reserved.
# 
#  @file           projectbody_emit.py
#  @brief          头文件
# 
#  @version        v1.0
#  @author         杨培豪
#  @date           2023/8/21
# 
#**************************************************************************

import logging
import os

class ProjectBody():
    """
    AUTOSAR {{ModelName}}.h文件代码生成
    """
    
    def __init__(self, code_engine):
        self.engine = code_engine
      
    def emit(self, splitter):
        """
        输出splitter
        @param[in]splitter             代码拆分器
        """
        self.engine.run_template(template_filename = "autosar/ProjectBody.tpl", splitter = splitter)
        

        splitter.notify_finished()