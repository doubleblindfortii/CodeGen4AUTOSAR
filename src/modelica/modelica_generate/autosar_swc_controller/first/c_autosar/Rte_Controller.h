/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "Controller"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 16:23:44 "  */

#ifndef Rte_Controller_h
#define Rte_Controller_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable_Step_APP_Percent_Value_2                                                \
  Rte_IRead_Controller_Runnable_Step_APP_Percent_Value_2
Double Rte_IRead_Runnable_Step_APP_Percent_Value_2(void);

#define Rte_IRead_Runnable_Step_TPS_Percent_Value_6                                                \
  Rte_IRead_Controller_Runnable_Step_TPS_Percent_Value_6
Double Rte_IRead_Runnable_Step_TPS_Percent_Value_6(void);

#define Rte_IWrite_Runnable_Step_ThrCmd_Percent_Value_4                                            \
  Rte_IWrite_Controller_Runnable_Step_ThrCmd_Percent_Value_4
void Rte_IWrite_Runnable_Step_ThrCmd_Percent_Value_4(Double u);

#define Rte_IWriteRef_Runnable_Step_ThrCmd_Percent_Value_4                                         \
  Rte_IWriteRef_Controller_Runnable_Step_ThrCmd_Percent_Value_4

Double *Rte_IWriteRef_Runnable_Step_ThrCmd_Percent_Value_4(void);

/* IRV functions */

/* Entry point functions */
extern FUNC(void, Controller_CODE) Controller_Init(void);
extern FUNC(void, Controller_CODE) Controller_Init(void);
extern FUNC(void, Controller_CODE) Runnable_Step(void);

#endif
