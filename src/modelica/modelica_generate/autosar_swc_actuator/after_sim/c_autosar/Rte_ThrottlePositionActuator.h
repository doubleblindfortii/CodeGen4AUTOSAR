/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "ThrottlePositionActuator"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 16:24:13 "  */

#ifndef Rte_ThrottlePositionActuator_h
#define Rte_ThrottlePositionActuator_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable_Step_ThrCmd_Percent_Value_4                                             \
  Rte_IRead_ThrottlePositionActuator_Runnable_Step_ThrCmd_Percent_Value_4
Rte_IRead_Runnable_Step_ThrCmd_Percent_Value_4(void);

#define Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value_3                                               \
  Rte_IWrite_ThrottlePositionActuator_Runnable_Step_ThrCmd_HwIO_Value_3
void Rte_IWrite_Runnable_Step_ThrCmd_HwIO_Value_3(u);

#define Rte_IWriteRef_Runnable_Step_ThrCmd_HwIO_Value_3                                            \
  Rte_IWriteRef_ThrottlePositionActuator_Runnable_Step_ThrCmd_HwIO_Value_3

*Rte_IWriteRef_Runnable_Step_ThrCmd_HwIO_Value_3(void);

/* IRV functions */

/* Entry point functions */
extern FUNC(void, ThrottlePositionActuator_CODE) ThrottlePositionActuator_Init(void);
extern FUNC(void, ThrottlePositionActuator_CODE) Runnable_Step(void);
extern FUNC(void, ThrottlePositionActuator_CODE) ThrottlePositionActuator_Init(void);

#endif
