# دفترچه آموزشی ۴۰ زبان برنامه‌نویسی

این دفترچه **۴۰ زبان برنامه‌نویسی** را با یک نمونه کوچک و قابل مقایسه معرفی می‌کند. این مجموعه نقطه شروع است، نه ۴۰ دوره کامل. زبان‌های قرارداد هوشمند مدل اجرای متفاوتی دارند.

## دسته‌بندی بر اساس کاربرد

- **General-purpose and application:** Python, Java, C#, Kotlin, Swift, Dart, Ruby, PHP
- **Web and scripting:** JavaScript, TypeScript, PHP, Ruby, Lua, Perl
- **Systems, performance and low-level:** C, C++, Rust, Go, Zig, Assembly
- **Functional and concurrent:** Haskell, Scala, Elixir, Erlang, Clojure, OCaml, F#
- **Scientific and data:** R, Julia, MATLAB, Fortran
- **Enterprise and legacy:** COBOL, Ada, Pascal, Groovy, Objective-C
- **Games, graphics and GPU:** GDScript, C++
- **Smart contracts:** Solidity, Move, Vyper
- **Automation:** Bash, PowerShell

## روش استفاده

۱. با یک زبان عمومی شروع کنید و متغیر، عبارت، شرط، حلقه، تابع و ساختمان داده را بیاموزید.  
۲. یک مفهوم را میان زبان‌ها مقایسه کنید؛ شباهت ظاهری دستورها به معنی یکسان بودن رفتار زبان‌ها نیست.  
۳. برای هر زبان، سیستم نوع، مدل حافظه، محیط اجرا، مدیر بسته، ابزار آزمون و کتابخانه استاندارد را بررسی کنید.  
۴. نمونه را با پسوند نشان‌داده‌شده ذخیره و با ابزار رسمی همان زبان اجرا کنید.  
۵. پیش از تأیید هر نمونه، نسخه دقیق ابزار و فرمان آزمون را ثبت کنید.

## ۴۰ نمونه کد

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


## دقت و وضعیت

- این نمونه‌ها مقدماتی‌اند و دوره کامل یا کد آماده تولید نیستند.
- همه نمونه‌ها هنوز در ابزارهای رسمی خود اجرا نشده‌اند؛ وضعیت آن‌ها **پیش‌نویس / تأییدنشده** است.
- زبان‌های Solidity و Move و Vyper برای قرارداد هوشمند هستند و Assembly به معماری پردازنده وابسته است.
- نمونه Assembly برای Linux x86-64 با دستور زبان NASM نوشته شده است.
- قراردادهای هوشمند را فقط در محیط محلی و شبکه آزمایشی بررسی کنید؛ برای تمرین مقدماتی از دارایی واقعی استفاده نکنید.
- راهنماهای کامل آینده باید نسخه زبان و ابزارها را مشخص و به مستندات رسمی ارجاع دهند.

## مسیر توسعه بعدی

برای هر زبان باید به‌تدریج این بخش‌ها افزوده شوند: معرفی و تاریخچه، نصب و ابزارها، نحو، نوع‌ها، کنترل جریان، تابع، مجموعه‌ها، ماژول، خطاها، آزمون، اشکال‌زدایی، هم‌روندی در صورت نیاز، مدل حافظه و اجرا، کتابخانه استاندارد، اکوسیستم بسته‌ها، امنیت، پروژه، تمرین و منابع تأییدشده.
