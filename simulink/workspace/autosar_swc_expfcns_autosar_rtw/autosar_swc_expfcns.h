/*
 * File: autosar_swc_expfcns.h
 *
 * Code generated for Simulink model 'autosar_swc_expfcns'.
 *
 * Model version                  : 4.20
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Mon Aug 11 11:51:31 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_expfcns_h_
#define RTW_HEADER_autosar_swc_expfcns_h_
#ifndef autosar_swc_expfcns_COMMON_INCLUDES_
#define autosar_swc_expfcns_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "Rte_ASWC.h"
#endif                                /* autosar_swc_expfcns_COMMON_INCLUDES_ */

/* Model Code Variants */

/* Macros for accessing real-time model data structure */

/* Block signals (default storage) */
typedef struct tag_BlockIO {
  float64 Add;                         /* '<S4>/Add' */
} BlockIO;

/* Block states (default storage) for system '<Root>' */
typedef struct tag_D_Work {
  float64 DiscreteTimeIntegrator_DSTATE;/* '<S2>/Discrete-Time Integrator' */
  sint8 Delay_DSTATE;                  /* '<S3>/Delay' */
  sint8 Delay_DSTATE_m;                /* '<S2>/Delay' */
  sint8 Delay_DSTATE_a;                /* '<S1>/Delay' */
} D_Work;

/* Block signals (default storage) */
extern BlockIO rtB;

/* Block states (default storage) */
extern D_Work rtDWork;

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
 * '<Root>' : 'autosar_swc_expfcns'
 * '<S1>'   : 'autosar_swc_expfcns/Runnable1_subsystem'
 * '<S2>'   : 'autosar_swc_expfcns/Runnable2_subsystem'
 * '<S3>'   : 'autosar_swc_expfcns/Runnable3_subsystem'
 * '<S4>'   : 'autosar_swc_expfcns/Runnable1_subsystem/Subsystem'
 */
#endif                                 /* RTW_HEADER_autosar_swc_expfcns_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
