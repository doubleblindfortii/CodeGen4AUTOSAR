/*
 * File: autosar_swc_monitor.h
 *
 * Code generated for Simulink model 'autosar_swc_monitor'.
 *
 * Model version                  : 4.0
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Thu Aug  7 15:21:28 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_monitor_h_
#define RTW_HEADER_autosar_swc_monitor_h_
#ifndef autosar_swc_monitor_COMMON_INCLUDES_
#define autosar_swc_monitor_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "Rte_ThrottlePositionMonitor.h"
#endif                                /* autosar_swc_monitor_COMMON_INCLUDES_ */

#include "autosar_swc_monitor_types.h"

/* Macros for accessing real-time model data structure */

/* Invariant block signals (default storage) */
typedef struct {
  const boolean Compare;               /* '<S2>/Compare' */
} ConstB_autosar_swc_monitor_T;

extern const ConstB_autosar_swc_monitor_T autosar_swc_monitor_ConstB;/* constant block i/o */

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
 * '<Root>' : 'autosar_swc_monitor'
 * '<S1>'   : 'autosar_swc_monitor/Runnable_Step_sys'
 * '<S2>'   : 'autosar_swc_monitor/Runnable_Step_sys/Compare To Constant'
 */
#endif                                 /* RTW_HEADER_autosar_swc_monitor_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
