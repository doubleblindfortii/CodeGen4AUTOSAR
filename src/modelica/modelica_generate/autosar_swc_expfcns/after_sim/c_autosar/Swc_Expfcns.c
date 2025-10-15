/*
 * File: Swc_Expfcns.c
 *
 *
 * C/C++ source code generated on : 2025-08-13 14:30:10
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "Swc_Expfcns.h"

/*Block signals (default storage)*/
BlockIO rtB;
/* Block states (default storage)*/
D_Work rtDWork;

/*Model initialize function*/
void Runnable_Init(void)
{
  rtDWork.Delay_DSTATE = 1.0f;

  rtDWork.Delay_DSTATE_a = 1.0f;

  rtDWork.Delay_DSTATE_b = 1.0f;
}
void Runnable1(void)
{

  Rte_IWrite_Runnable1_PPort_DE_1(rtDWork.Delay_DSTATE);

  if (0 == Rte_IStatus_Runnable1_RPort_DE1())
  {

    rtB.add = 1 * Rte_IStatus_Runnable1_RPort_DE1() + 1 * Rte_IrvIRead_Runnable1_IRV3();
  }

  float64 runnable1_subsystem_adder = rtB.add * 1;

  float64 irv1_u = runnable1_subsystem_adder;

  Rte_IrvIWrite_Runnable1_IRV1(irv1_u);

  rtDWork.Delay_DSTATE = (-1) * rtDWork.Delay_DSTATE;
}

void Runnable2(void)
{

  Rte_IWrite_Runnable2_PPort_DE_3(rtDWork.Delay_DSTATE);

  Rte_IWrite_Runnable2_PPort_DE_4(rtDWork.discreteTimeIntegrator_DSTATE);
  Rte_IrvIWrite_Runnable2_IRV4(rtDWork.discreteTimeIntegrator_DSTATE);

  Double irv1_y_ = Rte_IrvIRead_Runnable2_IRV1();

  Double irv2_y_ = Rte_IrvIRead_Runnable2_IRV2();

  Double runnable2_subsystem_substract_y = 1 * irv1_y_ + (-1) - irv2_y_ * irv2_y_;

  rtDWork.Delay_DSTATE_b = (-1) * rtDWork.Delay_DSTATE_b;

  rtDWork.discreteTimeIntegrator_DSTATE += 1 * 1.0f * runnable2_subsystem_substract_y;
}

void Runnable3(void)
{

  Rte_IWrite_Runnable3_PPort_DE_2(rtDWork.Delay_DSTATE);
  Rte_IrvIWrite_Runnable3_IRV3(rtDWork.Delay_DSTATE);

  Double RPort_2_y_ = Rte_IRead_Runnable3_RPort_DE2();

  Double runnable3_subsystem_u1 = RPort_2_y_;

  Double irv4_y_ = Rte_IrvIRead_Runnable3_IRV4();

  Double runnable3_subsystem_Multiplier = irv4_y_ * runnable3_subsystem_u1;

  Double irv2_u = runnable3_subsystem_Multiplier;

  Rte_IrvIWrite_Runnable3_IRV2(irv2_u);

  rtDWork.Delay_DSTATE_a = (-1) * rtDWork.Delay_DSTATE_a;
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
