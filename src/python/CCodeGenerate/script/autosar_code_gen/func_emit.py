#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           func_emit.py
#  @brief          函数代码生成
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/9/15
# 
#**************************************************************************

import logging


class FunctionEmit():
    """
    生成用户自定义函数代码
    """
    
    def __init__(self, code_env):
        self.code_env = code_env
      
    def emit(self, user_funcs_splitter):
        """
        输出用户自定义函数代码 函数实现可能很大，将结果生成到临时文件中
        @param[in]user_funcs_splitter                  代码拆分器
        """
        
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["user_function"]["implementation"], splitter = user_funcs_splitter)
        self.code_env.code_engine.run_piece_template(template_filename = self.code_env.template_map["user_function"]["prototype"])
        
        #splitter.notify_finished()
        #internal_header_emitter.notify_finished()
