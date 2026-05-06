/*
 * File: large_scale_autosar_swc_expfcns.c
 *
 * Code generated for Simulink model 'large_scale_autosar_swc_expfcns'.
 *
 * Model version                  : 4.148
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Fri Mar 20 11:44:29 2026
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "large_scale_autosar_swc_expfcns.h"
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
   *  UnitDelay: '<S20>/Delay'
   */
  Rte_IWrite_Runnable1_PPort_DE1(rtDWork.Delay_DSTATE_a);

  /* Gain: '<S20>/Gain' incorporates:
   *  UnitDelay: '<S20>/Delay'
   */
  rtDWork.Delay_DSTATE_a = (sint8)-rtDWork.Delay_DSTATE_a;

  /* Outputs for Enabled SubSystem: '<S20>/Subsystem' incorporates:
   *  EnablePort: '<S109>/Enable'
   */
  /* RelationalOperator: '<S20>/Data Valid' incorporates:
   *  Inport: '<Root>/RPort_DE1_ErrorStatus'
   */
  if (Rte_IStatus_Runnable1_RPort_DE1() == 0) {
    /* Sum: '<S109>/Add' incorporates:
     *  DataTransferBlock generated from: '<Root>/Runnable3_subsystem'
     *  Inport: '<Root>/RPort_DE1'
     */
    rtB.Add = Rte_IRead_Runnable1_RPort_DE1() + (float64)
      Rte_IrvIRead_Runnable1_IRV3();
  }

  /* End of RelationalOperator: '<S20>/Data Valid' */
  /* End of Outputs for SubSystem: '<S20>/Subsystem' */
  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' incorporates:
   *  SubSystem: '<Root>/Runnable1_subsystem'
   */
  /* DataTransferBlock generated from: '<Root>/Runnable1_subsystem' incorporates:
   *  SignalConversion generated from: '<S20>/Adder'
   */
  Rte_IrvIWrite_Runnable1_IRV1(rtB.Add);

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */
}

/* Model step function for TID2 */
void Runnable2(void)                   /* Explicit Task: Runnable2 */
{
  sint8 Delay_a[2];

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' incorporates:
   *  SubSystem: '<Root>/Runnable2_subsystem'
   */
  /* UnitDelay: '<S31>/Delay' */
  Delay_a[0] = rtDWork.Delay_DSTATE_m[0];

  /* Gain: '<S31>/Gain' incorporates:
   *  UnitDelay: '<S31>/Delay'
   */
  rtDWork.Delay_DSTATE_m[0] = (sint8)-rtDWork.Delay_DSTATE_m[0];

  /* UnitDelay: '<S31>/Delay' */
  Delay_a[1] = rtDWork.Delay_DSTATE_m[1];

  /* Gain: '<S31>/Gain' incorporates:
   *  UnitDelay: '<S31>/Delay'
   */
  rtDWork.Delay_DSTATE_m[1] = (sint8)-rtDWork.Delay_DSTATE_m[1];

  /* Outport: '<Root>/PPort_DE4' incorporates:
   *  DiscreteIntegrator: '<S31>/Discrete-Time Integrator'
   */
  Rte_IWrite_Runnable2_PPort_DE4(rtDWork.DiscreteTimeIntegrator_DSTATE);

  /* DataTransferBlock generated from: '<Root>/Runnable2_subsystem' incorporates:
   *  DiscreteIntegrator: '<S31>/Discrete-Time Integrator'
   */
  Rte_IrvIWrite_Runnable2_IRV4(rtDWork.DiscreteTimeIntegrator_DSTATE);

  /* Update for DiscreteIntegrator: '<S31>/Discrete-Time Integrator' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable1_subsystem'
   *  DataTransferBlock generated from: '<Root>/Runnable3_subsystem'
   *  Sum: '<S31>/Subtract'
   */
  rtDWork.DiscreteTimeIntegrator_DSTATE += Rte_IrvIRead_Runnable2_IRV1() -
    Rte_IrvIRead_Runnable2_IRV2();

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' */

  /* DataTransferBlock generated from: '<Root>/Runnable2_subsystem' */
  Rte_IrvIWrite_Runnable2_IRV5(Delay_a);

  /* Outport: '<Root>/PPort_DE3' */
  Rte_IWrite_Runnable2_PPort_DE3(Delay_a);
}

