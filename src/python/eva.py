import pandas as pd
import numpy as np

def compute_nrmse(file_ref, file_sim, eps=1e-12):
    """
    计算两个仿真结果文件之间的 NRMSE
    :param file_ref: 基准模型导出的 CSV 文件 (参考结果)
    :param file_sim: 待比较模型导出的 CSV 文件 (测试结果)
    :param eps: 防止除零的小数
    :return: dict，key 为变量名，value 为 NRMSE
    """

    # 读入 CSV
    df_ref = pd.read_csv(file_ref)
    df_sim = pd.read_csv(file_sim)

    # 检查时间列是否一致
    if not np.allclose(df_ref.iloc[:,0], df_sim.iloc[:,0], rtol=1e-9, atol=1e-12):
        raise ValueError("两个文件的时间列不一致，请检查！")

    # 对齐变量
    common_vars = set(df_ref.columns[1:]).intersection(df_sim.columns[1:])
    if not common_vars:
        raise ValueError("两个文件没有共同的变量列！")

    nrmse_results = {}
    for var in common_vars:
        y_ref = df_ref[var].values
        y_sim = df_sim[var].values

        rmse = np.sqrt(np.mean((y_ref - y_sim)**2))
        denom = (y_ref.max() - y_ref.min()) + eps
        nrmse = rmse / denom
        nrmse_results[var] = nrmse

    return nrmse_results


# 使用示例
if __name__ == "__main__":
    # 第一个autosar_swc
    # NRMSE 结果：
    # pport: 0.0000
    # pport1: 0.0000
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_mo.csv"    # 待比较模型

    # 第二个autosar_swc_expfcns

    # NRMSE 结果：
    # PPort_3: 0.0000
    # PPort_2: 0.0000
    # PPort_4: 0.0000
    # PPort_1: 0.0000
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_expfcns_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_Expfcns_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)

    # 第三个autosar_swc_throttle
    # TPS_Percent_Value: 0.0173
    # NRMSE 结果：
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_throttle_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_throttle_sensor_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)

    # 第四个autosar_swc_monitor
    # TPS_Percent_Value: 0.0000
    # NRMSE 结果：
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_monitor.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_monitor_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)


    # 第五个autosar_swc_pedal_sensor
    # NRMSE 结果：
    # APP_Percent_Value: 0.0000
    # NRMSE 结果：
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_pedal_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_pedal_sensor_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)

    # 第六个autosar_swc_controller
    # NRMSE 结果：0.0031
    # NRMSE 结果：
    #ThrCmd_HwIO_Value: 0.0000
    # NRMSE 结果：
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_controller_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_controller_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)


    # 第七个autosar_swc_actuator
    # NRMSE 结果：
    # ThrCmd_HwIO_Value: 0.0000
    file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_actuator_si.csv"   # 参考模型
    file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_actuator_mo.csv"    # 待比较模型
    scores = compute_nrmse(file_ref, file_sim)

    print("NRMSE 结果：")
    for var, score in scores.items():
        print(f"{var}: {score:.4f}")