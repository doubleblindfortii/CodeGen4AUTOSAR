/* This file contains stub implementations of the AUTOSAR RTE functions.
   The stub implementations can be used for testing the generated code in
   Simulink, for example, in SIL/PIL simulations of the component under
   test. Note that this file should be replaced with an appropriate RTE
   file when deploying the generated code outside of Simulink.

   This file is generated for:
   Atomic software component:  "ThrottlePositionSensor"
   ARXML schema: "4.2"
   File generated on: "09-Aug-2025 15:14:14"  */

#include "Rte_ThrottlePositionSensor.h"

/* Parameters */
MyStruct Rte_CData_TPSPercent_LkupTbl_data;
MyStruct* Rte_CData_TPSPercent_LkupTbl(Rte_Instance self)
{
  (void)self;
  return &Rte_CData_TPSPercent_LkupTbl_data;
}
