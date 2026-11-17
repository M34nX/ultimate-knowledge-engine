# 40 Programming Languages — Learning Workbook

This workbook introduces **40 programming languages** through one small, comparable example per language. It is a starting point, not 40 complete courses. Each example demonstrates basic syntax or the language's nearest equivalent; smart-contract languages have different execution models.

## Browse by purpose

- **General-purpose and application:** Python, Java, C#, Kotlin, Swift, Dart, Ruby, PHP
- **Web and scripting:** JavaScript, TypeScript, PHP, Ruby, Lua, Perl
- **Systems, performance and low-level:** C, C++, Rust, Go, Zig, Assembly
- **Functional and concurrent:** Haskell, Scala, Elixir, Erlang, Clojure, OCaml, F#
- **Scientific and data:** R, Julia, MATLAB, Fortran
- **Enterprise and legacy:** COBOL, Ada, Pascal, Groovy, Objective-C
- **Games, graphics and GPU:** GDScript, C++
- **Smart contracts:** Solidity, Move, Vyper
- **Automation:** Bash, PowerShell

## How to use this workbook

1. Start with one general-purpose language and understand variables, expressions, conditions, loops, functions, and data structures.
2. Compare the same idea across languages; do not assume syntax similarity means identical semantics.
3. For each language, study its type system, memory model, runtime, package manager, testing tools, and standard library.
4. Save each example with the shown file extension and use the official compiler, interpreter, or development environment.
5. Before marking an example verified, record the exact toolchain version and test command.

## 40 starter examples

### 01. Python

**Main use:** general-purpose  
**File extension:** `.py`

```python
print("Hello, world!")
```

### 02. JavaScript

**Main use:** web and scripting  
**File extension:** `.js`

```javascript
console.log("Hello, world!");
```

### 03. TypeScript

**Main use:** web and application  
**File extension:** `.ts`

```typescript
console.log("Hello, world!");
```

### 04. Java

**Main use:** enterprise and backend  
**File extension:** `.java`

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

### 05. C

**Main use:** systems  
**File extension:** `.c`

```c
#include <stdio.h>
int main(void) {
    puts("Hello, world!");
    return 0;
}
```

### 06. C++

**Main use:** systems and game development  
**File extension:** `.cpp`

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!\n";
}
```

### 07. C#

**Main use:** enterprise and applications  
**File extension:** `.cs`

```csharp
using System;
class Program {
    static void Main() => Console.WriteLine("Hello, world!");
}
```

### 08. Go

**Main use:** backend and cloud  
**File extension:** `.go`

```go
package main
import "fmt"
func main() {
    fmt.Println("Hello, world!")
}
```

### 09. Rust

**Main use:** systems  
**File extension:** `.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

### 10. PHP

**Main use:** web backend  
**File extension:** `.php`

```php
<?php
echo "Hello, world!\n";
```

### 11. Ruby

**Main use:** web and scripting  
**File extension:** `.rb`

```ruby
puts "Hello, world!"
```

### 12. Swift

**Main use:** Apple platforms  
**File extension:** `.swift`

```swift
print("Hello, world!")
```

### 13. Kotlin

**Main use:** Android and backend  
**File extension:** `.kt`

```kotlin
fun main() {
    println("Hello, world!")
}
```

### 14. Dart

**Main use:** cross-platform apps  
**File extension:** `.dart`

```dart
void main() {
  print('Hello, world!');
}
```

### 15. R

**Main use:** statistics and data science  
**File extension:** `.R`

```r
cat("Hello, world!\n")
```

### 16. Julia

**Main use:** scientific computing  
**File extension:** `.jl`

```julia
println("Hello, world!")
```

### 17. MATLAB

**Main use:** numerical computing  
**File extension:** `.m`

```matlab
disp('Hello, world!')
```

### 18. Scala

**Main use:** JVM and data engineering  
**File extension:** `.scala`

```scala
object Main extends App {
  println("Hello, world!")
}
```

### 19. Haskell

**Main use:** functional programming  
**File extension:** `.hs`

```haskell
main :: IO ()
main = putStrLn "Hello, world!"
```

### 20. Elixir

**Main use:** concurrent and distributed systems  
**File extension:** `.ex`

```elixir
IO.puts("Hello, world!")
```

### 21. Erlang

**Main use:** concurrent and distributed systems  
**File extension:** `.erl`

