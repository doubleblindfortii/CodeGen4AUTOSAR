#**************************************************************************
# 
#  Copyright (c) 2020, wumbuk
#  All rights reserved.
# 
#  @file           code_env.py
#  @brief          代码生成的环境数据
# 
#  @version        v1.0
#  @author         杨培豪
#  @date           2021/6/16
# 
#**************************************************************************

import logging
import re


class CodeEnvironment():
    """
    代码生成的环境数据
    """
    
    def __init__(self, model_data_context, model_data, options, code_engine):
        """
        构造函数
        @param[in]model_data_context    模型数据环境
        @param[in]model_data            模型数据
        @param[in]options               选项
        @param[in]code_engine           代码生成引擎
        """
        
        self.model_data_context = model_data_context
        self.model_data = model_data
        self.options = options
        self.code_engine = code_engine
        self.has_scalar_when = False
        self.has_vector_when = False
        self.has_sample = False
        # 是否有自定义函数
        self.has_user_function = False
        # 每个缩进的空格数量
        self.indent_size = 2
        # 当前缩进数
        self.cur_indent_num = 0
        # 当前缩进
        self.cur_indent = ""
        self.one_indent = ' ' * self.indent_size
        self.completed_integerator_step_count = 0
        '''
        self.use_fixed_point = options["use fixed point"]
        # 模板映射表
        self.float_point_template_map = options["template map"]["float_point"]
        self.fixed_point_template_map = options["template map"]["fixed_point"]
        if self.use_fixed_point:
            self.template_map = self.fixed_point_template_map
            self.c_function_map = options["builtin map"]["function"]["fixed_point"]
            self.c_header_map = options["builtin map"]["header"]["fixed_point"]
        else:
            self.template_map = self.float_point_template_map
            self.c_function_map = options["builtin map"]["function"]["float_point"]
            self.c_header_map = options["builtin map"]["header"]["float_point"]

        self.global_name_map = {}
        # 数据类型占用位数
        #YPH:在code_genertor中通过用户配置的设置
        self.num_of_char = 8
        self.num_of_double = 32
        self.num_of_float = 16
        self.num_of_int = 32
        self.num_of_size_t = 32
        self.num_of_long = 32
        self.num_of_longlong = 64
        self.num_of_pointer = 32
        self.num_of_ptrdiff = 32
        # 最大原子长度
        #YPH:在code_genertor中通过用户配置的设置
        self.integer_atomic_size = 32
        self.floating_atomic_size = 32

        #容器相加的中间变量
        self.temp_list_vars = []

        self.temp_front_statments = [] ## 临时前置语句集合，会在模板中及时输出并清空
        self.temp_front_back_statments = [] ## 临时前置语句后的语句集合，会在模板中及时输出并清空
        self.temp_back_statments = [] ## 临时后置语句集合，会在模板中及时输出并清空

        # 缺省生成文件名
        self.header_files_name = ["momodel.h"]
        self.source_files_name = ["momodel.c"]
        # .h文件分块生成代码内容
        self.interface_include = []
        self.interface_macro = []
        self.interface_type = []
        self.interface_var_declare = []
        self.interface_var_define = []
        self.interface_func_declare = []
        self.interface_func_define = []
        # .c文件分块生成代码内容
        self.implement_include = []
        self.implement_macro = []
        self.implement_type = []
        self.implement_var_declare = []
        self.implement_var_define = []
        self.implement_func_declare = []
        self.implement_func_define = []
        #self.undef_macro = []
        # 待插入内容
        # YPH值得注意的是，这里是词典，就是键值对。
        self.include_insert = {}
        self.macro_insert = {}
        self.type_insert = {}
        self.var_declare_insert = {}
        self.var_define_insert = {}
        self.func_declare_insert = {}
        self.func_define_insert = {}
        #self.undef_insert = {}
        # 段首是否已经插入
        self.has_insert_head_segment = False
        # 代码风格枚举
        self.default_style = 0
        self.camelCase = 1
        self.PascalCase = 2
        self.lower_snake_case = 3
        self.UPPER_SNAKE_CASE = 4
        # 标识符组成部分枚举
        self.name = 0
        self.model_name = 1
        self.prefix = 2
        self.data_type = 3
        # 标识符定制
        #YPH: 标识符的最大长度，在code_generator中设置
        self.ident_max_length = 32
        self.use_custom_model_var_name = False # 模型变量缺省不按定制方式生成【内部】
        #YPH:标识符的风格，在code_generator中设置
        self.global_variable_style = self.camelCase # 标识符风格
        self.local_variable_style = self.lower_snake_case
        self.function_style = self.PascalCase
        self.macro_style = self.UPPER_SNAKE_CASE
        self.type_style = self.PascalCase
        #YPH:感觉都是0，通过code_generator中设置后
        self.format_input = "in" # 标识符前缀
        self.format_output = "out"
        self.format_parameter = "p"
        self.format_real = "r" # 标识符类型
        self.format_integer = "i"
        self.format_boolean = "b"
        #YPH:在code_generator中设置，每个是列表，列表中具有表示组成的编号
        self.format_global_variable = [self.model_name, self.name] # 标识符组成部分
        self.format_local_variable = [self.name]
        self.format_function = [self.model_name, self.name]
        self.format_macro = [self.model_name, self.name]
        self.format_type = [self.model_name, self.name]
        
        self.format_component = {} # 标识符各组成部分的值
        self.format_component[self.model_name] = model_data_context.ModelCName
        self.format_component[self.prefix] = ""
        self.format_component[self.data_type] = ""
        self.format_component[self.name] = []
        
        # 对外接口函数名字（名字单独指定，不使用定制规则）
        # YPH:就是Model里面的名字，函数名的设置
        self.have_terminate = False
        self.init_name = model_data_context.ModelCName + "_" + "Init"
        self.do_step_name = model_data_context.ModelCName + "_DoStep"
        self.terminate_name = model_data_context.ModelCName + "_Terminate"
        # 定制优化内容
        # YPH:修改array_loop_thrshold
        self.array_loop_threshold = 5
        self.logical_operator = "logical"
        # 编译用的外部源文件和库
        self.compile_sources_list = []
        self.compile_libraries_list = []
        # 是否进行代码保护选项
        self.overflow = False
        self.integer_division_by_zero = False
        # 代码放置的模式，默认为Compact
        # YPH：代码放置的方式
        self.Compact = 0
        self.CompactS = 1 # Compact with seperate data
        self.Modular = 2
        self.file_organization = self.Compact
        # 浮点是否双精度
        #YPH在code_generator中使用
        self.real_as_float = False
        # 类型枚举(用于存储容器区分)
        self.real_type = 0
        self.int_type = 1
        self.bool_type = 2
        self.string_type = 3
        # 是否使用紧凑型的数据字典数组【内部】
        self.compact_dict_array = True
        # 调用的外部函数集合
        self.extern_func_names = []
        # 是否使用各个基础类型数组数据类型【内部】
        self.has_real_array = False
        self.has_int_array = False
        self.has_bool_array = False
        # target是否是get(generate embedcode target)模式【内部】
        self.is_get_target = False
        # 获取输出的接口函数中输出变量
        self.real_var_in_get_output_func = []
        self.int_var_in_get_output_func = []
        self.bool_var_in_get_output_func = []
        # 代码优选速度
        self.optimization_code_speed = (options["configuration parameters"]["optimization"]["code"] == "speed")
        # 内联积分
        self.inline_integration = options["configuration parameters"]["optimization"]["inline_integration"]
        self.in_gen_update_when_condition = False
        # 层次化结构体类型
        self.hierarchy_struct_type = []
        # 是否使用层次化的变量名
        self.use_hierarchy_model_variable_name = options["configuration parameters"]["optimization"]["hierarchy_name"]
        '''

    #YPH:在code_engine的CodeGeneratorEngine初始化时，回指定model_vars的值
    def set_model_variables(self, vars):
        """
        设置模型变量
        """
        self.model_vars = vars

    def set_indent_size(self, n):
        """
        当前缩进
        """
        self.indent_size = n

    def get_cur_indent(self):
        """
        当前缩进
        """
        return self.cur_indent

    def get_one_indent(self):
        """
        一个缩进
        """
        return self.one_indent

    def get_cur_indent_width(self):
        """
        当前缩进宽度
        """
        return self.cur_indent_num

    def increase_indent(self):
        """
        增加缩进
        """
        self.cur_indent_num += self.indent_size
        self.cur_indent = ' ' * self.cur_indent_num

    def decrease_indent(self):
        """
        减少缩进
        """
        self.cur_indent_num -= self.indent_size
        self.cur_indent = ' ' * self.cur_indent_num

    def enter_completed_integerator_step(self):
        """
        进入积分步完成代码生成
        """
        self.completed_integerator_step_count += 1
        
    def exit_completed_integerator_step(self):
        """
        退出积分步完成代码生成
        """
        self.completed_integerator_step_count -= 1
        
    def in_completed_integerator_step(self):
        """
        是否正在积分步完成代码生成
        """
        return self.completed_integerator_step_count > 0

    def get_completed_integerator_step_count(self):
        """
        获取积分步完成的计数
        """
        return self.completed_integerator_step_count

    def get_truncate_name(self, name, to_truncate_ident = ""):
        """
        获取截断后的名字（根据配置决定是否使名字不超过31个字符）
        """
        if len(name) < self.ident_max_length:
            return name
        else:
            if name in self.global_name_map:
                return self.global_name_map[name]
            postfix = str(self.model_data.UniqueId)
            if to_truncate_ident == "":
                # 整个名字截断
                new_name = name[0 : (self.ident_max_length-1) - len(postfix)] + postfix
            else:
                # 只截断指定的标识符
                truncate_len = len(name) - (self.ident_max_length-1) + len(postfix) # 需要截断的长度
                if len(to_truncate_ident) < truncate_len: # 如果指定的截断字符串长度小于需要截断的长度
                    new_name = name[len(to_truncate_ident) : len(name)]
                    new_name = new_name[0 : (self.ident_max_length-1) - len(postfix)] + postfix
                else:
                    truncated_ident = to_truncate_ident[0 : len(to_truncate_ident) - truncate_len] + postfix
                    #new_name = name.replace(to_truncate_ident, truncated_ident, 1)
                    new_name = re.sub(to_truncate_ident, truncated_ident, name, count = 1, flags = re.IGNORECASE)

                    if len(new_name) > self.ident_max_length-1: # 存在指定截断的字符串并不存在的情况，故再次检查字符串长度
                        new_name = new_name[0 : (self.ident_max_length-1) - len(postfix)] + postfix

                if new_name[0].isdigit() or new_name[0] == "_":
                    new_name = new_name.replace(new_name[0],"a",1)
            self.global_name_map[name] = new_name
            return new_name

    def set_has_vector_when(self):
        """
        设置有向量条件的when
        """
        self.has_vector_when = True

    def set_has_scalar_when(self):
        """
        设置有标量条件的when
        """
        self.has_scalar_when = True

    def set_has_user_func(self):
        """
        设置有自定义函数
        """
        self.has_user_function = True

    def set_has_real_array(self):
        """
        设置有实型数组
        """
        self.has_real_array = True    
    
    def set_has_int_array(self):
        """
        设置有整型数组
        """
        self.has_int_array = True    
    
    def set_has_bool_array(self):
        """
        设置有布尔型数组
        """
        self.has_bool_array = True

    def set_dict_data(self, target_dict, dict_key, dict_value):
        """
        设置python字典数据，设置此接口因为模板不支持新增python字典数据
        """
        target_dict[dict_key] = dict_value


    def vessel_add(self, left_vessel, right_vessel):
        """
        将两个容器相加
        """
        self.temp_list_vars = left_vessel + right_vessel

    def add_extern_func_name(self, extern_func_name):
        """
        添加非重复外部函数名到容器中
        """
        if extern_func_name in self.extern_func_names:
            pass
        else:
            self.extern_func_names.append(extern_func_name)

    def is_extern_func_first_declare(self, extern_func_name):
        """
        判断外部函数是否第一次被声明
        """
        if extern_func_name in self.extern_func_names:
            return False
        else:
            return True

    def has_extern_builtin_func(self, butilin_func_name):
        """
        判断外部函数是否为builtin函数，并且确保函数定义只进行一次
        """
        res = False
        if butilin_func_name in self.extern_func_names:
            res = True
            self.extern_func_names.remove(butilin_func_name)
        return res

    def integer_to_real(self, str):
        """
        判断传入的字符串是否包含"."、"E"、"e",若都不包含，在后面加上".0"，若为float型，则在最后加上f
        """
        if "." in str or "E" in str or "e" in str or str == "":
            if self.real_as_float and not "f" in str:
                str += "f"
            else:
                pass
        else:
            if self.real_as_float and not "f" in str:
                if ")" in str:
                    str_index = str.find(")")
                    str = str[:str_index] + ".0f" + str[str_index:]
                else:
                    str += ".0f"
            else:
                if ")" in str:
                    str_index = str.find(")")
                    str = str[:str_index] + ".0" + str[str_index:]
                else:
                    str += ".0"
            
        return str

    def set_has_sample(self):
        """
        设置有sample
        """
        self.has_sample = True
        
    def set_real_var_in_get_output_func(self, vars):
        """
        设置获取输出的函数中输出实型变量
        """
        self.real_var_in_get_output_func = vars
        
    def set_int_var_in_get_output_func(self, vars):
        """
        设置获取输出的函数中输出整型变量
        """
        self.int_var_in_get_output_func = vars
        
    def set_bool_var_in_get_output_func(self, vars):
        """
        设置获取输出的函数中输出布尔变量
        """
        self.bool_var_in_get_output_func = vars
        
    def set_in_generate_update_when_condition(self, in_gen):
        """
        设置是否在生成更新when条件的表达式
        """
        self.in_gen_update_when_condition = in_gen
    
    def in_generate_update_when_condition(self):
        """
        判断是否在生成更新when条件的表达式
        """
        return self.in_gen_update_when_condition

    def has_collected_struct(self, value):
        """
        判断是否已经收集当前层次化结构体
        """
        if(self.hierarchy_struct_type.count(value) > 0):
            return True
        else:
            self.hierarchy_struct_type.append(value)
            return False

    def set_has_insert_head_segment(self):
        """
        设置已经插入了段前代码
        """
        self.has_insert_head_segment = True

    def reset_has_insert_head_segment(self):
        """
        重置是否插入段前代码的状态（在一个段结束之后调用）
        """
        self.has_insert_head_segment = False