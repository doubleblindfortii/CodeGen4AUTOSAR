##**************************************************************************
## 
##  Copyright (c) 2021, 苏州同元软控信息技术有限公司
##  All rights reserved.
## 
##  @file           cvt2code.py
##  @brief          代码转换的基类
## 
##  @version        v1.0
##  @author         田显钊
##  @date           2021/05/20
## 
##**************************************************************************

import logging
import abc

from MwPyModelData import *

class StatementEnvironment:
    """
    语句输出的环境
    """
    def __init__(self):
        self.front_statements = []
        self.back_statements = []
        self.local_vars = []
        self.local_vars_with_init = []
        self.no_block_sym = False
        self.local_array_vars_map = {} ## key:涉及数组表达式 value:front_statements中定义的数组数据名
        self.local_iter_vars_map = {} ## key分配的临时变量名，value状态（占用False/空闲True）
        self.local_fixedpoint_vars_map = {} ## key:涉及定点表达式 value:front_statements中定义的定点数据名

class ForData:
    """
    for数据
    """
    def __init__(self):
        # for变量与c代码表达式的映射
        self.for_ident_map = {}

    def push_for_ident(self, for_ident, expr):
        """
        for变量入栈
        """
        self.for_ident_map[for_ident] = expr

    def get_for_ident_expression(self, for_ident):
        """
        获取for变量的表达式
        """
        if for_ident in self.for_ident_map:
            return self.for_ident_map[for_ident]
        else:
            return ""

    def is_for_ident_in(self, for_ident):
        """
        数据中是否f存在指定的for变量
        """
        if for_ident in self.for_ident_map:
            return True
        else:
            return False

