/*
 * File: autosar_swc_controller.c
 *
 *
 * C/C++ source code generated on : 2025-08-13 16:23:44
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */
#include "autosar_swc_controller.h"

/* Block states (default storage) */
DW_autosar_swc_controller_T autosar_swc_controller_DW;

/* Model step function */
void Runnable_Step(void)
{
  float32 rtb_IntegralGain;
  float32 rtb_IntegralGain_0;
  float32 rtb_SignPreIntegrator;
  float32 rtb_SignPreIntegrator_0;
  float32 rtb_Sum;

  rtb_IntegralGain =
      Rte_IRead_Runnable_Step_APP_Percent_Value_2() - Rte_IRead_Runnable_Step_TPS_Percent_Value_6();

  rtb_Sum = (rtb_IntegralGain + autosar_swc_controller_DW.Integrator_DSTATE) +
            (0.0F - autosar_swc_controller_DW.UD_DSTATE);

  if (rtb_Sum > 100.0F)
  {
    rtb_SignPreIntegrator = rtb_Sum - 100.0F;
  }
  else if (rtb_Sum >= -100.0F)
  {
    rtb_SignPreIntegrator = 0.0F;
  }
  else
  {
    rtb_SignPreIntegrator = rtb_Sum - -100.0F;
  }

  rtb_IntegralGain *= 2.0F;

  if (rtb_SignPreIntegrator < 0.0F)
  {
    rtb_SignPreIntegrator_0 = -1.0F;
  }
  else if (rtb_SignPreIntegrator > 0.0F)
  {
    rtb_SignPreIntegrator_0 = 1.0F;
  }
  else
  {
    rtb_SignPreIntegrator_0 = rtb_SignPreIntegrator;
  }

  /* End of Signum: '<S27>/SignPreSat' */

  /* DataTypeConversion: '<S27>/DataTypeConv1' */
  rtb_SignPreIntegrator_0 = fmodf(rtb_SignPreIntegrator_0, 256.0F);

  /* Signum: '<S27>/SignPreIntegrator' */
  if (rtb_IntegralGain < 0.0F)
  {
    rtb_IntegralGain_0 = -1.0F;
  }
  else if (rtb_IntegralGain > 0.0F)
  {
    rtb_IntegralGain_0 = 1.0F;
  }
  else
  {
    rtb_IntegralGain_0 = rtb_IntegralGain;
  }

  /* End of Signum: '<S27>/SignPreIntegrator' */

  /* DataTypeConversion: '<S27>/DataTypeConv2' */
  rtb_IntegralGain_0 = fmodf(rtb_IntegralGain_0, 256.0F);

  if ((0.0F != rtb_SignPreIntegrator) &&
      ((rtb_SignPreIntegrator_0 < 0.0F ? (sint32)(sint8) - (sint8)(uint8)-rtb_SignPreIntegrator_0
                                       : (sint32)(sint8)(uint8)rtb_SignPreIntegrator_0) ==
       (rtb_IntegralGain_0 < 0.0F ? (sint32)(sint8) - (sint8)(uint8)-rtb_IntegralGain_0
                                  : (sint32)(sint8)(uint8)rtb_IntegralGain_0)))
  {
    rtb_IntegralGain = 0.0F;
  }

  /* End of Switch: '<S27>/Switch' */

  /* Update for DiscreteIntegrator: '<S38>/Integrator' */
  autosar_swc_controller_DW.Integrator_DSTATE += 0.005F * rtb_IntegralGain;

  /* Update for Delay: '<S31>/UD' */
  autosar_swc_controller_DW.UD_DSTATE = 0.0F;

  /* Saturate: '<S45>/Saturation' */
  if (rtb_Sum > 100.0F)
  {
    rtb_Sum = 100.0F;
  }
  else if (rtb_Sum < -100.0F)
  {
    rtb_Sum = -100.0F;
  }

  Rte_IWrite_Runnable_Step_ThrCmd_Percent_Value_4(rtb_Sum);
}

/* Model initialize function */
void Controller_Init(void) { /* (no initialization code required) */ }

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
