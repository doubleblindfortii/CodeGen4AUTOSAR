/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "ThrottlePositionMonitor"
   ARXML schema: "4.2"
   File generated on: "07-Aug-2025 15:21:30"  */

#ifndef Rte_ThrottlePositionMonitor_h
#define Rte_ThrottlePositionMonitor_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_Step_TPS_Primary_Value Rte_IRead_ThrottlePositionMonitor_Runnable_Step_TPS_Primary_Value

float32 Rte_IRead_Runnable_Step_TPS_Primary_Value(void);

#define Rte_IRead_Runnable_Step_TPS_Seconday_Value Rte_IRead_ThrottlePositionMonitor_Runnable_Step_TPS_Seconday_Value

float32 Rte_IRead_Runnable_Step_TPS_Seconday_Value(void);

#define Rte_IWrite_Runnable_Step_TPS_Percent_Value Rte_IWrite_ThrottlePositionMonitor_Runnable_Step_TPS_Percent_Value

void Rte_IWrite_Runnable_Step_TPS_Percent_Value(float32 u);

#define Rte_IWriteRef_Runnable_Step_TPS_Percent_Value Rte_IWriteRef_ThrottlePositionMonitor_Runnable_Step_TPS_Percent_Value

float32* Rte_IWriteRef_Runnable_Step_TPS_Percent_Value(void);

/* Entry point functions */
extern FUNC(void, ThrottlePositionMonitor_CODE) Runnable_Step(void);
extern FUNC(void, ThrottlePositionMonitor_CODE) ThrottlePositionMonitor_Init
  (void);

#endif
