/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "ThrottlePositionMonitor"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 16:23:06 "  */

#ifndef Rte_ThrottlePositionMonitor_h
#define Rte_ThrottlePositionMonitor_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable_Step_TPS_Secondary_Value_6                                              \
  Rte_IRead_ThrottlePositionMonitor_Runnable_Step_TPS_Secondary_Value_6
Rte_IRead_Runnable_Step_TPS_Secondary_Value_6(void);

#define Rte_IRead_Runnable_Step_TPS_Primary_Value_6                                                \
  Rte_IRead_ThrottlePositionMonitor_Runnable_Step_TPS_Primary_Value_6
Rte_IRead_Runnable_Step_TPS_Primary_Value_6(void);

#define Rte_IWrite_Runnable_Step_TPS_Percent_Value_6                                               \
  Rte_IWrite_ThrottlePositionMonitor_Runnable_Step_TPS_Percent_Value_6
void Rte_IWrite_Runnable_Step_TPS_Percent_Value_6(u);

#define Rte_IWriteRef_Runnable_Step_TPS_Percent_Value_6                                            \
  Rte_IWriteRef_ThrottlePositionMonitor_Runnable_Step_TPS_Percent_Value_6

*Rte_IWriteRef_Runnable_Step_TPS_Percent_Value_6(void);

/* IRV functions */

/* Entry point functions */
extern FUNC(void, ThrottlePositionMonitor_CODE) ThrottlePositionMonitor_Init(void);
extern FUNC(void, ThrottlePositionMonitor_CODE) Runnable_Step(void);
extern FUNC(void, ThrottlePositionMonitor_CODE) ThrottlePositionMonitor_Init(void);

#endif
