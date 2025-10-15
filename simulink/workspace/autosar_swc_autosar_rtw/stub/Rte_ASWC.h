/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "ASWC"
   ARXML schema: "4.3"
   File generated on: "07-Aug-2025 15:26:16"  */

#ifndef Rte_ASWC_h
#define Rte_ASWC_h
#include "Rte_Type.h"
#include "Compiler.h"

/* Data access functions */
#define Rte_IRead_Runnable_1s_ReceivePort_In1 Rte_IRead_ASWC_Runnable_1s_ReceivePort_In1

Double Rte_IRead_Runnable_1s_ReceivePort_In1(void);

#define Rte_IStatus_Runnable_1s_ReceivePort_In1 Rte_IStatus_ASWC_Runnable_1s_ReceivePort_In1

Std_ReturnType Rte_IStatus_Runnable_1s_ReceivePort_In1(void);

#define Rte_IWrite_Runnable_1s_SenderPort_Out1 Rte_IWrite_ASWC_Runnable_1s_SenderPort_Out1

void Rte_IWrite_Runnable_1s_SenderPort_Out1(Double u);

#define Rte_IWriteRef_Runnable_1s_SenderPort_Out1 Rte_IWriteRef_ASWC_Runnable_1s_SenderPort_Out1

Double* Rte_IWriteRef_Runnable_1s_SenderPort_Out1(void);

#define Rte_IWrite_Runnable_1s_SenderPort_Out2 Rte_IWrite_ASWC_Runnable_1s_SenderPort_Out2

void Rte_IWrite_Runnable_1s_SenderPort_Out2(Double u);

#define Rte_IWriteRef_Runnable_1s_SenderPort_Out2 Rte_IWriteRef_ASWC_Runnable_1s_SenderPort_Out2

Double* Rte_IWriteRef_Runnable_1s_SenderPort_Out2(void);

#define Rte_IRead_Runnable_2s_ReceivePort_In2 Rte_IRead_ASWC_Runnable_2s_ReceivePort_In2

Double Rte_IRead_Runnable_2s_ReceivePort_In2(void);

#define Rte_IStatus_Runnable_2s_ReceivePort_In2 Rte_IStatus_ASWC_Runnable_2s_ReceivePort_In2

Std_ReturnType Rte_IStatus_Runnable_2s_ReceivePort_In2(void);

/* IRV functions */
#define Rte_IrvIRead_Runnable_1s_IRV1  Rte_IrvIRead_ASWC_Runnable_1s_IRV1

Double Rte_IrvIRead_Runnable_1s_IRV1(void);

#define Rte_IrvIWrite_Runnable_2s_IRV1 Rte_IrvIWrite_ASWC_Runnable_2s_IRV1

void Rte_IrvIWrite_Runnable_2s_IRV1(Double u);

/* Entry point functions */
extern FUNC(void, ASWC_CODE) Runnable_Initialize(void);
extern FUNC(void, ASWC_CODE) Runnable_1s(void);
extern FUNC(void, ASWC_CODE) Runnable_2s(void);

#endif
