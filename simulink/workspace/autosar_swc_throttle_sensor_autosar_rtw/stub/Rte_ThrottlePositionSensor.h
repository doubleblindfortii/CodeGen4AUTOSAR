/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "ThrottlePositionSensor"
   ARXML schema: "4.2"
   File generated on: "09-Aug-2025 15:14:14"  */

#ifndef Rte_ThrottlePositionSensor_h
#define Rte_ThrottlePositionSensor_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_Step_TPS_HwIO_Value Rte_IRead_ThrottlePositionSensor_Runnable_Step_TPS_HwIO_Value

uint16 Rte_IRead_Runnable_Step_TPS_HwIO_Value(Rte_Instance self);

#define Rte_IWrite_Runnable_Step_TPS_Percent_Value Rte_IWrite_ThrottlePositionSensor_Runnable_Step_TPS_Percent_Value

void Rte_IWrite_Runnable_Step_TPS_Percent_Value(Rte_Instance self, float32 u);

#define Rte_IWriteRef_Runnable_Step_TPS_Percent_Value Rte_IWriteRef_ThrottlePositionSensor_Runnable_Step_TPS_Percent_Value

float32* Rte_IWriteRef_Runnable_Step_TPS_Percent_Value(Rte_Instance self);

/* Entry point functions */
extern FUNC(void, ThrottlePositionSensor_CODE) Runnable_Step(Rte_Instance self);
extern FUNC(void, ThrottlePositionSensor_CODE) ThrottlePositionSensor_Init
  (Rte_Instance self);

/* Parameters */
extern MyStruct Rte_CData_TPSPercent_LkupTbl_data;

#define Rte_CData_TPSPercent_LkupTbl   Rte_CData_ThrottlePositionSensor_TPSPercent_LkupTbl

MyStruct* Rte_CData_TPSPercent_LkupTbl(Rte_Instance self);

#endif
