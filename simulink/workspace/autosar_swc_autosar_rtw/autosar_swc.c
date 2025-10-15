/*
 * File: autosar_swc.c
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

#include "autosar_swc.h"

/* Block signals and states (default storage) */
DW rtDW;

/* Model step function for TID0 */
void Runnable_1s(void)                 /* Sample time: [1.0s, 0.0s] */
{
  float64 rtb_RateTransition;
  float64 rtb_Sum_j;

  /* RateTransition: '<Root>/Rate Transition' */
  rtb_RateTransition = Rte_IrvIRead_Runnable_1s_IRV1();

  /* Sum: '<S4>/Sum' incorporates:
   *  Gain: '<S4>/Gain'
   *  Inport: '<Root>/In1_1s'
   */
  rtb_Sum_j = 2.0 * rtb_RateTransition + Rte_IRead_Runnable_1s_In1_1s_In1_1s();

  /* Outport: '<Root>/Out1' incorporates:
   *  Gain: '<S3>/Gain'
   *  Gain: '<S3>/Gain1'
   *  Inport: '<Root>/In1_1s'
   *  Sum: '<S2>/Sum'
   *  Sum: '<S3>/Sum'
   */
  Rte_IWrite_Runnable_1s_Out1_Out1(5.0 * (Rte_IRead_Runnable_1s_In1_1s_In1_1s()
    + 3.0 * rtb_RateTransition) + rtb_Sum_j);

  /* Outport: '<Root>/Out2' */
  Rte_IWrite_Runnable_1s_Out2_Out2(rtb_Sum_j);
}

/* Model step function for TID1 */
void Runnable_2s(void)                 /* Sample time: [2.0s, 0.0s] */
{
  /* RateTransition: '<Root>/Rate Transition' incorporates:
   *  DiscreteIntegrator: '<Root>/Integrator'
   */
  Rte_IrvIWrite_Runnable_2S_IRV1(rtDW.Integrator_DSTATE);

  /* Update for DiscreteIntegrator: '<Root>/Integrator' incorporates:
   *  Inport: '<Root>/In2_2S'
   */
  rtDW.Integrator_DSTATE += 2.0 * Rte_IRead_Runnable_2S_In2_2S_In2_2S();
}

/* Model initialize function */
void test_Init(void)
{
  /* Outputs for Atomic SubSystem: '<Root>/Runable_Initialize' */
  /* StateWriter: '<S1>/State Writer' incorporates:
   *  Constant: '<S1>/Constant'
   */
  rtDW.Integrator_DSTATE = 1.0;

  /* End of Outputs for SubSystem: '<Root>/Runable_Initialize' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
