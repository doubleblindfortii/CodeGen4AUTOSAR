/*
 * File: autosar_swc_actuator.c
 *
 * Code generated for Simulink model 'autosar_swc_actuator'.
 *
 * Model version                  : 3.1
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Thu Aug  7 15:20:36 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "autosar_swc_actuator.h"
#include "autosar_swc_actuator_private.h"

uint32 plook_u32f_linckan(float32 u, const float32 bp[], uint32 maxIndex)
{
  uint32 bpIndex;

  /* Prelookup - Index only
     Index Search method: 'linear'
     Interpolation method: 'Use nearest'
     Extrapolation method: 'Clip'
     Use previous index: 'off'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  if (u <= bp[0U]) {
    bpIndex = 0U;
  } else if (u < bp[maxIndex]) {
    bpIndex = linsearch_u32f(u, bp, maxIndex >> 1U);
    if ((bpIndex < maxIndex) && (bp[bpIndex + 1U] - u <= u - bp[bpIndex])) {
      bpIndex++;
    }
  } else {
    bpIndex = maxIndex;
  }

  return bpIndex;
}

uint32 linsearch_u32f(float32 u, const float32 bp[], uint32 startIndex)
{
  uint32 bpIndex;

  /* Linear Search */
  for (bpIndex = startIndex; u < bp[bpIndex]; bpIndex--) {
  }

  while (u >= bp[bpIndex + 1U]) {
    bpIndex++;
  }

  return bpIndex;
}

/* Model step function */
void Runnable_Step(void)
{
  /* Outputs for Atomic SubSystem: '<Root>/Runnable_Step_sys' */
  /* Outport: '<Root>/ThrCmd_HwIO_Value' incorporates:
   *  Inport: '<Root>/ThrCmd_Percent_Value'
   *  Lookup_n-D: '<S1>/HBridgeDriver Lookup'
   */
  Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value((Rte_CData_HBridgeCmd_LkupTbl())
    ->Table[plook_u32f_linckan(Rte_IRead_Runnable_Step_ThrCmd_Percent_Value(),
    (Rte_CData_HBridgeCmd_LkupTbl())->BP1, 20U)]);

  /* End of Outputs for SubSystem: '<Root>/Runnable_Step_sys' */
}

/* Model initialize function */
void ThrottlePositionActuator_Init(void)
{
  /* (no initialization code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
