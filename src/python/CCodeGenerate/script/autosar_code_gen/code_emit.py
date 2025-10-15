##**************************************************************************
## 
##  Copyright (c) 2021, 苏州同元软控信息技术有限公司
##  All rights reserved.
## 
##  @file           code_emit.py
##  @brief          代码生成模式
## 
##  @version        v1.0
##  @author         芦子豪
##  @date           2021/10/27
## 
##**************************************************************************

import os


from MwPyModelData import *

class CodeEmit:
    """
    代码生成模式
    """

    def __init__(self, code_env):
        """
        构造函数
        @param[in]code_env      代码生成环境
        """
        
        self.code_env = code_env

    def emit_compact(self, splitter, header_emitter, equ_content, user_funcs_content, mdl_data_content):
        """
        生成紧凑型代码
        @param[in]splitter                  代码拆分器
        @param[in]header_emitter            头文件输出器
        @param[in]equ_content               模型方程函数内容(初始化函数及计算函数)
        @param[in]user_funcs_content        用户自定义函数内容
        @param[in]mdl_data_content          模型数据结构体内容
        @param[in]need_include_macro        是否需要插入头文件唯一性控制宏
        @param[in]end_include_macro         控制宏结束
        @param[in]insert_head               是否插入模块头片段代码
        """
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = header_emitter,
                                 code_list = self.code_env.interface_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = True, end_include_macro = False, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_macro, insert_dict = self.code_env.macro_insert, 
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter, 
                                 code_list = self.code_env.interface_func_define, insert_dict = self.code_env.func_define_insert, 
                                 need_include_macro = False, end_include_macro = True, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"

        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_macro, insert_dict = self.code_env.macro_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.reset_has_insert_head_segment() # 将是否插入了段首的状态重置，以免前面的结果对此产生干扰
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = False)
        with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as mdl_data_obj:
            if "head" in self.code_env.type_insert and self.code_env.type_insert["head"] != "" and not self.code_env.has_insert_head_segment:
                mdl_data_obj.write(self.code_env.type_insert["head"]+ "\n")
            if "item_head" in self.code_env.type_insert and self.code_env.type_insert["item_head"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_head"] + "\n")
            mdl_data_obj.write(mdl_data_content) # 将模型数据结构体输出到文件
            if "item_tail" in self.code_env.type_insert and self.code_env.type_insert["item_tail"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_tail"] + "\n")
            if "tail" in self.code_env.type_insert and self.code_env.type_insert["tail"] != "": # 段尾在此输出
                mdl_data_obj.write(self.code_env.type_insert["tail"] + "\n")
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        # 将临时文件中的内容写入最终的目标文件中
        with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as func_obj:
            if "head" in self.code_env.func_define_insert and self.code_env.func_define_insert["head"] != "":
                func_obj.write(self.code_env.func_define_insert["head"]+ "\n")
            if "item_head" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_head"] != "":
                func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
            func_obj.write(equ_content)
            if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
            if self.code_env.has_user_function: # 如果有自定义函数，才插入
                if "item_head" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_head"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
                func_obj.write(user_funcs_content)
                if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
        # self.code_env.implement_func_define 中一定有内容，故不用考虑段尾会被遗漏的情形
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_define, insert_dict = self.code_env.func_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = False, insert_tail = True)
        # 按照misra-c 2012 20.5 禁用undef
        #self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
        #                         code_list = self.code_env.undef_macro, insert_dict = self.code_env.undef_insert,
        #                         need_include_macro = False, end_include_macro = False, insert_head = True)

        header_emitter.notify_finished()
        splitter.notify_finished()

    def emit_compact_with_separate_data(self, splitter, header_emitter, equ_content, user_funcs_content, mdl_data_content):
        """
        生成紧凑型代码(数据分开)
        @param[in]splitter                  代码拆分器
        @param[in]header_emitter            头文件输出器
        @param[in]equ_content               模型方程函数内容(初始化函数及计算函数)
        @param[in]user_funcs_content        用户自定义函数内容
        @param[in]mdl_data_content          模型数据结构体内容
        @param[in]need_include_macro        是否需要插入头文件唯一性控制宏
        @param[in]end_include_macro         控制宏结束
        @param[in]insert_head               是否插入模块头片段代码
        """
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = header_emitter,
                                 code_list = self.code_env.interface_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = True, end_include_macro = False, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_macro, insert_dict = self.code_env.macro_insert, 
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter, 
                                 code_list = self.code_env.interface_func_define, insert_dict = self.code_env.func_define_insert, 
                                 need_include_macro = False, end_include_macro = True, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"

        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_macro, insert_dict = self.code_env.macro_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.reset_has_insert_head_segment() # 将是否插入了段首的状态重置，以免前面的结果对此产生干扰
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = False)
        with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as mdl_data_obj:
            if "head" in self.code_env.type_insert and self.code_env.type_insert["head"] != "" and not self.code_env.has_insert_head_segment:
                mdl_data_obj.write(self.code_env.type_insert["head"]+ "\n")
            if "item_head" in self.code_env.type_insert and self.code_env.type_insert["item_head"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_head"] + "\n")
            mdl_data_obj.write(mdl_data_content)
            if "item_tail" in self.code_env.type_insert and self.code_env.type_insert["item_tail"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_tail"] + "\n")
            if "tail" in self.code_env.type_insert and self.code_env.type_insert["tail"] != "": # 段尾在此输出
                mdl_data_obj.write(self.code_env.type_insert["tail"] + "\n")
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as func_obj:
            if "head" in self.code_env.func_define_insert and self.code_env.func_define_insert["head"] != "":
                func_obj.write(self.code_env.func_define_insert["head"]+ "\n")
            if "item_head" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_head"] != "":
                func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
            func_obj.write(equ_content)
            if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
            if self.code_env.has_user_function: # 如果有自定义函数，才插入
                if "item_head" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_head"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
                func_obj.write(user_funcs_content)
                if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
        # self.code_env.implement_func_define 中一定有内容，故不用考虑段尾会被遗漏的情形
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_define, insert_dict = self.code_env.func_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = False, insert_tail = True)
        # 按照misra-c 2012 20.5 禁用undef
        #self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
        #                         code_list = self.code_env.undef_macro, insert_dict = self.code_env.undef_insert,
        #                         need_include_macro = False, end_include_macro = False, insert_head = True)

        header_emitter.notify_finished()
        splitter.notify_finished()

    def emit_modular(self, splitter, header_emitter,internal_header_emitter, equ_content, user_funcs_content, mdl_data_content):
        """
        生成模块型代码
        @param[in]splitter                  代码拆分器
        @param[in]header_emitter            momodel.h头文件输出器
        @param[in]internal_header_emitter   momodel_block1.h头文件输出器
        @param[in]equ_content               初始化函数内容
        @param[in]user_funcs_content        用户自定义函数内容
        @param[in]mdl_data_content          模型数据结构体内容
        @param[in]need_include_macro        是否需要插入头文件唯一性控制宏
        @param[in]end_include_macro         控制宏结束
        @param[in]insert_head               是否插入模块头片段代码
        @param[in]head_name                 需要插入唯一性控制宏时生成的宏名称
        """
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = header_emitter,
                                 code_list = self.code_env.interface_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = True, end_include_macro = False, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_macro, insert_dict = self.code_env.macro_insert, 
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter,
                                 code_list = self.code_env.interface_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"], header_emitter = header_emitter, 
                                 code_list = self.code_env.interface_func_define, insert_dict = self.code_env.func_define_insert, 
                                 need_include_macro = False, end_include_macro = True, insert_head = True, insert_tail = True, head_name = 0) ## 0 = "momodel.h"
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = internal_header_emitter,
                                 code_list = self.code_env.implement_macro, insert_dict = self.code_env.macro_insert,
                                 need_include_macro = True, end_include_macro = False, insert_head = True, insert_tail = True, head_name = 1) ## 1 = "momodel_block1.h"
        self.code_env.reset_has_insert_head_segment() # 将是否插入了段首的状态重置，以免前面的结果对此产生干扰
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = internal_header_emitter,
                                 code_list = self.code_env.implement_type, insert_dict = self.code_env.type_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = False, head_name = 1) ## 1 = "momodel_block1.h"
        with open(os.path.join(self.code_env.options["code path"], "momodel_block.h"), "a") as mdl_data_obj:
            if "head" in self.code_env.type_insert and self.code_env.type_insert["head"] != "" and not self.code_env.has_insert_head_segment:
                mdl_data_obj.write(self.code_env.type_insert["head"]+ "\n")
            if "item_head" in self.code_env.type_insert and self.code_env.type_insert["item_head"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_head"] + "\n")
            mdl_data_obj.write(mdl_data_content)
            if "item_tail" in self.code_env.type_insert and self.code_env.type_insert["item_tail"] != "":
                mdl_data_obj.write(self.code_env.type_insert["item_tail"] + "\n")
            if "tail" in self.code_env.type_insert and self.code_env.type_insert["tail"] != "": # 段尾在此输出
                mdl_data_obj.write(self.code_env.type_insert["tail"] + "\n")
            mdl_data_obj.write("#endif")
        # 按照misra-c 2012 20.5 禁用undef
        #self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["generate_implement"],header_emitter = undef_internal_header_emitter,
        #                         code_list = self.code_env.undef_macro, insert_dict = self.code_env.undef_insert,
        #                         need_include_macro = True, end_include_macro = True, insert_head = True, head_name = 2) ## 2 = "momodel_block2.h"
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_include, insert_dict = self.code_env.include_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_declare, insert_dict = self.code_env.var_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_var_define, insert_dict = self.code_env.var_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_declare, insert_dict = self.code_env.func_declare_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = True, insert_tail = True)
        with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as func_obj:
            if "head" in self.code_env.func_define_insert  and self.code_env.func_define_insert["head"] != "":
                func_obj.write(self.code_env.func_define_insert["head"]+ "\n")
            if "item_head" in self.code_env.func_define_insert  and self.code_env.func_define_insert["item_head"] != "":
                func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
            func_obj.write(equ_content)
            if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
            if self.code_env.has_user_function: # 如果有自定义函数，才插入
                if "item_head" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_head"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_head"] + "\n")
                func_obj.write(user_funcs_content)
                if "item_tail" in self.code_env.func_define_insert and self.code_env.func_define_insert["item_tail"] != "":
                    func_obj.write(self.code_env.func_define_insert["item_tail"] + "\n")
        # self.code_env.implement_func_define 中一定有内容，故不用考虑段尾会被遗漏的情形
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["generate_implement"], splitter= splitter, 
                                 code_list = self.code_env.implement_func_define, insert_dict = self.code_env.func_define_insert,
                                 need_include_macro = False, end_include_macro = False, insert_head = False, insert_tail = True)
        # 按照misra-c 2012 20.5 禁用undef
        #with open(os.path.join(self.code_env.options["code path"], "momodel.c"), "a") as func_obj:
        #    func_obj.write('#include"momodel_block2.h"'+ "\n")
        header_emitter.notify_finished()
        internal_header_emitter.notify_finished()
        splitter.notify_finished()


    def emit_init_array_data(self, header_emitter, splitter):
        """
        输出数据数组初始化源文件与头文件
        @param[in]header_emitter            头文件输出器
        @param[in]splitter                  源文件输出器
        """
        if self.code_env.model_vars.has_init_data_file():
            self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["initialize_array_data"], header_emitter = header_emitter, 
                                     model_vars = self.code_env.model_vars, index = 1)
            self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["initialize_array_data"], splitter= splitter, 
                                     model_vars = self.code_env.model_vars, index = 2)
            header_emitter.notify_finished()
            splitter.notify_finished
    
    def emit_extern_include(self, header_emitter):
        """
        输出外部函数include注解头文件
        @param[in]header_emitter            头文件输出器
        """
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["external_include"], header_emitter = header_emitter)
        header_emitter.notify_finished()