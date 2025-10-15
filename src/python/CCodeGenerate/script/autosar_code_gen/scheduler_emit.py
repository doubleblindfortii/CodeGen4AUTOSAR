#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           scheduler_emit.py
#  @brief          调度器
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/9/29
# 
#**************************************************************************

import logging


class SchedulerEmit():
    """
    调度器生成代码
    """
    
    def __init__(self, code_engine):
        self.engine = code_engine
      
    def emit(self, splitter):
        """
        输出求解调度代码
        @param[in]splitter                  代码拆分器
        """
        
        self.engine.run_template(template_filename = self.engine.code_env.template_map["scheduler"], splitter = splitter, 
                                 model_vars = self.engine.code_env.model_vars)
        
        splitter.notify_finished()