/* This file contains stub implementations of the AUTOSAR RTE functions.

   This file is generated for:
   Atomic software component:
   ARXML schema: 4.3
   File generated on: 2026-03-21 13:36:57  */

#define MEMMAP_ERROR

/* START_SEC Symbols */
#ifdef _START_SEC_CODE
#undef _START_SEC_CODE
#undef MEMMAP_ERROR
#elif defined(_START_SEC_CONST)
#undef _START_SEC_CONST
#undef MEMMAP_ERROR
#elif defined(_START_SEC_VAR)
#undef _START_SEC_VAR
#undef MEMMAP_ERROR
#endif

/* STOP_SEC symbols */
#ifdef _STOP_SEC_CODE
#undef _STOP_SEC_CODE
#undef MEMMAP_ERROR
#elif defined(_STOP_SEC_CONST)
#undef _STOP_SEC_CONST
#undef MEMMAP_ERROR
#elif defined(_STOP_SEC_VAR)
#undef _STOP_SEC_VAR
#undef MEMMAP_ERROR

/* Error out if none of the expected Memory Section keywords are defined */
#ifdef MEMMAP_ERROR
#error "_MemMap.h wrong pragma command"
#endif
#endif
