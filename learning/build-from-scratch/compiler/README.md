---
id: build-from-scratch.compiler
title: "Build a Small Programming Language"
content_type: project
locale: en
domain: programming-languages
level: advanced
status: draft
learning_objectives:
  - "Define a small grammar and precedence rules."
  - "Tokenize source text with source positions."
  - "Build and evaluate an abstract syntax tree."
  - "Add variables and useful diagnostics."
  - "Explain why host-language eval is unsafe for learner input."
prerequisites:
  - "Functions and recursion"
  - "Strings and tree data structures"
  - "Basic discrete mathematics"
milestones:
  - "Implement an arithmetic tokenizer."
  - "Parse precedence and parentheses."
  - "Evaluate an abstract syntax tree."
  - "Add variables and assignment."
  - "Add diagnostics and automated tests."
  - "Optionally implement a bytecode virtual machine."
---

# Build a Small Programming Language

**Level:** Intermediate–Advanced · **Language:** Python or TypeScript · **Status:** Draft

## Outcome
Create a tiny expression language with variables, arithmetic, parentheses, and useful errors. Begin with an interpreter; bytecode is an extension.

## Prerequisites
Functions, recursion, strings, trees, and discrete mathematics basics.

## Lessons
1. **Language design:** write a small grammar and define operator precedence.
2. **Lexing:** convert source text into tokens with source positions.
3. **Parsing:** build an abstract syntax tree (AST).
4. **Evaluation:** interpret the AST with an environment for variables.
5. **Diagnostics:** report invalid characters, unexpected tokens, and undefined names with locations.
6. **Extension:** add functions or compile the AST to documented bytecode.

## Milestones
- M1: arithmetic tokenizer.
- M2: parser for precedence and parentheses.
- M3: AST evaluator.
- M4: variables and assignment.
- M5: diagnostics and automated tests.
- M6: optional bytecode virtual machine.

## Practice
Trace 2 + 3 * 4 through tokenization, parsing, and evaluation. Explain why precedence is not the same as evaluating strictly left to right.

## Acceptance
The grammar is documented; tests cover precedence and malformed input; errors include locations; do not use the host language eval function to execute learner expressions.

## References
- [Crafting Interpreters](https://craftinginterpreters.com/)
- [LLVM documentation](https://llvm.org/docs/)
- [ANTLR documentation](https://www.antlr.org/)
