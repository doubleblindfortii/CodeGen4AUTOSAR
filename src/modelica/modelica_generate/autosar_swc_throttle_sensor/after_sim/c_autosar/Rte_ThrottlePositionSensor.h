/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "ThrottlePositionSensor"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 16:20:18 "  */

#ifndef Rte_ThrottlePositionSensor_h
#define Rte_ThrottlePositionSensor_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable_Step_TPS_HwIO_Value_5                                                   \
  Rte_IRead_ThrottlePositionSensor_Runnable_Step_TPS_HwIO_Value_5
Double Rte_IRead_Runnable_Step_TPS_HwIO_Value_5(void);

#define Rte_IWrite_Runnable_Step_TPS_Percent_Value_6                                               \
  Rte_IWrite_ThrottlePositionSensor_Runnable_Step_TPS_Percent_Value_6
void Rte_IWrite_Runnable_Step_TPS_Percent_Value_6(Double u);

#define Rte_IWriteRef_Runnable_Step_TPS_Percent_Value_6                                            \
  Rte_IWriteRef_ThrottlePositionSensor_Runnable_Step_TPS_Percent_Value_6

Double *Rte_IWriteRef_Runnable_Step_TPS_Percent_Value_6(void);

/* IRV functions */

/* Entry point functions */
extern FUNC(void, ThrottlePositionSensor_CODE) ThrottlePositionSensor_Init(void);
extern FUNC(void, ThrottlePositionSensor_CODE) Runnable_Step(void);
extern FUNC(void, ThrottlePositionSensor_CODE) ThrottlePositionSensor_Init(void);

#endif
