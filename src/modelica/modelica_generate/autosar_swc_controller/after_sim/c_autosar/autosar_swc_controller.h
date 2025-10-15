/*
 * File: autosar_swc_controller.h
 *
 * Code generated for Modelica model 'autosar_swc_controller'.
 *
 * Model version                  : 2.3
 * C/C++ source code generated on : 2025-08-13 16:23:44
 *
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives:
 *    1. Execution efficiency
 *    2. RAM efficiency
 * Validation result: Not run
 */

#ifndef RTW_HEADER_autosar_swc_controller_h_
#define RTW_HEADER_autosar_swc_controller_h_
#ifndef autosar_swc_controller_COMMON_INCLUDES_
#define autosar_swc_controller_COMMON_INCLUDES_
#include "Rte_Controller.h"
#include "rtwtypes.h"
#endif /* autosar_swc_controller_COMMON_INCLUDES_ */

#include "autosar_swc_controller_types.h"

/* Macros for accessing real-time model data structure */

/* Block states (default storage) for system '<Root>' */
typedef struct tag_DW_autosar_swc_controller_T
{
  float32 Integrator_DSTATE; /* '<S38>/Integrator' */
  float32 UD_DSTATE;         /* '<S31>/UD' */
} DW_autosar_swc_controller_T;

/* Block states (default storage) */
extern DW_autosar_swc_controller_T autosar_swc_controller_DW;

#endif /* RTW_HEADER_autosar_swc_controller_h_ */
