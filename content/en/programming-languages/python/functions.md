---
id: python.functions.basics
title: Python Functions — First Principles
content_type: lesson
locale: en
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - Explain why functions help organise reusable program logic.
  - Define a function with def and call it with an argument.
  - Distinguish a parameter from an argument.
  - Explain the purpose of a return statement.
prerequisites: []
concepts:
  - python.functions.parameters
  - python.functions.return-values
sources:
  - python-docs
estimated_minutes: 25
version_scope:
  minimum: "3"
  maximum: null
  notes: "Introductory syntax; check the official documentation for version-specific details."
---

# Python Functions — First Principles

> **Draft learning sample.** This page demonstrates the project format. It has not yet completed editorial or technical review.

## 1. What is a function?

A function is a named, reusable unit of program logic. It can accept input, perform a task, and optionally return a result.

Functions help programmers divide a larger problem into smaller parts, give meaningful names to operations, and reduce repeated code.

## 2. Define and call a function

```python
def greet(name):
    message = f"Hello, {name}!"
    return message

result = greet("Ada")
print(result)
```

Expected output:

```text
Hello, Ada!
```

The `def` statement defines the function. The indented statements form its body. The call `greet("Ada")` runs the function with the supplied argument.

## 3. Parameter and argument

A **parameter** is a name in the function definition, such as `name`. An **argument** is the value supplied when the function is called, such as `"Ada"`.

## 4. Return values

The `return` statement ends the current function call and sends a result back to the caller. A function can also finish without an explicit return statement; in that case Python returns `None`.

## 5. Common mistakes

- Defining a function but never calling it.
- Confusing the parameter name with the argument value.
- Expecting `print()` to return the displayed text.
- Forgetting indentation in the function body.
- Using a local variable outside the scope where it is defined.

## 6. Practice

1. Define a function named `square` that returns the square of a number.
2. Define a function that accepts a first name and returns a greeting.
3. Explain the difference between printing a value and returning a value.

## 7. Further reading

- [Python Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## 8. Review checklist

- [ ] Confirm explanations against the current Python documentation.
- [ ] Execute examples with a supported Python interpreter.
- [ ] Review terminology and accessibility.
- [ ] Add a reviewer and review date before changing the status.
