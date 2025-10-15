/* Copyright 2023 Wumbuk */

/*
 * File: Compiler.h
 *
 * Compiler Abstraction Macros
 *
 * This header file specifies macros for the abstraction of compiler specific
 * keywords used for addressing data and code within declarations and
 * definitions. This is used to overcome problems caused by the limited 16 bit
 * addressing range. For SIL/PIL macros behave as identity operators.
 *
 * Note that this file should be replaced with an appropriate RTE file when
 * deploying the generated code outside of Wumbuk Autosar Blokset tool.
 */

#ifndef Compiler_h
#define Compiler_h

/* Compiler abstraction macros */
#define FUNC(type, memclass) type
#define P2VAR(ptrtype, memclass, ptrclass) ptrtype *
#define P2CONST(ptrtype, memclass, ptrclass) const ptrtype *
#define CONSTP2VAR(ptrtype, memclass, ptrclass) ptrtype *const
#define CONSTP2CONST(ptrtype, memclass, ptrclass) const ptrtype *const
#define CONST(consttype, memclass) const consttype
#define VAR(type, memclass) type

#endif /* Compiler_h */