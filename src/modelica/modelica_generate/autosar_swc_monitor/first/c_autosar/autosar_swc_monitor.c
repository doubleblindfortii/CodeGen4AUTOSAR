/*
 * File: autosar_swc_monitor.c
 *
 *
 * C/C++ source code generated on : 2025-08-13 16:23:06
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "autosar_swc_monitor.h"

void Runnable_Step(void)
{
  float32 tmp;

  if (autosar_swc_monitor_ConstB.Compare)
  {
    tmp = Rte_IRead_Runnable_Step_TPS_Seconday_Value_6();
  }
  else
  {
    tmp = Rte_IRead_Runnable_Step_TPS_Primary_Value_6();
  }

  Rte_IWrite_Runnable_Step_TPS_Percent_Value_6(tmp);
}

/* Model initialize function */
void ThrottlePositionMonitor_Init(void) { /* (no initialization code required) */ }

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
