#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           modelequ.py
#  @brief          模型方程
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/1/6
# 
#**************************************************************************

import logging


class ModelEquations():
    """
    模型方程处理及生成代码
    """
    
    def __init__(self, code_engine):
        self.engine = code_engine
      
    def emit(self, equ_splitter):
        """
        输出求解器方程代码
        @param[in]equ_splitter             模型方程函数代码拆分器
        """
        self.engine.run_template(template_filename = self.engine.code_env.template_map["model_equations"][self.engine.code_env.options["configuration parameters"]["experiment"]["integration"]["algorithm"]], splitter = equ_splitter)

        equ_splitter.notify_finished()

