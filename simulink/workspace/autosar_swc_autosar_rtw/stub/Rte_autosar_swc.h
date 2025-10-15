/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "autosar_swc"
   ARXML schema: "4.3"
   File generated on: "10-Aug-2025 14:22:23"  */

#ifndef Rte_autosar_swc_h
#define Rte_autosar_swc_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_1s_In1_1s_In1_1s Rte_IRead_autosar_swc_Runnable_1s_In1_1s_In1_1s

Double Rte_IRead_Runnable_1s_In1_1s_In1_1s(void);

#define Rte_IWrite_Runnable_1s_Out1_Out1 Rte_IWrite_autosar_swc_Runnable_1s_Out1_Out1

void Rte_IWrite_Runnable_1s_Out1_Out1(Double u);

#define Rte_IWriteRef_Runnable_1s_Out1_Out1 Rte_IWriteRef_autosar_swc_Runnable_1s_Out1_Out1

Double* Rte_IWriteRef_Runnable_1s_Out1_Out1(void);

#define Rte_IWrite_Runnable_1s_Out2_Out2 Rte_IWrite_autosar_swc_Runnable_1s_Out2_Out2

void Rte_IWrite_Runnable_1s_Out2_Out2(Double u);

#define Rte_IWriteRef_Runnable_1s_Out2_Out2 Rte_IWriteRef_autosar_swc_Runnable_1s_Out2_Out2

Double* Rte_IWriteRef_Runnable_1s_Out2_Out2(void);

#define Rte_IRead_Runnable_2S_In2_2S_In2_2S Rte_IRead_autosar_swc_Runnable_2S_In2_2S_In2_2S

Double Rte_IRead_Runnable_2S_In2_2S_In2_2S(void);

/* IRV functions */
#define Rte_IrvIRead_Runnable_1s_IRV1  Rte_IrvIRead_autosar_swc_Runnable_1s_IRV1

Double Rte_IrvIRead_Runnable_1s_IRV1(void);

#define Rte_IrvIWrite_Runnable_2S_IRV1 Rte_IrvIWrite_autosar_swc_Runnable_2S_IRV1

void Rte_IrvIWrite_Runnable_2S_IRV1(Double u);

/* Entry point functions */
extern FUNC(void, autosar_swc_CODE) test_Init(void);
extern FUNC(void, autosar_swc_CODE) Runnable_1s(void);
extern FUNC(void, autosar_swc_CODE) Runnable_2s(void);

#endif
