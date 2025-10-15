/*
 * File: autosar_swc_throttle_sensor.h
 *
 * Code generated for Modelica model 'autosar_swc_throttle_sensor'.
 *
 * Model version                  : 2.3
 * C/C++ source code generated on : 2025-08-13 16:20:18
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_throttle_sensor_h_
#define RTW_HEADER_autosar_swc_throttle_sensor_h_
#ifndef autosar_swc_throttle_sensor_COMMON_INCLUDES_
#define autosar_swc_throttle_sensor_COMMON_INCLUDES_
#include "Rte_ThrottlePositionSensor.h"
#include "rtwtypes.h"
#endif /* autosar_swc_throttle_sensor_COMMON_INCLUDES_ */

/* Constant parameters (default storage) */
typedef struct
{
  /* Expression: TPSPercent_LkupTbl.Table
   * Referenced by: '<S1>/TPS Lookup'
   */
  float32 TPSLookup_tableData[11];

  /* Expression: TPSPercent_LkupTbl.Breakpoints(0)
   * Referenced by: '<S1>/TPS Lookup'
   */
  float32 TPSLookup_bp01Data[11];
} ConstP_autosar_swc_throttle_s_T;

/* Constant parameters (default storage) */
extern const ConstP_autosar_swc_throttle_s_T autosar_swc_throttle_sen_ConstP;

#endif /* RTW_HEADER_autosar_swc_throttle_sensor_h_ */
