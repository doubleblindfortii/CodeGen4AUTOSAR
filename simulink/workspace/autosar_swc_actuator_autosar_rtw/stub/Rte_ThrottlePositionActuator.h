/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "ThrottlePositionActuator"
   ARXML schema: "4.2"
   File generated on: "07-Aug-2025 15:20:39"  */

#ifndef Rte_ThrottlePositionActuator_h
#define Rte_ThrottlePositionActuator_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_Step_ThrCmd_Percent_Value Rte_IRead_ThrottlePositionActuator_Runnable_Step_ThrCmd_Percent_Value

float32 Rte_IRead_Runnable_Step_ThrCmd_Percent_Value(void);

#define Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value Rte_IWrite_ThrottlePositionActuator_Runnable_Step_ThrCmd_HwIO_Value

void Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value(SInt16 u);

#define Rte_IWriteRef_Runnable_Step_ThrCmd_HwIO_Value Rte_IWriteRef_ThrottlePositionActuator_Runnable_Step_ThrCmd_HwIO_Value

SInt16* Rte_IWriteRef_Runnable_Step_ThrCmd_HwIO_Value(void);

/* Entry point functions */
extern FUNC(void, ThrottlePositionActuator_CODE) Runnable_Step(void);
extern FUNC(void, ThrottlePositionActuator_CODE) ThrottlePositionActuator_Init
  (void);

/* Parameters */
extern MyStruct_Actuator Rte_CData_HBridgeCmd_LkupTbl_data;

#define Rte_CData_HBridgeCmd_LkupTbl   Rte_CData_ThrottlePositionActuator_HBridgeCmd_LkupTbl

MyStruct_Actuator* Rte_CData_HBridgeCmd_LkupTbl(void);

#endif
