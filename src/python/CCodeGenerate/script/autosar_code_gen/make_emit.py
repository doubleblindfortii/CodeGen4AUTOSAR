#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           make_emit.py
#  @brief          用于构建的文件生成
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/7/1
# 
#**************************************************************************

import logging


class MakefileEmit():
    """
    构建文件生成代码
    """
    
    def __init__(self, code_engine):
        self.engine = code_engine

    def emit(self, make_file_emitter):
        """
        输出求解器数据代码
        @param[in]make_file_emitter         makefile文件输出器
        """
        
        self.engine.run_header_template(template_filename = self.engine.code_env.template_map["makefile"], 
                                        header_emitter = make_file_emitter)
        
        make_file_emitter.notify_finished()