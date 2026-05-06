/* This file contains stub implementations of the AUTOSAR RTE functions.
   ARXML schema: "4.3"
*/

#ifndef Rte_Type_h
#define Rte_Type_h
#include "Std_Types.h"
#include "rtwtypes.h"

/* AUTOSAR RTE Status Types */
#ifndef RTE_E_OK
#define RTE_E_OK (0x00)
#endif

#ifndef RTE_E_LOST_DATA
#define RTE_E_LOST_DATA (0x40)
#endif

#ifndef RTE_E_LIMIT
#define RTE_E_LIMIT (0x82)
#endif

#ifndef E2E_E_OK
#define E2E_E_OK (0x00)
#endif

#ifndef E2EPW_STATUS_OK
#define E2EPW_STATUS_OK (0x00)
#endif

#ifndef E2EPW_STATUS_OKSOMELOST
#define E2EPW_STATUS_OKSOMELOST (0x20)
#endif

/* AUTOSAR Implementation data types, specific to software component */
typedef void *Rte_Instance;

#endif
