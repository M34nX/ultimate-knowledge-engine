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
