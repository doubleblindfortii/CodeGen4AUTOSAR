/*
 * File: autosar_swc.h
 *
 * Code generated for Simulink model 'autosar_swc'.
 *
 * Model version                  : 1.37
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Sun Aug 10 14:22:19 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_h_
#define RTW_HEADER_autosar_swc_h_
#ifndef autosar_swc_COMMON_INCLUDES_
#define autosar_swc_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "Rte_autosar_swc.h"
#endif                                 /* autosar_swc_COMMON_INCLUDES_ */

/* Model Code Variants */

/* Macros for accessing real-time model data structure */

/* Block signals and states (default storage) for system '<Root>' */
typedef struct tag_DW {
  float64 Integrator_DSTATE;           /* '<Root>/Integrator' */
} DW;

/* Block signals and states (default storage) */
extern DW rtDW;

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
 * '<Root>' : 'autosar_swc'
 * '<S1>'   : 'autosar_swc/Runable_Initialize'
 * '<S2>'   : 'autosar_swc/SS1'
 * '<S3>'   : 'autosar_swc/SS1/SS1'
 * '<S4>'   : 'autosar_swc/SS1/SS2'
 */
#endif                                 /* RTW_HEADER_autosar_swc_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
