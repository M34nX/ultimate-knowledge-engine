---
id: build-from-scratch.operating-systems
title: "Understand Operating Systems with a Safe Simulator"
content_type: project
locale: en
domain: systems-and-networking
level: advanced
status: draft
learning_objectives:
  - "Explain user mode and kernel mode."
  - "Simulate process states and scheduling in user space."
  - "Model virtual-page to physical-frame mappings."
  - "Describe system calls and an in-memory file tree."
  - "Explain why a simulator is not a production OS."
prerequisites:
  - "Data structures and debugging"
  - "Binary and hexadecimal notation"
  - "Basic computer architecture"
milestones:
  - "Draw user-mode and kernel-mode flow."
  - "Represent process states in user space."
  - "Simulate FCFS and round-robin."
  - "Add a page-mapping table."
  - "Model an in-memory file tree and its limits."
---

# Understand Operating Systems with a Safe Simulator

**Level:** Intermediate–Advanced · **Languages:** Python for simulation; C or Rust for further study · **Track:** `operating-system`

## Scope and safety
Start with a user-space teaching simulator. Model OS ideas without modifying boot sectors, installing a kernel, or interacting with physical hardware. Further kernel study belongs in a disposable virtual machine. Never run an experimental kernel on a primary device.

## Prerequisites
Data structures, debugging, binary and hexadecimal notation, basic computer architecture, and familiarity with processes and files.

## Lesson 1 — What an OS does
An operating system coordinates hardware resources and provides abstractions to applications. The kernel is the privileged core. Applications normally request services through defined interfaces rather than controlling hardware directly.

Common responsibilities include process and memory management, device abstraction, file systems, security boundaries, and networking.

## Lesson 2 — Processes and scheduling
A process is a running program together with its execution context and resources. A scheduler chooses which runnable task receives CPU time.

Represent each simulated task with an ID, required CPU time, remaining time, and a state such as ready, running, or finished. First implement first-come, first-served scheduling. Then compare it with round-robin using a fixed time quantum. Record waiting time and turnaround time and explain the trade-offs.

## Lesson 3 — Virtual memory
Programs use virtual addresses. The operating system and hardware cooperate to translate them to physical memory while enforcing isolation. A teaching model can represent a page table as a mapping from virtual page numbers to physical frame numbers.

This is a data-structure simulation only. Do not attempt to inspect or modify another process's memory.

## Lesson 4 — System calls and file systems
A system call is a controlled entry point through which a program requests a kernel service. A file system organises persistent data and metadata. Begin by modelling a tiny in-memory directory tree before studying on-disk formats.

## Project milestones
- **M1:** Draw user mode, kernel mode, and system-call flow.
- **M2:** Implement process states in an ordinary user-space program.
- **M3:** Simulate FCFS and round-robin scheduling.
- **M4:** Add a virtual-page-to-frame mapping table.
- **M5:** Model a tiny in-memory file tree and document its limitations.

## Exercises
1. Why should an application not execute every privileged operation directly?
2. Compare a process and a thread conceptually.
3. How does time quantum affect responsiveness and context-switch overhead?
4. What problem does virtual memory solve?
5. Why is a toy simulator not equivalent to a production kernel?

## Acceptance criteria
- The simulator runs entirely in user space.
- Results are deterministic for fixed input.
- Process states and transitions are documented.
- The memory model is labelled as a simplification.
- No real device, boot configuration, or host OS memory is modified.

## Further study
- [Operating Systems: From 0 to 1](https://tuhdo.github.io/os01/)
- [The Little Book About OS Development](https://littleosbook.github.io/)
- [Writing an OS in Rust](https://os.phil-opp.com/)
- [Linux Kernel Documentation](https://docs.kernel.org/)

External tutorials remain at their original locations.
