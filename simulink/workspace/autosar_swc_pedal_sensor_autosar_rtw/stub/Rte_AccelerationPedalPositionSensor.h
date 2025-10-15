/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "AccelerationPedalPositionSensor"
   ARXML schema: "4.2"
   File generated on: "07-Aug-2025 15:22:18"  */

#ifndef Rte_AccelerationPedalPositionSensor_h
#define Rte_AccelerationPedalPositionSensor_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_Step_APP_HwIO_Value Rte_IRead_AccelerationPedalPositionSensor_Runnable_Step_APP_HwIO_Value

uint16 Rte_IRead_Runnable_Step_APP_HwIO_Value(void);

#define Rte_IWrite_Runnable_Step_APP_Percent_Value Rte_IWrite_AccelerationPedalPositionSensor_Runnable_Step_APP_Percent_Value

void Rte_IWrite_Runnable_Step_APP_Percent_Value(float32 u);

#define Rte_IWriteRef_Runnable_Step_APP_Percent_Value Rte_IWriteRef_AccelerationPedalPositionSensor_Runnable_Step_APP_Percent_Value

float32* Rte_IWriteRef_Runnable_Step_APP_Percent_Value(void);

/* Entry point functions */
extern FUNC(void, AccelerationPedalPositionSensor_CODE)
  AccelerationPedalSensor_Init(void);
extern FUNC(void, AccelerationPedalPositionSensor_CODE) Runnable_Step(void);

/* Parameters */
extern MyStruct Rte_CData_SetpointPercent_LkupTbl_data;

#define Rte_CData_SetpointPercent_LkupTbl Rte_CData_AccelerationPedalPositionSensor_SetpointPercent_LkupTbl

MyStruct* Rte_CData_SetpointPercent_LkupTbl(void);

#endif