class ConvertToCode(abc.ABC):
    """
    代码转换的抽象基类
    """

    def __init__(self, code_env):
        """
        构造函数
        @param[in]code_env      代码生成环境
        """
        
        self.code_env = code_env
        # 语句环境
        self.statement_env = []
        # for环境
        self.for_context = []
        # 记录的C语言名字映射(记录全名，C语言名字)
        self.record_names_map = {}
        # 记录构造函数的C语言名字映射(记录全名，C语言名字)
        self.record_constructor_names_map = {}
        # 记录到变量的映射(记录全名，变量映射)
        self.record_var_map = {}
        # 记录成员变量的C语言名字映射(记录成员变量名，c语言名字)
        self.record_var_names_map = {}
        # array部分内置函数集合
        self.array_builtin_functions = { BuiltinFunKind.Promote, \
              BuiltinFunKind.Size1, \
              BuiltinFunKind.Size2, \
              BuiltinFunKind.Scalar, \
              BuiltinFunKind.Vector, \
              BuiltinFunKind.Matrix, \
              BuiltinFunKind.Identity, \
              BuiltinFunKind.Diagonal, \
              BuiltinFunKind.Zeros, \
              BuiltinFunKind.Ones, \
              BuiltinFunKind.Linspace, \
              BuiltinFunKind.Cross, \
              BuiltinFunKind.Skew, \
              BuiltinFunKind.Transpose, \
              BuiltinFunKind.Symmetric, \
              BuiltinFunKind.Outerproduct, \
              BuiltinFunKind.Min1, \
              BuiltinFunKind.Max1, \
              BuiltinFunKind.Sum, \
              BuiltinFunKind.Product }

        # C中的关键字且不是Modelica的关键字
        self.c_key_word = {"int", "short", "long", "double", "float", "char", "void", "sizeof", "signed", "unsigned", "struct", \
            "union", "enum", "typedef", "auto", "static", "extern", "register", "const", "volatile", "do", "goto", "switch", "case", \
            "default", "inline", "restrict", "_Bool", "_Complex", "_Imaginary", "_Alignas", "_Alignof", "_Atomic", "_Static_assert", \
            "_Noreturn", "_Thread_local", "_Generic"}

    def get_unique_postfix(self):
        """
        获取唯一性后缀
        """
        return "{0}".format(self.code_env.model_data.UniqueId)

    def set_no_block_scoping_symbol(self, st):
        """
        设置语句环境无需范围界定符号（C语言中“{}”）
        """
        if len(self.statement_env) > 0:
            self.statement_env[-1].no_block_sym = True

    def statement_contains_array_var(self, array_var_key):
        res = False
        if len(self.statement_env) > 0:
            if array_var_key in self.statement_env[-1].local_array_vars_map:
                res = True
        return res

    def statement_push_array_var(self, array_var_key, array_var_defined_name):
        if len(self.statement_env) > 0:
            self.statement_env[-1].local_array_vars_map[array_var_key] = array_var_defined_name

    def statement_get_array_var(self, array_var_key):
        st = self.statement_contains_array_var(array_var_key)
        if not st:
            return (st, "")
        if len(self.statement_env) > 0:
            return (st, self.statement_env[-1].local_array_vars_map[array_var_key])

    def statement_contains_fixedpoint_var(self, fixedpoint_var_key):
        res = False
        if len(self.statement_env) > 0:
            if fixedpoint_var_key in self.statement_env[-1].local_fixedpoint_vars_map:
                res = True
        return res

    def statement_push_fixedpoint_var(self, fixedpoint_var_key, fixedpoint_var_defined_name):
        if len(self.statement_env) > 0:
            self.statement_env[-1].local_fixedpoint_vars_map[fixedpoint_var_key] = fixedpoint_var_defined_name

    def statement_get_fixedpoint_var(self, fixedpoint_var_key):
        st = self.statement_contains_fixedpoint_var(fixedpoint_var_key)
        if not st:
            return (st, "")
        if len(self.statement_env) > 0:
            return (st, self.statement_env[-1].local_fixedpoint_vars_map[fixedpoint_var_key])

    def statement_iter_var_push(self, var_name):
        ## 外部确保var_name的唯一性
        ## 状态占用：False，空闲：True
        self.statement_env[-1].local_iter_vars_map[var_name] = False

    def statement_get_iter_var(self):
        st = False
        var_name = ""
        for name in self.statement_env[-1].local_iter_vars_map.keys():
            st = self.statement_env[-1].local_iter_vars_map[name]
            if st:
                ## 找到空闲的临时迭代变量，设置为占用
                self.statement_env[-1].local_iter_vars_map[name] = False
                return (st, name)
        return (st, var_name)

    def statement_release_iter_var(self, var_name):
        if var_name in self.statement_env[-1].local_iter_vars_map:
            self.statement_env[-1].local_iter_vars_map[var_name] = True

    def statement_front_push(self, st):
        """
        语句增加到置于前端的语句列表中
        """
        if len(self.statement_env) > 0:
            self.statement_env[-1].front_statements.append(st)

    def statement_back_push(self, st):
        """
        语句增加到置于后端的语句列表中
        """

        if len(self.statement_env) > 0:
            self.statement_env[-1].back_statements.append(st)

    def statement_back_push_front(self, st):
        """
        语句增加到置于后端的语句列表的前面
        """
        if len(self.statement_env) > 0:
            self.statement_env[-1].back_statements.insert(0, st)

    def statement_local_variable_push(self, st):
        """
        增加语句前的局部变量声明
        """
        if len(self.statement_env) > 0:
            self.statement_env[-1].local_vars.append(st)
    
    def statement_local_variable_with_init_push(self, st):
        """
        增加语句前的局部变量声明同时初始化
        """
        if len(self.statement_env) > 0:
            self.statement_env[-1].local_vars_with_init.append(st)

    def statement_environment_push(self):
        """
        压入语句环境
        """
        self.statement_env.append(StatementEnvironment())

    def statement_environment_pop(self):
        """
        弹出语句环境
        """
        self.statement_env.pop()

    def combine_statement_environment(self, st):
        """
        将语句与语句环境中的元素组合
        """
        logging.debug("Combine statement is {0}".format(st))

        if len(self.statement_env) == 0:
            return st

        res_code = ""
        local_scope = False
        if (self.statement_env[-1].local_vars or self.statement_env[-1].local_vars_with_init) and self.statement_env[-1].no_block_sym == False:
            res_code += self.code_env.get_cur_indent() + "{\n"
            self.code_env.increase_indent()
            local_scope = True
        for var in self.statement_env[-1].local_vars:
            res_code += self.code_env.get_cur_indent() + var
        for var in self.statement_env[-1].local_vars_with_init:
            res_code += self.code_env.get_cur_indent() + var
        for sm in self.statement_env[-1].front_statements:
            if local_scope:
                # 缩进
                res_code += sm.replace("\n", "\n" + self.code_env.get_one_indent())
            else:
                res_code += sm
        res_code += str(st)
        for sm in self.statement_env[-1].back_statements:
            if local_scope:
                # 缩进
                res_code += sm.replace("\n", "\n" + self.code_env.get_one_indent())
            else:
                res_code += sm
        if local_scope:
            self.code_env.decrease_indent()
            res_code += "\n" + self.code_env.get_cur_indent() + "}"

        return res_code

    def get_record_name(self, record_item):
        """
        获取记录名(如果名字过长则截断)
        """
        if record_item.Name in self.record_names_map:
            return self.record_names_map[record_item.Name]
        
        c_name = ToCName(record_item.Name)
        if c_name in self.c_key_word:
            c_name = c_name + "_"
        c_name = self.code_env.get_truncate_name(c_name, "")
        self.record_names_map[record_item.Name] = c_name
        return c_name

    def get_record_constructor_name(self, record_item):
        """
        获取记录构造函数名()
        """
        if record_item.Name in self.record_constructor_names_map:
            return self.record_constructor_names_map[record_item.Name]

        c_name = self.get_record_name(record_item)
        c_name = self.code_env.get_truncate_name(c_name + "Ctor", c_name)
        self.record_constructor_names_map[record_item.Name] = c_name
        return c_name

    def get_record_number_var_name(self, var_name, record_item):
        """
        获取记录成员变量名(如果名字过长则截断)
        """
        if record_item.Name in self.record_var_map and var_name in self.record_var_names_map:
            return self.record_var_map[record_item.Name][var_name]

        var_c_name = ""
        # Q-Ident进行转换
        if var_name.startswith("'"):
            var_c_name = ToCName(var_name)
        # C关键字末尾加下划线
        elif var_name in self.c_key_word:
            var_c_name = var_name + "_"
        # 其余原样输出
        else:
           var_c_name = var_name
        var_c_name = self.code_env.get_truncate_name(var_c_name, "")
        self.record_var_names_map[var_name] = var_c_name
        self.record_var_map[record_item.Name] = self.record_var_names_map

        return var_c_name

    @abc.abstractmethod
    def statement(self, stat):
        """
        语句转换
        """

    @abc.abstractmethod
    def expression(self, expr):
        """
        表达式转换
        """

    def to_real_literal(self, expr):
        """
        Real类型字面常量转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["real_literal"], expr_node = expr)

    def to_integer_literal(self, expr):
        """
        Real类型字面常量转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["integer_literal"], expr_node = expr)
    
    def to_boolean_literal(self, expr):
        """
        Boolean类型字面常量转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["boolean_literal"], expr_node = expr)

    def to_string_literal(self, expr):
        """
        String类型字面常量转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["string_literal"], expr_node = expr)

    def to_array_literal_helper(self, expr, key_name, is_real_from_int):
        '''
        数组常量的辅助函数（区分来自整型的实数数组，还是普通的数组常量）
        '''
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_literal"], 
                    expr_node=expr, is_real_from_int=is_real_from_int)

    def to_array_literal(self, expr):
        """
        Array类型字面量常量转换
        """
        return self.to_array_literal_helper(expr, expr.String.String, is_real_from_int=False)
        
    def to_multi_statement(self, stat):
        """
        多条语句转换
        """
        logging.debug("Statements is {0} of MultiStatement".format(stat.Statements))
        result_code = ""
        # TODO: 处理变量
        # 处理语句
        for it in stat.Statements:
            logging.debug("Statement is {0} in MultiStatement".format(it))
            result_code += self.statement(it)

        return result_code

    def to_binary_expr(self, expr):
        """
        二元表达式
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["binary_expression"], expr_node = expr)

    def to_unary_expr(self, expr):
        """
        一元表达式
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["unary_expression"], expr_node = expr)

    def to_builtin_func(self, expr):
        """
        内置函数
        """
        func=expr.Function
        if func == BuiltinFunKind.Cat:
            return self.to_array_cat_expr(expr)
        elif (func == BuiltinFunKind.Max1 or func == BuiltinFunKind.Min1 or func == BuiltinFunKind.Sum or func == BuiltinFunKind.Product) and expr.ArgumentsList[0].ExpressionKind == ExpressionKind.For:
            for_data = ForData()
            self.for_context.append(for_data)
            (final_expr, indices) = self.flatten_fun_for_expr(expr)
            res = self.code_env.code_engine.run_piece_template(self.code_env.template_map["fun_array_for"], expr_node = expr,
                final_expr = final_expr, indices = indices, for_data = for_data)
            self.for_context.pop()
            return res;
        elif func in self.array_builtin_functions:
            return self.to_array_builtin_fun(expr)
        elif func == BuiltinFunKind.Fill:
            return self.to_array_fill_expr(expr)
        else:
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["builtin_function"], expr_node = expr)


    def flatten_fun_for_expr(self, expr):
        '''
        内置函数中出现for数组生成时展平表达式并且将信息返回
        '''
        final_expr = expr.ArgumentsList[0]
        for_indices = []
        while final_expr.ExpressionKind == ExpressionKind.For:
            for_indices.append(final_expr.IndicesList[0])
            if final_expr.Expression.ExpressionKind != ExpressionKind.For:
                final_expr = final_expr.Expression
        return (final_expr, for_indices)



    def to_member_access(self, expr):
        """
        成员访问
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["member_access"], expr_node = expr)

    def to_while(self, stat):
        """
        while语句
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["while"], statement_node = stat)

    def to_for(self, stat):
        """
        for语句
        """
        for_data = ForData()
        self.for_context.append(for_data)
        to_res = self.code_env.code_engine.run_piece_template(self.code_env.template_map["for"], statement_node = stat, for_data = for_data)
        self.for_context.pop()
        return to_res

    def to_range(self, expr):
        """
        范围表达式
        """
        if expr.Type.DimensionsList[0].ExpressionKind != ExpressionKind.IntegerLiteral:
            raise Exception("UnSupported") # 不支持不定长度
        else:
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["range"], expr_node = expr)
     	    

    def to_for_ident(self, expr):
        """
        for变量
        """
        for data_tiem in reversed(self.for_context):
            if data_tiem.is_for_ident_in(expr.Ident.Variable.Name):
                return data_tiem.get_for_ident_expression(expr.Ident.Variable.Name)

        return ""

    def to_for_index(self, expr):
        """
        for
        """
        for_expr = self.expression(expr.Expression)
        return for_expr

    def to_single_statement(self, stat):
        """
        单一语句(如assert等函数调用)
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["single_statement"], statement_node = stat)

    def to_array_cat_expr_helper(self, expr, key_name, is_real_from_int):
        '''
        数组拼接的辅助函数（区分来自整型的实数数组，还是普通的数组拼接）
        '''
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_cat"], 
                    expr_node=expr, is_real_from_int=is_real_from_int)
    
    def to_array_cat_expr(self, expr):
        """
        数组拼接
        """
        return self.to_array_cat_expr_helper(expr, expr.String.String, is_real_from_int=False)

    def to_array_struct_var(self, expr):
        """
        结构化数组变量转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_struct_variable"], expr_node=expr)

    def to_array_constructor_helper(self, expr, key_name, is_real_from_int):
        '''
        数组构造的辅助函数（区分来自整型的实数数组，还是普通的数组构造）
        '''
        if expr.ArgumentsList[0].ExpressionKind == ExpressionKind.For:
            for_data = ForData()
            self.for_context.append(for_data)
            (final_expr, indices) = self.flatten_for_expr(expr)
            res = self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_for"], expr_node = expr.ArgumentsList[0],
                final_expr = final_expr, indices = indices, for_data = for_data)
            self.for_context.pop()
            return res
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_constructor"], 
                    expr_node=expr, is_real_from_int=is_real_from_int)


    def flatten_for_expr(self, expr):
        '''
        
        '''
        final_expr = expr.ArgumentsList[0].Expression
        for_indices = [ index for index in expr.ArgumentsList[0].IndicesList ]
        while final_expr.ExpressionKind == ExpressionKind.For or (final_expr.ExpressionKind == ExpressionKind.ArrayConstructor and final_expr.ArgumentsList[0].ExpressionKind == ExpressionKind.For):
            if final_expr.ExpressionKind == ExpressionKind.For:
                for index in final_expr.IndicesList:
                    for_indices.append(index)
                final_expr = final_expr.Expression
            elif final_expr.ExpressionKind == ExpressionKind.ArrayConstructor and final_expr.ArgumentsList[0].ExpressionKind == ExpressionKind.For:
                final_expr = final_expr.ArgumentsList[0]
            else:
                break
        return (final_expr, for_indices)

    def to_array_constructor(self, expr):
        """
        数组构造
        """
        return self.to_array_constructor_helper(expr, expr.String.String, is_real_from_int=False)

    def to_array_index(self, expr):
        """
        数组索引
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_index"], expr_node=expr)
        
    def to_array_real_from_int(self, expr):
        '''
        来自整型的实数数组
        除了数组构造、数组文字常量、数组拼接，其他情形不去查询表达式对应的临时变量是否被生成
        '''
        array_expr = expr.Array
        if array_expr.ExpressionKind == ExpressionKind.ArrayConstructor:
            return self.to_array_constructor_helper(array_expr, expr.String.String, is_real_from_int=True)
        elif array_expr.ExpressionKind == ExpressionKind.ArrayLiteral:
            return self.to_array_literal_helper(array_expr, expr.String.String, is_real_from_int=True)
        elif array_expr.ExpressionKind == ExpressionKind.BuiltinFun and array_expr.Function == BuiltinFunKind.Cat:
            return self.to_array_cat_expr_helper(array_expr, expr.String.String, is_real_from_int=True)
        else:
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_real_from_int"], expr_node=expr)

    def to_scalar_real_from_int(self, expr):
        """
        整数标量转为实数标量
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["scalar_real_from_int"], expr_node=expr)

    def to_array_fill_expr(self, expr):
        '''
        数组内置函数fill
        '''
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_fill"], expr_node=expr)

    def to_array_builtin_fun(self, expr):
        '''
        部分数组内置函数合集
        '''
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["array_builtin_function"], expr_node=expr)

    def to_break(self, stat):
        """
        break语句
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["break_statement"], statement_node = stat)

    def flatten_array_helper(self, expr, lst, depth):
        '''
        数组展平的辅助函数，服务于‘数组构造 := 数组类型表达式’情形下，将数组构造按照一维展平（其中每个元素为变量）
        '''
        if expr.ExpressionKind != ExpressionKind.ArrayConstructor:
            lst.append(expr)
        elif expr.ExpressionKind == ExpressionKind.ArrayConstructor:
            for sub_expr in expr.ArgumentsList:
                self.flatten_array_helper(sub_expr, lst, depth + 1)
                    
    def flatten_array_constructor_as_assign_left(self, expr):
        '''
        在‘数组构造 := 数组类型表达式’情形下，将数组构造按照一维展平（其中每个元素为变量），并返回相应List
        '''
        res_lst = []
        self.flatten_array_helper(expr, res_lst, 0)
        return res_lst

    def real_to_fixedpoint(self, int_part, frac_part):
        '''
        将实型转换成恰当的定点数策略（由于模板的逻辑流程支持不足，python实现此功能）
        首先尽量在整数位长范围内表示有效信息（整数部分优先，剩余空间记录小数部分信息），同时保证头部空位最大
        '''
        default_word_size = 31 ## 未来从配置中获取
        fp_value = int_part
        fp_exponent = 0
        fp_fracbits = default_word_size
        while int_part >= 2 ** (default_word_size - fp_fracbits + fp_exponent):
            if fp_fracbits > 0:
                fp_fracbits -= 1
            else:
                fp_exponent += 1
        if fp_exponent == 0:
            fp_value = int((int_part + frac_part) * 2 ** fp_fracbits)
            while fp_value > 0 and (fp_value & 0x1) == 0 and fp_fracbits > 0:
                fp_value >>= 1;
                fp_fracbits -= 1;
        return (fp_value, fp_fracbits, fp_exponent)

    def to_user_function(self, expr):
        """
        自定义函数调用
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["call_user_function"], expr_node = expr)

    def to_record_constructor(self, expr):
        """
        记录构造函数调用
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["record_constrcutor"], expr_node = expr)

    def to_null(self, stat):
        """
        NULL语句/表达式
        """
        return ""
    
    def is_int_type(self, expr):
        '''
        判断数组或者标量表达式节点是否为整数类型
        '''
        res = False
        if expr.Type.IsArray and expr.Type.ElementType.TypeKind == TypeKind.Builtin:
            if expr.Type.ElementType.BuiltinKind == BuiltinKind.Integer:
                res = True
        elif expr.Type.TypeKind == TypeKind.Builtin:
            if expr.Type.BuiltinKind == BuiltinKind.Integer:
                res = True
        return res

    def is_no_zero_literal_expr(self, expr):
        res = False
        if expr.ExpressionKind == ExpressionKind.IntegerLiteral and int(self.expression(expr)) != 0:
            res = True
        return res

    def is_bool_type(self, expr):
        '''
        判断数组或者标量表达式节点是否为布尔类型
        '''
        res = False
        if expr.Type.IsArray and expr.Type.ElementType.TypeKind == TypeKind.Builtin:
            if expr.Type.ElementType.BuiltinKind == BuiltinKind.Boolean:
                res = True
        elif expr.Type.TypeKind == TypeKind.Builtin:
            if expr.Type.BuiltinKind == BuiltinKind.Boolean:
                res = True
        return res

    def concat_array_index(self, lst):
        '''
        当for循环次数小于阈值时，数组索引构造的数组的结果的数据通过展开形式赋值
        lst：模板中会将数组索引的表达式汇总为列表[[], [], ...]，其中列表包含的元素是一个列表对应相应维度的索引表达式的具体内容同时其长度为相应维的大小Ni
        此函数会将lst展平为长度为N1 * N2 * ...的列表
        '''
        if len(lst) == 0:
            return lst
        elif len(lst) == 1:
            return [[e] for e in lst[0].lst]
        else:
            head = lst[0].lst
            nres = []
            for e in head:
                for tail in self.concat_array_index(lst[1:]):
                    nres.append([e] + tail)
            ##print(nres)
            return nres