/* Model step function for TID3 */
void Runnable4(void)                   /* Explicit Task: Runnable4 */
{
  sint8 gain_je[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable2_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable4_IRV5();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable4' incorporates:
   *  SubSystem: '<Root>/Runnable4_subsystem'
   */
  /* Gain: '<S53>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable2_subsystem'
   */
  gain_je[0] = (sint8)-tmpIrvIRead[0];
  gain_je[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable4' */

  /* DataTransferBlock generated from: '<Root>/Runnable4_subsystem' */
  Rte_IrvIWrite_Runnable4_IRV6(gain_je);

  /* Outport: '<Root>/PPort_4_1' */
  Rte_IWrite_Runnable4_PPort_4_1_DE1(gain_je);

  /* Outport: '<Root>/PPort_4_2' */
  Rte_IWrite_Runnable4_PPort_4_2_DE1(gain_je);
}

/* Model step function for TID4 */
void Runnable5(void)                   /* Explicit Task: Runnable5 */
{
  sint8 gain_a[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable4_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable5_IRV6();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable5' incorporates:
   *  SubSystem: '<Root>/Runnable5_subsystem'
   */
  /* Gain: '<S64>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable4_subsystem'
   */
  gain_a[0] = (sint8)-tmpIrvIRead[0];
  gain_a[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable5' */

  /* DataTransferBlock generated from: '<Root>/Runnable5_subsystem' */
  Rte_IrvIWrite_Runnable5_IRV7(gain_a);

  /* Outport: '<Root>/PPort_5_1' */
  Rte_IWrite_Runnable5_PPort_5_1_DE1(gain_a);

  /* Outport: '<Root>/PPort_5_2' */
  Rte_IWrite_Runnable5_PPort_5_2_DE1(gain_a);
}

/* Model step function for TID5 */
void Runnable6(void)                   /* Explicit Task: Runnable6 */
{
  sint8 gain_h[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable5_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable6_IRV7();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable6' incorporates:
   *  SubSystem: '<Root>/Runnable6_subsystem'
   */
  /* Gain: '<S75>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable5_subsystem'
   */
  gain_h[0] = (sint8)-tmpIrvIRead[0];
  gain_h[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable6' */

  /* DataTransferBlock generated from: '<Root>/Runnable6_subsystem' */
  Rte_IrvIWrite_Runnable6_IRV8(gain_h);

  /* Outport: '<Root>/PPort_6_1' */
  Rte_IWrite_Runnable6_PPort_6_1_DE1(gain_h);

  /* Outport: '<Root>/PPort_6_2' */
  Rte_IWrite_Runnable6_PPort_6_2_DE1(gain_h);
}

/* Model step function for TID6 */
void Runnable7(void)                   /* Explicit Task: Runnable7 */
{
  sint8 gain_b[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable6_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable7_IRV8();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable7' incorporates:
   *  SubSystem: '<Root>/Runnable7_subsystem'
   */
  /* Gain: '<S86>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable6_subsystem'
   */
  gain_b[0] = (sint8)-tmpIrvIRead[0];
  gain_b[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable7' */

  /* DataTransferBlock generated from: '<Root>/Runnable7_subsystem' */
  Rte_IrvIWrite_Runnable7_IRV9(gain_b);

  /* Outport: '<Root>/PPort_7_1' */
  Rte_IWrite_Runnable7_PPort_7_1_DE1(gain_b);

  /* Outport: '<Root>/PPort_7_2' */
  Rte_IWrite_Runnable7_PPort_7_2_DE1(gain_b);
}

/* Model step function for TID7 */
void Runnable8(void)                   /* Explicit Task: Runnable8 */
{
  sint8 gain_cp[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable7_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable8_IRV9();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable8' incorporates:
   *  SubSystem: '<Root>/Runnable8_subsystem'
   */
  /* Gain: '<S97>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable7_subsystem'
   */
  gain_cp[0] = (sint8)-tmpIrvIRead[0];
  gain_cp[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable8' */

  /* DataTransferBlock generated from: '<Root>/Runnable8_subsystem' */
  Rte_IrvIWrite_Runnable8_IRV10(gain_cp);

  /* Outport: '<Root>/PPort_8_1' */
  Rte_IWrite_Runnable8_PPort_8_1_DE1(gain_cp);

  /* Outport: '<Root>/PPort_8_2' */
  Rte_IWrite_Runnable8_PPort_8_2_DE1(gain_cp);
}

/* Model step function for TID8 */
void Runnable9(void)                   /* Explicit Task: Runnable9 */
{
  sint8 gain[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable8_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable9_IRV10();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable9' incorporates:
   *  SubSystem: '<Root>/Runnable9_subsystem'
   */
  /* Gain: '<S108>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable8_subsystem'
   */
  gain[0] = (sint8)-tmpIrvIRead[0];
  gain[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable9' */

  /* DataTransferBlock generated from: '<Root>/Runnable9_subsystem' */
  Rte_IrvIWrite_Runnable9_IRV11(gain);

  /* Outport: '<Root>/PPort_9_1' */
  Rte_IWrite_Runnable9_PPort_9_1_DE1(gain);

  /* Outport: '<Root>/PPort_9_2' */
  Rte_IWrite_Runnable9_PPort_9_2_DE1(gain);
}

/* Model step function for TID9 */
void Runnable10(void)                  /* Explicit Task: Runnable10 */
{
  sint8 gain_pq[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable9_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable10_IRV11();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable10' incorporates:
   *  SubSystem: '<Root>/Runnable10_subsystem'
   */
  /* Gain: '<S10>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable9_subsystem'
   */
  gain_pq[0] = (sint8)-tmpIrvIRead[0];
  gain_pq[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable10' */

  /* DataTransferBlock generated from: '<Root>/Runnable10_subsystem' */
  Rte_IrvIWrite_Runnable10_IRV12(gain_pq);

  /* Outport: '<Root>/PPort_10_1' */
  Rte_IWrite_Runnable10_PPort_10_1_DE1(gain_pq);

  /* Outport: '<Root>/PPort_10_2' */
  Rte_IWrite_Runnable10_PPort_10_2_DE1(gain_pq);
}

/* Model step function for TID10 */
void Runnable11(void)                  /* Explicit Task: Runnable11 */
{
  sint8 gain_cdg[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable10_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable11_IRV12();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable11' incorporates:
   *  SubSystem: '<Root>/Runnable11_subsystem'
   */
  /* Gain: '<S11>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable10_subsystem'
   */
  gain_cdg[0] = (sint8)-tmpIrvIRead[0];
  gain_cdg[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable11' */

  /* DataTransferBlock generated from: '<Root>/Runnable11_subsystem' */
  Rte_IrvIWrite_Runnable11_IRV13(gain_cdg);

  /* Outport: '<Root>/PPort_11_1' */
  Rte_IWrite_Runnable11_PPort_11_1_DE1(gain_cdg);

  /* Outport: '<Root>/PPort_11_2' */
  Rte_IWrite_Runnable11_PPort_11_2_DE1(gain_cdg);
}

/* Model step function for TID11 */
void Runnable12(void)                  /* Explicit Task: Runnable12 */
{
  sint8 gain_iy[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable11_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable12_IRV13();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable12' incorporates:
   *  SubSystem: '<Root>/Runnable12_subsystem'
   */
  /* Gain: '<S12>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable11_subsystem'
   */
  gain_iy[0] = (sint8)-tmpIrvIRead[0];
  gain_iy[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable12' */

  /* DataTransferBlock generated from: '<Root>/Runnable12_subsystem' */
  Rte_IrvIWrite_Runnable12_IRV14(gain_iy);

  /* Outport: '<Root>/PPort_12_1' */
  Rte_IWrite_Runnable12_PPort_12_1_DE1(gain_iy);

  /* Outport: '<Root>/PPort_12_2' */
  Rte_IWrite_Runnable12_PPort_12_2_DE1(gain_iy);
}

/* Model step function for TID12 */
void Runnable13(void)                  /* Explicit Task: Runnable13 */
{
  sint8 gain_e2[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable12_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable13_IRV14();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable13' incorporates:
   *  SubSystem: '<Root>/Runnable13_subsystem'
   */
  /* Gain: '<S13>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable12_subsystem'
   */
  gain_e2[0] = (sint8)-tmpIrvIRead[0];
  gain_e2[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable13' */

  /* DataTransferBlock generated from: '<Root>/Runnable13_subsystem' */
  Rte_IrvIWrite_Runnable13_IRV15(gain_e2);

  /* Outport: '<Root>/PPort_13_1' */
  Rte_IWrite_Runnable13_PPort_13_1_DE1(gain_e2);

  /* Outport: '<Root>/PPort_13_2' */
  Rte_IWrite_Runnable13_PPort_13_2_DE1(gain_e2);
}

/* Model step function for TID13 */
void Runnable14(void)                  /* Explicit Task: Runnable14 */
{
  sint8 gain_mv[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable13_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable14_IRV15();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable14' incorporates:
   *  SubSystem: '<Root>/Runnable14_subsystem'
   */
  /* Gain: '<S14>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable13_subsystem'
   */
  gain_mv[0] = (sint8)-tmpIrvIRead[0];
  gain_mv[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable14' */

  /* DataTransferBlock generated from: '<Root>/Runnable14_subsystem' */
  Rte_IrvIWrite_Runnable14_IRV16(gain_mv);

  /* Outport: '<Root>/PPort_14_1' */
  Rte_IWrite_Runnable14_PPort_14_1_DE1(gain_mv);

  /* Outport: '<Root>/PPort_14_2' */
  Rte_IWrite_Runnable14_PPort_14_2_DE1(gain_mv);
}

/* Model step function for TID14 */
void Runnable15(void)                  /* Explicit Task: Runnable15 */
{
  sint8 gain_n5[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable14_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable15_IRV16();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable15' incorporates:
   *  SubSystem: '<Root>/Runnable15_subsystem'
   */
  /* Gain: '<S15>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable14_subsystem'
   */
  gain_n5[0] = (sint8)-tmpIrvIRead[0];
  gain_n5[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable15' */

  /* DataTransferBlock generated from: '<Root>/Runnable15_subsystem' */
  Rte_IrvIWrite_Runnable15_IRV17(gain_n5);

  /* Outport: '<Root>/PPort_15_1' */
  Rte_IWrite_Runnable15_PPort_15_1_DE1(gain_n5);

  /* Outport: '<Root>/PPort_15_2' */
  Rte_IWrite_Runnable15_PPort_15_2_DE1(gain_n5);
}

/* Model step function for TID15 */
void Runnable16(void)                  /* Explicit Task: Runnable16 */
{
  sint8 gain_ft[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable15_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable16_IRV17();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable16' incorporates:
   *  SubSystem: '<Root>/Runnable16_subsystem'
   */
  /* Gain: '<S16>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable15_subsystem'
   */
  gain_ft[0] = (sint8)-tmpIrvIRead[0];
  gain_ft[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable16' */

  /* DataTransferBlock generated from: '<Root>/Runnable16_subsystem' */
  Rte_IrvIWrite_Runnable16_IRV18(gain_ft);

  /* Outport: '<Root>/PPort_16_1' */
  Rte_IWrite_Runnable16_PPort_16_1_DE1(gain_ft);

  /* Outport: '<Root>/PPort_16_2' */
  Rte_IWrite_Runnable16_PPort_16_2_DE1(gain_ft);
}

/* Model step function for TID16 */
void Runnable17(void)                  /* Explicit Task: Runnable17 */
{
  sint8 gain_fi[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable16_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable17_IRV18();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable17' incorporates:
   *  SubSystem: '<Root>/Runnable17_subsystem'
   */
  /* Gain: '<S17>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable16_subsystem'
   */
  gain_fi[0] = (sint8)-tmpIrvIRead[0];
  gain_fi[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable17' */

  /* DataTransferBlock generated from: '<Root>/Runnable17_subsystem' */
  Rte_IrvIWrite_Runnable17_IRV19(gain_fi);

  /* Outport: '<Root>/PPort_17_1' */
  Rte_IWrite_Runnable17_PPort_17_1_DE1(gain_fi);

  /* Outport: '<Root>/PPort_17_2' */
  Rte_IWrite_Runnable17_PPort_17_2_DE1(gain_fi);
}

/* Model step function for TID17 */
void Runnable18(void)                  /* Explicit Task: Runnable18 */
{
  sint8 gain_c1[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable17_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable18_IRV19();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable18' incorporates:
   *  SubSystem: '<Root>/Runnable18_subsystem'
   */
  /* Gain: '<S18>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable17_subsystem'
   */
  gain_c1[0] = (sint8)-tmpIrvIRead[0];
  gain_c1[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable18' */

  /* DataTransferBlock generated from: '<Root>/Runnable18_subsystem' */
  Rte_IrvIWrite_Runnable18_IRV20(gain_c1);

  /* Outport: '<Root>/PPort_18_1' */
  Rte_IWrite_Runnable18_PPort_18_1_DE1(gain_c1);

  /* Outport: '<Root>/PPort_18_2' */
  Rte_IWrite_Runnable18_PPort_18_2_DE1(gain_c1);
}

/* Model step function for TID18 */
void Runnable19(void)                  /* Explicit Task: Runnable19 */
{
  sint8 gain_gx[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable18_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable19_IRV20();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable19' incorporates:
   *  SubSystem: '<Root>/Runnable19_subsystem'
   */
  /* Gain: '<S19>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable18_subsystem'
   */
  gain_gx[0] = (sint8)-tmpIrvIRead[0];
  gain_gx[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable19' */

  /* DataTransferBlock generated from: '<Root>/Runnable19_subsystem' */
  Rte_IrvIWrite_Runnable19_IRV21(gain_gx);

  /* Outport: '<Root>/PPort_19_1' */
  Rte_IWrite_Runnable19_PPort_19_1_DE1(gain_gx);

  /* Outport: '<Root>/PPort_19_2' */
  Rte_IWrite_Runnable19_PPort_19_2_DE1(gain_gx);
}

/* Model step function for TID19 */
void Runnable20(void)                  /* Explicit Task: Runnable20 */
{
  sint8 gain_hg[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable19_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable20_IRV21();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable20' incorporates:
   *  SubSystem: '<Root>/Runnable20_subsystem'
   */
  /* Gain: '<S21>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable19_subsystem'
   */
  gain_hg[0] = (sint8)-tmpIrvIRead[0];
  gain_hg[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable20' */

  /* DataTransferBlock generated from: '<Root>/Runnable20_subsystem' */
  Rte_IrvIWrite_Runnable20_IRV22(gain_hg);

  /* Outport: '<Root>/PPort_20_1' */
  Rte_IWrite_Runnable20_PPort_20_1_DE1(gain_hg);

  /* Outport: '<Root>/PPort_20_2' */
  Rte_IWrite_Runnable20_PPort_20_2_DE1(gain_hg);
}

/* Model step function for TID20 */
void Runnable21(void)                  /* Explicit Task: Runnable21 */
{
  sint8 gain_d4[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable20_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable21_IRV22();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable21' incorporates:
   *  SubSystem: '<Root>/Runnable21_subsystem'
   */
  /* Gain: '<S22>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable20_subsystem'
   */
  gain_d4[0] = (sint8)-tmpIrvIRead[0];
  gain_d4[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable21' */

  /* DataTransferBlock generated from: '<Root>/Runnable21_subsystem' */
  Rte_IrvIWrite_Runnable21_IRV23(gain_d4);

  /* Outport: '<Root>/PPort_21_1' */
  Rte_IWrite_Runnable21_PPort_21_1_DE1(gain_d4);

  /* Outport: '<Root>/PPort_21_2' */
  Rte_IWrite_Runnable21_PPort_21_2_DE1(gain_d4);
}

/* Model step function for TID21 */
void Runnable22(void)                  /* Explicit Task: Runnable22 */
{
  sint8 gain_dq[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable21_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable22_IRV23();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable22' incorporates:
   *  SubSystem: '<Root>/Runnable22_subsystem'
   */
  /* Gain: '<S23>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable21_subsystem'
   */
  gain_dq[0] = (sint8)-tmpIrvIRead[0];
  gain_dq[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable22' */

  /* DataTransferBlock generated from: '<Root>/Runnable22_subsystem' */
  Rte_IrvIWrite_Runnable22_IRV24(gain_dq);

  /* Outport: '<Root>/PPort_22_1' */
  Rte_IWrite_Runnable22_PPort_22_1_DE1(gain_dq);

  /* Outport: '<Root>/PPort_22_2' */
  Rte_IWrite_Runnable22_PPort_22_2_DE1(gain_dq);
}

/* Model step function for TID22 */
void Runnable23(void)                  /* Explicit Task: Runnable23 */
{
  sint8 gain_c3[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable22_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable23_IRV24();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable23' incorporates:
   *  SubSystem: '<Root>/Runnable23_subsystem'
   */
  /* Gain: '<S24>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable22_subsystem'
   */
  gain_c3[0] = (sint8)-tmpIrvIRead[0];
  gain_c3[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable23' */

  /* DataTransferBlock generated from: '<Root>/Runnable23_subsystem' */
  Rte_IrvIWrite_Runnable23_IRV25(gain_c3);

  /* Outport: '<Root>/PPort_23_1' */
  Rte_IWrite_Runnable23_PPort_23_1_DE1(gain_c3);

  /* Outport: '<Root>/PPort_23_2' */
  Rte_IWrite_Runnable23_PPort_23_2_DE1(gain_c3);
}

/* Model step function for TID23 */
void Runnable24(void)                  /* Explicit Task: Runnable24 */
{
  sint8 gain_ac[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable23_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable24_IRV25();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable24' incorporates:
   *  SubSystem: '<Root>/Runnable24_subsystem'
   */
  /* Gain: '<S25>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable23_subsystem'
   */
  gain_ac[0] = (sint8)-tmpIrvIRead[0];
  gain_ac[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable24' */

  /* DataTransferBlock generated from: '<Root>/Runnable24_subsystem' */
  Rte_IrvIWrite_Runnable24_IRV26(gain_ac);

  /* Outport: '<Root>/PPort_24_1' */
  Rte_IWrite_Runnable24_PPort_24_1_DE1(gain_ac);

  /* Outport: '<Root>/PPort_24_2' */
  Rte_IWrite_Runnable24_PPort_24_2_DE1(gain_ac);
}

/* Model step function for TID24 */
void Runnable25(void)                  /* Explicit Task: Runnable25 */
{
  sint8 gain_h3[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable24_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable25_IRV26();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable25' incorporates:
   *  SubSystem: '<Root>/Runnable25_subsystem'
   */
  /* Gain: '<S26>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable24_subsystem'
   */
  gain_h3[0] = (sint8)-tmpIrvIRead[0];
  gain_h3[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable25' */

  /* DataTransferBlock generated from: '<Root>/Runnable25_subsystem' */
  Rte_IrvIWrite_Runnable25_IRV27(gain_h3);

  /* Outport: '<Root>/PPort_25_1' */
  Rte_IWrite_Runnable25_PPort_25_1_DE1(gain_h3);

  /* Outport: '<Root>/PPort_25_2' */
  Rte_IWrite_Runnable25_PPort_25_2_DE1(gain_h3);
}

/* Model step function for TID25 */
void Runnable26(void)                  /* Explicit Task: Runnable26 */
{
  sint8 gain_od[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable25_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable26_IRV27();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable26' incorporates:
   *  SubSystem: '<Root>/Runnable26_subsystem'
   */
  /* Gain: '<S27>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable25_subsystem'
   */
  gain_od[0] = (sint8)-tmpIrvIRead[0];
  gain_od[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable26' */

  /* DataTransferBlock generated from: '<Root>/Runnable26_subsystem' */
  Rte_IrvIWrite_Runnable26_IRV28(gain_od);

  /* Outport: '<Root>/PPort_26_1' */
  Rte_IWrite_Runnable26_PPort_26_1_DE1(gain_od);

  /* Outport: '<Root>/PPort_26_2' */
  Rte_IWrite_Runnable26_PPort_26_2_DE1(gain_od);
}

/* Model step function for TID26 */
void Runnable27(void)                  /* Explicit Task: Runnable27 */
{
  sint8 gain_nj[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable26_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable27_IRV28();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable27' incorporates:
   *  SubSystem: '<Root>/Runnable27_subsystem'
   */
  /* Gain: '<S28>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable26_subsystem'
   */
  gain_nj[0] = (sint8)-tmpIrvIRead[0];
  gain_nj[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable27' */

  /* DataTransferBlock generated from: '<Root>/Runnable27_subsystem' */
  Rte_IrvIWrite_Runnable27_IRV29(gain_nj);

  /* Outport: '<Root>/PPort_27_1' */
  Rte_IWrite_Runnable27_PPort_27_1_DE1(gain_nj);

  /* Outport: '<Root>/PPort_27_2' */
  Rte_IWrite_Runnable27_PPort_27_2_DE1(gain_nj);
}

/* Model step function for TID27 */
void Runnable28(void)                  /* Explicit Task: Runnable28 */
{
  sint8 gain_bc[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable27_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable28_IRV29();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable28' incorporates:
   *  SubSystem: '<Root>/Runnable28_subsystem'
   */
  /* Gain: '<S29>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable27_subsystem'
   */
  gain_bc[0] = (sint8)-tmpIrvIRead[0];
  gain_bc[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable28' */

  /* DataTransferBlock generated from: '<Root>/Runnable28_subsystem' */
  Rte_IrvIWrite_Runnable28_IRV30(gain_bc);

  /* Outport: '<Root>/PPort_28_1' */
  Rte_IWrite_Runnable28_PPort_28_1_DE1(gain_bc);

  /* Outport: '<Root>/PPort_28_2' */
  Rte_IWrite_Runnable28_PPort_28_2_DE1(gain_bc);
}

/* Model step function for TID28 */
void Runnable29(void)                  /* Explicit Task: Runnable29 */
{
  sint8 gain_da[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable28_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable29_IRV30();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable29' incorporates:
   *  SubSystem: '<Root>/Runnable29_subsystem'
   */
  /* Gain: '<S30>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable28_subsystem'
   */
  gain_da[0] = (sint8)-tmpIrvIRead[0];
  gain_da[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable29' */

  /* DataTransferBlock generated from: '<Root>/Runnable29_subsystem' */
  Rte_IrvIWrite_Runnable29_IRV31(gain_da);

  /* Outport: '<Root>/PPort_29_1' */
  Rte_IWrite_Runnable29_PPort_29_1_DE1(gain_da);

  /* Outport: '<Root>/PPort_29_2' */
  Rte_IWrite_Runnable29_PPort_29_2_DE1(gain_da);
}

/* Model step function for TID29 */
void Runnable30(void)                  /* Explicit Task: Runnable30 */
{
  sint8 gain_g5[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable29_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable30_IRV31();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable30' incorporates:
   *  SubSystem: '<Root>/Runnable30_subsystem'
   */
  /* Gain: '<S32>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable29_subsystem'
   */
  gain_g5[0] = (sint8)-tmpIrvIRead[0];
  gain_g5[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable30' */

  /* DataTransferBlock generated from: '<Root>/Runnable30_subsystem' */
  Rte_IrvIWrite_Runnable30_IRV32(gain_g5);

  /* Outport: '<Root>/PPort_30_1' */
  Rte_IWrite_Runnable30_PPort_30_1_DE1(gain_g5);

  /* Outport: '<Root>/PPort_30_2' */
  Rte_IWrite_Runnable30_PPort_30_2_DE1(gain_g5);
}

/* Model step function for TID30 */
void Runnable31(void)                  /* Explicit Task: Runnable31 */
{
  sint8 gain_kp[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable30_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable31_IRV32();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable31' incorporates:
   *  SubSystem: '<Root>/Runnable31_subsystem'
   */
  /* Gain: '<S33>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable30_subsystem'
   */
  gain_kp[0] = (sint8)-tmpIrvIRead[0];
  gain_kp[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable31' */

  /* DataTransferBlock generated from: '<Root>/Runnable31_subsystem' */
  Rte_IrvIWrite_Runnable31_IRV33(gain_kp);

  /* Outport: '<Root>/PPort_31_1' */
  Rte_IWrite_Runnable31_PPort_31_1_DE1(gain_kp);

  /* Outport: '<Root>/PPort_31_2' */
  Rte_IWrite_Runnable31_PPort_31_2_DE1(gain_kp);
}

/* Model step function for TID31 */
void Runnable32(void)                  /* Explicit Task: Runnable32 */
{
  sint8 gain_m2[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable31_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable32_IRV33();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable32' incorporates:
   *  SubSystem: '<Root>/Runnable32_subsystem'
   */
  /* Gain: '<S34>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable31_subsystem'
   */
  gain_m2[0] = (sint8)-tmpIrvIRead[0];
  gain_m2[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable32' */

  /* DataTransferBlock generated from: '<Root>/Runnable32_subsystem' */
  Rte_IrvIWrite_Runnable32_IRV34(gain_m2);

  /* Outport: '<Root>/PPort_32_1' */
  Rte_IWrite_Runnable32_PPort_32_1_DE1(gain_m2);

  /* Outport: '<Root>/PPort_32_2' */
  Rte_IWrite_Runnable32_PPort_32_2_DE1(gain_m2);
}

/* Model step function for TID32 */
void Runnable33(void)                  /* Explicit Task: Runnable33 */
{
  sint8 gain_ol[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable32_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable33_IRV34();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable33' incorporates:
   *  SubSystem: '<Root>/Runnable33_subsystem'
   */
  /* Gain: '<S35>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable32_subsystem'
   */
  gain_ol[0] = (sint8)-tmpIrvIRead[0];
  gain_ol[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable33' */

  /* DataTransferBlock generated from: '<Root>/Runnable33_subsystem' */
  Rte_IrvIWrite_Runnable33_IRV35(gain_ol);

  /* Outport: '<Root>/PPort_33_1' */
  Rte_IWrite_Runnable33_PPort_33_1_DE1(gain_ol);

  /* Outport: '<Root>/PPort_33_2' */
  Rte_IWrite_Runnable33_PPort_33_2_DE1(gain_ol);
}

/* Model step function for TID33 */
void Runnable34(void)                  /* Explicit Task: Runnable34 */
{
  sint8 gain_p2[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable33_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable34_IRV35();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable34' incorporates:
   *  SubSystem: '<Root>/Runnable34_subsystem'
   */
  /* Gain: '<S36>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable33_subsystem'
   */
  gain_p2[0] = (sint8)-tmpIrvIRead[0];
  gain_p2[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable34' */

  /* DataTransferBlock generated from: '<Root>/Runnable34_subsystem' */
  Rte_IrvIWrite_Runnable34_IRV36(gain_p2);

  /* Outport: '<Root>/PPort_34_1' */
  Rte_IWrite_Runnable34_PPort_34_1_DE1(gain_p2);

  /* Outport: '<Root>/PPort_34_2' */
  Rte_IWrite_Runnable34_PPort_34_2_DE1(gain_p2);
}

/* Model step function for TID34 */
void Runnable35(void)                  /* Explicit Task: Runnable35 */
{
  sint8 gain_lx[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable34_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable35_IRV36();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable35' incorporates:
   *  SubSystem: '<Root>/Runnable35_subsystem'
   */
  /* Gain: '<S37>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable34_subsystem'
   */
  gain_lx[0] = (sint8)-tmpIrvIRead[0];
  gain_lx[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable35' */

  /* DataTransferBlock generated from: '<Root>/Runnable35_subsystem' */
  Rte_IrvIWrite_Runnable35_IRV37(gain_lx);

  /* Outport: '<Root>/PPort_35_1' */
  Rte_IWrite_Runnable35_PPort_35_1_DE1(gain_lx);

  /* Outport: '<Root>/PPort_35_2' */
  Rte_IWrite_Runnable35_PPort_35_2_DE1(gain_lx);
}

/* Model step function for TID35 */
void Runnable36(void)                  /* Explicit Task: Runnable36 */
{
  sint8 gain_m3[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable35_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable36_IRV37();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable36' incorporates:
   *  SubSystem: '<Root>/Runnable36_subsystem'
   */
  /* Gain: '<S38>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable35_subsystem'
   */
  gain_m3[0] = (sint8)-tmpIrvIRead[0];
  gain_m3[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable36' */

  /* DataTransferBlock generated from: '<Root>/Runnable36_subsystem' */
  Rte_IrvIWrite_Runnable36_IRV38(gain_m3);

  /* Outport: '<Root>/PPort_36_1' */
  Rte_IWrite_Runnable36_PPort_36_1_DE1(gain_m3);

  /* Outport: '<Root>/PPort_36_2' */
  Rte_IWrite_Runnable36_PPort_36_2_DE1(gain_m3);
}

/* Model step function for TID36 */
void Runnable37(void)                  /* Explicit Task: Runnable37 */
{
  sint8 gain_pp[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable36_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable37_IRV38();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable37' incorporates:
   *  SubSystem: '<Root>/Runnable37_subsystem'
   */
  /* Gain: '<S39>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable36_subsystem'
   */
  gain_pp[0] = (sint8)-tmpIrvIRead[0];
  gain_pp[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable37' */

  /* DataTransferBlock generated from: '<Root>/Runnable37_subsystem' */
  Rte_IrvIWrite_Runnable37_IRV39(gain_pp);

  /* Outport: '<Root>/PPort_37_1' */
  Rte_IWrite_Runnable37_PPort_37_1_DE1(gain_pp);

  /* Outport: '<Root>/PPort_37_2' */
  Rte_IWrite_Runnable37_PPort_37_2_DE1(gain_pp);
}

/* Model step function for TID37 */
void Runnable38(void)                  /* Explicit Task: Runnable38 */
{
  sint8 gain_h5[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable37_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable38_IRV39();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable38' incorporates:
   *  SubSystem: '<Root>/Runnable38_subsystem'
   */
  /* Gain: '<S40>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable37_subsystem'
   */
  gain_h5[0] = (sint8)-tmpIrvIRead[0];
  gain_h5[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable38' */

  /* DataTransferBlock generated from: '<Root>/Runnable38_subsystem' */
  Rte_IrvIWrite_Runnable38_IRV40(gain_h5);

  /* Outport: '<Root>/PPort_38_1' */
  Rte_IWrite_Runnable38_PPort_38_1_DE1(gain_h5);

  /* Outport: '<Root>/PPort_38_2' */
  Rte_IWrite_Runnable38_PPort_38_2_DE1(gain_h5);
}

/* Model step function for TID38 */
void Runnable39(void)                  /* Explicit Task: Runnable39 */
{
  sint8 gain_cd[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable38_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable39_IRV40();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable39' incorporates:
   *  SubSystem: '<Root>/Runnable39_subsystem'
   */
  /* Gain: '<S41>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable38_subsystem'
   */
  gain_cd[0] = (sint8)-tmpIrvIRead[0];
  gain_cd[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable39' */

  /* DataTransferBlock generated from: '<Root>/Runnable39_subsystem' */
  Rte_IrvIWrite_Runnable39_IRV41(gain_cd);

  /* Outport: '<Root>/PPort_39_1' */
  Rte_IWrite_Runnable39_PPort_39_1_DE1(gain_cd);

  /* Outport: '<Root>/PPort_39_2' */
  Rte_IWrite_Runnable39_PPort_39_2_DE1(gain_cd);
}

/* Model step function for TID39 */
void Runnable40(void)                  /* Explicit Task: Runnable40 */
{
  sint8 gain_cy[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable39_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable40_IRV41();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable40' incorporates:
   *  SubSystem: '<Root>/Runnable40_subsystem'
   */
  /* Gain: '<S43>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable39_subsystem'
   */
  gain_cy[0] = (sint8)-tmpIrvIRead[0];
  gain_cy[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable40' */

  /* DataTransferBlock generated from: '<Root>/Runnable40_subsystem' */
  Rte_IrvIWrite_Runnable40_IRV42(gain_cy);

  /* Outport: '<Root>/PPort_40_1' */
  Rte_IWrite_Runnable40_PPort_40_1_DE1(gain_cy);

  /* Outport: '<Root>/PPort_40_2' */
  Rte_IWrite_Runnable40_PPort_40_2_DE1(gain_cy);
}

/* Model step function for TID40 */
void Runnable41(void)                  /* Explicit Task: Runnable41 */
{
  sint8 gain_bf[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable40_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable41_IRV42();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable41' incorporates:
   *  SubSystem: '<Root>/Runnable41_subsystem'
   */
  /* Gain: '<S44>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable40_subsystem'
   */
  gain_bf[0] = (sint8)-tmpIrvIRead[0];
  gain_bf[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable41' */

  /* DataTransferBlock generated from: '<Root>/Runnable41_subsystem' */
  Rte_IrvIWrite_Runnable41_IRV43(gain_bf);

  /* Outport: '<Root>/PPort_41_1' */
  Rte_IWrite_Runnable41_PPort_41_1_DE1(gain_bf);

  /* Outport: '<Root>/PPort_41_2' */
  Rte_IWrite_Runnable41_PPort_41_2_DE1(gain_bf);
}

/* Model step function for TID41 */
void Runnable42(void)                  /* Explicit Task: Runnable42 */
{
  sint8 gain_ea[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable41_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable42_IRV43();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable42' incorporates:
   *  SubSystem: '<Root>/Runnable42_subsystem'
   */
  /* Gain: '<S45>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable41_subsystem'
   */
  gain_ea[0] = (sint8)-tmpIrvIRead[0];
  gain_ea[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable42' */

  /* DataTransferBlock generated from: '<Root>/Runnable42_subsystem' */
  Rte_IrvIWrite_Runnable42_IRV44(gain_ea);

  /* Outport: '<Root>/PPort_42_1' */
  Rte_IWrite_Runnable42_PPort_42_1_DE1(gain_ea);

  /* Outport: '<Root>/PPort_42_2' */
  Rte_IWrite_Runnable42_PPort_42_2_DE1(gain_ea);
}

/* Model step function for TID42 */
void Runnable43(void)                  /* Explicit Task: Runnable43 */
{
  sint8 gain_gy[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable42_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable43_IRV44();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable43' incorporates:
   *  SubSystem: '<Root>/Runnable43_subsystem'
   */
  /* Gain: '<S46>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable42_subsystem'
   */
  gain_gy[0] = (sint8)-tmpIrvIRead[0];
  gain_gy[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable43' */

  /* DataTransferBlock generated from: '<Root>/Runnable43_subsystem' */
  Rte_IrvIWrite_Runnable43_IRV45(gain_gy);

  /* Outport: '<Root>/PPort_43_1' */
  Rte_IWrite_Runnable43_PPort_43_1_DE1(gain_gy);

  /* Outport: '<Root>/PPort_43_2' */
  Rte_IWrite_Runnable43_PPort_43_2_DE1(gain_gy);
}

/* Model step function for TID43 */
void Runnable44(void)                  /* Explicit Task: Runnable44 */
{
  sint8 gain_f1[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable43_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable44_IRV45();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable44' incorporates:
   *  SubSystem: '<Root>/Runnable44_subsystem1'
   */
  /* Gain: '<S47>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable43_subsystem'
   */
  gain_f1[0] = (sint8)-tmpIrvIRead[0];
  gain_f1[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable44' */

  /* DataTransferBlock generated from: '<Root>/Runnable44_subsystem1' */
  Rte_IrvIWrite_Runnable44_IRV46(gain_f1);

  /* Outport: '<Root>/PPort_44_1' */
  Rte_IWrite_Runnable44_PPort_44_1_DE1(gain_f1);

  /* Outport: '<Root>/PPort_44_2' */
  Rte_IWrite_Runnable44_PPort_44_2_DE1(gain_f1);
}

/* Model step function for TID44 */
void Runnable45(void)                  /* Explicit Task: Runnable45 */
{
  sint8 gain_jz[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable44_subsystem1' */
  tmpIrvIRead = Rte_IrvIRead_Runnable45_IRV46();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable45' incorporates:
   *  SubSystem: '<Root>/Runnable45_subsystem'
   */
  /* Gain: '<S48>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable44_subsystem1'
   */
  gain_jz[0] = (sint8)-tmpIrvIRead[0];
  gain_jz[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable45' */

  /* DataTransferBlock generated from: '<Root>/Runnable45_subsystem' */
  Rte_IrvIWrite_Runnable45_IRV47(gain_jz);

  /* Outport: '<Root>/PPort_45_1' */
  Rte_IWrite_Runnable45_PPort_45_1_DE1(gain_jz);

  /* Outport: '<Root>/PPort_45_2' */
  Rte_IWrite_Runnable45_PPort_45_2_DE1(gain_jz);
}

/* Model step function for TID45 */
void Runnable46(void)                  /* Explicit Task: Runnable46 */
{
  sint8 gain_dm[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable45_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable46_IRV47();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable46' incorporates:
   *  SubSystem: '<Root>/Runnable46_subsystem'
   */
  /* Gain: '<S49>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable45_subsystem'
   */
  gain_dm[0] = (sint8)-tmpIrvIRead[0];
  gain_dm[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable46' */

  /* DataTransferBlock generated from: '<Root>/Runnable46_subsystem' */
  Rte_IrvIWrite_Runnable46_IRV48(gain_dm);

  /* Outport: '<Root>/PPort_46_1' */
  Rte_IWrite_Runnable46_PPort_46_1_DE1(gain_dm);

  /* Outport: '<Root>/PPort_46_2' */
  Rte_IWrite_Runnable46_PPort_46_2_DE1(gain_dm);
}

/* Model step function for TID46 */
void Runnable47(void)                  /* Explicit Task: Runnable47 */
{
  sint8 gain_b5[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable46_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable47_IRV48();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable47' incorporates:
   *  SubSystem: '<Root>/Runnable47_subsystem'
   */
  /* Gain: '<S50>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable46_subsystem'
   */
  gain_b5[0] = (sint8)-tmpIrvIRead[0];
  gain_b5[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable47' */

  /* DataTransferBlock generated from: '<Root>/Runnable47_subsystem' */
  Rte_IrvIWrite_Runnable47_IRV49(gain_b5);

  /* Outport: '<Root>/PPort_47_1' */
  Rte_IWrite_Runnable47_PPort_47_1_DE1(gain_b5);

  /* Outport: '<Root>/PPort_47_2' */
  Rte_IWrite_Runnable47_PPort_47_2_DE1(gain_b5);
}

/* Model step function for TID47 */
void Runnable48(void)                  /* Explicit Task: Runnable48 */
{
  sint8 gain_pz[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable47_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable48_IRV49();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable48' incorporates:
   *  SubSystem: '<Root>/Runnable48_subsystem'
   */
  /* Gain: '<S51>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable47_subsystem'
   */
  gain_pz[0] = (sint8)-tmpIrvIRead[0];
  gain_pz[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable48' */

  /* DataTransferBlock generated from: '<Root>/Runnable48_subsystem' */
  Rte_IrvIWrite_Runnable48_IRV50(gain_pz);

  /* Outport: '<Root>/PPort_48_1' */
  Rte_IWrite_Runnable48_PPort_48_1_DE1(gain_pz);

  /* Outport: '<Root>/PPort_48_2' */
  Rte_IWrite_Runnable48_PPort_48_2_DE1(gain_pz);
}

/* Model step function for TID48 */
void Runnable49(void)                  /* Explicit Task: Runnable49 */
{
  sint8 gain_hy[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable48_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable49_IRV50();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable49' incorporates:
   *  SubSystem: '<Root>/Runnable49_subsystem'
   */
  /* Gain: '<S52>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable48_subsystem'
   */
  gain_hy[0] = (sint8)-tmpIrvIRead[0];
  gain_hy[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable49' */

  /* DataTransferBlock generated from: '<Root>/Runnable49_subsystem' */
  Rte_IrvIWrite_Runnable49_IRV51(gain_hy);

  /* Outport: '<Root>/PPort_49_1' */
  Rte_IWrite_Runnable49_PPort_49_1_DE1(gain_hy);

  /* Outport: '<Root>/PPort_49_2' */
  Rte_IWrite_Runnable49_PPort_49_2_DE1(gain_hy);
}

/* Model step function for TID49 */
void Runnable50(void)                  /* Explicit Task: Runnable50 */
{
  sint8 gain_ae[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable49_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable50_IRV51();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable50' incorporates:
   *  SubSystem: '<Root>/Runnable50_subsystem1'
   */
  /* Gain: '<S54>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable49_subsystem'
   */
  gain_ae[0] = (sint8)-tmpIrvIRead[0];
  gain_ae[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable50' */

  /* DataTransferBlock generated from: '<Root>/Runnable50_subsystem1' */
  Rte_IrvIWrite_Runnable50_IRV52(gain_ae);

  /* Outport: '<Root>/PPort_50_1' */
  Rte_IWrite_Runnable50_PPort_50_1_DE1(gain_ae);

  /* Outport: '<Root>/PPort_50_2' */
  Rte_IWrite_Runnable50_PPort_50_2_DE1(gain_ae);
}

/* Model step function for TID50 */
void Runnable51(void)                  /* Explicit Task: Runnable51 */
{
  sint8 gain_aa[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable50_subsystem1' */
  tmpIrvIRead = Rte_IrvIRead_Runnable51_IRV52();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable51' incorporates:
   *  SubSystem: '<Root>/Runnable51_subsystem2'
   */
  /* Gain: '<S55>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable50_subsystem1'
   */
  gain_aa[0] = (sint8)-tmpIrvIRead[0];
  gain_aa[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable51' */

  /* DataTransferBlock generated from: '<Root>/Runnable51_subsystem2' */
  Rte_IrvIWrite_Runnable51_IRV53(gain_aa);

  /* Outport: '<Root>/PPort_51_1' */
  Rte_IWrite_Runnable51_PPort_51_1_DE1(gain_aa);

  /* Outport: '<Root>/PPort_51_2' */
  Rte_IWrite_Runnable51_PPort_51_2_DE1(gain_aa);
}

/* Model step function for TID51 */
void Runnable52(void)                  /* Explicit Task: Runnable52 */
{
  sint8 gain_as[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable51_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable52_IRV53();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable52' incorporates:
   *  SubSystem: '<Root>/Runnable52_subsystem2'
   */
  /* Gain: '<S56>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable51_subsystem2'
   */
  gain_as[0] = (sint8)-tmpIrvIRead[0];
  gain_as[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable52' */

  /* DataTransferBlock generated from: '<Root>/Runnable52_subsystem2' */
  Rte_IrvIWrite_Runnable52_IRV54(gain_as);

  /* Outport: '<Root>/PPort_52_1' */
  Rte_IWrite_Runnable52_PPort_52_1_DE1(gain_as);

  /* Outport: '<Root>/PPort_52_2' */
  Rte_IWrite_Runnable52_PPort_52_2_DE1(gain_as);
}

/* Model step function for TID52 */
void Runnable53(void)                  /* Explicit Task: Runnable53 */
{
  sint8 gain_hh[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable52_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable53_IRV54();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable53' incorporates:
   *  SubSystem: '<Root>/Runnable53_subsystem2'
   */
  /* Gain: '<S57>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable52_subsystem2'
   */
  gain_hh[0] = (sint8)-tmpIrvIRead[0];
  gain_hh[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable53' */

  /* DataTransferBlock generated from: '<Root>/Runnable53_subsystem2' */
  Rte_IrvIWrite_Runnable53_IRV55(gain_hh);

  /* Outport: '<Root>/PPort_53_1' */
  Rte_IWrite_Runnable53_PPort_53_1_DE1(gain_hh);

  /* Outport: '<Root>/PPort_53_2' */
  Rte_IWrite_Runnable53_PPort_53_2_DE1(gain_hh);
}

/* Model step function for TID53 */
void Runnable54(void)                  /* Explicit Task: Runnable54 */
{
  sint8 gain_nl[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable53_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable54_IRV55();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable54' incorporates:
   *  SubSystem: '<Root>/Runnable54_subsystem2'
   */
  /* Gain: '<S58>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable53_subsystem2'
   */
  gain_nl[0] = (sint8)-tmpIrvIRead[0];
  gain_nl[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable54' */

  /* DataTransferBlock generated from: '<Root>/Runnable54_subsystem2' */
  Rte_IrvIWrite_Runnable54_IRV56(gain_nl);

  /* Outport: '<Root>/PPort_54_1' */
  Rte_IWrite_Runnable54_PPort_54_1_DE1(gain_nl);

  /* Outport: '<Root>/PPort_54_2' */
  Rte_IWrite_Runnable54_PPort_54_2_DE1(gain_nl);
}

/* Model step function for TID54 */
void Runnable55(void)                  /* Explicit Task: Runnable55 */
{
  sint8 gain_kk[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable54_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable55_IRV56();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable55' incorporates:
   *  SubSystem: '<Root>/Runnable55_subsystem2'
   */
  /* Gain: '<S59>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable54_subsystem2'
   */
  gain_kk[0] = (sint8)-tmpIrvIRead[0];
  gain_kk[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable55' */

  /* DataTransferBlock generated from: '<Root>/Runnable55_subsystem2' */
  Rte_IrvIWrite_Runnable55_IRV57(gain_kk);

  /* Outport: '<Root>/PPort_55_1' */
  Rte_IWrite_Runnable55_PPort_55_1_DE1(gain_kk);

  /* Outport: '<Root>/PPort_55_2' */
  Rte_IWrite_Runnable55_PPort_55_2_DE1(gain_kk);
}

/* Model step function for TID55 */
void Runnable56(void)                  /* Explicit Task: Runnable56 */
{
  sint8 gain_pg[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable55_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable56_IRV57();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable56' incorporates:
   *  SubSystem: '<Root>/Runnable56_subsystem2'
   */
  /* Gain: '<S60>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable55_subsystem2'
   */
  gain_pg[0] = (sint8)-tmpIrvIRead[0];
  gain_pg[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable56' */

  /* DataTransferBlock generated from: '<Root>/Runnable56_subsystem2' */
  Rte_IrvIWrite_Runnable56_IRV58(gain_pg);

  /* Outport: '<Root>/PPort_56_1' */
  Rte_IWrite_Runnable56_PPort_56_1_DE1(gain_pg);

  /* Outport: '<Root>/PPort_56_2' */
  Rte_IWrite_Runnable56_PPort_56_2_DE1(gain_pg);
}

/* Model step function for TID56 */
void Runnable57(void)                  /* Explicit Task: Runnable57 */
{
  sint8 gain_jf[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable56_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable57_IRV58();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable57' incorporates:
   *  SubSystem: '<Root>/Runnable57_subsystem2'
   */
  /* Gain: '<S61>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable56_subsystem2'
   */
  gain_jf[0] = (sint8)-tmpIrvIRead[0];
  gain_jf[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable57' */

  /* DataTransferBlock generated from: '<Root>/Runnable57_subsystem2' */
  Rte_IrvIWrite_Runnable57_IRV59(gain_jf);

  /* Outport: '<Root>/PPort_57_1' */
  Rte_IWrite_Runnable57_PPort_57_1_DE1(gain_jf);

  /* Outport: '<Root>/PPort_57_2' */
  Rte_IWrite_Runnable57_PPort_57_2_DE1(gain_jf);
}

/* Model step function for TID57 */
void Runnable58(void)                  /* Explicit Task: Runnable58 */
{
  sint8 gain_mw[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable57_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable58_IRV59();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable58' incorporates:
   *  SubSystem: '<Root>/Runnable58_subsystem2'
   */
  /* Gain: '<S62>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable57_subsystem2'
   */
  gain_mw[0] = (sint8)-tmpIrvIRead[0];
  gain_mw[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable58' */

  /* DataTransferBlock generated from: '<Root>/Runnable58_subsystem2' */
  Rte_IrvIWrite_Runnable58_IRV60(gain_mw);

  /* Outport: '<Root>/PPort_58_1' */
  Rte_IWrite_Runnable58_PPort_58_1_DE1(gain_mw);

  /* Outport: '<Root>/PPort_58_2' */
  Rte_IWrite_Runnable58_PPort_58_2_DE1(gain_mw);
}

/* Model step function for TID58 */
void Runnable59(void)                  /* Explicit Task: Runnable59 */
{
  sint8 gain_eh[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable58_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable59_IRV60();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable59' incorporates:
   *  SubSystem: '<Root>/Runnable59_subsystem2'
   */
  /* Gain: '<S63>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable58_subsystem2'
   */
  gain_eh[0] = (sint8)-tmpIrvIRead[0];
  gain_eh[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable59' */

  /* DataTransferBlock generated from: '<Root>/Runnable59_subsystem2' */
  Rte_IrvIWrite_Runnable59_IRV61(gain_eh);

  /* Outport: '<Root>/PPort_59_1' */
  Rte_IWrite_Runnable59_PPort_59_1_DE1(gain_eh);

  /* Outport: '<Root>/PPort_59_2' */
  Rte_IWrite_Runnable59_PPort_59_2_DE1(gain_eh);
}

/* Model step function for TID59 */
void Runnable60(void)                  /* Explicit Task: Runnable60 */
{
  sint8 gain_br[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable59_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable60_IRV61();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable60' incorporates:
   *  SubSystem: '<Root>/Runnable60_subsystem2'
   */
  /* Gain: '<S65>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable59_subsystem2'
   */
  gain_br[0] = (sint8)-tmpIrvIRead[0];
  gain_br[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable60' */

  /* DataTransferBlock generated from: '<Root>/Runnable60_subsystem2' */
  Rte_IrvIWrite_Runnable60_IRV62(gain_br);

  /* Outport: '<Root>/PPort_60_1' */
  Rte_IWrite_Runnable60_PPort_60_1_DE1(gain_br);

  /* Outport: '<Root>/PPort_60_2' */
  Rte_IWrite_Runnable60_PPort_60_2_DE1(gain_br);
}

/* Model step function for TID60 */
void Runnable61(void)                  /* Explicit Task: Runnable61 */
{
  sint8 gain_ld[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable60_subsystem2' */
  tmpIrvIRead = Rte_IrvIRead_Runnable61_IRV62();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable61' incorporates:
   *  SubSystem: '<Root>/Runnable61_subsystem'
   */
  /* Gain: '<S66>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable60_subsystem2'
   */
  gain_ld[0] = (sint8)-tmpIrvIRead[0];
  gain_ld[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable61' */

  /* DataTransferBlock generated from: '<Root>/Runnable61_subsystem' */
  Rte_IrvIWrite_Runnable61_IRV63(gain_ld);

  /* Outport: '<Root>/PPort_61_1' */
  Rte_IWrite_Runnable61_PPort_61_1_DE1(gain_ld);

  /* Outport: '<Root>/PPort_61_2' */
  Rte_IWrite_Runnable61_PPort_61_2_DE1(gain_ld);
}

/* Model step function for TID61 */
void Runnable62(void)                  /* Explicit Task: Runnable62 */
{
  sint8 gain_ik[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable61_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable62_IRV63();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable62' incorporates:
   *  SubSystem: '<Root>/Runnable62_subsystem'
   */
  /* Gain: '<S67>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable61_subsystem'
   */
  gain_ik[0] = (sint8)-tmpIrvIRead[0];
  gain_ik[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable62' */

  /* DataTransferBlock generated from: '<Root>/Runnable62_subsystem' */
  Rte_IrvIWrite_Runnable62_IRV64(gain_ik);

  /* Outport: '<Root>/PPort_62_1' */
  Rte_IWrite_Runnable62_PPort_62_1_DE1(gain_ik);

  /* Outport: '<Root>/PPort_62_2' */
  Rte_IWrite_Runnable62_PPort_62_2_DE1(gain_ik);
}

/* Model step function for TID62 */
void Runnable63(void)                  /* Explicit Task: Runnable63 */
{
  sint8 gain_oj[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable62_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable63_IRV64();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable63' incorporates:
   *  SubSystem: '<Root>/Runnable63_subsystem'
   */
  /* Gain: '<S68>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable62_subsystem'
   */
  gain_oj[0] = (sint8)-tmpIrvIRead[0];
  gain_oj[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable63' */

  /* DataTransferBlock generated from: '<Root>/Runnable63_subsystem' */
  Rte_IrvIWrite_Runnable63_IRV65(gain_oj);

  /* Outport: '<Root>/PPort_63_1' */
  Rte_IWrite_Runnable63_PPort_63_1_DE1(gain_oj);

  /* Outport: '<Root>/PPort_63_2' */
  Rte_IWrite_Runnable63_PPort_63_2_DE1(gain_oj);
}

/* Model step function for TID63 */
void Runnable64(void)                  /* Explicit Task: Runnable64 */
{
  sint8 gain_dh[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable63_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable64_IRV65();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable64' incorporates:
   *  SubSystem: '<Root>/Runnable64_subsystem'
   */
  /* Gain: '<S69>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable63_subsystem'
   */
  gain_dh[0] = (sint8)-tmpIrvIRead[0];
  gain_dh[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable64' */

  /* DataTransferBlock generated from: '<Root>/Runnable64_subsystem' */
  Rte_IrvIWrite_Runnable64_IRV66(gain_dh);

  /* Outport: '<Root>/PPort_64_1' */
  Rte_IWrite_Runnable64_PPort_64_1_DE1(gain_dh);

  /* Outport: '<Root>/PPort_64_2' */
  Rte_IWrite_Runnable64_PPort_64_2_DE1(gain_dh);
}

/* Model step function for TID64 */
void Runnable65(void)                  /* Explicit Task: Runnable65 */
{
  sint8 gain_nr[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable64_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable65_IRV66();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable65' incorporates:
   *  SubSystem: '<Root>/Runnable65_subsystem'
   */
  /* Gain: '<S70>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable64_subsystem'
   */
  gain_nr[0] = (sint8)-tmpIrvIRead[0];
  gain_nr[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable65' */

  /* DataTransferBlock generated from: '<Root>/Runnable65_subsystem' */
  Rte_IrvIWrite_Runnable65_IRV67(gain_nr);

  /* Outport: '<Root>/PPort_65_1' */
  Rte_IWrite_Runnable65_PPort_65_1_DE1(gain_nr);

  /* Outport: '<Root>/PPort_65_2' */
  Rte_IWrite_Runnable65_PPort_65_2_DE1(gain_nr);
}

/* Model step function for TID65 */
void Runnable66(void)                  /* Explicit Task: Runnable66 */
{
  sint8 gain_ib[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable65_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable66_IRV67();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable66' incorporates:
   *  SubSystem: '<Root>/Runnable66_subsystem3'
   */
  /* Gain: '<S71>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable65_subsystem'
   */
  gain_ib[0] = (sint8)-tmpIrvIRead[0];
  gain_ib[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable66' */

  /* DataTransferBlock generated from: '<Root>/Runnable66_subsystem3' */
  Rte_IrvIWrite_Runnable66_IRV68(gain_ib);

  /* Outport: '<Root>/PPort_66_1' */
  Rte_IWrite_Runnable66_PPort_66_1_DE1(gain_ib);

  /* Outport: '<Root>/PPort_66_2' */
  Rte_IWrite_Runnable66_PPort_66_2_DE1(gain_ib);
}

/* Model step function for TID66 */
void Runnable67(void)                  /* Explicit Task: Runnable67 */
{
  sint8 gain_hk[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable66_subsystem3' */
  tmpIrvIRead = Rte_IrvIRead_Runnable67_IRV68();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable67' incorporates:
   *  SubSystem: '<Root>/Runnable67_subsystem'
   */
  /* Gain: '<S72>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable66_subsystem3'
   */
  gain_hk[0] = (sint8)-tmpIrvIRead[0];
  gain_hk[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable67' */

  /* DataTransferBlock generated from: '<Root>/Runnable67_subsystem' */
  Rte_IrvIWrite_Runnable67_IRV69(gain_hk);

  /* Outport: '<Root>/PPort_67_1' */
  Rte_IWrite_Runnable67_PPort_67_1_DE1(gain_hk);

  /* Outport: '<Root>/PPort_67_2' */
  Rte_IWrite_Runnable67_PPort_67_2_DE1(gain_hk);
}

/* Model step function for TID67 */
void Runnable68(void)                  /* Explicit Task: Runnable68 */
{
  sint8 gain_fd[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable67_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable68_IRV69();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable68' incorporates:
   *  SubSystem: '<Root>/Runnable68_subsystem'
   */
  /* Gain: '<S73>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable67_subsystem'
   */
  gain_fd[0] = (sint8)-tmpIrvIRead[0];
  gain_fd[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable68' */

  /* DataTransferBlock generated from: '<Root>/Runnable68_subsystem' */
  Rte_IrvIWrite_Runnable68_IRV70(gain_fd);

  /* Outport: '<Root>/PPort_68_1' */
  Rte_IWrite_Runnable68_PPort_68_1_DE1(gain_fd);

  /* Outport: '<Root>/PPort_68_2' */
  Rte_IWrite_Runnable68_PPort_68_2_DE1(gain_fd);
}

/* Model step function for TID68 */
void Runnable69(void)                  /* Explicit Task: Runnable69 */
{
  sint8 gain_ch[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable68_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable69_IRV70();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable69' incorporates:
   *  SubSystem: '<Root>/Runnable69_subsystem'
   */
  /* Gain: '<S74>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable68_subsystem'
   */
  gain_ch[0] = (sint8)-tmpIrvIRead[0];
  gain_ch[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable69' */

  /* DataTransferBlock generated from: '<Root>/Runnable69_subsystem' */
  Rte_IrvIWrite_Runnable69_IRV71(gain_ch);

  /* Outport: '<Root>/PPort_69_1' */
  Rte_IWrite_Runnable69_PPort_69_1_DE1(gain_ch);

  /* Outport: '<Root>/PPort_69_2' */
  Rte_IWrite_Runnable69_PPort_69_2_DE1(gain_ch);
}

/* Model step function for TID69 */
void Runnable70(void)                  /* Explicit Task: Runnable70 */
{
  sint8 gain_jo[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable69_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable70_IRV71();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable70' incorporates:
   *  SubSystem: '<Root>/Runnable70_subsystem'
   */
  /* Gain: '<S76>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable69_subsystem'
   */
  gain_jo[0] = (sint8)-tmpIrvIRead[0];
  gain_jo[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable70' */

  /* DataTransferBlock generated from: '<Root>/Runnable70_subsystem' */
  Rte_IrvIWrite_Runnable70_IRV72(gain_jo);

  /* Outport: '<Root>/PPort_70_1' */
  Rte_IWrite_Runnable70_PPort_70_1_DE1(gain_jo);

  /* Outport: '<Root>/PPort_70_2' */
  Rte_IWrite_Runnable70_PPort_70_2_DE1(gain_jo);
}

/* Model step function for TID70 */
void Runnable71(void)                  /* Explicit Task: Runnable71 */
{
  sint8 gain_dy[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable70_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable71_IRV72();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable71' incorporates:
   *  SubSystem: '<Root>/Runnable71_subsystem'
   */
  /* Gain: '<S77>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable70_subsystem'
   */
  gain_dy[0] = (sint8)-tmpIrvIRead[0];
  gain_dy[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable71' */

  /* DataTransferBlock generated from: '<Root>/Runnable71_subsystem' */
  Rte_IrvIWrite_Runnable71_IRV73(gain_dy);

  /* Outport: '<Root>/PPort_71_1' */
  Rte_IWrite_Runnable71_PPort_71_1_DE1(gain_dy);

  /* Outport: '<Root>/PPort_71_2' */
  Rte_IWrite_Runnable71_PPort_71_2_DE1(gain_dy);
}

/* Model step function for TID71 */
void Runnable72(void)                  /* Explicit Task: Runnable72 */
{
  sint8 gain_fb[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable71_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable72_IRV73();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable72' incorporates:
   *  SubSystem: '<Root>/Runnable72_subsystem'
   */
  /* Gain: '<S78>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable71_subsystem'
   */
  gain_fb[0] = (sint8)-tmpIrvIRead[0];
  gain_fb[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable72' */

  /* DataTransferBlock generated from: '<Root>/Runnable72_subsystem' */
  Rte_IrvIWrite_Runnable72_IRV74(gain_fb);

  /* Outport: '<Root>/PPort_72_1' */
  Rte_IWrite_Runnable72_PPort_72_1_DE1(gain_fb);

  /* Outport: '<Root>/PPort_72_2' */
  Rte_IWrite_Runnable72_PPort_72_2_DE1(gain_fb);
}

/* Model step function for TID72 */
void Runnable73(void)                  /* Explicit Task: Runnable73 */
{
  sint8 gain_ix[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable72_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable73_IRV74();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable73' incorporates:
   *  SubSystem: '<Root>/Runnable73_subsystem'
   */
  /* Gain: '<S79>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable72_subsystem'
   */
  gain_ix[0] = (sint8)-tmpIrvIRead[0];
  gain_ix[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable73' */

  /* DataTransferBlock generated from: '<Root>/Runnable73_subsystem' */
  Rte_IrvIWrite_Runnable73_IRV75(gain_ix);

  /* Outport: '<Root>/PPort_73_1' */
  Rte_IWrite_Runnable73_PPort_73_1_DE1(gain_ix);

  /* Outport: '<Root>/PPort_73_2' */
  Rte_IWrite_Runnable73_PPort_73_2_DE1(gain_ix);
}

/* Model step function for TID73 */
void Runnable74(void)                  /* Explicit Task: Runnable74 */
{
  sint8 gain_i3[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable73_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable74_IRV75();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable74' incorporates:
   *  SubSystem: '<Root>/Runnable74_subsystem'
   */
  /* Gain: '<S80>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable73_subsystem'
   */
  gain_i3[0] = (sint8)-tmpIrvIRead[0];
  gain_i3[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable74' */

  /* DataTransferBlock generated from: '<Root>/Runnable74_subsystem' */
  Rte_IrvIWrite_Runnable74_IRV76(gain_i3);

  /* Outport: '<Root>/PPort_74_1' */
  Rte_IWrite_Runnable74_PPort_74_1_DE1(gain_i3);

  /* Outport: '<Root>/PPort_74_2' */
  Rte_IWrite_Runnable74_PPort_74_2_DE1(gain_i3);
}

/* Model step function for TID74 */
void Runnable75(void)                  /* Explicit Task: Runnable75 */
{
  sint8 gain_f5[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable74_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable75_IRV76();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable75' incorporates:
   *  SubSystem: '<Root>/Runnable75_subsystem'
   */
  /* Gain: '<S81>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable74_subsystem'
   */
  gain_f5[0] = (sint8)-tmpIrvIRead[0];
  gain_f5[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable75' */

  /* DataTransferBlock generated from: '<Root>/Runnable75_subsystem' */
  Rte_IrvIWrite_Runnable75_IRV77(gain_f5);

  /* Outport: '<Root>/PPort_75_1' */
  Rte_IWrite_Runnable75_PPort_75_1_DE1(gain_f5);

  /* Outport: '<Root>/PPort_75_2' */
  Rte_IWrite_Runnable75_PPort_75_2_DE1(gain_f5);
}

/* Model step function for TID75 */
void Runnable76(void)                  /* Explicit Task: Runnable76 */
{
  sint8 gain_ex[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable75_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable76_IRV77();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable76' incorporates:
   *  SubSystem: '<Root>/Runnable76_subsystem'
   */
  /* Gain: '<S82>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable75_subsystem'
   */
  gain_ex[0] = (sint8)-tmpIrvIRead[0];
  gain_ex[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable76' */

  /* DataTransferBlock generated from: '<Root>/Runnable76_subsystem' */
  Rte_IrvIWrite_Runnable76_IRV78(gain_ex);

  /* Outport: '<Root>/PPort_76_1' */
  Rte_IWrite_Runnable76_PPort_76_1_DE1(gain_ex);

  /* Outport: '<Root>/PPort_76_2' */
  Rte_IWrite_Runnable76_PPort_76_2_DE1(gain_ex);
}

/* Model step function for TID76 */
void Runnable77(void)                  /* Explicit Task: Runnable77 */
{
  sint8 gain_e[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable76_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable77_IRV78();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable77' incorporates:
   *  SubSystem: '<Root>/Runnable77_subsystem'
   */
  /* Gain: '<S83>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable76_subsystem'
   */
  gain_e[0] = (sint8)-tmpIrvIRead[0];
  gain_e[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable77' */

  /* DataTransferBlock generated from: '<Root>/Runnable77_subsystem' */
  Rte_IrvIWrite_Runnable77_IRV79(gain_e);

  /* Outport: '<Root>/PPort_77_1' */
  Rte_IWrite_Runnable77_PPort_77_1_DE1(gain_e);

  /* Outport: '<Root>/PPort_77_2' */
  Rte_IWrite_Runnable77_PPort_77_2_DE1(gain_e);
}

/* Model step function for TID77 */
void Runnable78(void)                  /* Explicit Task: Runnable78 */
{
  sint8 gain_mc[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable77_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable78_IRV79();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable78' incorporates:
   *  SubSystem: '<Root>/Runnable78_subsystem'
   */
  /* Gain: '<S84>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable77_subsystem'
   */
  gain_mc[0] = (sint8)-tmpIrvIRead[0];
  gain_mc[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable78' */

  /* DataTransferBlock generated from: '<Root>/Runnable78_subsystem' */
  Rte_IrvIWrite_Runnable78_IRV80(gain_mc);

  /* Outport: '<Root>/PPort_78_1' */
  Rte_IWrite_Runnable78_PPort_78_1_DE1(gain_mc);

  /* Outport: '<Root>/PPort_78_2' */
  Rte_IWrite_Runnable78_PPort_78_2_DE1(gain_mc);
}

/* Model step function for TID78 */
void Runnable79(void)                  /* Explicit Task: Runnable79 */
{
  sint8 gain_otp[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable78_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable79_IRV80();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable79' incorporates:
   *  SubSystem: '<Root>/Runnable79_subsystem'
   */
  /* Gain: '<S85>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable78_subsystem'
   */
  gain_otp[0] = (sint8)-tmpIrvIRead[0];
  gain_otp[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable79' */

  /* DataTransferBlock generated from: '<Root>/Runnable79_subsystem' */
  Rte_IrvIWrite_Runnable79_IRV81(gain_otp);

  /* Outport: '<Root>/PPort_79_1' */
  Rte_IWrite_Runnable79_PPort_79_1_DE1(gain_otp);

  /* Outport: '<Root>/PPort_79_2' */
  Rte_IWrite_Runnable79_PPort_79_2_DE1(gain_otp);
}

/* Model step function for TID79 */
void Runnable80(void)                  /* Explicit Task: Runnable80 */
{
  sint8 gain_lu[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable79_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable80_IRV81();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable80' incorporates:
   *  SubSystem: '<Root>/Runnable80_subsystem'
   */
  /* Gain: '<S87>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable79_subsystem'
   */
  gain_lu[0] = (sint8)-tmpIrvIRead[0];
  gain_lu[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable80' */

  /* DataTransferBlock generated from: '<Root>/Runnable80_subsystem' */
  Rte_IrvIWrite_Runnable80_IRV82(gain_lu);

  /* Outport: '<Root>/PPort_80_1' */
  Rte_IWrite_Runnable80_PPort_80_1_DE1(gain_lu);

  /* Outport: '<Root>/PPort_80_2' */
  Rte_IWrite_Runnable80_PPort_80_2_DE1(gain_lu);
}

/* Model step function for TID80 */
void Runnable81(void)                  /* Explicit Task: Runnable81 */
{
  sint8 gain_i[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable80_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable81_IRV82();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable81' incorporates:
   *  SubSystem: '<Root>/Runnable81_subsystem'
   */
  /* Gain: '<S88>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable80_subsystem'
   */
  gain_i[0] = (sint8)-tmpIrvIRead[0];
  gain_i[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable81' */

  /* DataTransferBlock generated from: '<Root>/Runnable81_subsystem' */
  Rte_IrvIWrite_Runnable81_IRV83(gain_i);

  /* Outport: '<Root>/PPort_81_1' */
  Rte_IWrite_Runnable81_PPort_81_1_DE1(gain_i);

  /* Outport: '<Root>/PPort_81_2' */
  Rte_IWrite_Runnable81_PPort_81_2_DE1(gain_i);
}

/* Model step function for TID81 */
void Runnable82(void)                  /* Explicit Task: Runnable82 */
{
  sint8 gain_k[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable81_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable82_IRV83();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable82' incorporates:
   *  SubSystem: '<Root>/Runnable82_subsystem'
   */
  /* Gain: '<S89>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable81_subsystem'
   */
  gain_k[0] = (sint8)-tmpIrvIRead[0];
  gain_k[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable82' */

  /* DataTransferBlock generated from: '<Root>/Runnable82_subsystem' */
  Rte_IrvIWrite_Runnable82_IRV84(gain_k);

  /* Outport: '<Root>/PPort_82_1' */
  Rte_IWrite_Runnable82_PPort_82_1_DE1(gain_k);

  /* Outport: '<Root>/PPort_82_2' */
  Rte_IWrite_Runnable82_PPort_82_2_DE1(gain_k);
}

/* Model step function for TID82 */
void Runnable83(void)                  /* Explicit Task: Runnable83 */
{
  sint8 gain_pf[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable82_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable83_IRV84();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable83' incorporates:
   *  SubSystem: '<Root>/Runnable83_subsystem'
   */
  /* Gain: '<S90>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable82_subsystem'
   */
  gain_pf[0] = (sint8)-tmpIrvIRead[0];
  gain_pf[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable83' */

  /* DataTransferBlock generated from: '<Root>/Runnable83_subsystem' */
  Rte_IrvIWrite_Runnable83_IRV85(gain_pf);

  /* Outport: '<Root>/PPort_83_1' */
  Rte_IWrite_Runnable83_PPort_83_1_DE1(gain_pf);

  /* Outport: '<Root>/PPort_83_2' */
  Rte_IWrite_Runnable83_PPort_83_2_DE1(gain_pf);
}

/* Model step function for TID83 */
void Runnable84(void)                  /* Explicit Task: Runnable84 */
{
  sint8 gain_j[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable83_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable84_IRV85();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable84' incorporates:
   *  SubSystem: '<Root>/Runnable84_subsystem'
   */
  /* Gain: '<S91>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable83_subsystem'
   */
  gain_j[0] = (sint8)-tmpIrvIRead[0];
  gain_j[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable84' */

  /* DataTransferBlock generated from: '<Root>/Runnable84_subsystem' */
  Rte_IrvIWrite_Runnable84_IRV86(gain_j);

  /* Outport: '<Root>/PPort_84_1' */
  Rte_IWrite_Runnable84_PPort_84_1_DE1(gain_j);

  /* Outport: '<Root>/PPort_84_2' */
  Rte_IWrite_Runnable84_PPort_84_2_DE1(gain_j);
}

/* Model step function for TID84 */
void Runnable85(void)                  /* Explicit Task: Runnable85 */
{
  sint8 gain_d0[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable84_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable85_IRV86();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable85' incorporates:
   *  SubSystem: '<Root>/Runnable85_subsystem'
   */
  /* Gain: '<S92>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable84_subsystem'
   */
  gain_d0[0] = (sint8)-tmpIrvIRead[0];
  gain_d0[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable85' */

  /* DataTransferBlock generated from: '<Root>/Runnable85_subsystem' */
  Rte_IrvIWrite_Runnable85_IRV87(gain_d0);

  /* Outport: '<Root>/PPort_85_1' */
  Rte_IWrite_Runnable85_PPort_85_1_DE1(gain_d0);

  /* Outport: '<Root>/PPort_85_2' */
  Rte_IWrite_Runnable85_PPort_85_2_DE1(gain_d0);
}

/* Model step function for TID85 */
void Runnable86(void)                  /* Explicit Task: Runnable86 */
{
  sint8 gain_l[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable85_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable86_IRV87();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable86' incorporates:
   *  SubSystem: '<Root>/Runnable86_subsystem'
   */
  /* Gain: '<S93>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable85_subsystem'
   */
  gain_l[0] = (sint8)-tmpIrvIRead[0];
  gain_l[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable86' */

  /* DataTransferBlock generated from: '<Root>/Runnable86_subsystem' */
  Rte_IrvIWrite_Runnable86_IRV88(gain_l);

  /* Outport: '<Root>/PPort_86_1' */
  Rte_IWrite_Runnable86_PPort_86_1_DE1(gain_l);

  /* Outport: '<Root>/PPort_86_2' */
  Rte_IWrite_Runnable86_PPort_86_2_DE1(gain_l);
}

/* Model step function for TID86 */
void Runnable87(void)                  /* Explicit Task: Runnable87 */
{
  sint8 gain_p[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable86_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable87_IRV88();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable87' incorporates:
   *  SubSystem: '<Root>/Runnable87_subsystem'
   */
  /* Gain: '<S94>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable86_subsystem'
   */
  gain_p[0] = (sint8)-tmpIrvIRead[0];
  gain_p[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable87' */

  /* DataTransferBlock generated from: '<Root>/Runnable87_subsystem' */
  Rte_IrvIWrite_Runnable87_IRV89(gain_p);

  /* Outport: '<Root>/PPort_87_1' */
  Rte_IWrite_Runnable87_PPort_87_1_DE1(gain_p);

  /* Outport: '<Root>/PPort_87_2' */
  Rte_IWrite_Runnable87_PPort_87_2_DE1(gain_p);
}

/* Model step function for TID87 */
void Runnable88(void)                  /* Explicit Task: Runnable88 */
{
  sint8 gain_fz[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable87_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable88_IRV89();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable88' incorporates:
   *  SubSystem: '<Root>/Runnable88_subsystem'
   */
  /* Gain: '<S95>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable87_subsystem'
   */
  gain_fz[0] = (sint8)-tmpIrvIRead[0];
  gain_fz[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable88' */

  /* DataTransferBlock generated from: '<Root>/Runnable88_subsystem' */
  Rte_IrvIWrite_Runnable88_IRV90(gain_fz);

  /* Outport: '<Root>/PPort_88_1' */
  Rte_IWrite_Runnable88_PPort_88_1_DE1(gain_fz);

  /* Outport: '<Root>/PPort_88_2' */
  Rte_IWrite_Runnable88_PPort_88_2_DE1(gain_fz);
}

/* Model step function for TID88 */
void Runnable89(void)                  /* Explicit Task: Runnable89 */
{
  sint8 gain_m[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable88_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable89_IRV90();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable89' incorporates:
   *  SubSystem: '<Root>/Runnable89_subsystem'
   */
  /* Gain: '<S96>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable88_subsystem'
   */
  gain_m[0] = (sint8)-tmpIrvIRead[0];
  gain_m[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable89' */

  /* DataTransferBlock generated from: '<Root>/Runnable89_subsystem' */
  Rte_IrvIWrite_Runnable89_IRV91(gain_m);

  /* Outport: '<Root>/PPort_89_1' */
  Rte_IWrite_Runnable89_PPort_89_1_DE1(gain_m);

  /* Outport: '<Root>/PPort_89_2' */
  Rte_IWrite_Runnable89_PPort_89_2_DE1(gain_m);
}

/* Model step function for TID89 */
void Runnable90(void)                  /* Explicit Task: Runnable90 */
{
  sint8 gain_f[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable89_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable90_IRV91();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable90' incorporates:
   *  SubSystem: '<Root>/Runnable90_subsystem'
   */
  /* Gain: '<S98>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable89_subsystem'
   */
  gain_f[0] = (sint8)-tmpIrvIRead[0];
  gain_f[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable90' */

  /* DataTransferBlock generated from: '<Root>/Runnable90_subsystem' */
  Rte_IrvIWrite_Runnable90_IRV92(gain_f);

  /* Outport: '<Root>/PPort_90_1' */
  Rte_IWrite_Runnable90_PPort_90_1_DE1(gain_f);

  /* Outport: '<Root>/PPort_90_2' */
  Rte_IWrite_Runnable90_PPort_90_2_DE1(gain_f);
}

/* Model step function for TID90 */
void Runnable91(void)                  /* Explicit Task: Runnable91 */
{
  sint8 gain_os[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable90_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable91_IRV92();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable91' incorporates:
   *  SubSystem: '<Root>/Runnable91_subsystem'
   */
  /* Gain: '<S99>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable90_subsystem'
   */
  gain_os[0] = (sint8)-tmpIrvIRead[0];
  gain_os[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable91' */

  /* DataTransferBlock generated from: '<Root>/Runnable91_subsystem' */
  Rte_IrvIWrite_Runnable91_IRV93(gain_os);

  /* Outport: '<Root>/PPort_91_1' */
  Rte_IWrite_Runnable91_PPort_91_1_DE1(gain_os);

  /* Outport: '<Root>/PPort_91_2' */
  Rte_IWrite_Runnable91_PPort_91_2_DE1(gain_os);
}

/* Model step function for TID91 */
void Runnable92(void)                  /* Explicit Task: Runnable92 */
{
  sint8 gain_nz[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable91_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable92_IRV93();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable92' incorporates:
   *  SubSystem: '<Root>/Runnable92_subsystem6'
   */
  /* Gain: '<S100>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable91_subsystem'
   */
  gain_nz[0] = (sint8)-tmpIrvIRead[0];
  gain_nz[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable92' */

  /* DataTransferBlock generated from: '<Root>/Runnable92_subsystem6' */
  Rte_IrvIWrite_Runnable92_IRV94(gain_nz);

  /* Outport: '<Root>/PPort_92_1' */
  Rte_IWrite_Runnable92_PPort_92_1_DE1(gain_nz);

  /* Outport: '<Root>/PPort_92_2' */
  Rte_IWrite_Runnable92_PPort_92_2_DE1(gain_nz);
}

/* Model step function for TID92 */
void Runnable93(void)                  /* Explicit Task: Runnable93 */
{
  sint8 gain_ot[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable92_subsystem6' */
  tmpIrvIRead = Rte_IrvIRead_Runnable93_IRV94();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable93' incorporates:
   *  SubSystem: '<Root>/Runnable93_subsystem'
   */
  /* Gain: '<S101>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable92_subsystem6'
   */
  gain_ot[0] = (sint8)-tmpIrvIRead[0];
  gain_ot[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable93' */

  /* DataTransferBlock generated from: '<Root>/Runnable93_subsystem' */
  Rte_IrvIWrite_Runnable93_IRV95(gain_ot);

  /* Outport: '<Root>/PPort_93_1' */
  Rte_IWrite_Runnable93_PPort_93_1_DE1(gain_ot);

  /* Outport: '<Root>/PPort_93_2' */
  Rte_IWrite_Runnable93_PPort_93_2_DE1(gain_ot);
}

/* Model step function for TID93 */
void Runnable94(void)                  /* Explicit Task: Runnable94 */
{
  sint8 gain_n[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable93_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable94_IRV95();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable94' incorporates:
   *  SubSystem: '<Root>/Runnable94_subsystem'
   */
  /* Gain: '<S102>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable93_subsystem'
   */
  gain_n[0] = (sint8)-tmpIrvIRead[0];
  gain_n[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable94' */

  /* DataTransferBlock generated from: '<Root>/Runnable94_subsystem' */
  Rte_IrvIWrite_Runnable94_IRV96(gain_n);

  /* Outport: '<Root>/PPort_94_1' */
  Rte_IWrite_Runnable94_PPort_94_1_DE1(gain_n);

  /* Outport: '<Root>/PPort_94_2' */
  Rte_IWrite_Runnable94_PPort_94_2_DE1(gain_n);
}

/* Model step function for TID94 */
void Runnable95(void)                  /* Explicit Task: Runnable95 */
{
  sint8 gain_ca[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable94_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable95_IRV96();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable95' incorporates:
   *  SubSystem: '<Root>/Runnable95_subsystem'
   */
  /* Gain: '<S103>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable94_subsystem'
   */
  gain_ca[0] = (sint8)-tmpIrvIRead[0];
  gain_ca[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable95' */

  /* DataTransferBlock generated from: '<Root>/Runnable95_subsystem' */
  Rte_IrvIWrite_Runnable95_IRV97(gain_ca);

  /* Outport: '<Root>/PPort_95_1' */
  Rte_IWrite_Runnable95_PPort_95_1_DE1(gain_ca);

  /* Outport: '<Root>/PPort_95_2' */
  Rte_IWrite_Runnable95_PPort_95_2_DE1(gain_ca);
}

/* Model step function for TID95 */
void Runnable96(void)                  /* Explicit Task: Runnable96 */
{
  sint8 gain_g[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable95_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable96_IRV97();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable96' incorporates:
   *  SubSystem: '<Root>/Runnable96_subsystem'
   */
  /* Gain: '<S104>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable95_subsystem'
   */
  gain_g[0] = (sint8)-tmpIrvIRead[0];
  gain_g[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable96' */

  /* DataTransferBlock generated from: '<Root>/Runnable96_subsystem' */
  Rte_IrvIWrite_Runnable96_IRV98(gain_g);

  /* Outport: '<Root>/PPort_96_1' */
  Rte_IWrite_Runnable96_PPort_96_1_DE1(gain_g);

  /* Outport: '<Root>/PPort_96_2' */
  Rte_IWrite_Runnable96_PPort_96_2_DE1(gain_g);
}

/* Model step function for TID96 */
void Runnable97(void)                  /* Explicit Task: Runnable97 */
{
  sint8 gain_d[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable96_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable97_IRV98();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable97' incorporates:
   *  SubSystem: '<Root>/Runnable97_subsystem'
   */
  /* Gain: '<S105>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable96_subsystem'
   */
  gain_d[0] = (sint8)-tmpIrvIRead[0];
  gain_d[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable97' */

  /* DataTransferBlock generated from: '<Root>/Runnable97_subsystem' */
  Rte_IrvIWrite_Runnable97_IRV99(gain_d);

  /* Outport: '<Root>/PPort_97_1' */
  Rte_IWrite_Runnable97_PPort_97_1_DE1(gain_d);

  /* Outport: '<Root>/PPort_97_2' */
  Rte_IWrite_Runnable97_PPort_97_2_DE1(gain_d);
}

/* Model step function for TID97 */
void Runnable98(void)                  /* Explicit Task: Runnable98 */
{
  sint8 gain_o[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable97_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable98_IRV99();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable98' incorporates:
   *  SubSystem: '<Root>/Runnable98_subsystem'
   */
  /* Gain: '<S106>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable97_subsystem'
   */
  gain_o[0] = (sint8)-tmpIrvIRead[0];
  gain_o[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable98' */

  /* DataTransferBlock generated from: '<Root>/Runnable98_subsystem' */
  Rte_IrvIWrite_Runnable98_IRV100(gain_o);

  /* Outport: '<Root>/PPort_98_1' */
  Rte_IWrite_Runnable98_PPort_98_1_DE1(gain_o);

  /* Outport: '<Root>/PPort_98_2' */
  Rte_IWrite_Runnable98_PPort_98_2_DE1(gain_o);
}

/* Model step function for TID98 */
void Runnable99(void)                  /* Explicit Task: Runnable99 */
{
  sint8 gain_c[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable98_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable99_IRV100();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable99' incorporates:
   *  SubSystem: '<Root>/Runnable99_subsystem'
   */
  /* Gain: '<S107>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable98_subsystem'
   */
  gain_c[0] = (sint8)-tmpIrvIRead[0];
  gain_c[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable99' */

  /* DataTransferBlock generated from: '<Root>/Runnable99_subsystem' */
  Rte_IrvIWrite_Runnable99_IRV101(gain_c);

  /* Outport: '<Root>/PPort_99_1' */
  Rte_IWrite_Runnable99_PPort_99_1_DE1(gain_c);

  /* Outport: '<Root>/PPort_99_2' */
  Rte_IWrite_Runnable99_PPort_99_2_DE1(gain_c);
}

/* Model step function for TID99 */
void Runnable100(void)                 /* Explicit Task: Runnable100 */
{
  sint8 gain_gg[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable99_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable100_IRV101();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable100' incorporates:
   *  SubSystem: '<Root>/Runnable100_subsystem'
   */
  /* Gain: '<S1>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable99_subsystem'
   */
  gain_gg[0] = (sint8)-tmpIrvIRead[0];
  gain_gg[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable100' */

  /* DataTransferBlock generated from: '<Root>/Runnable100_subsystem' */
  Rte_IrvIWrite_Runnable100_IRV102(gain_gg);

  /* Outport: '<Root>/PPort_100_1' */
  Rte_IWrite_Runnable100_PPort_100_1_DE1(gain_gg);

  /* Outport: '<Root>/PPort_100_2' */
  Rte_IWrite_Runnable100_PPort_100_2_DE1(gain_gg);
}

/* Model step function for TID100 */
void Runnable101(void)                 /* Explicit Task: Runnable101 */
{
  sint8 gain_il[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable100_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable101_IRV102();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable101' incorporates:
   *  SubSystem: '<Root>/Runnable101_subsystem'
   */
  /* Gain: '<S2>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable100_subsystem'
   */
  gain_il[0] = (sint8)-tmpIrvIRead[0];
  gain_il[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable101' */

  /* DataTransferBlock generated from: '<Root>/Runnable101_subsystem' */
  Rte_IrvIWrite_Runnable101_IRV103(gain_il);

  /* Outport: '<Root>/PPort_101_1' */
  Rte_IWrite_Runnable101_PPort_101_1_DE1(gain_il);

  /* Outport: '<Root>/PPort_101_2' */
  Rte_IWrite_Runnable101_PPort_101_2_DE1(gain_il);
}

/* Model step function for TID101 */
void Runnable102(void)                 /* Explicit Task: Runnable102 */
{
  sint8 gain_l4[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable101_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable102_IRV103();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable102' incorporates:
   *  SubSystem: '<Root>/Runnable102_subsystem'
   */
  /* Gain: '<S3>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable101_subsystem'
   */
  gain_l4[0] = (sint8)-tmpIrvIRead[0];
  gain_l4[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable102' */

  /* DataTransferBlock generated from: '<Root>/Runnable102_subsystem' */
  Rte_IrvIWrite_Runnable102_IRV104(gain_l4);

  /* Outport: '<Root>/PPort_102_1' */
  Rte_IWrite_Runnable102_PPort_102_1_DE1(gain_l4);

  /* Outport: '<Root>/PPort_102_2' */
  Rte_IWrite_Runnable102_PPort_102_2_DE1(gain_l4);
}

/* Model step function for TID102 */
void Runnable103(void)                 /* Explicit Task: Runnable103 */
{
  sint8 gain_ah[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable102_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable103_IRV104();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable103' incorporates:
   *  SubSystem: '<Root>/Runnable103_subsystem'
   */
  /* Gain: '<S4>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable102_subsystem'
   */
  gain_ah[0] = (sint8)-tmpIrvIRead[0];
  gain_ah[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable103' */

  /* DataTransferBlock generated from: '<Root>/Runnable103_subsystem' */
  Rte_IrvIWrite_Runnable103_IRV105(gain_ah);

  /* Outport: '<Root>/PPort_103_1' */
  Rte_IWrite_Runnable103_PPort_103_1_DE1(gain_ah);

  /* Outport: '<Root>/PPort_103_2' */
  Rte_IWrite_Runnable103_PPort_103_2_DE1(gain_ah);
}

/* Model step function for TID103 */
void Runnable104(void)                 /* Explicit Task: Runnable104 */
{
  sint8 gain_pr[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable103_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable104_IRV105();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable104' incorporates:
   *  SubSystem: '<Root>/Runnable104_subsystem'
   */
  /* Gain: '<S5>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable103_subsystem'
   */
  gain_pr[0] = (sint8)-tmpIrvIRead[0];
  gain_pr[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable104' */

  /* DataTransferBlock generated from: '<Root>/Runnable104_subsystem' */
  Rte_IrvIWrite_Runnable104_IRV106(gain_pr);

  /* Outport: '<Root>/PPort_104_1' */
  Rte_IWrite_Runnable104_PPort_104_1_DE1(gain_pr);

  /* Outport: '<Root>/PPort_104_2' */
  Rte_IWrite_Runnable104_PPort_104_2_DE1(gain_pr);
}

/* Model step function for TID104 */
void Runnable105(void)                 /* Explicit Task: Runnable105 */
{
  sint8 gain_dyq[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable104_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable105_IRV106();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable105' incorporates:
   *  SubSystem: '<Root>/Runnable105_subsystem'
   */
  /* Gain: '<S6>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable104_subsystem'
   */
  gain_dyq[0] = (sint8)-tmpIrvIRead[0];
  gain_dyq[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable105' */

  /* DataTransferBlock generated from: '<Root>/Runnable105_subsystem' */
  Rte_IrvIWrite_Runnable105_IRV107(gain_dyq);

  /* Outport: '<Root>/PPort_105_1' */
  Rte_IWrite_Runnable105_PPort_105_1_DE1(gain_dyq);

  /* Outport: '<Root>/PPort_105_2' */
  Rte_IWrite_Runnable105_PPort_105_2_DE1(gain_dyq);
}

/* Model step function for TID105 */
void Runnable106(void)                 /* Explicit Task: Runnable106 */
{
  sint8 gain_ne[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable105_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable106_IRV107();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable106' incorporates:
   *  SubSystem: '<Root>/Runnable106_subsystem'
   */
  /* Gain: '<S7>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable105_subsystem'
   */
  gain_ne[0] = (sint8)-tmpIrvIRead[0];
  gain_ne[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable106' */

  /* DataTransferBlock generated from: '<Root>/Runnable106_subsystem' */
  Rte_IrvIWrite_Runnable106_IRV108(gain_ne);

  /* Outport: '<Root>/PPort_106_1' */
  Rte_IWrite_Runnable106_PPort_106_1_DE1(gain_ne);

  /* Outport: '<Root>/PPort_106_2' */
  Rte_IWrite_Runnable106_PPort_106_2_DE1(gain_ne);
}

/* Model step function for TID106 */
void Runnable107(void)                 /* Explicit Task: Runnable107 */
{
  sint8 gain_ma[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable106_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable107_IRV108();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable107' incorporates:
   *  SubSystem: '<Root>/Runnable107_subsystem'
   */
  /* Gain: '<S8>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable106_subsystem'
   */
  gain_ma[0] = (sint8)-tmpIrvIRead[0];
  gain_ma[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable107' */

  /* DataTransferBlock generated from: '<Root>/Runnable107_subsystem' */
  Rte_IrvIWrite_Runnable107_IRV109(gain_ma);

  /* Outport: '<Root>/PPort_107_1' */
  Rte_IWrite_Runnable107_PPort_107_1_DE1(gain_ma);

  /* Outport: '<Root>/PPort_107_2' */
  Rte_IWrite_Runnable107_PPort_107_2_DE1(gain_ma);
}

/* Model step function for TID107 */
void Runnable108(void)                 /* Explicit Task: Runnable108 */
{
  sint8 gain_og[2];
  const sint8 *tmpIrvIRead;

  /* DataTransferBlock generated from: '<Root>/Runnable107_subsystem' */
  tmpIrvIRead = Rte_IrvIRead_Runnable108_IRV109();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable108' incorporates:
   *  SubSystem: '<Root>/Runnable108_subsystem'
   */
  /* Gain: '<S9>/gain' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable107_subsystem'
   */
  gain_og[0] = (sint8)-tmpIrvIRead[0];
  gain_og[1] = (sint8)-tmpIrvIRead[1];

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable108' */

  /* Outport: '<Root>/PPort_108_1' */
  Rte_IWrite_Runnable108_PPort_108_1_DE1(gain_og);

  /* Outport: '<Root>/PPort_108_2' */
  Rte_IWrite_Runnable108_PPort_108_2_DE1(gain_og);
}

/* Model step function for TID108 */
void Runnable3(void)                   /* Explicit Task: Runnable3 */
{
  const float64 *tmpIRead;
  sint8 Delay;

  /* Inport: '<Root>/RPort_DE2' */
  tmpIRead = Rte_IRead_Runnable3_RPort_DE2();

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* UnitDelay: '<S42>/Delay' */
  Delay = rtDWork.Delay_DSTATE;

  /* Gain: '<S42>/Gain' incorporates:
   *  UnitDelay: '<S42>/Delay'
   */
  rtDWork.Delay_DSTATE = (sint8)-rtDWork.Delay_DSTATE;

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */

  /* DataTransferBlock generated from: '<Root>/Runnable3_subsystem' incorporates:
   *  DataTransferBlock generated from: '<Root>/Runnable2_subsystem'
   *  Product: '<S42>/Product'
   */
  Rte_IrvIWrite_Runnable3_IRV2(Rte_IrvIRead_Runnable3_IRV4() * tmpIRead[0]);

  /* End of Outputs for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* DataTransferBlock generated from: '<Root>/Runnable3_subsystem' */
  Rte_IrvIWrite_Runnable3_IRV3(Delay);

  /* RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* Outport: '<Root>/PPort_DE2' incorporates:
   *  SignalConversion generated from: '<S42>/TicToc'
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
  /* InitializeConditions for UnitDelay: '<S20>/Delay' */
  rtDWork.Delay_DSTATE_a = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable1' */

  /* SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' incorporates:
   *  SubSystem: '<Root>/Runnable3_subsystem'
   */
  /* InitializeConditions for UnitDelay: '<S42>/Delay' */
  rtDWork.Delay_DSTATE = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable3' */

  /* SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' incorporates:
   *  SubSystem: '<Root>/Runnable2_subsystem'
   */
  /* InitializeConditions for UnitDelay: '<S31>/Delay' */
  rtDWork.Delay_DSTATE_m[0] = 1;
  rtDWork.Delay_DSTATE_m[1] = 1;

  /* End of SystemInitialize for RootInportFunctionCallGenerator generated from: '<Root>/Runnable2' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
