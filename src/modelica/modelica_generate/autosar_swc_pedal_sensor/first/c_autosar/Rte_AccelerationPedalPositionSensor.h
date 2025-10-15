/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "AccelerationPedalPositionSensor"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 16:21:33 "  */

#ifndef Rte_AccelerationPedalPositionSensor_h
#define Rte_AccelerationPedalPositionSensor_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable_Step_APP_HwIO_Value_1                                                   \
  Rte_IRead_AccelerationPedalPositionSensor_Runnable_Step_APP_HwIO_Value_1
Double Rte_IRead_Runnable_Step_APP_HwIO_Value_1(void);

#define Rte_IWrite_Runnable_Step_APP_Percent_Value_2                                               \
  Rte_IWrite_AccelerationPedalPositionSensor_Runnable_Step_APP_Percent_Value_2
void Rte_IWrite_Runnable_Step_APP_Percent_Value_2(Double u);

#define Rte_IWriteRef_Runnable_Step_APP_Percent_Value_2                                            \
  Rte_IWriteRef_AccelerationPedalPositionSensor_Runnable_Step_APP_Percent_Value_2

Double *Rte_IWriteRef_Runnable_Step_APP_Percent_Value_2(void);

/* IRV functions */

/* Entry point functions */
extern FUNC(void, AccelerationPedalPositionSensor_CODE) AccelerationPedalPositionSensor_Init(void);
extern FUNC(void, AccelerationPedalPositionSensor_CODE) AccelerationPedalSensor_Init(void);
extern FUNC(void, AccelerationPedalPositionSensor_CODE) Runnable_Step(void);

#endif
