/*
 * File: large_scale_autosar_swc_expfcns.h
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

#ifndef RTW_HEADER_large_scale_autosar_swc_expfcns_h_
#define RTW_HEADER_large_scale_autosar_swc_expfcns_h_
#ifndef large_scale_autosar_swc_expfcns_COMMON_INCLUDES_
#define large_scale_autosar_swc_expfcns_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "Rte_ASWC.h"
#endif                    /* large_scale_autosar_swc_expfcns_COMMON_INCLUDES_ */

/* Model Code Variants */

/* Macros for accessing real-time model data structure */

/* Block signals (default storage) */
typedef struct tag_BlockIO {
  float64 Add;                         /* '<S109>/Add' */
} BlockIO;

/* Block states (default storage) for system '<Root>' */
typedef struct tag_D_Work {
  float64 DiscreteTimeIntegrator_DSTATE;/* '<S31>/Discrete-Time Integrator' */
  sint8 Delay_DSTATE;                  /* '<S42>/Delay' */
  sint8 Delay_DSTATE_m[2];             /* '<S31>/Delay' */
  sint8 Delay_DSTATE_a;                /* '<S20>/Delay' */
} D_Work;

/* Block signals (default storage) */
extern BlockIO rtB;

/* Block states (default storage) */
extern D_Work rtDWork;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'large_scale_autosar_swc_expfcns'
 * '<S1>'   : 'large_scale_autosar_swc_expfcns/Runnable100_subsystem'
 * '<S2>'   : 'large_scale_autosar_swc_expfcns/Runnable101_subsystem'
 * '<S3>'   : 'large_scale_autosar_swc_expfcns/Runnable102_subsystem'
 * '<S4>'   : 'large_scale_autosar_swc_expfcns/Runnable103_subsystem'
 * '<S5>'   : 'large_scale_autosar_swc_expfcns/Runnable104_subsystem'
 * '<S6>'   : 'large_scale_autosar_swc_expfcns/Runnable105_subsystem'
 * '<S7>'   : 'large_scale_autosar_swc_expfcns/Runnable106_subsystem'
 * '<S8>'   : 'large_scale_autosar_swc_expfcns/Runnable107_subsystem'
 * '<S9>'   : 'large_scale_autosar_swc_expfcns/Runnable108_subsystem'
 * '<S10>'  : 'large_scale_autosar_swc_expfcns/Runnable10_subsystem'
 * '<S11>'  : 'large_scale_autosar_swc_expfcns/Runnable11_subsystem'
 * '<S12>'  : 'large_scale_autosar_swc_expfcns/Runnable12_subsystem'
 * '<S13>'  : 'large_scale_autosar_swc_expfcns/Runnable13_subsystem'
 * '<S14>'  : 'large_scale_autosar_swc_expfcns/Runnable14_subsystem'
 * '<S15>'  : 'large_scale_autosar_swc_expfcns/Runnable15_subsystem'
 * '<S16>'  : 'large_scale_autosar_swc_expfcns/Runnable16_subsystem'
 * '<S17>'  : 'large_scale_autosar_swc_expfcns/Runnable17_subsystem'
 * '<S18>'  : 'large_scale_autosar_swc_expfcns/Runnable18_subsystem'
 * '<S19>'  : 'large_scale_autosar_swc_expfcns/Runnable19_subsystem'
 * '<S20>'  : 'large_scale_autosar_swc_expfcns/Runnable1_subsystem'
 * '<S21>'  : 'large_scale_autosar_swc_expfcns/Runnable20_subsystem'
 * '<S22>'  : 'large_scale_autosar_swc_expfcns/Runnable21_subsystem'
 * '<S23>'  : 'large_scale_autosar_swc_expfcns/Runnable22_subsystem'
 * '<S24>'  : 'large_scale_autosar_swc_expfcns/Runnable23_subsystem'
 * '<S25>'  : 'large_scale_autosar_swc_expfcns/Runnable24_subsystem'
 * '<S26>'  : 'large_scale_autosar_swc_expfcns/Runnable25_subsystem'
 * '<S27>'  : 'large_scale_autosar_swc_expfcns/Runnable26_subsystem'
 * '<S28>'  : 'large_scale_autosar_swc_expfcns/Runnable27_subsystem'
 * '<S29>'  : 'large_scale_autosar_swc_expfcns/Runnable28_subsystem'
 * '<S30>'  : 'large_scale_autosar_swc_expfcns/Runnable29_subsystem'
 * '<S31>'  : 'large_scale_autosar_swc_expfcns/Runnable2_subsystem'
 * '<S32>'  : 'large_scale_autosar_swc_expfcns/Runnable30_subsystem'
 * '<S33>'  : 'large_scale_autosar_swc_expfcns/Runnable31_subsystem'
 * '<S34>'  : 'large_scale_autosar_swc_expfcns/Runnable32_subsystem'
 * '<S35>'  : 'large_scale_autosar_swc_expfcns/Runnable33_subsystem'
 * '<S36>'  : 'large_scale_autosar_swc_expfcns/Runnable34_subsystem'
 * '<S37>'  : 'large_scale_autosar_swc_expfcns/Runnable35_subsystem'
 * '<S38>'  : 'large_scale_autosar_swc_expfcns/Runnable36_subsystem'
 * '<S39>'  : 'large_scale_autosar_swc_expfcns/Runnable37_subsystem'
 * '<S40>'  : 'large_scale_autosar_swc_expfcns/Runnable38_subsystem'
 * '<S41>'  : 'large_scale_autosar_swc_expfcns/Runnable39_subsystem'
 * '<S42>'  : 'large_scale_autosar_swc_expfcns/Runnable3_subsystem'
 * '<S43>'  : 'large_scale_autosar_swc_expfcns/Runnable40_subsystem'
 * '<S44>'  : 'large_scale_autosar_swc_expfcns/Runnable41_subsystem'
 * '<S45>'  : 'large_scale_autosar_swc_expfcns/Runnable42_subsystem'
 * '<S46>'  : 'large_scale_autosar_swc_expfcns/Runnable43_subsystem'
 * '<S47>'  : 'large_scale_autosar_swc_expfcns/Runnable44_subsystem1'
 * '<S48>'  : 'large_scale_autosar_swc_expfcns/Runnable45_subsystem'
 * '<S49>'  : 'large_scale_autosar_swc_expfcns/Runnable46_subsystem'
 * '<S50>'  : 'large_scale_autosar_swc_expfcns/Runnable47_subsystem'
 * '<S51>'  : 'large_scale_autosar_swc_expfcns/Runnable48_subsystem'
 * '<S52>'  : 'large_scale_autosar_swc_expfcns/Runnable49_subsystem'
 * '<S53>'  : 'large_scale_autosar_swc_expfcns/Runnable4_subsystem'
 * '<S54>'  : 'large_scale_autosar_swc_expfcns/Runnable50_subsystem1'
 * '<S55>'  : 'large_scale_autosar_swc_expfcns/Runnable51_subsystem2'
 * '<S56>'  : 'large_scale_autosar_swc_expfcns/Runnable52_subsystem2'
 * '<S57>'  : 'large_scale_autosar_swc_expfcns/Runnable53_subsystem2'
 * '<S58>'  : 'large_scale_autosar_swc_expfcns/Runnable54_subsystem2'
 * '<S59>'  : 'large_scale_autosar_swc_expfcns/Runnable55_subsystem2'
 * '<S60>'  : 'large_scale_autosar_swc_expfcns/Runnable56_subsystem2'
 * '<S61>'  : 'large_scale_autosar_swc_expfcns/Runnable57_subsystem2'
 * '<S62>'  : 'large_scale_autosar_swc_expfcns/Runnable58_subsystem2'
 * '<S63>'  : 'large_scale_autosar_swc_expfcns/Runnable59_subsystem2'
 * '<S64>'  : 'large_scale_autosar_swc_expfcns/Runnable5_subsystem'
 * '<S65>'  : 'large_scale_autosar_swc_expfcns/Runnable60_subsystem2'
 * '<S66>'  : 'large_scale_autosar_swc_expfcns/Runnable61_subsystem'
 * '<S67>'  : 'large_scale_autosar_swc_expfcns/Runnable62_subsystem'
 * '<S68>'  : 'large_scale_autosar_swc_expfcns/Runnable63_subsystem'
 * '<S69>'  : 'large_scale_autosar_swc_expfcns/Runnable64_subsystem'
 * '<S70>'  : 'large_scale_autosar_swc_expfcns/Runnable65_subsystem'
 * '<S71>'  : 'large_scale_autosar_swc_expfcns/Runnable66_subsystem3'
 * '<S72>'  : 'large_scale_autosar_swc_expfcns/Runnable67_subsystem'
 * '<S73>'  : 'large_scale_autosar_swc_expfcns/Runnable68_subsystem'
 * '<S74>'  : 'large_scale_autosar_swc_expfcns/Runnable69_subsystem'
 * '<S75>'  : 'large_scale_autosar_swc_expfcns/Runnable6_subsystem'
 * '<S76>'  : 'large_scale_autosar_swc_expfcns/Runnable70_subsystem'
 * '<S77>'  : 'large_scale_autosar_swc_expfcns/Runnable71_subsystem'
 * '<S78>'  : 'large_scale_autosar_swc_expfcns/Runnable72_subsystem'
 * '<S79>'  : 'large_scale_autosar_swc_expfcns/Runnable73_subsystem'
 * '<S80>'  : 'large_scale_autosar_swc_expfcns/Runnable74_subsystem'
 * '<S81>'  : 'large_scale_autosar_swc_expfcns/Runnable75_subsystem'
 * '<S82>'  : 'large_scale_autosar_swc_expfcns/Runnable76_subsystem'
 * '<S83>'  : 'large_scale_autosar_swc_expfcns/Runnable77_subsystem'
 * '<S84>'  : 'large_scale_autosar_swc_expfcns/Runnable78_subsystem'
 * '<S85>'  : 'large_scale_autosar_swc_expfcns/Runnable79_subsystem'
 * '<S86>'  : 'large_scale_autosar_swc_expfcns/Runnable7_subsystem'
 * '<S87>'  : 'large_scale_autosar_swc_expfcns/Runnable80_subsystem'
 * '<S88>'  : 'large_scale_autosar_swc_expfcns/Runnable81_subsystem'
 * '<S89>'  : 'large_scale_autosar_swc_expfcns/Runnable82_subsystem'
 * '<S90>'  : 'large_scale_autosar_swc_expfcns/Runnable83_subsystem'
 * '<S91>'  : 'large_scale_autosar_swc_expfcns/Runnable84_subsystem'
 * '<S92>'  : 'large_scale_autosar_swc_expfcns/Runnable85_subsystem'
 * '<S93>'  : 'large_scale_autosar_swc_expfcns/Runnable86_subsystem'
 * '<S94>'  : 'large_scale_autosar_swc_expfcns/Runnable87_subsystem'
 * '<S95>'  : 'large_scale_autosar_swc_expfcns/Runnable88_subsystem'
 * '<S96>'  : 'large_scale_autosar_swc_expfcns/Runnable89_subsystem'
 * '<S97>'  : 'large_scale_autosar_swc_expfcns/Runnable8_subsystem'
 * '<S98>'  : 'large_scale_autosar_swc_expfcns/Runnable90_subsystem'
 * '<S99>'  : 'large_scale_autosar_swc_expfcns/Runnable91_subsystem'
 * '<S100>' : 'large_scale_autosar_swc_expfcns/Runnable92_subsystem6'
 * '<S101>' : 'large_scale_autosar_swc_expfcns/Runnable93_subsystem'
 * '<S102>' : 'large_scale_autosar_swc_expfcns/Runnable94_subsystem'
 * '<S103>' : 'large_scale_autosar_swc_expfcns/Runnable95_subsystem'
 * '<S104>' : 'large_scale_autosar_swc_expfcns/Runnable96_subsystem'
 * '<S105>' : 'large_scale_autosar_swc_expfcns/Runnable97_subsystem'
 * '<S106>' : 'large_scale_autosar_swc_expfcns/Runnable98_subsystem'
 * '<S107>' : 'large_scale_autosar_swc_expfcns/Runnable99_subsystem'
 * '<S108>' : 'large_scale_autosar_swc_expfcns/Runnable9_subsystem'
 * '<S109>' : 'large_scale_autosar_swc_expfcns/Runnable1_subsystem/Subsystem'
 */
#endif                       /* RTW_HEADER_large_scale_autosar_swc_expfcns_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
