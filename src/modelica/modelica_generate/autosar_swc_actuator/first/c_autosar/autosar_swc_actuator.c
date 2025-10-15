/*
 * File: autosar_swc_actuator.c
 *
 *
 * C/C++ source code generated on : 2025-08-13 16:24:13
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "autosar_swc_actuator.h"

uint32 plook_u32f_linckan(float32 u, const float32 bp[], uint32 maxIndex)
{
  uint32 bpIndex;

  if (u <= bp[0U])
  {
    bpIndex = 0U;
  }
  else if (u < bp[maxIndex])
  {
    bpIndex = linsearch_u32f(u, bp, maxIndex >> 1U);
    if ((bpIndex < maxIndex) && (bp[bpIndex + 1U] - u <= u - bp[bpIndex]))
    {
      bpIndex++;
    }
  }
  else
  {
    bpIndex = maxIndex;
  }

  return bpIndex;
}

uint32 linsearch_u32f(float32 u, const float32 bp[], uint32 startIndex)
{
  uint32 bpIndex;

  /* Linear Search */
  for (bpIndex = startIndex; u < bp[bpIndex]; bpIndex--)
  {
  }

  while (u >= bp[bpIndex + 1U])
  {
    bpIndex++;
  }

  return bpIndex;
}

/* Model step function */
void Runnable_Step(void)
{
  Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value_3(
      (Rte_CData_HBridgeCmd_LkupTbl())
          ->Table[plook_u32f_linckan(Rte_IRead_Runnable_Step_ThrCmd_Percent_Value_4(),
                                     (Rte_CData_HBridgeCmd_LkupTbl())->BP1, 20U)]);
}

/* Model initialize function */
void ThrottlePositionActuator_Init(void) { /* (no initialization code required) */ }

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
