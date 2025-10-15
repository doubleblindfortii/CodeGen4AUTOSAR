/*
 * File: autosar_swc_throttle_sensor.h
 *
 * Code generated for Simulink model 'autosar_swc_throttle_sensor'.
 *
 * Model version                  : 3.13
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Sat Aug  9 15:14:12 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_throttle_sensor_h_
#define RTW_HEADER_autosar_swc_throttle_sensor_h_
#ifndef autosar_swc_throttle_sensor_COMMON_INCLUDES_
#define autosar_swc_throttle_sensor_COMMON_INCLUDES_
#include "rtwtypes.h"
#endif                        /* autosar_swc_throttle_sensor_COMMON_INCLUDES_ */

#include "autosar_swc_throttle_sensor_types.h"

/* Macros for accessing real-time model data structure */

/* Constant parameters (default storage) */
typedef struct {
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

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<Root>/Scope' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'autosar_swc_throttle_sensor'
 * '<S1>'   : 'autosar_swc_throttle_sensor/Runnable_Step_sys'
 */
#endif                           /* RTW_HEADER_autosar_swc_throttle_sensor_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