```erlang
-module(hello).
-export([main/0]).
main() -> io:format("Hello, world!~n").
```

### 22. Clojure

**Main use:** functional programming  
**File extension:** `.clj`

```clojure
(println "Hello, world!")
```

### 23. OCaml

**Main use:** functional programming  
**File extension:** `.ml`

```ocaml
let () = print_endline "Hello, world!"
```

### 24. F#

**Main use:** functional and .NET  
**File extension:** `.fsx`

```fsharp
printfn "Hello, world!"
```

### 25. Lua

**Main use:** embedded scripting and games  
**File extension:** `.lua`

```lua
print("Hello, world!")
```

### 26. Perl

**Main use:** text processing and scripting  
**File extension:** `.pl`

```perl
print "Hello, world!\n";
```

### 27. Bash

**Main use:** shell scripting  
**File extension:** `.sh`

```bash
#!/usr/bin/env bash
printf '%s\n' 'Hello, world!'
```

### 28. PowerShell

**Main use:** automation and administration  
**File extension:** `.ps1`

```powershell
Write-Output 'Hello, world!'
```

### 29. Fortran

**Main use:** scientific computing  
**File extension:** `.f90`

```fortran
program hello
  print *, "Hello, world!"
end program hello
```

### 30. COBOL

**Main use:** business and legacy systems  
**File extension:** `.cob`

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY "Hello, world!".
           STOP RUN.
```

### 31. Ada

**Main use:** reliable and safety-critical systems  
**File extension:** `.adb`

```ada
with Ada.Text_IO;
procedure Hello is
begin
   Ada.Text_IO.Put_Line("Hello, world!");
end Hello;
```

### 32. Pascal

**Main use:** education and general-purpose  
**File extension:** `.pas`

```pascal
program Hello;
begin
  writeln('Hello, world!');
end.
```

### 33. Groovy

**Main use:** JVM scripting  
**File extension:** `.groovy`

```groovy
println 'Hello, world!'
```

### 34. Solidity

**Main use:** smart contracts  
**File extension:** `.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract Hello {
    function message() external pure returns (string memory) {
        return "Hello, world!";
    }
}
```

### 35. Move

**Main use:** resource-oriented smart contracts  
**File extension:** `.move`

```move
module example::hello {
    public fun message(): vector<u8> {
        b"Hello, world!"
    }
}
```

### 36. Zig

**Main use:** systems programming  
**File extension:** `.zig`

```zig
const std = @import("std");
pub fn main() void {
    std.debug.print("Hello, world!\n", .{});
}
```

### 37. GDScript

**Main use:** game development  
**File extension:** `.gd`

```gdscript
extends SceneTree

func _initialize() -> void:
    print("Hello, world!")
    quit()
```

### 38. Vyper

**Main use:** smart contracts  
**File extension:** `.vy`

```vyper
@external
@view
def message() -> String[13]:
    return "Hello, world!"
```

### 39. Objective-C

**Main use:** Apple platforms  
**File extension:** `.m`

```objective-c
#import <Foundation/Foundation.h>
int main(void) {
    @autoreleasepool {
        NSLog(@"Hello, world!");
    }
    return 0;
}
```

### 40. Assembly (x86-64 NASM)

**Main use:** low-level systems  
**File extension:** `.asm`

```asm
section .data
    msg db "Hello, world!", 10
    len equ $ - msg
section .text
    global _start
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall
    mov rax, 60
    xor rdi, rdi
    syscall
```


## Accuracy and status

- These are introductory snippets, not full lessons or production examples.
- Examples have not all been executed in their respective toolchains. Treat them as **Draft / unverified** until tested.
- Solidity, Move, and Vyper are smart-contract languages; Assembly is an architecture-specific language family. They are included because they teach important programming concepts, but they are not interchangeable with general-purpose languages.
- The Assembly sample targets Linux x86-64 with NASM syntax. Other CPU architectures and operating systems require different code.
- Smart-contract examples should be studied in local development environments and test networks, never deployed with real funds as a beginner exercise.
- Prefer official language documentation and specify version scope in every future deep-dive guide.

## Next learning sequence

For every language, UKE should eventually add: profile and history, installation/toolchain, syntax, types, control flow, functions, collections, modules, errors, testing, debugging, concurrency where relevant, memory/runtime model, standard library, package ecosystem, security notes, projects, exercises, and verified references.
