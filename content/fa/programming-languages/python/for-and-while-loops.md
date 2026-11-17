---
id: python.for-and-while-loops
title: حلقه‌های for و while در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - کاربرد حلقه را توضیح دهید.
  - روی یک دنباله با for پیمایش کنید.
  - شرط پایان حلقه while را طراحی کنید.
  - خطر حلقه بی‌نهایت را تشخیص دهید.
prerequisites:
  - python.conditional-statements
concepts:
  - python.loops
  - python.iteration
sources:
  - python-tutorial
estimated_minutes: 30
version_scope:
  minimum: "3"
  maximum: null
  notes: "حلقه‌های پایه پایتون ۳."
---

# حلقه‌های for و while در پایتون

## ۱. حلقه چرا لازم است؟

وقتی عملیاتی باید چند بار تکرار شود، حلقه از نوشتن چندباره دستورهای مشابه جلوگیری می‌کند. هر تکرار را یک دور یا iteration می‌نامند.

## ۲. حلقه for

حلقه `for` روی اعضای یک دنباله یا شیء قابل پیمایش حرکت می‌کند:

```python
for name in ["Mina", "Reza", "Nima"]:
    print(name)
```

تابع `range()` برای تولید دنباله‌ای از عددها کاربرد دارد:

```python
for number in range(1, 5):
    print(number)
```

خروجی عددهای ۱ تا ۴ است؛ کران پایانی در `range` شامل نمی‌شود.

## ۳. حلقه while

حلقه `while` تا زمانی ادامه می‌یابد که شرط آن درست باشد:

```python
count = 3

while count > 0:
    print(count)
    count -= 1

print("پایان")
```

در هر دور مقدار `count` کاهش می‌یابد تا شرط نادرست شود.

## ۴. کنترل حلقه

- `break` حلقه فعلی را فوراً پایان می‌دهد.
- `continue` ادامه بدنه همان دور را کنار می‌گذارد و به دور بعد می‌رود.

از این دستورها فقط وقتی استفاده کنید که جریان برنامه را واضح‌تر می‌کنند.

## ۵. حلقه بی‌نهایت

اگر شرط حلقه `while` همیشه درست بماند و راه خروجی وجود نداشته باشد، حلقه پایان نمی‌یابد. برای پیشگیری، تغییر متغیرهای مؤثر بر شرط و مسیر خروج را از ابتدا طراحی کنید.

## ۶. اشتباهات رایج

- اشتباه در محدوده `range` و فراموش‌کردن اینکه انتهای آن شامل نمی‌شود.
- تغییرندادن متغیر شرط در حلقه `while`.
- استفاده نادرست از `break` در حلقه‌های تو در تو.
- تغییر دادن مجموعه‌ای که هم‌زمان روی آن پیمایش می‌کنید، بدون درک اثر آن.

## ۷. تمرین

۱. مجموع عددهای ۱ تا ۱۰۰ را با حلقه محاسبه کنید.
۲. اعضای یک فهرست نام را با `for` چاپ کنید.
۳. برنامه‌ای بنویسید که تا رسیدن شمارنده به صفر ادامه یابد.

## ۸. منابع

- [آموزش رسمی پایتون: دستورهای for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [آموزش رسمی پایتون: دستورهای while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
