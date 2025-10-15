/*
 * File: Swc_Expfcns.h
 *
 * Code generated for Modelica model 'Swc_Expfcns'.
 *
 * Model version                  : 2.3
 * C/C++ source code generated on : 2025-08-13 14:30:10
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */

#ifndef RTW_HEADER_Swc_Expfcns_h_
#define RTW_HEADER_Swc_Expfcns_h_
#ifndef Swc_Expfcns_COMMON_INCLUDES_
#define Swc_Expfcns_COMMON_INCLUDES_
#include "Rte_ASWC.h"
#include "rtwtypes.h"
#endif /* Swc_Expfcns_COMMON_INCLUDES_ */

/* Model Code Variants */

/* Macros for accessing real-time model data structure */

/* Block signals (default storage) */
typedef struct tag_BlockIO
{
  float64 add; /*'<runnable1_subsystem.subsystem_EnableSubsystem>/add' */
} BlockIO;
/* Block signals and states (default storage) for system*/
typedef struct tag_D_Work
{
  sint8 Delay_DSTATE;   /*'Swc_Expfcns.runnable1_subsystem.Delay'*/
  sint8 Delay_DSTATE_a; /*'Swc_Expfcns.runnable3_subsystem.Delay'*/
  sint8 Delay_DSTATE_b; /*'Swc_Expfcns.runnable2_subsystem.Delay'*/
  float64
      discreteTimeIntegrator_DSTATE; /*'Swc_Expfcns.runnable2_subsystem.discreteTimeIntegrator'*/
} D_Work;

/*Block signals (default storage)*/
extern BlockIO rtB;
/* Block signals and states (default storage) */
extern D_Work rtDWork;

#endif /* RTW_HEADER_Swc_Expfcns_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
