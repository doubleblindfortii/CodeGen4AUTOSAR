/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:  "ASWC"
   ARXML schema: "4.3"
   File generated on: "2025-08-13 14:30:10 "  */

#ifndef Rte_ASWC_h
#define Rte_ASWC_h
#include "Compiler.h"
#include "Rte_Type.h"

/* Data access functions */

#define Rte_IRead_Runnable1_RPort_DE1 Rte_IRead_ASWC_Runnable1_RPort_DE1
Double Rte_IRead_Runnable1_RPort_DE1(void);

#define Rte_IStatus_Runnable1_RPort_DE1 Rte_IStatus__ASWC_Runnable1_RPort_DE1
Std_ReturnType Rte_IStatus_Runnable1_RPort_DE1(void);

#define Rte_IRead_Runnable1_RPort_DE1 Rte_IRead_ASWC_Runnable1_RPort_DE1
Double Rte_IRead_Runnable1_RPort_DE1(void);

#define Rte_IStatus_Runnable1_RPort_DE1 Rte_IStatus__ASWC_Runnable1_RPort_DE1
Std_ReturnType Rte_IStatus_Runnable1_RPort_DE1(void);

#define Rte_IWrite_Runnable1_PPort_DE_1 Rte_IWrite_ASWC_Runnable1_PPort_DE_1
void Rte_IWrite_Runnable1_PPort_DE_1(Double u);

#define Rte_IWriteRef_Runnable1_PPort_DE_1 Rte_IWriteRef_ASWC_Runnable1_PPort_DE_1

Double *Rte_IWriteRef_Runnable1_PPort_DE_1(void);

#define Rte_IWrite_Runnable2_PPort_DE_3 Rte_IWrite_ASWC_Runnable2_PPort_DE_3
void Rte_IWrite_Runnable2_PPort_DE_3(Double u);

#define Rte_IWriteRef_Runnable2_PPort_DE_3 Rte_IWriteRef_ASWC_Runnable2_PPort_DE_3

Double *Rte_IWriteRef_Runnable2_PPort_DE_3(void);

#define Rte_IWrite_Runnable2_PPort_DE_4 Rte_IWrite_ASWC_Runnable2_PPort_DE_4
void Rte_IWrite_Runnable2_PPort_DE_4(Double u);

#define Rte_IWriteRef_Runnable2_PPort_DE_4 Rte_IWriteRef_ASWC_Runnable2_PPort_DE_4

Double *Rte_IWriteRef_Runnable2_PPort_DE_4(void);

#define Rte_IRead_Runnable3_RPort_DE2 Rte_IRead_ASWC_Runnable3_RPort_DE2
Double Rte_IRead_Runnable3_RPort_DE2(void);

#define Rte_IWrite_Runnable3_PPort_DE_2 Rte_IWrite_ASWC_Runnable3_PPort_DE_2
void Rte_IWrite_Runnable3_PPort_DE_2(Double u);

#define Rte_IWriteRef_Runnable3_PPort_DE_2 Rte_IWriteRef_ASWC_Runnable3_PPort_DE_2

Double *Rte_IWriteRef_Runnable3_PPort_DE_2(void);

/* IRV functions */

#define Rte_IrvIRead_Runnable1_IRV3 Rte_IrvIRead_ASWC_Runnable1_IRV3
Double Rte_IrvIRead_Runnable1_IRV3(void);

#define Rte_IrvIWrite_Runnable1_IRV1 Rte_IrvIWrite_ASWC_Runnable1_IRV1
void Rte_IrvIWrite_Runnable1_IRV1(Double u);

#define Rte_IrvIRead_Runnable2_IRV1 Rte_IrvIRead_ASWC_Runnable2_IRV1
Double Rte_IrvIRead_Runnable2_IRV1(void);

#define Rte_IrvIRead_Runnable2_IRV2 Rte_IrvIRead_ASWC_Runnable2_IRV2
Double Rte_IrvIRead_Runnable2_IRV2(void);

#define Rte_IrvIWrite_Runnable2_IRV4 Rte_IrvIWrite_ASWC_Runnable2_IRV4
void Rte_IrvIWrite_Runnable2_IRV4(Double u);

#define Rte_IrvIRead_Runnable3_IRV4 Rte_IrvIRead_ASWC_Runnable3_IRV4
Double Rte_IrvIRead_Runnable3_IRV4(void);

#define Rte_IrvIWrite_Runnable3_IRV2 Rte_IrvIWrite_ASWC_Runnable3_IRV2
void Rte_IrvIWrite_Runnable3_IRV2(Double u);

#define Rte_IrvIWrite_Runnable3_IRV3 Rte_IrvIWrite_ASWC_Runnable3_IRV3
void Rte_IrvIWrite_Runnable3_IRV3(Double u);

/* Entry point functions */
extern FUNC(void, ASWC_CODE) ASWC_Init(void);
extern FUNC(void, ASWC_CODE) Runnable1(void);
extern FUNC(void, ASWC_CODE) Runnable2(void);
extern FUNC(void, ASWC_CODE) Runnable3(void);

#endif
