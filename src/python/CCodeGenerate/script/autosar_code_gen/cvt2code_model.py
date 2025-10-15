##**************************************************************************
## 
##  Copyright (c) 2021, 苏州同元软控信息技术有限公司
##  All rights reserved.
## 
##  @file           cvt2code_model.py
##  @brief          模型中代码转换
## 
##  @version        v1.0
##  @author         田显钊
##  @date           2021/05/20
## 
##**************************************************************************

import logging

import MwPyModelData
from autosar_code_gen.cvt2code import ConvertToCode 

class ConvertToCodeInModel(ConvertToCode):
    """
    模型中代码转换的类
    """

    def __init__(self, code_env):
        """
        构造函数
        @param[in]code_env      代码生成环境
        """
        
        super().__init__(code_env)
        # 是否与计算导数有关的参数
        self.involve_der = False
        self.is_pre_der = False
        self.is_completed_integerator_step_closed = True
        self.in_when_count = 0
        self.statement_handler={}
        self.expression_handler={}
        # TODO 表达式和语句映射表
        self.expression_handler[MwPyModelData.ExpressionKind.RealLiteral] = self.to_real_literal
        self.expression_handler[MwPyModelData.ExpressionKind.IntegerLiteral] = self.to_integer_literal
        self.expression_handler[MwPyModelData.ExpressionKind.BooleanLiteral] = self.to_boolean_literal
        self.expression_handler[MwPyModelData.ExpressionKind.StringLiteral] = self.to_string_literal
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayLiteral] = self.to_array_literal
        self.expression_handler[MwPyModelData.ExpressionKind.Variable] = self.to_variable
        self.expression_handler[MwPyModelData.ExpressionKind.Time] = self.to_time
        self.expression_handler[MwPyModelData.ExpressionKind.BinaryExpr] = self.to_binary_expr
        self.expression_handler[MwPyModelData.ExpressionKind.UnaryExpr] = self.to_unary_expr
        self.expression_handler[MwPyModelData.ExpressionKind.BuiltinFun] = self.to_builtin_func
        self.expression_handler[MwPyModelData.ExpressionKind.MemberAccess] = self.to_member_access
        self.expression_handler[MwPyModelData.ExpressionKind.Range] = self.to_range
        self.expression_handler[MwPyModelData.ExpressionKind.ForIdent] = self.to_for_ident
        self.expression_handler[MwPyModelData.ExpressionKind.ForIndex] = self.to_for_index
        self.expression_handler[MwPyModelData.ExpressionKind.If] = self.to_if_expression
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayStructVar] = self.to_array_struct_var
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayConstructor] = self.to_array_constructor
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayRealFromInt] = self.to_array_real_from_int
        self.expression_handler[MwPyModelData.ExpressionKind.ArrayIndex] = self.to_array_index
        self.expression_handler[MwPyModelData.ExpressionKind.ScalarRealFromInt] = self.to_scalar_real_from_int
        self.expression_handler[MwPyModelData.ExpressionKind.UserFunction] = self.to_user_function
        self.expression_handler[MwPyModelData.ExpressionKind.RecordConstructor] = self.to_record_constructor
        self.expression_handler[MwPyModelData.ExpressionKind.Null] = self.to_null
        self.statement_handler[MwPyModelData.StatementKind.Single] = self.to_single_statement
        self.statement_handler[MwPyModelData.StatementKind.Assign] = self.to_model_assign
        self.statement_handler[MwPyModelData.StatementKind.Multi] = self.to_multi_statement
        self.statement_handler[MwPyModelData.StatementKind.While] = self.to_while
        self.statement_handler[MwPyModelData.StatementKind.When] = self.to_when
        self.statement_handler[MwPyModelData.StatementKind.For] = self.to_for
        self.statement_handler[MwPyModelData.StatementKind.If] = self.to_if_statement
        self.statement_handler[MwPyModelData.StatementKind.Break] = self.to_break
        self.statement_handler[MwPyModelData.StatementKind.Null] = self.to_null
        #logging.debug("Expression handler map in model is {0}".format(self.expression_handler))
        #logging.debug("Statement handler map in model is {0}".format(self.statement_handler))
        #f=open("E:\\MwPyModelData.txt","w");
        #print("statement_handler is {0}".format(self.statement_handler),file=f)
        #print("MwPyModelData.ExpressionKind.RealLiteral is {0}".format(MwPyModelData.ExpressionKind.RealLiteral),file=f)
        #print("MwPyModelData.ExpressionKind.IntegerLiteral is {0}".format(MwPyModelData.ExpressionKind.IntegerLiteral),file=f)
        #print("MwPyModelData.ExpressionKind.BooleanLiteral is {0}".format(MwPyModelData.ExpressionKind.BooleanLiteral),file=f)
        #print("MwPyModelData.ExpressionKind.StringLiteral is {0}".format(MwPyModelData.ExpressionKind.StringLiteral),file=f)
        #print("MwPyModelData.ExpressionKind.ArrayLiteral is {0}".format(MwPyModelData.ExpressionKind.ArrayLiteral),file=f)
        #print("MwPyModelData.ExpressionKind.Variable is {0}".format(MwPyModelData.ExpressionKind.Variable),file=f)
        #print("MwPyModelData.ExpressionKind.Time is {0}".format(MwPyModelData.ExpressionKind.Time),file=f)
        #print("MwPyModelData.ExpressionKind.BinaryExpr is {0}".format(MwPyModelData.ExpressionKind.BinaryExpr),file=f)
        #print("MwPyModelData.ExpressionKind.UnaryExpr is {0}".format(MwPyModelData.ExpressionKind.UnaryExpr),file=f)
        #print("MwPyModelData.ExpressionKind.BuiltinFun is {0}".format(MwPyModelData.ExpressionKind.BuiltinFun),file=f)
        #print("MwPyModelData.ExpressionKind.MemberAccess is {0}".format(MwPyModelData.ExpressionKind.MemberAccess),file=f)
        #print("MwPyModelData.ExpressionKind.Range is {0}".format(MwPyModelData.ExpressionKind.Range),file=f)
        #print("MwPyModelData.ExpressionKind.ForIdent is {0}".format(MwPyModelData.ExpressionKind.ForIdent),file=f)
        #print("MwPyModelData.ExpressionKind.ForIndex is {0}".format(MwPyModelData.ExpressionKind.ForIndex),file=f)
        #print("MwPyModelData.ExpressionKind.If is {0}".format(MwPyModelData.ExpressionKind.If),file=f)
        #print("MwPyModelData.ExpressionKind.ArrayStructVar is {0}".format(MwPyModelData.ExpressionKind.ArrayStructVar),file=f)
        
        #print("MwPyModelData.StatementKind.Single is {0}".format(MwPyModelData.StatementKind.Single),file=f)
        #print("MwPyModelData.StatementKind.Assign is {0}".format(MwPyModelData.StatementKind.Assign),file=f)
        #print("MwPyModelData.StatementKind.Multi is {0}".format(MwPyModelData.StatementKind.Multi),file=f)
        #print("MwPyModelData.StatementKind.While is {0}".format(MwPyModelData.StatementKind.While),file=f)
        #print("MwPyModelData.StatementKind.When is {0}".format(MwPyModelData.StatementKind.When),file=f)
        #print("MwPyModelData.StatementKind.For is {0}".format(MwPyModelData.StatementKind.For),file=f)
        #print("MwPyModelData.StatementKind.If is {0}".format(MwPyModelData.StatementKind.If),file=f)
        #print("MwPyModelData.StatementKind.Break is {0}".format(MwPyModelData.StatementKind.Break),file=f)
        #print("MwPyModelData.StatementKind.Null is {0}".format(MwPyModelData.StatementKind.Null),file=f)
        
        #f.close()

    def set_involve_der(self, b):
        self.involve_der = b

    def get_involve_der(self):
        return self.involve_der

    def try_completed_integerator_step_begin(self):
        """
        生成积分步完成开始的代码
        """
        if self.code_env.get_completed_integerator_step_count() == 1:
            if self.is_completed_integerator_step_closed:
                self.is_completed_integerator_step_closed = False
                return self.combine_completed_integerator_step(True)
        return ""

    def try_completed_integerator_step_end(self):
        """
        生成积分步完成结束的代码
        """
        if self.code_env.get_completed_integerator_step_count() == 0:
            if not self.is_completed_integerator_step_closed:
                self.is_completed_integerator_step_closed = True
                return self.combine_completed_integerator_step(False)
        return ""

    def _to_solve_scalar_linear(self, blk):
        """
        标量线性方程
        """
        logging.debug("Scalar linear to be assigned is {0}".format(blk.Variable))
        self.statement_environment_push()

        res = self.code_env.code_engine.run_piece_template(self.code_env.template_map["solve_scalar_linear"],
                                                          solving_variable = blk.Variable, coef_value = blk.CoefValue, 
                                                          const_value = blk.ConstValue)

        res = self.combine_statement_environment(res)
        self.statement_environment_pop()

        return res

    def _equation_block_internal(self, blk):
        """
        方程块转换（内部使用）
        """
        st = ""
        logging.debug("blk.BlockKind is {0}".format(blk.BlockKind))
        logging.debug("blk.Statement is {0}".format(blk.Statement))
        if blk.BlockKind == MwPyModelData.EquationBlockKind.Assign:
            logging.debug("blk.BlockKind is Assign")
            st = self.statement(blk.Statement)
        elif blk.BlockKind == MwPyModelData.EquationBlockKind.TornLinear:
            logging.debug("blk.BlockKind is TornLinear")
            st = self.statement(blk.HelpStatement)
            st += self.statement(blk.Statement)
        elif blk.BlockKind == MwPyModelData.EquationBlockKind.ScalarLinear:
            logging.debug("blk.BlockKind is ScalarLinear")
            st = self.statement(blk.Statement)
            st += self._to_solve_scalar_linear(blk)
        else:
            raise Exception("Not supported equation!")
        return st

    def equation_block(self, blk):
        """
        方程块转换
        """
        logging.debug("Equation block is {0}".format(blk))
        if blk.BlockKind == MwPyModelData.EquationBlockKind.Unsupported:
            raise Exception("Not supported equation!")
        #不计算与导数有关的参数
        self.set_involve_der(False)
        logging.debug("blk.SectionKind != MwPyModelData.EquationSectionKind.Der is {0}".format(blk.SectionKind != MwPyModelData.EquationSectionKind.Der))
        logging.debug("not self.code_env.in_completed_integerator_step() is {0}".format(not self.code_env.in_completed_integerator_step()))
        ##第一个if是进行积分步骤的计算的
        ##第二个else是进行理算步骤的计算的
        if blk.SectionKind != MwPyModelData.EquationSectionKind.Der and not self.code_env.in_completed_integerator_step():
            logging.debug("第一个if")

            # 离散块在积分步完成后计算
            self.code_env.enter_completed_integerator_step()
            st = self.try_completed_integerator_step_begin()
            logging.debug("try_completed_integerator_step_begin为{0}".format(st))
            self.code_env.increase_indent()
            st += self._equation_block_internal(blk)
            self.code_env.decrease_indent()
            self.code_env.exit_completed_integerator_step()
        else:
            logging.debug("进入else")
            st = self.try_completed_integerator_step_end()
            self.set_involve_der(True)
            st += self._equation_block_internal(blk)
        logging.debug("Equation block convert to {0}".format(st))
        return st
    
    def get_equtation(self,blk):
        """
        只获得等式
        """
        res=""
        if blk.BlockKind==MwPyModelData.EquationBlockKind.Assign:
            state=blk.Statement
            if state.StatementKind==MwPyModelData.StatementKind.Assign:
                res=self.statement_handler[state.StatementKind](state)
            if state.StatementKind==MwPyModelData.StatementKind.Multi:
                res+=self.to_multi_statement(state)
            
        return res
        
    
    

    def statement(self, stat):
        """
        语句转换
        """
        logging.debug("Statement is {0}".format(stat))
        logging.debug("stat.StatementKind is {0}".format(stat.StatementKind))
        logging.debug("对应的 self.statement_handler is {0}".format(self.statement_handler[stat.StatementKind]))
        
        self.statement_environment_push()

        res = self.statement_handler[stat.StatementKind](stat)
        # 去掉多余的换行
        res.strip('\n') + '\n'

        res = self.combine_statement_environment(res)
        self.statement_environment_pop()

        return res

    def variable_assign_start(self, var):
        """
        变量赋值start
        """
        logging.debug("Variable to be assigned is {0}".format(var))
        self.statement_environment_push()

        res = self.code_env.code_engine.run_piece_template(self.code_env.template_map["variable_assign_start"],
                                                          model_var = var, start_value = var.Variable.Start)

        res = self.combine_statement_environment(res)
        self.statement_environment_pop()

        return res

    def variable_assign_variable(self, var_left, var_right):
        """
        变量赋值start
        """
        logging.debug("Variable to be assigned is {0}".format(var_left))

        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["variable_assign_variable"],
                                                          left = var_left, right = var_right)
    
    def when_condition_update(self, index, pre_when_condition, when_condition, when_condition_size):
        """
        when条件更新
        """
        logging.debug("When condition is {0} {1} at {2}, size {3}".format(pre_when_condition, when_condition, index, when_condition_size))

        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["when_condition_update"],
                                         when_index = index, pre_when_condition = pre_when_condition, when_condition = when_condition, 
                                         when_condition_size = when_condition_size)

    def expression(self, expr):
        """
        表达式转换
        """
        if not expr is None and not self.code_env.has_real_array and not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Real:
            self.code_env.has_real_array = True
        if not expr is None and not self.code_env.has_int_array and not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
            self.code_env.has_int_array = True
        if not expr is None and not self.code_env.has_bool_array and not expr.Type is None and expr.Type.IsArray and expr.Type.ElementType.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
            self.code_env.has_bool_array = True
        logging.debug("Expression is {0}".format(expr.String.String))
        logging.debug("ExpressionKind is {0}".format(expr.ExpressionKind))
        logging.debug("self.expression_handler is {0}".format(self.expression_handler[expr.ExpressionKind]))
        logging.debug("res: {0}".format(self.expression_handler[expr.ExpressionKind](expr).strip('\n')))
        return self.expression_handler[expr.ExpressionKind](expr).strip('\n')


    def combine_completed_integerator_step(self, is_begin):
        """
        积分步完成相关代码
        """
        # TODO
        return self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["code_snippet"]["completed_integerator_step"], 
                                                   is_begin = is_begin)

    def to_variable(self, expr):
        """
        变量转换
        """
        return self.code_env.code_engine.model_vars.get_variable_name(expr.Variable)
    
    def to_time(self, expr):
        """
        变量转换
        """
        return self.code_env.code_engine.model_vars.get_time_name()

    def to_model_assign(self, stat):
        """
        赋值转换
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["model_assign"], statement_node = stat)
        
    def when_condition_previous_from_statement_environment(self):
        """
        获取语句环境中when条件前的语句，可能没有语句
        """

        if len(self.statement_env) == 0:
            return ""

        res_code = ""
        for var in self.statement_env[-1].local_vars:
            res_code += self.code_env.get_cur_indent() + var
        for var in self.statement_env[-1].local_vars_with_init:
            res_code += self.code_env.get_cur_indent() + var
        for sm in self.statement_env[-1].front_statements:
            res_code += sm
        
        return res_code
        
    def to_when(self, stat):
        """
        when转换
        """
        self.in_when_count += 1
        this_enter_flag = False
        when_res = ""
        if not self.code_env.in_completed_integerator_step():
            # when在积分步完成后计算
            self.code_env.enter_completed_integerator_step()
            when_res += self.try_completed_integerator_step_begin()
            self.code_env.increase_indent()
            this_enter_flag = True

        logging.debug("When is {0}".format(stat))
        has_else_when = (stat.ElseWhen.StatementKind != MwPyModelData.StatementKind.Null)
        when_res += self.to_when_internal(stat, False)
        else_when = stat.ElseWhen
        while has_else_when:
            else_when_res = self.to_when_internal(else_when, True)
            when_res += else_when_res
            has_else_when = (else_when.ElseWhen.StatementKind != MwPyModelData.StatementKind.Null)
            else_when = else_when.ElseWhen

        if this_enter_flag:
            self.code_env.decrease_indent()
            self.code_env.exit_completed_integerator_step()

        self.in_when_count -= 1
        logging.debug("when_res is {0}".format(when_res))
        return when_res

    def to_when_internal(self, stat, is_else_when):
        """
        when转换
        """
        if stat.Condition.ExpressionKind == MwPyModelData.ExpressionKind.BuiltinFun and stat.Condition.Function == MwPyModelData.BuiltinFunKind.Sample:
            # 与when直接关联的sample语句
            sample_index = self.code_env.code_engine.model_vars.add_sample(stat.Condition.ArgumentsList[0], stat.Condition.ArgumentsList[1])        
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["sample_when"], statement_node = stat,
                                                               index = sample_index, else_when = is_else_when, is_sample = True)

        elif stat.Condition.ExpressionKind == MwPyModelData.ExpressionKind.Variable and stat.Condition.Variable.Name in self.code_env.code_engine.model_vars.sample_bool_name:
            # 与when间接关联的sample语句（通过中间布尔变量）
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["sample_when"], statement_node = stat,
                                                                else_when = is_else_when, is_sample = False)

        vector_size = 0
        if stat.Condition.Type.IsArray:
            try:
                vector_size = stat.Condition.Type.DimensionsList[0].Value
            except Exception as e:
                return ""
            self.code_env.set_has_vector_when()
        else:
            self.code_env.set_has_scalar_when()
        
        self.statement_environment_push()
        self.code_env.set_in_generate_update_when_condition(True)
        when_condition_for_update = self.expression(stat.Condition)
        self.code_env.set_in_generate_update_when_condition(False)
        pre_condition_for_update = self.when_condition_previous_from_statement_environment()
        self.statement_environment_pop()
        
        when_condition = self.expression(stat.Condition)
        logging.debug("When condition is {0}".format(when_condition))
        when_index = self.code_env.code_engine.model_vars.add_when_condition(pre_condition_for_update, when_condition_for_update, vector_size)

        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["when"], statement_node = stat, 
                                                            index = when_index, condition = when_condition, vector_condition_size = vector_size,
                                                            else_when = is_else_when)
    
    def is_in_when(self):
        """
        是否在when中（包括条件中）
        """
        return (self.in_when_count > 0)

    def to_if_expression(self, expr):
        ndims = 0
        if expr.Type.IsArray:
            ndims = expr.Type.Ndims
        has_event = expr.HasEvent
        conditions = [expr.Condition]
        expressions = [expr.TrueBranch]
        next_node = expr.FalseBranch
        while next_node.Type == MwPyModelData.ExpressionKind.If:
            # 任何条件中包含事件，即需要特殊处理
            has_event = has_event or next_node.HasEvent
            conditions.apend(next_node.Condition)
            expressions.append(next_node.TrueBranch)
            next_node = next_node.FalseBranch
        expressions.append(next_node)
        if has_event and self.get_involve_der():
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_expression_has_event_pre"], expr_node=expr, ndims=ndims,
                                            conditions=conditions, expressions=expressions)
        else:
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_expression"], expr_node = expr, ndims=ndims)

    def to_if_statement(self, stat):
        # 若当前if语句包含事件处理且与导数计算有关，则通过特殊的方式表示
        has_event = stat.HasEvent
        conditions = [stat.Condition]
        statements = [stat.TrueBranch]
        next_node = stat.FalseBranch
        while True:
            if next_node.StatementKind == MwPyModelData.StatementKind.If:
                has_event = has_event or next_node.HasEvent
                conditions.append(next_node.Condition)
                statements.append(next_node.TrueBranch)
                next_node = next_node.FalseBranch
            elif next_node.StatementKind == MwPyModelData.StatementKind.Multi and next_node.StatementSize == 1:
                tmp_node = next_node
                for stm in next_node.Statements:
                    if stm.StatementKind == MwPyModelData.StatementKind.If:
                        tmp_node = stm
                        break
                    else:
                        break
                next_node = tmp_node
                if next_node.StatementKind != MwPyModelData.StatementKind.If:
                    break
            else:
                break
        if next_node.StatementKind != MwPyModelData.StatementKind.Null:
            statements.append(next_node)
        if has_event and self.get_involve_der():
            cur_if_cond_index = self.code_env.code_engine.model_vars.add_if_condition()
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_statement_has_event"], statement_node = stat, code_env=self.code_env,
                                                                          if_cond_index=cur_if_cond_index, conditions = conditions, statements = statements)
        else:
            return self.code_env.code_engine.run_piece_template(self.code_env.template_map["if_statement"], statement_node = stat)

    def internel_record_assign(self, parent_record, cur_record_member, origin_record_member, parent_record_name):
        """
        针对记录成员赋值
        """
        return self.code_env.code_engine.run_piece_template(self.code_env.template_map["record_assign"], parent_record = parent_record, cur_record_member = cur_record_member, origin_record_member = origin_record_member, parent_record_name = parent_record_name)
