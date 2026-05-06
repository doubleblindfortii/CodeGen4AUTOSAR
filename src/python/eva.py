import pandas as pd
import numpy as np


def find_best_shift(y_ref, y_sim, max_shift=200):
    best_shift = 0
    best_error = np.inf

    for shift in range(-max_shift, max_shift + 1):
        if shift > 0:
            y_ref_cut = y_ref[:-shift]
            y_sim_cut = y_sim[shift:]
        elif shift < 0:
            y_ref_cut = y_ref[-shift:]
            y_sim_cut = y_sim[:shift]
        else:
            y_ref_cut = y_ref
            y_sim_cut = y_sim

        if len(y_ref_cut) < 10:
            continue

        rmse = np.sqrt(np.mean((y_ref_cut - y_sim_cut) ** 2))

        if rmse < best_error:
            best_error = rmse
            best_shift = shift

    return best_shift


def compute_nrmse_with_alignment(file_ref, file_sim, eps=1e-12):
    df_ref = pd.read_csv(file_ref)
    df_sim = pd.read_csv(file_sim)

    # 时间检查
    if not np.allclose(df_ref.iloc[:, 0], df_sim.iloc[:, 0], rtol=1e-9, atol=1e-12):
        raise ValueError("时间列不一致")

    common_vars = set(df_ref.columns[1:]).intersection(df_sim.columns[1:])
    if not common_vars:
        raise ValueError("没有公共变量")

    results = {}

    for var in common_vars:
        y_ref = df_ref[var].values
        y_sim = df_sim[var].values

        shift = find_best_shift(y_ref, y_sim)

        if shift > 0:
            y_ref_cut = y_ref[:-shift]
            y_sim_cut = y_sim[shift:]
        elif shift < 0:
            y_ref_cut = y_ref[-shift:]
            y_sim_cut = y_sim[:shift]
        else:
            y_ref_cut = y_ref
            y_sim_cut = y_sim

        rmse = np.sqrt(np.mean((y_ref_cut - y_sim_cut) ** 2))
        denom = (y_ref.max() - y_ref.min()) + eps
        nrmse = rmse / denom

        results[var] = {
            "nrmse": nrmse,
            "shift": shift
        }

    return results

# 使用示例
if __name__ == "__main__":
    # # 第一个autosar_swc
    # # NRMSE 结果：
    # # pport: 0.0000
    # # pport1: 0.0000
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_mo.csv"    # 待比较模型

    # # 第二个autosar_swc_expfcns

    # # NRMSE 结果：
    # # PPort_3: 0.0000
    # # PPort_2: 0.0000
    # # PPort_4: 0.0000
    # # PPort_1: 0.0000
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_expfcns_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_Expfcns_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)

    # # 第三个autosar_swc_throttle
    # # TPS_Percent_Value: 0.0173
    # # NRMSE 结果：
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_throttle_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_throttle_sensor_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)

    # # 第四个autosar_swc_monitor
    # # TPS_Percent_Value: 0.0000
    # # NRMSE 结果：
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_monitor.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_monitor_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)


    # # 第五个autosar_swc_pedal_sensor
    # # NRMSE 结果：
    # # APP_Percent_Value: 0.0000
    # # NRMSE 结果：
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_pedal_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_pedal_sensor_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)

    # # 第六个autosar_swc_controller
    # # NRMSE 结果：0.0031
    # # NRMSE 结果：
    # #ThrCmd_HwIO_Value: 0.0000
    # # NRMSE 结果：
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_controller_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_controller_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)


    # # 第七个autosar_swc_actuator
    # # NRMSE 结果：
    # # ThrCmd_HwIO_Value: 0.0000
    # file_ref = "dataset/sim_from_matlab_mo/res_matlab/autosar_swc_actuator_si.csv"   # 参考模型
    # file_sim = "dataset/sim_from_matlab_mo/res_mo/autosar_swc_actuator_mo.csv"    # 待比较模型
    # scores = compute_nrmse(file_ref, file_sim)

    # 第七个autosar_swc_actuator
    # NRMSE 结果：
    # ThrCmd_HwIO_Value: 0.0000
    file_ref = "large_scale_autosar_swc_expfcns_autosar_si.csv"   # 参考模型
    file_sim = "large_scale_autosar_swc_expfcns_mo.csv"    # 待比较模型
    scores = compute_nrmse_with_alignment(file_ref, file_sim)


    # ⭐ 论文里的整体指标
    avg_nrmse = np.mean([info['nrmse'] for info in scores.values()])
    print(f"\n平均 NRMSE: {avg_nrmse:.6f}")