/*
 * File: autosar_swc_expfcns.c
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

#include "autosar_swc_expfcns.h"
#ifndef PORTABLE_WORDSIZES
#ifndef UCHAR_MAX
#include <limits.h>
#endif

#if ( UCHAR_MAX != (0xFFU) ) || ( SCHAR_MAX != (0x7F) )
#error Code was generated for compiler with different sized uchar/char. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if ( USHRT_MAX != (0xFFFFU) ) || ( SHRT_MAX != (0x7FFF) )
#error Code was generated for compiler with different sized ushort/short. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if ( UINT_MAX != (0xFFFFFFFFU) ) || ( INT_MAX != (0x7FFFFFFF) )
#error Code was generated for compiler with different sized uint/int. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if ( ULONG_MAX != (0xFFFFFFFFU) ) || ( LONG_MAX != (0x7FFFFFFF) )
#error Code was generated for compiler with different sized ulong/long. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

/* Skipping ulong_long/long_long check: insufficient preprocessor integer range. */
#endif                                 /* PORTABLE_WORDSIZES */

/* Block signals (default storage) */
BlockIO rtB;

/* Block states (default storage) */
D_Work rtDWork;

/* Model step function for TID1 */
void Runnable1(void)                   /* Explicit Task: Runnable1 */
{
  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' incorporates:
   *  SubSystem: '<Root>/Runnable1_subsystem'
   */
  /* Outport: '<Root>/PPort_DE1' incorporates:
   *  UnitDelay: '<S1>/Delay'
   */
  Rte_IWrite_Runnable1_PPort_DE1(rtDWork.Delay_DSTATE_a);

  /* Gain: '<S1>/Gain' incorporates:
   *  UnitDelay: '<S1>/Delay'
   */
  rtDWork.Delay_DSTATE_a = (sint8)-rtDWork.Delay_DSTATE_a;

  /* Outputs for Enabled SubSystem: '<S1>/Subsystem' incorporates:
   *  EnablePort: '<S4>/Enable'
   */
  /* RelationalOperator: '<S1>/Data Valid' incorporates:
   *  Inport: '<Root>/RPort_DE1_ErrorStatus'
   */
  if (Rte_IStatus_Runnable1_RPort_DE1() == 0) {
    /* Sum: '<S4>/Add' incorporates:
     *  DataTransferBlock generated from: '<Root>/Runnable3_subsystem'
     *  Inport: '<Root>/RPort_DE1'
     */
    rtB.Add = Rte_IRead_Runnable1_RPort_DE1() + (float64)
      Rte_IrvIRead_Runnable1_IRV3();
  }

  /* End of RelationalOperator: '<S1>/Data Valid' */
  /* End of Outputs for SubSystem: '<S1>/Subsystem' */
  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' incorporates:
   *  SubSystem: '<Root>/Runnable1_subsystem'
   */
  /* DataTransferBlock generated from: '<Root>/Runnable1_subsystem' incorporates:
   *  SignalConversion generated from: '<S1>/Adder'
   */
  Rte_IrvIWrite_Runnable1_IRV1(rtB.Add);

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */
}

/* Model step function for TID2 */
void Runnable2(void)                   /* Explicit Task: Runnable2 */
{
  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' incorporates:
   *  SubSystem: '<Root>/Runnable2_subsystem'
   */
  /* Outport: '<Root>/PPort_DE3' incorporates:
   *  UnitDelay: '<S2>/Delay'
   */
  Rte_IWrite_Runnable2_PPort_DE3(rtDWork.Delay_DSTATE_m);

  /* Gain: '<S2>/Gain' incorporates:
   *  UnitDelay: '<S2>/Delay'
   */
  rtDWork.Delay_DSTATE_m = (sint8)-rtDWork.Delay_DSTATE_m;

  /* Outport: '<Root>/PPort_DE4' incorporates:
   *  DiscreteIntegrator: '<S2>/Discrete-Time Integrator'
   */
  Rte_IWrite_Runnable2_PPort_DE4(rtDWork.DiscreteTimeIntegrator_DSTATE);

  /* DataTransferBlock generated from: '<Root>/Runnable2_subsystem' incorporates:
   *  DiscreteIntegrator: '<S2>/Discrete-Time Integrator'
   */
  Rte_IrvIWrite_Runnable2_IRV4(rtDWork.DiscreteTimeIntegrator_DSTATE);

  /* Update for DiscreteIntegrator: '<S2>/Discrete-Time Integrator' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable1_subsystem'
   *  DataTransferBlock generated from: '<Root>/Runnable3_subsystem'
   *  Sum: '<S2>/Subtract'
   */
  rtDWork.DiscreteTimeIntegrator_DSTATE += Rte_IrvIRead_Runnable2_IRV1() -
    Rte_IrvIRead_Runnable2_IRV2();

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' */
}

/* Model step function for TID3 */
void Runnable3(void)                   /* Explicit Task: Runnable3 */
{
  const float64 *tmpIRead;
  sint8 Delay;

  /* Inport: '<Root>/RPort_DE2' */
  tmpIRead = Rte_IRead_Runnable3_RPort_DE2();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* UnitDelay: '<S3>/Delay' */
  Delay = rtDWork.Delay_DSTATE;

  /* Gain: '<S3>/Gain' incorporates:
   *  UnitDelay: '<S3>/Delay'
   */
  rtDWork.Delay_DSTATE = (sint8)-rtDWork.Delay_DSTATE;

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */

  /* DataTransferBlock generated from: '<Root>/Runnable3_subsystem' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable2_subsystem'
   *  Product: '<S3>/Product'
   */
  Rte_IrvIWrite_Runnable3_IRV2(Rte_IrvIRead_Runnable3_IRV4() * tmpIRead[0]);

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* DataTransferBlock generated from: '<Root>/Runnable3_subsystem' */
  Rte_IrvIWrite_Runnable3_IRV3(Delay);

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* Outport: '<Root>/PPort_DE2' incorporates:
   *  SignalConversion generated from: '<S3>/TicToc'
   */
  Rte_IWrite_Runnable3_PPort_DE2(Delay);

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */
}

/* Model initialize function */
void Runnable_Init(void)
{
  /* SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' incorporates:
   *  SubSystem: '<Root>/Runnable1_subsystem'
   */
  /* InitializeConditions for UnitDelay: '<S1>/Delay' */
  rtDWork.Delay_DSTATE_a = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */

  /* SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* InitializeConditions for UnitDelay: '<S3>/Delay' */
  rtDWork.Delay_DSTATE = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' incorporates:
   *  SubSystem: '<Root>/Runnable2_subsystem'
   */
  /* InitializeConditions for UnitDelay: '<S2>/Delay' */
  rtDWork.Delay_DSTATE_m = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
