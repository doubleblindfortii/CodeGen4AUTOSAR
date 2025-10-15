#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           record_emit.py
#  @brief          函数代码生成
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/9/15
# 
#**************************************************************************

import logging


class RecordEmit():
    """
    生成记录的声明代码
    """
    
    def __init__(self, code_env):
        self.code_env = code_env
      
    def emit(self):
        """
        输出记录声明代码
        @param[in]splitter                  代码拆分器
        @param[in]header_emitter            头文件输出器
        @param[in]internal_header_emitter   内部头文件输出器
        """
        self.code_env.code_engine.run_piece_template(template_filename = self.code_env.template_map["record"]["constructor_implementation"])
        self.code_env.code_engine.run_piece_template(template_filename = self.code_env.template_map["record"]["declaration"])
        self.code_env.code_engine.run_piece_template(template_filename = self.code_env.template_map["record"]["prototype"])
        
