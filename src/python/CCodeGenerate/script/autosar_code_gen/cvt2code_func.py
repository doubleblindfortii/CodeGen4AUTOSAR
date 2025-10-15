##**************************************************************************
## 
##  Copyright (c) 2021, 苏州同元软控信息技术有限公司
##  All rights reserved.
## 
##  @file           cvt2code_func.py
##  @brief          函数中代码转换
## 
##  @version        v1.0
##  @author         田显钊
##  @date           2021/05/20
## 
##**************************************************************************

import logging

import MwPyModelData

from autosar_code_gen.cvt2code import ConvertToCode 

class FunctionEnvironment:
    """
    函数输出的环境
    """
    def __init__(self):
        # 需要前置的数据
        self.front_declare_data = []
        # 前置数据末尾的数据（主要存放变量声明之后的初始化，以保证遵循C89规范）
        self.front_declare_data_back = []
        # 除了需要前置以外的语句
        self.stat = []
        # 当前正在生成代码的函数（考虑嵌套调用，栈中最后一个为当前函数） set
        self.func_item = []

class ConvertToCodeInFunc(ConvertToCode):
    """
    函数中代码转换的类
    """

    def __init__(self, code_env):
        """
        构造函数
        @param[in]code_env      代码生成环境
        """
        super().__init__(code_env)
        # 外部函数include
        self.extern_func_includes = []
        # 外部函数链接库，每一项都是列表
        self.extern_func_libraries = []
        # 函数的C语言名字映射(函数id，C语言名字)
        self.function_names_map = {}
        # 函数到变量的映射(函数id，变量映射)
        self.func_var_map = {}
        # 变量的C语言名字映射(变量名，c语言名字)
        self.var_names_map = {}
        
        self.cur_func_env = []
        # 当函数返回类型为数组时的输入参数
        self.array_vars = []
        # 当前自定义函数是否有输入参数(模板中判断并更改此标志位)
        self.has_input = False

        self.statement_handler={}
        self.expression_handler={}
        self.expression_handler[MwPyModelData.ExpressionKind.RealLiteral] = self.to_real_literal
        self.expression_handler[MwPyModelData.ExpressionKind.IntegerLiteral] = self.to_integer_literal
        self.expression_handler[MwPyModelData.ExpressionKind.BooleanLiteral] = self.to_boolean_literal
        self.expression_handler[MwPyModelData.ExpressionKind.StringLiteral] = self.to_string_literal
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayLiteral] = self.to_array_literal
        self.expression_handler[MwPyModelData.ExpressionKind.Variable] = self.to_variable

        self.expression_handler[MwPyModelData.ExpressionKind.BinaryExpr] = self.to_binary_expr
        self.expression_handler[MwPyModelData.ExpressionKind.UnaryExpr] = self.to_unary_expr
        self.expression_handler[MwPyModelData.ExpressionKind.BuiltinFun] = self.to_builtin_func
        self.expression_handler[MwPyModelData.ExpressionKind.Range] = self.to_range
        self.expression_handler[MwPyModelData.ExpressionKind.ForIdent] = self.to_for_ident
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayStructVar] = self.to_array_struct_var
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayConstructor] = self.to_array_constructor
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayRealFromInt] = self.to_array_real_from_int
        self.expression_handler[MwPyModelData.ExpressionKind.ScalarRealFromInt] = self.to_scalar_real_from_int
        self.expression_handler[MwPyModelData.ExpressionKind.UserFunction] = self.to_user_function
        self.expression_handler[MwPyModelData.ExpressionKind.RecordConstructor] = self.to_record_constructor
        self.expression_handler[MwPyModelData.ExpressionKind.If] = self.to_func_if_expression
        self.expression_handler[MwPyModelData.ExpressionKind.Null] = self.to_null
        self.statement_handler[MwPyModelData.StatementKind.Single] = self.to_single_statement
        self.statement_handler[MwPyModelData.StatementKind.Multi] = self.to_multi_statement
        self.statement_handler[MwPyModelData.StatementKind.While] = self.to_while
        self.statement_handler[MwPyModelData.StatementKind.For] = self.to_for
        self.statement_handler[MwPyModelData.StatementKind.Null] = self.to_null
        
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayIndex] = self.to_array_index
        self.expression_handler[MwPyModelData.ExpressionKind.MemberAccess] = self.to_member_access
        self.statement_handler[MwPyModelData.StatementKind.Assign] = self.to_func_assign
        self.statement_handler[MwPyModelData.StatementKind.If] = self.to_func_if_statement
        self.statement_handler[MwPyModelData.StatementKind.Return] = self.to_return
        self.statement_handler[MwPyModelData.StatementKind.Break] = self.to_break

    def func_environment_push(self, func_type):
        """
        当前函数环境入栈 
        """
        self.cur_func_env.append(FunctionEnvironment())
        self.cur_func_env[-1].func_item.append(func_type)

    def func_environment_pop(self):
        """
        当前函数环境出栈
        """
        self.cur_func_env.pop()

    def get_cur_function(self):
        """
        获取当前函数
        """
        return self.cur_func_env[-1].func_item[-1]

    def declare_front_push(self, data):
        """
        函数前端增加变量声明
        """
        self.cur_func_env[-1].front_declare_data.append(data)

    def declare_front_back_push(self, data):
        """
        函数前端增加变量声明后的内容（变量初始化等）
        """
        self.cur_func_env[-1].front_declare_data_back.append(data)

    def stat_push(self, stat):
        """
        函数除了需要前置的数据之外的其他语句
        """
        self.cur_func_env[-1].stat.append(stat)

    def has_input_param(self):
        """
        设置当前函数为拥有输入参数
        """
        self.has_input = True
        
    def statement(self, stat):
        """
        语句转换
        """
        logging.debug("Statement is {0}".format(stat))
        self.statement_environment_push()

        res = self.statement_handler[stat.StatementKind](stat)
        # 去掉多余的换行
        res.strip('\n') + '\n'

        res = self.combine_statement_environment(res)
        self.statement_environment_pop()

        return res

    def expression(self, expr):
        """
        表达式转换
        """
        if not expr is None and not self.code_env.has_real_array and  not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Real:
            self.code_env.has_real_array = True
        if not expr is None and not self.code_env.has_int_array and  not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
            self.code_env.has_int_array = True
        if not expr is None and not self.code_env.has_bool_array and  not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
            self.code_env.has_bool_array = True
        logging.debug("Expression is {0}".format(expr.String.String))
        logging.debug("ExpressionKind is {0}".format(expr.ExpressionKind))
        return self.expression_handler[expr.ExpressionKind](expr).strip('\n')

    def add_external_function_include(self, inc):
        """
        添加外部函数include内容
        """
        self.extern_func_includes.append(inc)

    def add_external_function_libraries(self, libs):
        """
        添加外部函数的链接库
        """
        self.extern_func_libraries.append(libs)

    def get_external_function_includes(self):
        """
        获取所有外部函数include内容
        """
        return self.extern_func_includes

    def get_external_function_libraries(self):
        """
        取所有外部函数的链接库
        """
        res_libs = []
        # TODO： 对库进行依赖性排序，然后加入到res_libs
        return res_libs

    def get_function_c_name(self, func_type):
        """
        获取函数C语言名字(如果名字过长则会截断)
        """
        if func_type.ID in self.function_names_map:
            return self.function_names_map[func_type.ID]
        
        c_name = MwPyModelData.ToCName(func_type.Name)
        if c_name in self.c_key_word:
            c_name = c_name + "_"
        c_name = self.code_env.get_truncate_name(c_name, "")
        self.function_names_map[func_type.ID] = c_name
        return c_name

    def get_local_variable_c_name(self, var_name, func_type):   ## TODO , func_type 如果是同一函数中的同一个变量，则缓存起来
        """
        获取局部变量C语言的名字（名字过长则会截断）
        """
        if func_type.ID in self.func_var_map and var_name in self.var_names_map:
            return self.func_var_map[func_type.ID][var_name]

        var_c_name = ""
        # Q-Ident进行转换
        if var_name.startswith("'"):
            var_c_name = MwPyModelData.ToCName(var_name)
        # C关键字末尾加下划线
        elif var_name in self.c_key_word:
            var_c_name = var_name + "_"
        # 其余原样输出
        else:
           var_c_name = var_name
        var_c_name = self.code_env.get_truncate_name(var_c_name, "")
        self.var_names_map[var_name] = var_c_name
        self.func_var_map[func_type.ID] = self.var_names_map

        return var_c_name

    def to_func_assign(self, stat):
        """
        函数内部赋值转换
        """      
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["user_function_assign"], statement_node = stat)

    def to_func_arrray_index(self, expr):
        """
        函数内部数组索引
        """
        return self.to_array_index(self,expr)

    def to_func_if_statement(self, stat):
        """
        函数内部if语句
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_statement"], statement_node = stat)

    def to_return(self, stat):
        """
        函数内部return语句
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["return_statement"], statement_node = stat)

    def to_variable(self, expr):
       """
       函数内部变量转换
       """
       return self.get_local_variable_c_name(expr.Variable.Name, self.cur_func_env[-1].func_item[-1])

    def to_func_if_expression(self, expr):
        ndims = 0
        if expr.Type.IsArray:
            ndims = expr.Type.Ndims

        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_expression"], expr_node = expr, ndims=ndims)

