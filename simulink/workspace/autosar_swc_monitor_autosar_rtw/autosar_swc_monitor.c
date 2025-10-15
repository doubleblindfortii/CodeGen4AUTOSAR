/*
 * File: autosar_swc_monitor.c
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

#include "autosar_swc_monitor.h"
#include "autosar_swc_monitor_private.h"

/* Model step function */
void Runnable_Step(void)
{
  float32 tmp;

  /* Outputs for Atomic SubSystem: '<Root>/Runnable_Step_sys' */
  /* Switch: '<S1>/Switch' incorporates:
   *  Inport: '<Root>/TPS_Primary_Value'
   *  Inport: '<Root>/TPS_Seconday_Value'
   */
  if (autosar_swc_monitor_ConstB.Compare) {
    tmp = Rte_IRead_Runnable_Step_TPS_Seconday_Value();
  } else {
    tmp = Rte_IRead_Runnable_Step_TPS_Primary_Value();
  }

  /* End of Switch: '<S1>/Switch' */
  /* End of Outputs for SubSystem: '<Root>/Runnable_Step_sys' */

  /* Outport: '<Root>/TPS_Percent_Value' */
  Rte_IWrite_Runnable_Step_TPS_Percent_Value(tmp);
}

/* Model initialize function */
void ThrottlePositionMonitor_Init(void)
{
  /* (no initialization code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
