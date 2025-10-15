/*
 * File: autosar_swc.c
 *
 *
 * C/C++ source code generated on : 2025-08-13 12:46:42
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "autosar_swc.h"

/* Block states (default storage)*/
DW rtDW;

/*Model initialize function*/
void test_Init(void) { rtDW.pID_I_DSTATE = 1.0f; }
void Runnable_1s(void)
{

  Double irv1_1_y_ = Rte_IrvIRead_Runnable_1s_IRV1();

  Double runnableEntity_subsystem1_add_u2 = 3 * irv1_1_y_;

  Double rport_y_ = Rte_IRead_Runnable_1s_In1_1s_In1_1s();

  Double runnableEntity_subsystem1_add_y = 1 * rport_y_ + 1 * runnableEntity_subsystem1_add_u2;

  Double runnableEntity_subsystem1_y_ = 5 * runnableEntity_subsystem1_add_y;

  Double runnableEntity_subsystem1_1_gain_y = 2 * irv1_1_y_;

  Double pport1 = 1 * runnableEntity_subsystem1_1_gain_y + 1 * rport_y_;

  Rte_IWrite_Runnable_1s_Out2_Out2(pport1);

  Double pport = 1 * runnableEntity_subsystem1_y_ +
                 1 * (1 * runnableEntity_subsystem1_1_gain_y + 1 * rport_y_);

  Rte_IWrite_Runnable_1s_Out1_Out1(pport);
}

void Runnable_2s(void)
{

  Rte_IrvIWrite_Runnable_2S_IRV1(rtDW.pID_I_DSTATE);

  Double rport1_y_ = Rte_IRead_Runnable_2S_In2_2S_In2_2S();

  rtDW.pID_I_DSTATE += 2 * 1.0f * rport1_y_;
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
