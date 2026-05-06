/*
 * File: large_scale_autosar_swc_expfcns.c
 *
 *
 * C/C++ source code generated on : 2026-03-21 13:36:57
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "large_scale_autosar_swc_expfcns.h"

#ifndef PORTABLE_WORDSIZES
#ifndef UCHAR_MAX
#include <limits.h>
#endif

#if (UCHAR_MAX != (0xFFU)) || (SCHAR_MAX != (0x7F))
#error Code was generated for compiler with different sized uchar/char. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if (USHRT_MAX != (0xFFFFU)) || (SHRT_MAX != (0x7FFF))
#error Code was generated for compiler with different sized ushort/short. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if (UINT_MAX != (0xFFFFFFFFU)) || (INT_MAX != (0x7FFFFFFF))
#error Code was generated for compiler with different sized uint/int. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#if (ULONG_MAX != (0xFFFFFFFFU)) || (LONG_MAX != (0x7FFFFFFF))
#error Code was generated for compiler with different sized ulong/long. \
Consider adjusting Test hardware word size settings on the \
Hardware Implementation pane to match your compiler word sizes as \
defined in limits.h of the compiler. Alternatively, you can \
select the Test hardware is the same as production hardware option and \
select the Enable portable word sizes option on the Code Generation > \
Verification pane for ERT based targets, which will disable the \
preprocessor word size checks.
#endif

#endif

BlockIO rtB;

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

void Runnable4(void)
{
  Double gain_je[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable4_IRV5();

  gain_je[0] = (Double)-tmpIrvIRead[0];
  gain_je[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable4_IRV6(gain_je);

  Rte_IWrite_Runnable4_PPort_4_1_element_Interface_4_1_0(gain_je);

  Rte_IWrite_Runnable4_PPort_4_2_element_Interface_4_2_0(gain_je);
}

void Runnable5(void)
{
  Double gain_a[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable5_IRV6();

  gain_a[0] = (Double)-tmpIrvIRead[0];
  gain_a[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable5_IRV7(gain_a);

  Rte_IWrite_Runnable5_PPort_5_1_element_Interface_5_1_0(gain_a);

  Rte_IWrite_Runnable5_PPort_5_2_element_Interface_5_2_0(gain_a);
}

void Runnable6(void)
{
  Double gain_h[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable6_IRV7();

  gain_h[0] = (Double)-tmpIrvIRead[0];
  gain_h[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable6_IRV8(gain_h);

  Rte_IWrite_Runnable6_PPort_6_1_element_Interface_6_1_0(gain_h);

  Rte_IWrite_Runnable6_PPort_6_2_element_Interface_6_2_0(gain_h);
}

void Runnable7(void)
{
  Double gain_b[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable7_IRV8();

  gain_b[0] = (Double)-tmpIrvIRead[0];
  gain_b[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable7_IRV9(gain_b);

  Rte_IWrite_Runnable7_PPort_7_1_element_Interface_7_1_0(gain_b);

  Rte_IWrite_Runnable7_PPort_7_2_element_Interface_7_2_0(gain_b);
}

void Runnable8(void)
{
  Double gain_cp[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable8_IRV9();

  gain_cp[0] = (Double)-tmpIrvIRead[0];
  gain_cp[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable8_IRV10(gain_cp);

  Rte_IWrite_Runnable8_PPort_8_1_element_Interface_8_1_0(gain_cp);

  Rte_IWrite_Runnable8_PPort_8_2_element_Interface_8_2_0(gain_cp);
}

void Runnable9(void)
{
  Double gain[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable9_IRV10();

  gain[0] = (Double)-tmpIrvIRead[0];
  gain[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable9_IRV11(gain);

  Rte_IWrite_Runnable9_PPort_9_1_element_Interface_9_1_0(gain);

  Rte_IWrite_Runnable9_PPort_9_2_element_Interface_9_2_0(gain);
}

void Runnable10(void)
{
  Double gain_pq[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable10_IRV11();

  gain_pq[0] = (Double)-tmpIrvIRead[0];
  gain_pq[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable10_IRV12(gain_pq);

  Rte_IWrite_Runnable10_PPort_10_1_element_Interface_10_1_0(gain_pq);

  Rte_IWrite_Runnable10_PPort_10_2_element_Interface_10_2_0(gain_pq);
}

void Runnable11(void)
{
  Double gain_cdg[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable11_IRV12();

  gain_cdg[0] = (Double)-tmpIrvIRead[0];
  gain_cdg[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable11_IRV13(gain_cdg);

  Rte_IWrite_Runnable11_PPort_11_1_element_Interface_11_1_0(gain_cdg);

  Rte_IWrite_Runnable11_PPort_11_2_element_Interface_11_2_0(gain_cdg);
}

void Runnable12(void)
{
  Double gain_iy[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable12_IRV13();

  gain_iy[0] = (Double)-tmpIrvIRead[0];
  gain_iy[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable12_IRV14(gain_iy);

  Rte_IWrite_Runnable12_PPort_12_1_element_Interface_12_1_0(gain_iy);

  Rte_IWrite_Runnable12_PPort_12_2_element_Interface_12_2_0(gain_iy);
}

void Runnable13(void)
{
  Double gain_e2[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable13_IRV14();

  gain_e2[0] = (Double)-tmpIrvIRead[0];
  gain_e2[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable13_IRV15(gain_e2);

  Rte_IWrite_Runnable13_PPort_13_1_element_Interface_13_1_0(gain_e2);

  Rte_IWrite_Runnable13_PPort_13_2_element_Interface_13_2_0(gain_e2);
}

void Runnable14(void)
{
  Double gain_mv[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable14_IRV15();

  gain_mv[0] = (Double)-tmpIrvIRead[0];
  gain_mv[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable14_IRV16(gain_mv);

  Rte_IWrite_Runnable14_PPort_14_1_element_Interface_14_1_0(gain_mv);

  Rte_IWrite_Runnable14_PPort_14_2_element_Interface_14_2_0(gain_mv);
}

void Runnable15(void)
{
  Double gain_n5[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable15_IRV16();

  gain_n5[0] = (Double)-tmpIrvIRead[0];
  gain_n5[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable15_IRV17(gain_n5);

  Rte_IWrite_Runnable15_PPort_15_1_element_Interface_15_1_0(gain_n5);

  Rte_IWrite_Runnable15_PPort_15_2_element_Interface_15_2_0(gain_n5);
}

void Runnable16(void)
{
  Double gain_ft[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable16_IRV17();

  gain_ft[0] = (Double)-tmpIrvIRead[0];
  gain_ft[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable16_IRV18(gain_ft);

  Rte_IWrite_Runnable16_PPort_16_1_element_Interface_16_1_0(gain_ft);

  Rte_IWrite_Runnable16_PPort_16_2_element_Interface_16_2_0(gain_ft);
}

void Runnable17(void)
{
  Double gain_fi[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable17_IRV18();

  gain_fi[0] = (Double)-tmpIrvIRead[0];
  gain_fi[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable17_IRV19(gain_fi);

  Rte_IWrite_Runnable17_PPort_17_1_element_Interface_17_1_0(gain_fi);

  Rte_IWrite_Runnable17_PPort_17_2_element_Interface_17_2_0(gain_fi);
}

void Runnable18(void)
{
  Double gain_c1[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable18_IRV19();

  gain_c1[0] = (Double)-tmpIrvIRead[0];
  gain_c1[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable18_IRV20(gain_c1);

  Rte_IWrite_Runnable18_PPort_18_1_element_Interface_18_1_0(gain_c1);

  Rte_IWrite_Runnable18_PPort_18_2_element_Interface_18_2_0(gain_c1);
}

void Runnable19(void)
{
  Double gain_gx[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable19_IRV20();

  gain_gx[0] = (Double)-tmpIrvIRead[0];
  gain_gx[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable19_IRV21(gain_gx);

  Rte_IWrite_Runnable19_PPort_19_1_element_Interface_19_1_0(gain_gx);

  Rte_IWrite_Runnable19_PPort_19_2_element_Interface_19_2_0(gain_gx);
}

void Runnable20(void)
{
  Double gain_hg[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable20_IRV21();

  gain_hg[0] = (Double)-tmpIrvIRead[0];
  gain_hg[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable20_IRV22(gain_hg);

  Rte_IWrite_Runnable20_PPort_20_1_element_Interface_20_1_0(gain_hg);

  Rte_IWrite_Runnable20_PPort_20_2_element_Interface_20_2_0(gain_hg);
}

void Runnable21(void)
{
  Double gain_d4[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable21_IRV22();

  gain_d4[0] = (Double)-tmpIrvIRead[0];
  gain_d4[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable21_IRV23(gain_d4);

  Rte_IWrite_Runnable21_PPort_21_1_element_Interface_21_1_0(gain_d4);

  Rte_IWrite_Runnable21_PPort_21_2_element_Interface_21_2_0(gain_d4);
}

void Runnable22(void)
{
  Double gain_dq[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable22_IRV23();

  gain_dq[0] = (Double)-tmpIrvIRead[0];
  gain_dq[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable22_IRV24(gain_dq);

  Rte_IWrite_Runnable22_PPort_22_1_element_Interface_22_1_0(gain_dq);

  Rte_IWrite_Runnable22_PPort_22_2_element_Interface_22_2_0(gain_dq);
}

void Runnable23(void)
{
  Double gain_c3[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable23_IRV24();

  gain_c3[0] = (Double)-tmpIrvIRead[0];
  gain_c3[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable23_IRV25(gain_c3);

  Rte_IWrite_Runnable23_PPort_23_1_element_Interface_23_1_0(gain_c3);

  Rte_IWrite_Runnable23_PPort_23_2_element_Interface_23_2_0(gain_c3);
}

void Runnable24(void)
{
  Double gain_ac[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable24_IRV25();

  gain_ac[0] = (Double)-tmpIrvIRead[0];
  gain_ac[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable24_IRV26(gain_ac);

  Rte_IWrite_Runnable24_PPort_24_1_element_Interface_24_1_0(gain_ac);

  Rte_IWrite_Runnable24_PPort_24_2_element_Interface_24_2_0(gain_ac);
}

void Runnable25(void)
{
  Double gain_h3[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable25_IRV26();

  gain_h3[0] = (Double)-tmpIrvIRead[0];
  gain_h3[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable25_IRV27(gain_h3);

  Rte_IWrite_Runnable25_PPort_25_1_element_Interface_25_1_0(gain_h3);

  Rte_IWrite_Runnable25_PPort_25_2_element_Interface_25_2_0(gain_h3);
}

void Runnable26(void)
{
  Double gain_od[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable26_IRV27();

  gain_od[0] = (Double)-tmpIrvIRead[0];
  gain_od[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable26_IRV28(gain_od);

  Rte_IWrite_Runnable26_PPort_26_1_element_Interface_26_1_0(gain_od);

  Rte_IWrite_Runnable26_PPort_26_2_element_Interface_26_2_0(gain_od);
}

void Runnable27(void)
{
  Double gain_nj[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable27_IRV28();

  gain_nj[0] = (Double)-tmpIrvIRead[0];
  gain_nj[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable27_IRV29(gain_nj);

  Rte_IWrite_Runnable27_PPort_27_1_element_Interface_27_1_0(gain_nj);

  Rte_IWrite_Runnable27_PPort_27_2_element_Interface_27_2_0(gain_nj);
}

void Runnable28(void)
{
  Double gain_bc[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable28_IRV29();

  gain_bc[0] = (Double)-tmpIrvIRead[0];
  gain_bc[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable28_IRV30(gain_bc);

  Rte_IWrite_Runnable28_PPort_28_1_element_Interface_28_1_0(gain_bc);

  Rte_IWrite_Runnable28_PPort_28_2_element_Interface_28_2_0(gain_bc);
}

void Runnable29(void)
{
  Double gain_da[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable29_IRV30();

  gain_da[0] = (Double)-tmpIrvIRead[0];
  gain_da[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable29_IRV31(gain_da);

  Rte_IWrite_Runnable29_PPort_29_1_element_Interface_29_1_0(gain_da);

  Rte_IWrite_Runnable29_PPort_29_2_element_Interface_29_2_0(gain_da);
}

void Runnable30(void)
{
  Double gain_g5[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable30_IRV31();

  gain_g5[0] = (Double)-tmpIrvIRead[0];
  gain_g5[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable30_IRV32(gain_g5);

  Rte_IWrite_Runnable30_PPort_30_1_element_Interface_30_1_0(gain_g5);

  Rte_IWrite_Runnable30_PPort_30_2_element_Interface_30_2_0(gain_g5);
}

void Runnable31(void)
{
  Double gain_kp[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable31_IRV32();

  gain_kp[0] = (Double)-tmpIrvIRead[0];
  gain_kp[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable31_IRV33(gain_kp);

  Rte_IWrite_Runnable31_PPort_31_1_element_Interface_31_1_0(gain_kp);

  Rte_IWrite_Runnable31_PPort_31_2_element_Interface_31_2_0(gain_kp);
}

void Runnable32(void)
{
  Double gain_m2[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable32_IRV33();

  gain_m2[0] = (Double)-tmpIrvIRead[0];
  gain_m2[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable32_IRV34(gain_m2);

  Rte_IWrite_Runnable32_PPort_32_1_element_Interface_32_1_0(gain_m2);

  Rte_IWrite_Runnable32_PPort_32_2_element_Interface_32_2_0(gain_m2);
}

void Runnable33(void)
{
  Double gain_ol[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable33_IRV34();

  gain_ol[0] = (Double)-tmpIrvIRead[0];
  gain_ol[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable33_IRV35(gain_ol);

  Rte_IWrite_Runnable33_PPort_33_1_element_Interface_33_1_0(gain_ol);

  Rte_IWrite_Runnable33_PPort_33_2_element_Interface_33_2_0(gain_ol);
}

void Runnable34(void)
{
  Double gain_p2[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable34_IRV35();

  gain_p2[0] = (Double)-tmpIrvIRead[0];
  gain_p2[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable34_IRV36(gain_p2);

  Rte_IWrite_Runnable34_PPort_34_1_element_Interface_34_1_0(gain_p2);

  Rte_IWrite_Runnable34_PPort_34_2_element_Interface_34_2_0(gain_p2);
}

void Runnable35(void)
{
  Double gain_lx[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable35_IRV36();

  gain_lx[0] = (Double)-tmpIrvIRead[0];
  gain_lx[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable35_IRV37(gain_lx);

  Rte_IWrite_Runnable35_PPort_35_1_element_Interface_35_1_0(gain_lx);

  Rte_IWrite_Runnable35_PPort_35_2_element_Interface_35_2_0(gain_lx);
}

void Runnable36(void)
{
  Double gain_m3[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable36_IRV37();

  gain_m3[0] = (Double)-tmpIrvIRead[0];
  gain_m3[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable36_IRV38(gain_m3);

  Rte_IWrite_Runnable36_PPort_36_1_element_Interface_36_1_0(gain_m3);

  Rte_IWrite_Runnable36_PPort_36_2_element_Interface_36_2_0(gain_m3);
}

void Runnable37(void)
{
  Double gain_pp[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable37_IRV38();

  gain_pp[0] = (Double)-tmpIrvIRead[0];
  gain_pp[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable37_IRV39(gain_pp);

  Rte_IWrite_Runnable37_PPort_37_1_element_Interface_37_1_0(gain_pp);

  Rte_IWrite_Runnable37_PPort_37_2_element_Interface_37_2_0(gain_pp);
}

void Runnable38(void)
{
  Double gain_h5[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable38_IRV39();

  gain_h5[0] = (Double)-tmpIrvIRead[0];
  gain_h5[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable38_IRV40(gain_h5);

  Rte_IWrite_Runnable38_PPort_38_1_element_Interface_38_1_0(gain_h5);

  Rte_IWrite_Runnable38_PPort_38_2_element_Interface_38_2_0(gain_h5);
}

void Runnable39(void)
{
  Double gain_cd[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable39_IRV40();

  gain_cd[0] = (Double)-tmpIrvIRead[0];
  gain_cd[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable39_IRV41(gain_cd);

  Rte_IWrite_Runnable39_PPort_39_1_element_Interface_39_1_0(gain_cd);

  Rte_IWrite_Runnable39_PPort_39_2_element_Interface_39_2_0(gain_cd);
}

void Runnable40(void)
{
  Double gain_cy[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable40_IRV41();

  gain_cy[0] = (Double)-tmpIrvIRead[0];
  gain_cy[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable40_IRV42(gain_cy);

  Rte_IWrite_Runnable40_PPort_40_1_element_Interface_40_1_0(gain_cy);

  Rte_IWrite_Runnable40_PPort_40_2_element_Interface_40_2_0(gain_cy);
}

void Runnable41(void)
{
  Double gain_bf[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable41_IRV42();

  gain_bf[0] = (Double)-tmpIrvIRead[0];
  gain_bf[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable41_IRV43(gain_bf);

  Rte_IWrite_Runnable41_PPort_41_1_element_Interface_41_1_0(gain_bf);

  Rte_IWrite_Runnable41_PPort_41_2_element_Interface_41_2_0(gain_bf);
}

void Runnable42(void)
{
  Double gain_ea[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable42_IRV43();

  gain_ea[0] = (Double)-tmpIrvIRead[0];
  gain_ea[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable42_IRV44(gain_ea);

  Rte_IWrite_Runnable42_PPort_42_1_element_Interface_42_1_0(gain_ea);

  Rte_IWrite_Runnable42_PPort_42_2_element_Interface_42_2_0(gain_ea);
}

void Runnable43(void)
{
  Double gain_gy[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable43_IRV44();

  gain_gy[0] = (Double)-tmpIrvIRead[0];
  gain_gy[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable43_IRV45(gain_gy);

  Rte_IWrite_Runnable43_PPort_43_1_element_Interface_43_1_0(gain_gy);

  Rte_IWrite_Runnable43_PPort_43_2_element_Interface_43_2_0(gain_gy);
}

void Runnable44(void)
{
  Double gain_f1[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable44_IRV45();

  gain_f1[0] = (Double)-tmpIrvIRead[0];
  gain_f1[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable44_IRV46(gain_f1);

  Rte_IWrite_Runnable44_PPort_44_1_element_Interface_44_1_0(gain_f1);

  Rte_IWrite_Runnable44_PPort_44_2_element_Interface_44_2_0(gain_f1);
}

void Runnable45(void)
{
  Double gain_jz[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable45_IRV46();

  gain_jz[0] = (Double)-tmpIrvIRead[0];
  gain_jz[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable45_IRV47(gain_jz);

  Rte_IWrite_Runnable45_PPort_45_1_element_Interface_45_1_0(gain_jz);

  Rte_IWrite_Runnable45_PPort_45_2_element_Interface_45_2_0(gain_jz);
}

void Runnable46(void)
{
  Double gain_dm[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable46_IRV47();

  gain_dm[0] = (Double)-tmpIrvIRead[0];
  gain_dm[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable46_IRV48(gain_dm);

  Rte_IWrite_Runnable46_PPort_46_1_element_Interface_46_1_0(gain_dm);

  Rte_IWrite_Runnable46_PPort_46_2_element_Interface_46_2_0(gain_dm);
}

void Runnable47(void)
{
  Double gain_b5[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable47_IRV48();

  gain_b5[0] = (Double)-tmpIrvIRead[0];
  gain_b5[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable47_IRV49(gain_b5);

  Rte_IWrite_Runnable47_PPort_47_1_element_Interface_47_1_0(gain_b5);

  Rte_IWrite_Runnable47_PPort_47_2_element_Interface_47_2_0(gain_b5);
}

void Runnable48(void)
{
  Double gain_pz[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable48_IRV49();

  gain_pz[0] = (Double)-tmpIrvIRead[0];
  gain_pz[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable48_IRV50(gain_pz);

  Rte_IWrite_Runnable48_PPort_48_1_element_Interface_48_1_0(gain_pz);

  Rte_IWrite_Runnable48_PPort_48_2_element_Interface_48_2_0(gain_pz);
}

void Runnable49(void)
{
  Double gain_hy[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable49_IRV50();

  gain_hy[0] = (Double)-tmpIrvIRead[0];
  gain_hy[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable49_IRV51(gain_hy);

  Rte_IWrite_Runnable49_PPort_49_1_element_Interface_49_1_0(gain_hy);

  Rte_IWrite_Runnable49_PPort_49_2_element_Interface_49_2_0(gain_hy);
}

void Runnable50(void)
{
  Double gain_ae[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable50_IRV51();

  gain_ae[0] = (Double)-tmpIrvIRead[0];
  gain_ae[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable50_IRV52(gain_ae);

  Rte_IWrite_Runnable50_PPort_50_1_element_Interface_50_1_0(gain_ae);

  Rte_IWrite_Runnable50_PPort_50_2_element_Interface_50_2_0(gain_ae);
}

void Runnable51(void)
{
  Double gain_aa[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable51_IRV52();

  gain_aa[0] = (Double)-tmpIrvIRead[0];
  gain_aa[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable51_IRV53(gain_aa);

  Rte_IWrite_Runnable51_PPort_51_1_element_Interface_51_1_0(gain_aa);

  Rte_IWrite_Runnable51_PPort_51_2_element_Interface_51_2_0(gain_aa);
}

void Runnable52(void)
{
  Double gain_as[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable52_IRV53();

  gain_as[0] = (Double)-tmpIrvIRead[0];
  gain_as[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable52_IRV54(gain_as);

  Rte_IWrite_Runnable52_PPort_52_1_element_Interface_52_1_0(gain_as);

  Rte_IWrite_Runnable52_PPort_52_2_element_Interface_52_2_0(gain_as);
}

void Runnable53(void)
{
  Double gain_hh[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable53_IRV54();

  gain_hh[0] = (Double)-tmpIrvIRead[0];
  gain_hh[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable53_IRV55(gain_hh);

  Rte_IWrite_Runnable53_PPort_53_1_element_Interface_53_1_0(gain_hh);

  Rte_IWrite_Runnable53_PPort_53_2_element_Interface_53_2_0(gain_hh);
}

void Runnable54(void)
{
  Double gain_nl[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable54_IRV55();

  gain_nl[0] = (Double)-tmpIrvIRead[0];
  gain_nl[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable54_IRV56(gain_nl);

  Rte_IWrite_Runnable54_PPort_54_1_element_Interface_54_1_0(gain_nl);

  Rte_IWrite_Runnable54_PPort_54_2_element_Interface_54_2_0(gain_nl);
}

void Runnable55(void)
{
  Double gain_kk[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable55_IRV56();

  gain_kk[0] = (Double)-tmpIrvIRead[0];
  gain_kk[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable55_IRV57(gain_kk);

  Rte_IWrite_Runnable55_PPort_55_1_element_Interface_55_1_0(gain_kk);

  Rte_IWrite_Runnable55_PPort_55_2_element_Interface_55_2_0(gain_kk);
}

void Runnable56(void)
{
  Double gain_pg[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable56_IRV57();

  gain_pg[0] = (Double)-tmpIrvIRead[0];
  gain_pg[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable56_IRV58(gain_pg);

  Rte_IWrite_Runnable56_PPort_56_1_element_Interface_56_1_0(gain_pg);

  Rte_IWrite_Runnable56_PPort_56_2_element_Interface_56_2_0(gain_pg);
}

void Runnable57(void)
{
  Double gain_jf[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable57_IRV58();

  gain_jf[0] = (Double)-tmpIrvIRead[0];
  gain_jf[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable57_IRV59(gain_jf);

  Rte_IWrite_Runnable57_PPort_57_1_element_Interface_57_1_0(gain_jf);

  Rte_IWrite_Runnable57_PPort_57_2_element_Interface_57_2_0(gain_jf);
}

void Runnable58(void)
{
  Double gain_mw[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable58_IRV59();

  gain_mw[0] = (Double)-tmpIrvIRead[0];
  gain_mw[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable58_IRV60(gain_mw);

  Rte_IWrite_Runnable58_PPort_58_1_element_Interface_58_1_0(gain_mw);

  Rte_IWrite_Runnable58_PPort_58_2_element_Interface_58_2_0(gain_mw);
}

void Runnable59(void)
{
  Double gain_eh[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable59_IRV60();

  gain_eh[0] = (Double)-tmpIrvIRead[0];
  gain_eh[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable59_IRV61(gain_eh);

  Rte_IWrite_Runnable59_PPort_59_1_element_Interface_59_1_0(gain_eh);

  Rte_IWrite_Runnable59_PPort_59_2_element_Interface_59_2_0(gain_eh);
}

void Runnable60(void)
{
  Double gain_br[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable60_IRV61();

  gain_br[0] = (Double)-tmpIrvIRead[0];
  gain_br[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable60_IRV62(gain_br);

  Rte_IWrite_Runnable60_PPort_60_1_element_Interface_60_1_0(gain_br);

  Rte_IWrite_Runnable60_PPort_60_2_element_Interface_60_2_0(gain_br);
}

void Runnable61(void)
{
  Double gain_ld[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable61_IRV62();

  gain_ld[0] = (Double)-tmpIrvIRead[0];
  gain_ld[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable61_IRV63(gain_ld);

  Rte_IWrite_Runnable61_PPort_61_1_element_Interface_61_1_0(gain_ld);

  Rte_IWrite_Runnable61_PPort_61_2_element_Interface_61_2_0(gain_ld);
}

void Runnable62(void)
{
  Double gain_ik[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable62_IRV63();

  gain_ik[0] = (Double)-tmpIrvIRead[0];
  gain_ik[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable62_IRV64(gain_ik);

  Rte_IWrite_Runnable62_PPort_62_1_element_Interface_62_1_0(gain_ik);

  Rte_IWrite_Runnable62_PPort_62_2_element_Interface_62_2_0(gain_ik);
}

void Runnable63(void)
{
  Double gain_oj[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable63_IRV64();

  gain_oj[0] = (Double)-tmpIrvIRead[0];
  gain_oj[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable63_IRV65(gain_oj);

  Rte_IWrite_Runnable63_PPort_63_1_element_Interface_63_1_0(gain_oj);

  Rte_IWrite_Runnable63_PPort_63_2_element_Interface_63_2_0(gain_oj);
}

void Runnable64(void)
{
  Double gain_dh[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable64_IRV65();

  gain_dh[0] = (Double)-tmpIrvIRead[0];
  gain_dh[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable64_IRV66(gain_dh);

  Rte_IWrite_Runnable64_PPort_64_1_element_Interface_64_1_0(gain_dh);

  Rte_IWrite_Runnable64_PPort_64_2_element_Interface_64_2_0(gain_dh);
}

void Runnable65(void)
{
  Double gain_nr[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable65_IRV66();

  gain_nr[0] = (Double)-tmpIrvIRead[0];
  gain_nr[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable65_IRV67(gain_nr);

  Rte_IWrite_Runnable65_PPort_65_1_element_Interface_65_1_0(gain_nr);

  Rte_IWrite_Runnable65_PPort_65_2_element_Interface_65_2_0(gain_nr);
}

void Runnable66(void)
{
  Double gain_ib[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable66_IRV67();

  gain_ib[0] = (Double)-tmpIrvIRead[0];
  gain_ib[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable66_IRV68(gain_ib);

  Rte_IWrite_Runnable66_PPort_66_1_element_Interface_66_1_0(gain_ib);

  Rte_IWrite_Runnable66_PPort_66_2_element_Interface_66_2_0(gain_ib);
}

void Runnable67(void)
{
  Double gain_hk[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable67_IRV68();

  gain_hk[0] = (Double)-tmpIrvIRead[0];
  gain_hk[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable67_IRV69(gain_hk);

  Rte_IWrite_Runnable67_PPort_67_1_element_Interface_67_1_0(gain_hk);

  Rte_IWrite_Runnable67_PPort_67_2_element_Interface_67_2_0(gain_hk);
}

void Runnable68(void)
{
  Double gain_fd[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable68_IRV69();

  gain_fd[0] = (Double)-tmpIrvIRead[0];
  gain_fd[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable68_IRV70(gain_fd);

  Rte_IWrite_Runnable68_PPort_68_1_element_Interface_68_1_0(gain_fd);

  Rte_IWrite_Runnable68_PPort_68_2_element_Interface_68_2_0(gain_fd);
}

void Runnable69(void)
{
  Double gain_ch[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable69_IRV70();

  gain_ch[0] = (Double)-tmpIrvIRead[0];
  gain_ch[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable69_IRV71(gain_ch);

  Rte_IWrite_Runnable69_PPort_69_1_element_Interface_69_1_0(gain_ch);

  Rte_IWrite_Runnable69_PPort_69_2_element_Interface_69_2_0(gain_ch);
}

void Runnable70(void)
{
  Double gain_jo[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable70_IRV71();

  gain_jo[0] = (Double)-tmpIrvIRead[0];
  gain_jo[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable70_IRV72(gain_jo);

  Rte_IWrite_Runnable70_PPort_70_1_element_Interface_70_1_0(gain_jo);

  Rte_IWrite_Runnable70_PPort_70_2_element_Interface_70_2_0(gain_jo);
}

void Runnable71(void)
{
  Double gain_dy[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable71_IRV72();

  gain_dy[0] = (Double)-tmpIrvIRead[0];
  gain_dy[1] = (Double)-tmpIrvIRead[1];
  Rte_IrvIWrite_Runnable71_IRV73(gain_dy);

  Rte_IWrite_Runnable71_PPort_71_1_element_Interface_71_1_0(gain_dy);

  Rte_IWrite_Runnable71_PPort_71_2_element_Interface_71_2_0(gain_dy);
}

void Runnable72(void)
{
  Double gain_fb[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable72_IRV73();

  gain_fb[0] = (Double)-tmpIrvIRead[0];
  gain_fb[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable72_IRV74(gain_fb);

  Rte_IWrite_Runnable72_PPort_72_1_element_Interface_72_1_0(gain_fb);

  Rte_IWrite_Runnable72_PPort_72_2_element_Interface_72_2_0(gain_fb);
}

void Runnable73(void)
{
  Double gain_ix[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable73_IRV74();
  gain_ix[0] = (Double)-tmpIrvIRead[0];
  gain_ix[1] = (Double)-tmpIrvIRead[1];
  Rte_IrvIWrite_Runnable73_IRV75(gain_ix);

  Rte_IWrite_Runnable73_PPort_73_1_element_Interface_73_1_0(gain_ix);

  Rte_IWrite_Runnable73_PPort_73_2_element_Interface_73_2_0(gain_ix);
}

void Runnable74(void)
{
  Double gain_i3[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable74_IRV75();

  gain_i3[0] = (Double)-tmpIrvIRead[0];
  gain_i3[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable74_IRV76(gain_i3);

  Rte_IWrite_Runnable74_PPort_74_1_element_Interface_74_1_0(gain_i3);

  Rte_IWrite_Runnable74_PPort_74_2_element_Interface_74_2_0(gain_i3);
}

void Runnable75(void)
{
  Double gain_f5[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable75_IRV76();

  gain_f5[0] = (Double)-tmpIrvIRead[0];
  gain_f5[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable75_IRV77(gain_f5);

  Rte_IWrite_Runnable75_PPort_75_1_element_Interface_75_1_0(gain_f5);

  Rte_IWrite_Runnable75_PPort_75_2_element_Interface_75_2_0(gain_f5);
}

void Runnable76(void)
{
  Double gain_ex[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable76_IRV77();

  gain_ex[0] = (Double)-tmpIrvIRead[0];
  gain_ex[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable76_IRV78(gain_ex);

  Rte_IWrite_Runnable76_PPort_76_1_element_Interface_76_1_0(gain_ex);

  Rte_IWrite_Runnable76_PPort_76_2_element_Interface_76_2_0(gain_ex);
}

void Runnable77(void)
{
  Double gain_e[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable77_IRV78();

  gain_e[0] = (Double)-tmpIrvIRead[0];
  gain_e[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable77_IRV79(gain_e);

  Rte_IWrite_Runnable77_PPort_77_1_element_Interface_77_1_0(gain_e);

  Rte_IWrite_Runnable77_PPort_77_2_element_Interface_77_2_0(gain_e);
}

void Runnable78(void)
{
  Double gain_mc[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable78_IRV79();

  gain_mc[0] = (Double)-tmpIrvIRead[0];
  gain_mc[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable78_IRV80(gain_mc);

  Rte_IWrite_Runnable78_PPort_78_1_element_Interface_78_1_0(gain_mc);

  Rte_IWrite_Runnable78_PPort_78_2_element_Interface_78_2_0(gain_mc);
}

void Runnable79(void)
{
  Double gain_otp[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable79_IRV80();

  gain_otp[0] = (Double)-tmpIrvIRead[0];
  gain_otp[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable79_IRV81(gain_otp);

  Rte_IWrite_Runnable79_PPort_79_1_element_Interface_79_1_0(gain_otp);

  Rte_IWrite_Runnable79_PPort_79_2_element_Interface_79_2_0(gain_otp);
}

void Runnable80(void)
{
  Double gain_lu[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable80_IRV81();

  gain_lu[0] = (Double)-tmpIrvIRead[0];
  gain_lu[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable80_IRV82(gain_lu);

  Rte_IWrite_Runnable80_PPort_80_1_element_Interface_80_1_0(gain_lu);

  Rte_IWrite_Runnable80_PPort_80_2_element_Interface_80_2_0(gain_lu);
}

void Runnable81(void)
{
  Double gain_i[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable81_IRV82();

  gain_i[0] = (Double)-tmpIrvIRead[0];
  gain_i[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable81_IRV83(gain_i);

  Rte_IWrite_Runnable81_PPort_81_1_element_Interface_81_1_0(gain_i);

  Rte_IWrite_Runnable81_PPort_81_2_element_Interface_81_2_0(gain_i);
}

void Runnable82(void)
{
  Double gain_k[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable82_IRV83();

  gain_k[0] = (Double)-tmpIrvIRead[0];
  gain_k[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable82_IRV84(gain_k);

  Rte_IWrite_Runnable82_PPort_82_1_element_Interface_82_1_0(gain_k);

  Rte_IWrite_Runnable82_PPort_82_2_element_Interface_82_2_0(gain_k);
}

void Runnable83(void)
{
  Double gain_pf[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable83_IRV84();

  gain_pf[0] = (Double)-tmpIrvIRead[0];
  gain_pf[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable83_IRV85(gain_pf);

  Rte_IWrite_Runnable83_PPort_83_1_element_Interface_83_1_0(gain_pf);

  Rte_IWrite_Runnable83_PPort_83_2_element_Interface_83_2_0(gain_pf);
}

void Runnable84(void)
{
  Double gain_j[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable84_IRV85();

  gain_j[0] = (Double)-tmpIrvIRead[0];
  gain_j[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable84_IRV86(gain_j);

  Rte_IWrite_Runnable84_PPort_84_1_element_Interface_84_1_0(gain_j);

  Rte_IWrite_Runnable84_PPort_84_2_element_Interface_84_2_0(gain_j);
}

void Runnable85(void)
{
  Double gain_d0[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable85_IRV86();

  gain_d0[0] = (Double)-tmpIrvIRead[0];
  gain_d0[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable85_IRV87(gain_d0);

  Rte_IWrite_Runnable85_PPort_85_1_element_Interface_85_1_0(gain_d0);

  Rte_IWrite_Runnable85_PPort_85_2_element_Interface_85_2_0(gain_d0);
}

void Runnable86(void)
{
  Double gain_l[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable86_IRV87();

  gain_l[0] = (Double)-tmpIrvIRead[0];
  gain_l[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable86_IRV88(gain_l);

  Rte_IWrite_Runnable86_PPort_86_1_element_Interface_86_1_0(gain_l);

  Rte_IWrite_Runnable86_PPort_86_2_element_Interface_86_2_0(gain_l);
}

void Runnable87(void)
{
  Double gain_p[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable87_IRV88();

  gain_p[0] = (Double)-tmpIrvIRead[0];
  gain_p[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable87_IRV89(gain_p);

  Rte_IWrite_Runnable87_PPort_87_1_element_Interface_87_1_0(gain_p);

  Rte_IWrite_Runnable87_PPort_87_2_element_Interface_87_2_0(gain_p);
}

void Runnable88(void)
{
  Double gain_fz[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable88_IRV89();

  gain_fz[0] = (Double)-tmpIrvIRead[0];
  gain_fz[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable88_IRV90(gain_fz);

  Rte_IWrite_Runnable88_PPort_88_1_element_Interface_88_1_0(gain_fz);

  Rte_IWrite_Runnable88_PPort_88_2_element_Interface_88_2_0(gain_fz);
}

void Runnable89(void)
{
  Double gain_m[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable89_IRV90();

  gain_m[0] = (Double)-tmpIrvIRead[0];
  gain_m[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable89_IRV91(gain_m);

  Rte_IWrite_Runnable89_PPort_89_1_element_Interface_89_1_0(gain_m);

  Rte_IWrite_Runnable89_PPort_89_2_element_Interface_89_2_0(gain_m);
}

void Runnable90(void)
{
  Double gain_f[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable90_IRV91();

  gain_f[0] = (Double)-tmpIrvIRead[0];
  gain_f[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable90_IRV92(gain_f);

  Rte_IWrite_Runnable90_PPort_90_1_element_Interface_90_1_0(gain_f);

  Rte_IWrite_Runnable90_PPort_90_2_element_Interface_90_2_0(gain_f);
}

void Runnable91(void)
{
  Double gain_os[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable91_IRV92();

  gain_os[0] = (Double)-tmpIrvIRead[0];
  gain_os[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable91_IRV93(gain_os);

  Rte_IWrite_Runnable91_PPort_91_1_element_Interface_91_1_0(gain_os);

  Rte_IWrite_Runnable91_PPort_91_2_element_Interface_91_2_0(gain_os);
}

void Runnable92(void)
{
  Double gain_nz[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable92_IRV93();

  gain_nz[0] = (Double)-tmpIrvIRead[0];
  gain_nz[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable92_IRV94(gain_nz);

  Rte_IWrite_Runnable92_PPort_92_1_element_Interface_92_1_0(gain_nz);

  Rte_IWrite_Runnable92_PPort_92_2_element_Interface_92_2_0(gain_nz);
}

void Runnable93(void)
{
  Double gain_ot[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable93_IRV94();

  gain_ot[0] = (Double)-tmpIrvIRead[0];
  gain_ot[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable93_IRV95(gain_ot);

  Rte_IWrite_Runnable93_PPort_93_1_element_Interface_93_1_0(gain_ot);

  Rte_IWrite_Runnable93_PPort_93_2_element_Interface_93_2_0(gain_ot);
}

void Runnable94(void)
{
  Double gain_n[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable94_IRV95();

  gain_n[0] = (Double)-tmpIrvIRead[0];
  gain_n[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable94_IRV96(gain_n);

  Rte_IWrite_Runnable94_PPort_94_1_element_Interface_94_1_0(gain_n);

  Rte_IWrite_Runnable94_PPort_94_2_element_Interface_94_2_0(gain_n);
}

void Runnable95(void)
{
  Double gain_ca[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable95_IRV96();

  gain_ca[0] = (Double)-tmpIrvIRead[0];
  gain_ca[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable95_IRV97(gain_ca);

  Rte_IWrite_Runnable95_PPort_95_1_element_Interface_95_1_0(gain_ca);

  Rte_IWrite_Runnable95_PPort_95_2_element_Interface_95_2_0(gain_ca);
}

void Runnable96(void)
{
  Double gain_g[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable96_IRV97();

  gain_g[0] = (Double)-tmpIrvIRead[0];
  gain_g[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable96_IRV98(gain_g);

  Rte_IWrite_Runnable96_PPort_96_1_element_Interface_96_1_0(gain_g);

  Rte_IWrite_Runnable96_PPort_96_2_element_Interface_96_2_0(gain_g);
}

void Runnable97(void)
{
  Double gain_d[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable97_IRV98();

  gain_d[0] = (Double)-tmpIrvIRead[0];
  gain_d[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable97_IRV99(gain_d);

  Rte_IWrite_Runnable97_PPort_97_1_element_Interface_97_1_0(gain_d);

  Rte_IWrite_Runnable97_PPort_97_2_element_Interface_97_2_0(gain_d);
}

void Runnable98(void)
{
  Double gain_o[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable98_IRV99();

  gain_o[0] = (Double)-tmpIrvIRead[0];
  gain_o[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable98_IRV100(gain_o);

  Rte_IWrite_Runnable98_PPort_98_1_element_Interface_98_1_0(gain_o);

  Rte_IWrite_Runnable98_PPort_98_2_element_Interface_98_2_0(gain_o);
}

void Runnable99(void)
{
  Double gain_c[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable99_IRV100();

  gain_c[0] = (Double)-tmpIrvIRead[0];
  gain_c[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable99_IRV101(gain_c);

  Rte_IWrite_Runnable99_PPort_99_1_element_Interface_99_1_0(gain_c);

  Rte_IWrite_Runnable99_PPort_99_2_element_Interface_99_2_0(gain_c);
}

void Runnable100(void)
{
  Double gain_gg[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable100_IRV101();

  gain_gg[0] = (Double)-tmpIrvIRead[0];
  gain_gg[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable100_IRV102(gain_gg);

  Rte_IWrite_Runnable100_PPort_100_1_element_Interface_100_1_0(gain_gg);

  Rte_IWrite_Runnable100_PPort_100_2_element_Interface_100_2_0(gain_gg);
}

void Runnable101(void)
{
  Double gain_il[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable101_IRV102();

  gain_il[0] = (Double)-tmpIrvIRead[0];
  gain_il[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable101_IRV103(gain_il);

  Rte_IWrite_Runnable101_PPort_101_1_element_Interface_101_1_0(gain_il);

  Rte_IWrite_Runnable101_PPort_101_2_element_Interface_101_2_0(gain_il);
}

void Runnable102(void)
{
  Double gain_l4[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable102_IRV103();

  gain_l4[0] = (Double)-tmpIrvIRead[0];
  gain_l4[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable102_IRV104(gain_l4);

  Rte_IWrite_Runnable102_PPort_102_1_element_Interface_102_1_0(gain_l4);

  Rte_IWrite_Runnable102_PPort_102_2_element_Interface_102_2_0(gain_l4);
}

void Runnable103(void)
{
  Double gain_ah[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable103_IRV104();

  gain_ah[0] = (Double)-tmpIrvIRead[0];
  gain_ah[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable103_IRV105(gain_ah);

  Rte_IWrite_Runnable103_PPort_103_1_element_Interface_103_1_0(gain_ah);

  Rte_IWrite_Runnable103_PPort_103_2_element_Interface_103_2_0(gain_ah);
}

void Runnable104(void)
{
  Double gain_pr[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable104_IRV105();

  gain_pr[0] = (Double)-tmpIrvIRead[0];
  gain_pr[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable104_IRV106(gain_pr);

  Rte_IWrite_Runnable104_PPort_104_1_element_Interface_104_1_0(gain_pr);

  Rte_IWrite_Runnable104_PPort_104_2_element_Interface_104_2_0(gain_pr);
}

void Runnable105(void)
{
  Double gain_dyq[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable105_IRV106();

  gain_dyq[0] = (Double)-tmpIrvIRead[0];
  gain_dyq[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable105_IRV107(gain_dyq);

  Rte_IWrite_Runnable105_PPort_105_1_element_Interface_105_1_0(gain_dyq);

  Rte_IWrite_Runnable105_PPort_105_2_element_Interface_105_2_0(gain_dyq);
}

void Runnable106(void)
{
  Double gain_ne[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable106_IRV107();

  gain_ne[0] = (Double)-tmpIrvIRead[0];
  gain_ne[1] = (Double)-tmpIrvIRead[1];

  Rte_IrvIWrite_Runnable106_IRV108(gain_ne);

  Rte_IWrite_Runnable106_PPort_106_1_element_Interface_106_1_0(gain_ne);

  Rte_IWrite_Runnable106_PPort_106_2_element_Interface_106_2_0(gain_ne);
}

void Runnable107(void) Double gain_ma[2];
const Double *tmpIrvIRead;

tmpIrvIRead = Rte_IrvIRead_Runnable107_IRV108();

gain_ma[0] = (Double)-tmpIrvIRead[0];
gain_ma[1] = (Double)-tmpIrvIRead[1];

Rte_IrvIWrite_Runnable107_IRV109(gain_ma);

Rte_IWrite_Runnable107_PPort_107_1_element_Interface_107_1_0(gain_ma);

Rte_IWrite_Runnable107_PPort_107_2_element_Interface_107_2_0(gain_ma);
}

void Runnable108(void)
{
  Double gain_og[2];
  const Double *tmpIrvIRead;

  tmpIrvIRead = Rte_IrvIRead_Runnable108_IRV109();

  gain_og[0] = (Double)-tmpIrvIRead[0];
  gain_og[1] = (Double)-tmpIrvIRead[1];

  Rte_IWrite_Runnable108_PPort_108_1_element_Interface_108_1_0(gain_og);

  Rte_IWrite_Runnable108_PPort_108_2_element_Interface_108_2_0(gain_og);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
