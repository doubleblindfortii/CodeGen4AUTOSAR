/*
 * File: autosar_swc_controller.c
 *
 * Code generated for Simulink model 'autosar_swc_controller'.
 *
 * Model version                  : 4.1
 * Simulink Coder version         : 9.5 (R2021a) 14-Nov-2020
 * C/C++ source code generated on : Thu Aug  7 15:21:09 2025
 *
 * Target selection: autosar.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "autosar_swc_controller.h"
#include "autosar_swc_controller_private.h"

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

  /* Outputs for Atomic SubSystem: '<Root>/Runnable_Step_sys' */
  /* Gain: '<S35>/Integral Gain' incorporates:
   *  Inport: '<Root>/APP_Percent_Value'
   *  Inport: '<Root>/TPS_Percent_Value'
   *  Sum: '<S1>/Subtract'
   */
  rtb_IntegralGain = Rte_IRead_Runnable_Step_APP_Percent_Value() -
    Rte_IRead_Runnable_Step_TPS_Percent_Value();

  /* Sum: '<S47>/Sum' incorporates:
   *  Delay: '<S31>/UD'
   *  DiscreteIntegrator: '<S38>/Integrator'
   *  Sum: '<S31>/Diff'
   */
  rtb_Sum = (rtb_IntegralGain + autosar_swc_controller_DW.Integrator_DSTATE) +
    (0.0F - autosar_swc_controller_DW.UD_DSTATE);

  /* DeadZone: '<S29>/DeadZone' */
  if (rtb_Sum > 100.0F) {
    /* Signum: '<S27>/SignPreIntegrator' */
    rtb_SignPreIntegrator = rtb_Sum - 100.0F;
  } else if (rtb_Sum >= -100.0F) {
    /* Signum: '<S27>/SignPreIntegrator' */
    rtb_SignPreIntegrator = 0.0F;
  } else {
    /* Signum: '<S27>/SignPreIntegrator' */
    rtb_SignPreIntegrator = rtb_Sum - -100.0F;
  }

  /* End of DeadZone: '<S29>/DeadZone' */

  /* Gain: '<S35>/Integral Gain' */
  rtb_IntegralGain *= 2.0F;

  /* Signum: '<S27>/SignPreSat' */
  if (rtb_SignPreIntegrator < 0.0F) {
    rtb_SignPreIntegrator_0 = -1.0F;
  } else if (rtb_SignPreIntegrator > 0.0F) {
    rtb_SignPreIntegrator_0 = 1.0F;
  } else {
    rtb_SignPreIntegrator_0 = rtb_SignPreIntegrator;
  }

  /* End of Signum: '<S27>/SignPreSat' */

  /* DataTypeConversion: '<S27>/DataTypeConv1' */
  rtb_SignPreIntegrator_0 = fmodf(rtb_SignPreIntegrator_0, 256.0F);

  /* Signum: '<S27>/SignPreIntegrator' */
  if (rtb_IntegralGain < 0.0F) {
    rtb_IntegralGain_0 = -1.0F;
  } else if (rtb_IntegralGain > 0.0F) {
    rtb_IntegralGain_0 = 1.0F;
  } else {
    rtb_IntegralGain_0 = rtb_IntegralGain;
  }

  /* End of Signum: '<S27>/SignPreIntegrator' */

  /* DataTypeConversion: '<S27>/DataTypeConv2' */
  rtb_IntegralGain_0 = fmodf(rtb_IntegralGain_0, 256.0F);

  /* Switch: '<S27>/Switch' incorporates:
   *  Constant: '<S27>/Constant1'
   *  DataTypeConversion: '<S27>/DataTypeConv1'
   *  DataTypeConversion: '<S27>/DataTypeConv2'
   *  Gain: '<S27>/ZeroGain'
   *  Logic: '<S27>/AND3'
   *  RelationalOperator: '<S27>/Equal1'
   *  RelationalOperator: '<S27>/NotEqual'
   */
  if ((0.0F != rtb_SignPreIntegrator) && ((rtb_SignPreIntegrator_0 < 0.0F ?
        (sint32)(sint8)-(sint8)(uint8)-rtb_SignPreIntegrator_0 : (sint32)(sint8)
        (uint8)rtb_SignPreIntegrator_0) == (rtb_IntegralGain_0 < 0.0F ? (sint32)
        (sint8)-(sint8)(uint8)-rtb_IntegralGain_0 : (sint32)(sint8)(uint8)
        rtb_IntegralGain_0))) {
    rtb_IntegralGain = 0.0F;
  }

  /* End of Switch: '<S27>/Switch' */

  /* Update for DiscreteIntegrator: '<S38>/Integrator' */
  autosar_swc_controller_DW.Integrator_DSTATE += 0.005F * rtb_IntegralGain;

  /* Update for Delay: '<S31>/UD' */
  autosar_swc_controller_DW.UD_DSTATE = 0.0F;

  /* Saturate: '<S45>/Saturation' */
  if (rtb_Sum > 100.0F) {
    rtb_Sum = 100.0F;
  } else if (rtb_Sum < -100.0F) {
    rtb_Sum = -100.0F;
  }

  /* End of Saturate: '<S45>/Saturation' */
  /* End of Outputs for SubSystem: '<Root>/Runnable_Step_sys' */

  /* Outport: '<Root>/ThrCmd_Percent_Value' */
  Rte_IWrite_Runnable_Step_ThrCmd_Percent_Value(rtb_Sum);
}

/* Model initialize function */
void Controller_Init(void)
{
  /* (no initialization code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
