/*
 * File: autosar_swc_controller.h
 *
 * Code generated for Simulink model 'autosar_swc_controller'.
 *
 * Model version                  : 4.1
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Thu Aug  7 15:21:09 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_controller_h_
#define RTW_HEADER_autosar_swc_controller_h_
#include <math.h>
#ifndef autosar_swc_controller_COMMON_INCLUDES_
#define autosar_swc_controller_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "Rte_Controller.h"
#endif                             /* autosar_swc_controller_COMMON_INCLUDES_ */

#include "autosar_swc_controller_types.h"

/* Macros for accessing real-time model data structure */

/* Block states (default storage) for system '<Root>' */
typedef struct tag_DW_autosar_swc_controller_T {
  float32 Integrator_DSTATE;           /* '<S38>/Integrator' */
  float32 UD_DSTATE;                   /* '<S31>/UD' */
} DW_autosar_swc_controller_T;

/* Block states (default storage) */
extern DW_autosar_swc_controller_T autosar_swc_controller_DW;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S31>/DTDup' : Unused code path elimination
 * Block '<S1>/Scope' : Unused code path elimination
 * Block '<S43>/Proportional Gain' : Eliminated nontunable gain of 1
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
 * '<Root>' : 'autosar_swc_controller'
 * '<S1>'   : 'autosar_swc_controller/Runnable_Step_sys'
 * '<S2>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller'
 * '<S3>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Anti-windup'
 * '<S4>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/D Gain'
 * '<S5>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter'
 * '<S6>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter ICs'
 * '<S7>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/I Gain'
 * '<S8>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Ideal P Gain'
 * '<S9>'   : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Ideal P Gain Fdbk'
 * '<S10>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Integrator'
 * '<S11>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Integrator ICs'
 * '<S12>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/N Copy'
 * '<S13>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/N Gain'
 * '<S14>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/P Copy'
 * '<S15>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Parallel P Gain'
 * '<S16>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Reset Signal'
 * '<S17>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Saturation'
 * '<S18>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Saturation Fdbk'
 * '<S19>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Sum'
 * '<S20>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Sum Fdbk'
 * '<S21>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tracking Mode'
 * '<S22>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tracking Mode Sum'
 * '<S23>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tsamp - Integral'
 * '<S24>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tsamp - Ngain'
 * '<S25>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/postSat Signal'
 * '<S26>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/preSat Signal'
 * '<S27>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Anti-windup/Disc. Clamping Parallel'
 * '<S28>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Anti-windup/Disc. Clamping Parallel/Dead Zone'
 * '<S29>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Anti-windup/Disc. Clamping Parallel/Dead Zone/Enabled'
 * '<S30>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/D Gain/Internal Parameters'
 * '<S31>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter/Differentiator'
 * '<S32>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter/Differentiator/Tsamp'
 * '<S33>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter/Differentiator/Tsamp/Internal Ts'
 * '<S34>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Filter ICs/Internal IC - Differentiator'
 * '<S35>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/I Gain/Internal Parameters'
 * '<S36>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Ideal P Gain/Passthrough'
 * '<S37>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Ideal P Gain Fdbk/Disabled'
 * '<S38>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Integrator/Discrete'
 * '<S39>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Integrator ICs/Internal IC'
 * '<S40>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/N Copy/Disabled wSignal Specification'
 * '<S41>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/N Gain/Passthrough'
 * '<S42>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/P Copy/Disabled'
 * '<S43>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Parallel P Gain/Internal Parameters'
 * '<S44>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Reset Signal/Disabled'
 * '<S45>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Saturation/Enabled'
 * '<S46>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Saturation Fdbk/Disabled'
 * '<S47>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Sum/Sum_PID'
 * '<S48>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Sum Fdbk/Disabled'
 * '<S49>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tracking Mode/Disabled'
 * '<S50>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tracking Mode Sum/Passthrough'
 * '<S51>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tsamp - Integral/Passthrough'
 * '<S52>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/Tsamp - Ngain/Passthrough'
 * '<S53>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/postSat Signal/Forward_Path'
 * '<S54>'  : 'autosar_swc_controller/Runnable_Step_sys/Discrete PID Controller/preSat Signal/Forward_Path'
 */
#endif                                /* RTW_HEADER_autosar_swc_controller_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
