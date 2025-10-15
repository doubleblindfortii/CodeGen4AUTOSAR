#**************************************************************************
# 
#  Copyright (c) 2020, 苏州同元软控信息技术有限公司
#  All rights reserved.
# 
#  @file           modelvar.py
#  @brief          模型变量
# 
#  @version        v1.0
#  @author         田显钊
#  @date           2021/1/6
# 
#*************************************************************************/

import logging
import MwPyModelData

class ModelVariables():
    """
    模型变量处理及生成变量代码
    """
    
    def __init__(self, code_env):
        """
        构造函数
        @param[in]code_env        代码生成环境
        """
        self.code_env = code_env
        # 变量id与变量的映射
        self.var_map = {}
        # 此处的input、output包括常量、参量和变量，因为有些变量被分析器统计到常量或者参量类中
        self.real_input_vars = []
        self.int_input_vars = []
        self.bool_input_vars = []
        self.real_output_vars = []
        self.int_output_vars = []
        self.bool_output_vars = []

        self.real_free_params = []
        self.int_free_params = []
        self.bool_free_params = []
        self.state_vars = []
        self.der_vars = []
        self.der_vars_id = []
        self.pre_vars_id = []
        # pre变量(pre变量，原变量的元组集合)
        self.real_pre_vars = []
        self.int_pre_vars = []
        self.bool_pre_vars = []
        # when条件(when序号，when条件的元组集合)
        self.when_conditions = []
        self.when_condition_count = 0
        # if条件的数量
        self.if_condition_count = 0
        # sample数量
        self.sample_count = 0
        # sample数据(sample序号，(sample_argu1,sample_argu2))
        self.sample_data = []
        # 和sample关联的布尔变量名(表达式中取到的Variable是ScopeVariable,取不到id号，故取变量名)
        self.sample_bool_name = []
        # TODO 外部对象、结构化变量、pre
        # 其它变量
        self.real_storage_vars = []
        self.int_storage_vars = []
        self.bool_storage_vars = []
        self.string_storage_vars = []
        self.time_var = ""
        # TODO 变量的时钟分区
        # 自由参量起始位置
        self.real_free_param_start = 0
        self.int_free_param_start = 0
        self.bool_free_param_start = 0
        # 状态变量和微分变量起始位置
        self.state_var_start = 0
        self.der_var_start = 0
        # 变量id与代码中名字的映射
        #  YPH:在emit中用
        self.var_names = {}
        # 变量id与代码中名字的映射【id从小到大顺序排列】
        self.var_names_ordered = {}
        # 别名变量id和原始变量id的映射
        self.origin_id = {}
        # 变量id与代码中名字的映射【区分类型】
        self.real_var_id = []
        self.int_var_id = []
        self.bool_var_id = []
        self.neg_real_alis_id = []
        self.neg_int_alis_id = []
        self.max_id = 0;
        # 变量id与名字索引的映射，用作模型名定制生成时的变量定位
        self.var_custom_names = {}
        # 时间变量索引为0，故实型变量索引从1开始
        real_index = 1
        int_index = 0
        bool_index = 0
        string_index = 0
        # 数据字典
        self.dict_real_input_vars = []
        self.dict_int_input_vars = []
        self.dict_bool_input_vars = []
        self.dict_real_output_vars = []
        self.dict_int_output_vars = []
        self.dict_bool_output_vars = []
        self.dict_real_free_params = []
        self.dict_int_free_params = []
        self.dict_bool_free_params = []

        self.dict_real_storage_vars = []
        self.dict_int_storage_vars = []
        self.dict_bool_storage_vars = []
        self.dict_string_storage_vars = []

        # 【注】
        # 为了保证需要被初始化的变量部分索引尽可能的连续，调整变量收集方式及存放分类
        # 分类保证五个原则：
        # 1、尽可能多的初始化部分索引保持连续 --> 保证初始化可以使用for循环赋值
        # 2、自由参量索引连续  --> 自由参量对外接口SetParameter可以使用for循环赋值
        # 3、状态变量索引连续  --> 积分步骤中需要通过索引步进
        # 4、导数变量索引连续  --> 积分步骤中需要通过索引步进
        # 5、状态变量和导数变量按照C++端传递数据一一对应
        # 为了遵守以上原则，变量分类规则如下：
        # real：常量\输入变量\自由参量 初始化部分 + 自由参量非初始化部分 + 其他非初始化部分 + 状态变量 + 导数变量
        # int : 常量\输入变量\自由参量 初始化部分 + 自由参量非初始化部分 + 其他非初始化部分
        # bool: 常量\输入变量\自由参量 初始化部分 + 自由参量非初始化部分 + 其他非初始化部分
        # 需要初始化的有：常量、自由参量、输入变量
        # 故收集时的顺序：
        # 常量有start + 输入变量有start + 自由参量有start + 自由参量无start + 其他无start + 状态变量 + 导数变量

        # 组成：常量、输入变量、自由参量三类数据中需要初始化的部分
        self.real_with_start = []
        self.int_with_start = []
        self.bool_with_start = []

        # 组成：常量、输入变量两类数据中不需要初始化的部分，以及依赖参量、非输入变量
        self.real_without_start = []
        self.int_without_start = []
        self.bool_without_start = []

        # 自由参量中不需要初始化的部分
        self.real_free_parameter_without_start = []
        self.int_free_parameter_without_start = []
        self.bool_free_parameter_without_start = []

        #包含所有（非状态变量和非导数变量的）输入【变量】的数据集 收集原因是：只有输入变量需要初始化，非输入不需要
        self.real_variables_input = []
        self.int_variables_input = []
        self.bool_variables_input = []

        #分别存储所有状态变量和导数变量中有start值和无start值的数据集
        self.state_vars_with_start = []
        self.state_vars_without_start = []
        self.der_vars_with_start = []
        self.der_vars_without_start = []

        self.custom_header_file = [] # 数据字典头文件（include用）
        self.custom_header_file_gen_export = [] # 数据字典头文件（生成export头文件用）
        self.custom_header_file_gen_import = [] # 数据字典头文件（生成import头文件用）

        self.data_dictionary = {} # 在python端记录变量ID和数据字典的映射

        ## 存放der变量名，避免重复
        self.der_names = []

        ##  ID到数据字典的映射
        for var_item in self.code_env.model_data.DataDictionaries:
            self.data_dictionary[var_item.DictVariable.ID] = var_item
        #YPH:常量
        for var_item in self.code_env.model_data.ModelConstants:
            self.var_map[var_item.ID] = var_item
            assert(var_item.ScopeKind == MwPyModelData.ScopeVariableKind.Model)
            assert(var_item.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
            if var_item.ID in self.data_dictionary.keys():
            #如果模型的常量出现在数据字典中
                logging.debug("Model data dictionary constant '{0}'".format(var_item.Variable.Name))
                if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                    if var_item.Variable.IsInput:
                        self.dict_real_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_real_output_vars.append(var_item)
                    self.dict_real_storage_vars.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                    if var_item.Variable.IsInput:
                        self.dict_int_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_int_output_vars.append(var_item)
                    self.dict_int_storage_vars.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                    if var_item.Variable.IsInput:
                        self.dict_bool_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_bool_output_vars.append(var_item)
                    self.dict_bool_storage_vars.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.String:
                    self.dict_string_storage_vars.append(var_item)
                else:
                    assert(False)
            else:
                logging.debug("Model constant '{0}'".format(var_item.Variable.Name))
                if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                    if var_item.Variable.IsInput:
                        self.real_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.real_output_vars.append(var_item)
                    if var_item.Variable.HasStart:
                        if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.RealLiteral or var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                            self.real_with_start.append(var_item)
                        else:
                            self.real_without_start.append(var_item)
                    else:
                        self.real_without_start.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                    if var_item.Variable.IsInput:
                        self.int_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.int_output_vars.append(var_item)
                    if var_item.Variable.HasStart:
                        if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                            self.int_with_start.append(var_item)
                        else:
                            self.int_without_start.append(var_item)
                    else:
                        self.int_without_start.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                    if var_item.Variable.IsInput:
                        self.bool_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.bool_output_vars.append(var_item)
                    if var_item.Variable.HasStart:
                        if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.BooleanLiteral:
                            self.bool_with_start.append(var_item)
                        else:
                            self.bool_without_start.append(var_item)
                    else:
                        self.bool_without_start.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.String:
                    self.string_storage_vars.append(var_item)
                else:
                    assert(False)

        for var_item in self.code_env.model_data.ModelVariables:
            self.var_map[var_item.ID] = var_item
            assert(var_item.ScopeKind == MwPyModelData.ScopeVariableKind.Model)
            assert(var_item.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
            if var_item.ID in self.data_dictionary.keys():
                logging.debug("Model data dictionary variable '{0}'".format(var_item.Variable.Name))
                if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                    if var_item.IsState:
                        raise Exception("不支持数据字典绑定状态变量")
                    elif var_item.IsDerivative:
                        raise Exception("不支持数据字典绑定导数变量")

                    if var_item.Variable.IsInput:
                        self.dict_real_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_real_output_vars.append(var_item)
                    self.dict_real_storage_vars.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                    if var_item.Variable.IsInput:
                        self.dict_int_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_int_output_vars.append(var_item)
                    self.dict_int_storage_vars.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                    if var_item.Variable.IsInput:
                        self.dict_bool_input_vars.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.dict_bool_output_vars.append(var_item)
                    self.dict_bool_storage_vars.append(var_item)
            else:
                logging.debug("Model variable '{0}'".format(var_item.Variable.Name))
                if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                    if var_item.IsState:
                        if var_item.Variable.IsInput:
                            self.real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.real_output_vars.append(var_item)
                        continue
                    elif var_item.IsDerivative:
                        if var_item.Variable.IsInput:
                            self.real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.real_output_vars.append(var_item)
                        continue
                    if var_item.Variable.IsInput:
                        self.real_input_vars.append(var_item)
                        self.real_variables_input.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.real_output_vars.append(var_item)
                        self.real_without_start.append(var_item)
                    else:
                        self.real_without_start.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                    if var_item.Variable.IsInput:
                        self.int_input_vars.append(var_item)
                        self.int_variables_input.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.int_output_vars.append(var_item)
                        self.int_without_start.append(var_item)
                    else:
                        self.int_without_start.append(var_item)
                elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                    if var_item.Variable.IsInput:
                        self.bool_input_vars.append(var_item)
                        self.bool_variables_input.append(var_item)
                    elif var_item.Variable.IsOutput:
                        self.bool_output_vars.append(var_item)
                        self.bool_without_start.append(var_item)
                    else:
                        self.bool_without_start.append(var_item)
                else:
                    assert(False)

        for var_item in self.real_variables_input:
            if var_item.Variable.HasStart:
                if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.RealLiteral or var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                    self.real_with_start.append(var_item)
                else:
                    self.real_without_start.append(var_item)
            else:
                self.real_without_start.append(var_item)

        for var_item in self.int_variables_input:
            if var_item.Variable.HasStart:
                if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                    self.int_with_start.append(var_item)
                else:
                    self.int_without_start.append(var_item)
            else:
                self.int_without_start.append(var_item)

        for var_item in self.bool_variables_input:
            if var_item.Variable.HasStart:
                if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.BooleanLiteral:
                    self.bool_with_start.append(var_item)
                else:
                    self.bool_without_start.append(var_item)
            else:
                self.bool_without_start.append(var_item)

        for var_item in self.code_env.model_data.ModelParameters:
            self.var_map[var_item.ID] = var_item
            assert(var_item.ScopeKind == MwPyModelData.ScopeVariableKind.Model)
            assert(var_item.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
            if var_item.ID in self.data_dictionary.keys():
                logging.debug("Model data dictionary parameter '{0}'".format(var_item.Variable.Name))
                if var_item.ParameterKind == MwPyModelData.ParameterKind.Free:
                    if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                        if var_item.Variable.IsInput:
                            self.dict_real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_real_output_vars.append(var_item)
                        self.dict_real_free_params.append(var_item)
                        self.dict_real_storage_vars.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                        if var_item.Variable.IsInput:
                            self.dict_int_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_int_output_vars.append(var_item)
                        self.dict_int_free_params.append(var_item)
                        self.dict_int_storage_vars.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                        if var_item.Variable.IsInput:
                            self.dict_bool_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_bool_output_vars.append(var_item)
                        self.dict_bool_free_params.append(var_item)
                        self.dict_bool_storage_vars.append(var_item)
                    else:
                        assert(False)
                else:
                    if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                        if var_item.Variable.IsInput:
                            self.dict_real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_real_output_vars.append(var_item)
                        self.dict_real_storage_vars.append(var_item)
                    elif var_item.Variable.Type.BuiiltinKind == MwPyModelData.BuiltinKind.Integer:
                        if var_item.Variable.IsInput:
                            self.dict_int_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_int_output_vars.append(var_item)
                        self.dict_int_storage_vars.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                        if var_item.Variable.IsInput:
                            self.dict_bool_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.dict_bool_output_vars.append(var_item)
                        self.dict_bool_storage_vars.append(var_item)
                    else:
                        assert(False)
            else:
                logging.debug("Model parameter '{0}'".format(var_item.Variable.Name))
                if var_item.ParameterKind == MwPyModelData.ParameterKind.Free:
                    if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                        if var_item.Variable.IsInput:
                            self.real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.real_output_vars.append(var_item)
                        self.real_free_params.append(var_item)
                        if self.real_free_param_start == 0:
                            self.real_free_param_start = len(self.real_with_start) + 1
                        if var_item.Variable.HasStart:
                            if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.RealLiteral or var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                                self.real_with_start.append(var_item)
                            else:
                                self.real_free_parameter_without_start.append(var_item)
                        else:
                            self.real_free_parameter_without_start.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                        if var_item.Variable.IsInput:
                            self.int_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.int_output_vars.append(var_item)
                        self.int_free_params.append(var_item)
                        if self.int_free_param_start == 0:
                            self.int_free_param_start = len(self.int_with_start)
                        if var_item.Variable.HasStart:
                            if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.IntegerLiteral:
                                self.int_with_start.append(var_item)
                            else:
                                self.int_free_parameter_without_start.append(var_item)
                        else:
                            self.int_free_parameter_without_start.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                        if var_item.Variable.IsInput:
                            self.bool_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.bool_output_vars.append(var_item)
                        self.bool_free_params.append(var_item)
                        if self.bool_free_param_start == 0:
                            self.boll_free_param_start = len(self.bool_with_start)
                        if var_item.Variable.HasStart:
                            if var_item.Variable.Start.ExpressionKind == MwPyModelData.ExpressionKind.BooleanLiteral:
                                self.bool_with_start.append(var_item)
                            else:
                                self.bool_free_parameter_without_start.append(var_item)
                        else:
                            self.bool_free_parameter_without_start.append(var_item)
                    else:
                        assert(False)
                else: # 非自由参量不需初始化
                    if var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                        if var_item.Variable.IsInput:
                            self.real_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.real_output_vars.append(var_item)
                        self.real_without_start.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                        if var_item.Variable.IsInput:
                            self.int_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.int_output_vars.append(var_item)
                        self.int_without_start.append(var_item)
                    elif var_item.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                        if var_item.Variable.IsInput:
                            self.bool_input_vars.append(var_item)
                        elif var_item.Variable.IsOutput:
                            self.bool_output_vars.append(var_item)
                        self.bool_without_start.append(var_item)
                    else:
                        assert(False)

        # 状态变量
        for var_item in self.code_env.model_data.StateVariables:
            if self.state_var_start == 0:
                self.state_var_start = len(self.real_with_start + self.real_free_parameter_without_start + self.real_without_start) + 1
            self.state_vars.append(var_item)
        # 导数变量
        for var_item in self.code_env.model_data.DerivativeVariables:
            if self.der_var_start == 0:
                self.der_var_start = len(self.real_with_start + self.real_free_parameter_without_start + self.real_without_start + self.state_vars) + 1
            self.der_vars.append(var_item)

        for var_item in self.code_env.model_data.AliasModelVariables:
            self.var_map[var_item.ID] = var_item
            assert(var_item.ScopeKind == MwPyModelData.ScopeVariableKind.Alias)
            assert(var_item.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
            logging.debug("Model alias variable '{0}'".format(var_item.Variable.Name))
        # 收集pre变量
        for map_item in self.code_env.model_data.PreVariables:
            origin_id = map_item.key()
            pre_id = map_item.data()
            if origin_id in self.var_map and pre_id in self.var_map:
                origin_var = self.var_map[origin_id]
                pre_var = self.var_map[pre_id]
                assert(pre_var.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
                logging.debug("Pre variable '{0}'".format(pre_var.Variable.Name))
                if pre_var.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Real:
                    self.real_pre_vars.append((pre_var,origin_var))
                elif pre_var.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Integer:
                    self.int_pre_vars.append((pre_var,origin_var))
                elif pre_var.Variable.Type.BuiltinKind == MwPyModelData.BuiltinKind.Boolean:
                    self.bool_pre_vars.append((pre_var,origin_var))
                else:
                    assert(False)
            
        # TODO 字符串变量和结构变量(数组和记录)
        
        #logging.debug("Model variable is {0}".format(self.var_map))

        # 对header_file做整理
        temp_header_list = []
        temp_header_list_gen_export = []
        temp_header_list_gen_import = []
        for var_item in self.dict_real_storage_vars:
            if self.data_dictionary[var_item.ID].HeaderFile != "":
                temp_header_list.append(self.data_dictionary[var_item.ID].HeaderFile)
                if self.data_dictionary[var_item.ID].StorageType == "ExportedGlobal":
                    temp_header_list_gen_export.append(self.data_dictionary[var_item.ID].HeaderFile)
                elif self.data_dictionary[var_item.ID].StorageType == "ImportedExtern" or self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                    temp_header_list_gen_import.append(self.data_dictionary[var_item.ID].HeaderFile)
        for var_item in self.dict_int_storage_vars:
            if self.data_dictionary[var_item.ID].HeaderFile != "":
                temp_header_list.append(self.data_dictionary[var_item.ID].HeaderFile)
                if self.data_dictionary[var_item.ID].StorageType == "ExportedGlobal":
                    temp_header_list_gen_export.append(self.data_dictionary[var_item.ID].HeaderFile)
                elif self.data_dictionary[var_item.ID].StorageType == "ImportedExtern" or self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                    temp_header_list_gen_import.append(self.data_dictionary[var_item.ID].HeaderFile)
        for var_item in self.dict_bool_storage_vars:
            if self.data_dictionary[var_item.ID].HeaderFile != "":
                temp_header_list.append(self.data_dictionary[var_item.ID].HeaderFile)
                if self.data_dictionary[var_item.ID].StorageType == "ExportedGlobal":
                    temp_header_list_gen_export.append(self.data_dictionary[var_item.ID].HeaderFile)
                elif self.data_dictionary[var_item.ID].StorageType == "ImportedExtern" or self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                    temp_header_list_gen_import.append(self.data_dictionary[var_item.ID].HeaderFile)
        for var_item in self.dict_string_storage_vars:
            if self.data_dictionary[var_item.ID].HeaderFile != "":
                temp_header_list.append(self.data_dictionary[var_item.ID].HeaderFile)
                if self.data_dictionary[var_item.ID].StorageType == "ExportedGlobal":
                    temp_header_list_gen_export.append(self.data_dictionary[var_item.ID].HeaderFile)
                elif self.data_dictionary[var_item.ID].StorageType == "ImportedExtern" or self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                    temp_header_list_gen_import.append(self.data_dictionary[var_item.ID].HeaderFile)
        for item in temp_header_list:
            if item not in self.custom_header_file:
                self.custom_header_file.append(item)
        for item in temp_header_list_gen_export:
            if item not in self.custom_header_file_gen_export:
                self.custom_header_file_gen_export.append(item)
        for item in temp_header_list_gen_import:
            if item not in self.custom_header_file_gen_import:
                self.custom_header_file_gen_import.append(item)
        #f2=open("E:\\heard_file.txt","w");   
        #print("self.custom_header_file is '{0}\n'".format(self.custom_header_file),file=f2);
        #print("self.custom_header_file_gen_export is '{0}\n'".format(self.custom_header_file_gen_export),file=f2);
        #print("self.temp_header_list_gen_import is '{0}\n'".format(self.custom_header_file_gen_import),file=f2);
        #print("self.string_storage_vars is {0} \n".format(self.string_storage_vars),file=f2);
        #f2.close();

    def add_when_condition(self, pre_cond, cond, cond_size):
        """
        添加when条件，并返回的序号
        @param[in]pre_cond                  when条件之前的部分
        @param[in]cond                      when条件
        @return 序号(0-base)
        """
        if cond == "":
            return -1
        cur_count = self.when_condition_count
        self.when_conditions.append((cur_count, pre_cond, cond, cond_size))
        if cond_size == 0:
            self.when_condition_count += 1
        else:
            self.when_condition_count += cond_size
        return cur_count

    def add_if_condition(self):
        """
        添加if条件，并返回的序号
        @return 序号(0-base)
        """
        cur_count = self.if_condition_count
        self.if_condition_count += 1
        return cur_count

    def add_sample(self, argu1, argu2):
        """
        添加sample，并返回的序号
        @param[in]argu1                     sample第一个参数
        @param[in]argu2                     sample第二个参数
        @return 序号(0-base)
        """
        self.code_env.set_has_sample()
        cur_count = self.sample_count
        self.sample_data.append((self.sample_count, argu1, argu2))
        self.sample_count += 1
        return cur_count

    def emit(self):
        """
        输出求解器数据代码
        @param[in]splitter                  代码拆分器
        @param[in]header_emitter            头文件输出器
        @param[in]internal_header_emitter   内部头文件输出器
        """
        # TODO 变量名和存储定制

        # 为变量分配名字，代码生成时直接引用
        # 时间
        if self.code_env.use_hierarchy_model_variable_name:
            self.time_var = "_TIME"
        else:
            idx = 0
            self.time_var = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["time_name"],
                                               index=idx, name = "time").strip()
            logging.debug("Time name is '{0}'".format(self.time_var))

            


        #pre(x)、der(x)不需要取地址
        self.real_storage_vars = self.real_with_start + self.real_free_parameter_without_start + self.real_without_start + self.state_vars + self.der_vars
        #f=open("E:\\checkVar.txt","w")
        if self.code_env.use_hierarchy_model_variable_name:
            for var_item in self.real_storage_vars:
                #print("var_item.Name is {0}".format(var_item.Name),file=f)
                hierarchy_var_name = self.gen_hierarchy_variable_name(var_item.Name)
                #print("hierarchy_var_name is {0}".format(hierarchy_var_name),file=f)
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["hierarchy_var_name"], 
                                               hierarchy_var_name = hierarchy_var_name).strip()
                #print("final_name is {0}".format(self.var_names[var_item.ID]),file=f)
                self.real_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                if "pre(" in var_item.Name:
                    self.pre_vars_id.append(var_item.ID)
                if "der(" in var_item.Name:
                    self.der_vars_id.append(var_item.ID)
        else:
            idx = 1
            for var_item in self.real_storage_vars:
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                               model_var = var_item, index=idx, type = MwPyModelData.BuiltinKind.Real, is_dict_var = False).strip()
                self.real_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                logging.debug("Model variable name is '{0}' for '{1}'".format(self.var_names[var_item.ID], var_item.Name))
                idx += 1
        #f.close()
        self.int_storage_vars = self.int_with_start + self.int_free_parameter_without_start + self.int_without_start
        if self.code_env.use_hierarchy_model_variable_name:
            for var_item in self.int_storage_vars:
                hierarchy_var_name = self.gen_hierarchy_variable_name(var_item.Name)
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["hierarchy_var_name"], 
                                               hierarchy_var_name = hierarchy_var_name).strip()
                self.int_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                if "pre(" in var_item.Name:
                    self.pre_vars_id.append(var_item.ID)
        else:
            idx = 0
            for var_item in self.int_storage_vars:
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                               model_var = var_item, index=idx, type = MwPyModelData.BuiltinKind.Integer, is_dict_var = False).strip()
                self.int_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                logging.debug("Model variable name is '{0}' for '{1}'".format(self.var_names[var_item.ID], var_item.Name))
                idx += 1

        self.bool_storage_vars = self.bool_with_start + self.bool_free_parameter_without_start + self.bool_without_start
        if self.code_env.use_hierarchy_model_variable_name:
            for var_item in self.bool_storage_vars:
                hierarchy_var_name = self.gen_hierarchy_variable_name(var_item.Name)
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["hierarchy_var_name"], 
                                               hierarchy_var_name = hierarchy_var_name).strip()
                self.bool_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                if "pre(" in var_item.Name:
                    self.pre_vars_id.append(var_item.ID)
        else:
            idx = 0
            for var_item in self.bool_storage_vars:
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                               model_var = var_item, index=idx, type = MwPyModelData.BuiltinKind.Boolean, is_dict_var = False).strip()
                self.bool_var_id.append(var_item.ID)
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                logging.debug("Model variable name is '{0}' for '{1}'".format(self.var_names[var_item.ID], var_item.Name))
                idx += 1

        if self.code_env.use_hierarchy_model_variable_name:
            for var_item in self.string_storage_vars:
                hierarchy_var_name = self.gen_hierarchy_variable_name(var_item.Name)
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["hierarchy_var_name"], 
                                               hierarchy_var_name = hierarchy_var_name).strip()
        else:
            idx = 0
            for var_item in self.string_storage_vars:
                self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                               model_var = var_item, index=idx, type = MwPyModelData.BuiltinKind.String, is_dict_var = False).strip()
                logging.debug("Model variable name is '{0}' for '{1}'".format(self.var_names[var_item.ID], var_item.Name))
                idx += 1
        


        for var_item in self.dict_real_storage_vars:
            is_pointer = False
            if self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                is_pointer = True
                if self.data_dictionary[var_item.ID].IsArray:
                    is_pointer = False
            self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                           type = MwPyModelData.BuiltinKind.Real, is_dict_var = True, dict_var_name = self.data_dictionary[var_item.ID].Name,
                                           is_array = self.data_dictionary[var_item.ID].IsArray, array_index = self.data_dictionary[var_item.ID].ArrayIndex,
                                           is_pointer = is_pointer).strip()
            self.real_var_id.append(var_item.ID)
            if(var_item.ID > self.max_id):
                self.max_id = var_item.ID
        for var_item in self.dict_int_storage_vars:
            is_pointer = False
            if self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                is_pointer = True
                if self.data_dictionary[var_item.ID].IsArray:
                    is_pointer = False
            self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                           type = MwPyModelData.BuiltinKind.Integer, is_dict_var = True, dict_var_name = self.data_dictionary[var_item.ID].Name,
                                           is_array = self.data_dictionary[var_item.ID].IsArray, array_index = self.data_dictionary[var_item.ID].ArrayIndex,
                                           is_pointer = is_pointer).strip()
            self.int_var_id.append(var_item.ID)
            if(var_item.ID > self.max_id):
                self.max_id = var_item.ID
        for var_item in self.dict_bool_storage_vars:
            is_pointer = False
            if self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                is_pointer = True
                if self.data_dictionary[var_item.ID].IsArray:
                    is_pointer = False
            self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                           type = MwPyModelData.BuiltinKind.Boolean, is_dict_var = True, dict_var_name = self.data_dictionary[var_item.ID].Name,
                                           is_array = self.data_dictionary[var_item.ID].IsArray, array_index = self.data_dictionary[var_item.ID].ArrayIndex,
                                           is_pointer = is_pointer).strip()
            self.bool_var_id.append(var_item.ID)
            if(var_item.ID > self.max_id):
                self.max_id = var_item.ID
        for var_item in self.dict_string_storage_vars:
            is_pointer = False
            if self.data_dictionary[var_item.ID].StorageType == "ImportedExternPointer":
                is_pointer = True
                if self.data_dictionary[var_item.ID].IsArray:
                    is_pointer = False
            self.var_names[var_item.ID] = self.code_env.code_engine.run_piece_template(self.code_env.options["template map"]["model_variable_name"], 
                                           type = MwPyModelData.BuiltinKind.String, is_dict_var = True, dict_var_name = self.data_dictionary[var_item.ID].Name,
                                           is_array = self.data_dictionary[var_item.ID].IsArray, array_index = self.data_dictionary[var_item.ID].ArrayIndex,
                                           is_pointer = is_pointer).strip()

        # 别名变量
        for var_item in self.code_env.model_data.AliasModelVariables:
            assert(var_item.ScopeKind == MwPyModelData.ScopeVariableKind.Alias)
            assert(var_item.Variable.VariableKind == MwPyModelData.VariableKind.Builtin)
            logging.debug("Model alias variable '{0}'".format(var_item.Variable.Name))
            var_name = ""
            if var_item.Autonym.ID in self.var_names:
                var_name = self.var_names[var_item.Autonym.ID]
                if var_item.Sign == -1:
                    var_name = "(-" + var_name + ")"
                    if var_item.Autonym.ID in self.real_var_id:
                        self.neg_real_alis_id.append(var_item.ID)
                    elif var_item.Autonym.ID in self.int_var_id:
                        self.neg_int_alis_id.append(var_item.ID)
                if var_item.Autonym.ID in self.real_var_id:
                    self.real_var_id.append(var_item.ID)
                elif var_item.Autonym.ID in self.int_var_id:
                    self.int_var_id.append(var_item.ID)
                elif var_item.Autonym.ID in self.bool_var_id:
                    self.bool_var_id.append(var_item.ID)
                self.var_names[var_item.ID] = var_name
                if(var_item.ID > self.max_id):
                    self.max_id = var_item.ID
                self.origin_id[var_item.ID] = var_item.Autonym.ID

        # 将变量id从小到大排序，从而保证数组索引和变量id对应，方便取出变量地址
        # 同时将别名变量的名字记录为原始变量名（负别名无法直接取地址）
        for num in range(self.max_id+1):
            if num in self.var_names:
                if num in self.der_vars_id or num in self.pre_vars_id: # pre、der变量不会取地址，临时将名字替换为"_TIME"，在地址数组中只起占位作用
                    self.var_names_ordered[num] = "_TIME"
                else:
                    if num in self.origin_id:
                        self.var_names_ordered[num] = self.var_names[self.origin_id[num]]
                    else:
                        self.var_names_ordered[num] = self.var_names[num]
            else:
                self.var_names_ordered[num] = 0
        self.real_var_id.sort()
        self.int_var_id.sort()
        self.bool_var_id.sort()
        self.neg_real_alis_id.sort()
        self.neg_int_alis_id.sort()
        #f2=open("E:\\log_model_var.txt","w");   
        #print("Time name is '{0}\n'".format(self.time_var),file=f2);
        #print("self.real_var_id is '{0}\n'".format(self.real_var_id),file=f2);
        #print("self.int_var_id is '{0}\n'".format(self.int_var_id),file=f2);
        #print("self.bool_var_id is '{0}\n'".format(self.bool_var_id),file=f2);
        #print("self.neg_real_alis_id is '{0}\n'".format(self.neg_real_alis_id),file=f2);
        #print("self.neg_int_alis_id is '{0}\n'".format(self.neg_int_alis_id),file=f2);
        #print("self.var_names_ordered is '{0}\n'".format(self.var_names_ordered),file=f2);
        #print("self.var_names_ordered is '{0}\n'".format(self.var_names_ordered),file=f2);
        #print("self.real_with_start is '{0}\n'".format(self.real_with_start),file=f2);
        #print("self.dict_real_storage_vars is '{0}\n'".format(self.dict_real_storage_vars),file=f2);
        #print("self.dict_int_storage_vars is '{0}\n'".format(self.dict_int_storage_vars),file=f2);
        #print("self.dict_bool_storage_vars is '{0}\n'".format(self.dict_bool_storage_vars),file=f2);
        #print("self.dict_string_storage_vars is '{0}\n'".format(self.dict_string_storage_vars),file=f2);
        #print("self.data_dictionary is '{0}\n'".format(self.data_dictionary),file=f2);
        #print("self.real_pre_vars is '{0}\n'".format(self.real_pre_vars),file=f2);
        #print("self.int_pre_vars is '{0}\n'".format(self.int_pre_vars),file=f2);
        #print("self.bool_pre_vars is '{0}\n'".format(self.bool_pre_vars),file=f2);
        #print("self.der_vars is '{0}\n'".format(self.der_vars),file=f2);
        #f2.close();  
        # TODO pre变量

        # TODO 生成全局变量的定义或者外部声明等

        #splitter.notify_finished()


    def get_variable_name(self, var):
        """
        获取变量的名字
        @param[in]var   变量
        """
        if var.ID in self.var_names:
            return self.var_names[var.ID]
        return ""

    def get_pre_variable_name(self, var):
        """
        获取pre变量的名字
        @param[in]var   原始变量
        """
        if var.ID in self.code_env.model_data.PreVariables:
            if self.code_env.model_data.PreVariables[var.ID] in self.var_names:
                return self.var_names[self.code_env.model_data.PreVariables[var.ID]]
        return ""

    def get_time_name(self):
        """
        获取时间变量的名字
        """
        return self.time_var

    def emit_data_dictionary_customed_header(self, header_emitter, file_name, is_export):
        """
        输出用户自定义头文件，可能有多个
        @param[in]header_emitter            头文件输出器
        @param[in]file_name                 头文件名
        @param[in]is_export                 是否是export模式
        """
        self.code_env.code_engine.run_header_template(template_filename = self.code_env.template_map["data_dictionary_custom_header"], 
            header_emitter = header_emitter, model_vars = self.code_env.model_vars, file_name = file_name, is_export = is_export)

        header_emitter.notify_finished()

    def emit_data_dictionary_import_c_for_sim(self, import_splitter):
        """
        输出数据字典import模式的变量定义（仅用于仿真，【代码生成】时不会生成）
        @param[in]import_splitter          代码拆分器
        """
        self.code_env.code_engine.run_template(template_filename = self.code_env.template_map["import_data_for_simulation"], splitter = import_splitter)

        import_splitter.notify_finished()

    def is_var_in_data_dictionary(self, var):
        """
        判断变量是否位于数据字典中
        @param[in]var           待判断的变量
        """
        res = False
        if var.ID in self.data_dictionary.keys():
            res = True
        return res

    def get_int_type_info(self, var):
        """
        返回数据字典中整数类型变量的信息：是否是有符号的，整数位长，json中注册的key以及设置的类型
        @param[in]var_expr           变量
        """
        is_signed = True
        int_size = 32
        type_str = "int"
        ctype_str = self.code_env.options["builtin map"]["type"]["int"]
        data_type = self.data_dictionary[var.ID].DataType
        for (key, value) in self.code_env.options["builtin map"]["type"].items():
            if value == data_type:
                type_str = key
                ctype_str = value
                break
        if type_str.startswith("u"):
            is_signed = False
        if type_str.endswith("8"):
            int_size = 8
        elif type_str.endswith("16"):
            int_size = 16
        elif type_str.endswith("32"):
            int_size = 32
        elif type_str.endswith("64"):
            int_size = 64
        else:
            int_size = int(self.code_env.num_of_int)
        return (is_signed, int_size, type_str, ctype_str)

    def has_init_data_file(self):
        """
        判断模块型和数据分开的紧凑型时是否需要生成modata.c和modata.h文件
        """

        res = False
        if len(self.real_var_id) > 0 or len(self.int_var_id) > 0 or len(self.bool_var_id) > 0:
            res = True
        # 以下判断代码，应不可能为真
        if res == False and len(self.real_with_start) > 0 or len(self.state_vars_with_start) > 0 or len(self.der_vars_with_start) > 0 or len(self.int_with_start) > 0 or len(self.bool_with_start) > 0:
            res = True
        if res == False and (len(self.dict_real_storage_vars) > 0 or len(self.dict_int_storage_vars) > 0 or len(self.dict_bool_storage_vars) > 0 or  len(self.dict_string_storage_vars) > 0):
            if self.has_init_dict_array(self.dict_real_storage_vars):
                res = True
            elif self.has_init_dict_array(self.dict_int_storage_vars):
                res = True
            elif self.has_init_dict_array(self.dict_bool_storage_vars):
                res = True
            elif self.has_init_dict_array(self.dict_string_storage_vars):
                res = True
        return res

    def has_init_dict_array(self, vars):
        """
        判断数据字典容器中是否含有数组部分
        @param[in]vars       数据字典容器
        """

        for var_item in vars:
            if self.data_dictionary[var_item.ID].IsArray and self.data_dictionary[var_item.ID].ArrayIndex == 0:
                if len(self.data_dictionary[var_item.ID].Value) > 0 or len(self.data_dictionary[var_item.ID].InitialValue) > 0 or var_item.Variable.HasStart:
                    return True
    
    def has_max_compare(self, vars):
        """
        判断数据字典容器中数据是否有最大值限制
        @param[in]vars       数据字典容器
        """

        for var_item in vars:
            if len(self.data_dictionary[var_item.ID].Max) > 0:
                return True

    def has_min_compare(self, vars):
        """
        判断数据字典容器中数据是否有最小值限制
        @param[in]vars       数据字典容器
        """

        for var_item in vars:
            if len(self.data_dictionary[var_item.ID].Min) > 0:
                return True

    def has_pre_variables(self):
        """
        判断是否有pre变量
        """
        return (len(self.real_pre_vars) > 0 or len(self.int_pre_vars) > 0 or len(self.bool_pre_vars) > 0)

    #YPH:生成结构化的变量名
    #目前来看，就是把原来变量名的括号给想办法去掉
    def gen_hierarchy_variable_name(self, name):
        """
        生成层次化的变量名 
        效果： a.b[2].pre(c) --> a.b[2].c_uupre
               a.b.der(c[2]) --> a.b.c_uuder[2]
        """
        name = self.handle_c_key_name(name)
        if "." in name:
            dot_index = name.rfind(".")
            sub_str = name[dot_index+1:]
            if sub_str.isdigit():
                name = name[:dot_index] + "_" + name[dot_index+1:]
        if "pre(" in name:
            name = name.replace("pre(", "")
            name = name.replace(")", "")
            if "." in name:
                sub_index = name.rfind(".")
                sub_str = name[sub_index:]
                name = name[:sub_index]
                if "[" in sub_str:
                    pre_index = sub_str.find("[")
                    sub_str = sub_str[:pre_index] + "_uupre" + sub_str[pre_index:]
                else:
                    sub_str += "_uupre"
                name += sub_str
            else:
                if "[" in name:
                    pre_index = name.find("[")
                    name = name[:pre_index] + "_uupre" + name[pre_index:]
                else:
                    name = name + "_uupre"
        if "der(" in name:
            if ",2)" in name:#例如der(x,2)的情形
                name = name.replace(",2)", ")")
                has_second_der = True
            else:
                has_second_der = False
            name = name.replace("der(", "")
            name = name.replace(")", "")
            if "." in name:
                sub_index = name.rfind(".")
                sub_str = name[sub_index:]
                name = name[:sub_index]
                if "[" in sub_str:
                    der_index = sub_str.find("[")
                    if has_second_der:
                        sub_str = sub_str[:der_index] + "_uuder_uuder" + sub_str[der_index:]
                    else:
                        sub_str = sub_str[:der_index] + "_uuder" + sub_str[der_index:]
                else:
                    if has_second_der:
                        sub_str = sub_str + "_uuder_uuder"
                    else:
                        sub_str = sub_str + "_uuder"
                name += sub_str
            else:
                if "[" in name:
                    der_index = name.find("[")
                    name = name[:der_index] + "_uuder" + name[der_index:]
                else:
                    name = name + "_uuder"
            name = self.handle_repetition_der_name(name)
        name = name.replace("]", "-1]")
        name = name.replace(",", "-1][")
        #处理长度大于限制长度的名字
        new_name = ""
        is_first_loop = True
        for item in name.split("."):
            if "[" in item:
                pre_index = item.find("[")
                item = self.code_env.get_truncate_name( item[:pre_index], "") + item[pre_index:]
            else:
                item = self.code_env.get_truncate_name(item, "")
            if is_first_loop:
                new_name = item
            else:
                new_name = new_name + "." + item
            is_first_loop = False

        return new_name

    def handle_repetition_der_name(self, name):
        """
        处理重复的der名字
        """
        if name in self.der_names:
            der_index = name.find("_uuder")
            name = name[:der_index] + "_uuder" + name[der_index:]
            self.der_names.append(name)
            name = self.handle_repetition_der_name(name)
        return name

    def handle_c_key_name(self, name):
        """
        处理c关键字
        """
        new_name = ""
        is_first_loop = True
        for item in name.split("."):
            if item in self.code_env.code_engine.converter.c_key_word:
                item = MwPyModelData.ToCName(item)
                if item in self.code_env.code_engine.converter.c_key_word:
                    item += "_"
            if is_first_loop:
                new_name = item
            else:
                new_name = new_name + "." + item
            is_first_loop = False

        return new_name