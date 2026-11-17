---
id: python.comprehensions-and-iteration
title: پیمایش و درک‌لیست‌ها در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: intermediate
status: draft
learning_objectives:
  - مفهوم iterable و iterator را از هم تفکیک کنید.
  - از list comprehension برای ساخت فهرست استفاده کنید.
  - comprehensionهای دیکشنری و مجموعه را بشناسید.
  - خوانایی را در انتخاب حلقه یا comprehension ارزیابی کنید.
prerequisites:
  - python.for-and-while-loops
  - python.lists-and-tuples
  - python.dictionaries-and-sets
concepts:
  - python.iterables
  - python.iterators
  - python.comprehensions
sources:
  - python-docs
estimated_minutes: 40
version_scope:
  minimum: "3"
  maximum: null
  notes: "مفاهیم iterable، iterator و comprehension در پایتون ۳."
---

# پیمایش و درک‌لیست‌ها در پایتون

## ۱. Iterable و Iterator

شیء iterable می‌تواند یک iterator تولید کند؛ مانند رشته، فهرست، تاپل و مجموعه. iterator وضعیت پیمایش را نگه می‌دارد و با `next()` عضو بعدی را ارائه می‌کند:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
```

پس از پایان عضوها، فراخوانی بعدی `next()` استثنای `StopIteration` ایجاد می‌کند. حلقه for این سازوکار را به‌صورت خودکار مدیریت می‌کند.

## ۲. درک‌لیست

درک‌لیست (List comprehension) راهی فشرده برای ساخت فهرست از یک iterable است:

```python
squares = [number ** 2 for number in range(1, 6)]
print(squares)
```

خروجی `[1, 4, 9, 16, 25]` است.

## ۳. شرط داخل comprehension

```python
even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]
print(even_numbers)
```

عبارت `if` عضوهایی را فیلتر می‌کند که شرط را برآورده نمی‌کنند.

## ۴. دیکشنری و مجموعه

```python
word_lengths = {word: len(word) for word in ["code", "learn"]}
unique_lengths = {len(word) for word in ["cat", "dog", "python"]}
```

شکل اول دیکشنری و شکل دوم مجموعه می‌سازد. در مجموعه، عضوهای تکراری فقط یک بار نگهداری می‌شوند.

## ۵. چه زمانی از comprehension استفاده کنیم؟

comprehension برای تبدیل و فیلتر ساده مناسب است. اگر چند شرط تو در تو، محاسبه سنگین یا چند مرحله با اثر جانبی دارید، حلقه معمولی اغلب خواناتر است. کوتاه‌بودن کد به‌تنهایی معیار کیفیت نیست.

## ۶. Generator expression

با پرانتز می‌توان generator expression ساخت که مقدارها را به‌صورت تنبل (lazy) تولید می‌کند:

```python
total = sum(number * number for number in range(1000))
```

این شکل از ساختن یک فهرست کامل برای همین محاسبه جلوگیری می‌کند؛ مقدارها هنگام نیاز تولید می‌شوند.

## ۷. خطاهای رایج

- نوشتن comprehension بسیار پیچیده و دشوارخوان.
- تصور اینکه generator را می‌توان بارها از ابتدا پیمایش کرد؛ بسیاری از generatorها یک‌بارمصرف‌اند.
- مصرف ناخواسته حافظه با ساخت فهرست بسیار بزرگ.
- تغییر دادن داده بیرونی در حین ساخت comprehension.

## ۸. تمرین

۱. از فهرست عددها، فهرست مربع عددهای زوج را بسازید.
۲. دیکشنری‌ای بسازید که هر واژه را به طول آن نگاشت کند.
۳. مجموع مربع‌های اعداد را با generator expression محاسبه و روش آن را توضیح دهید.

## منابع

- [ساختارهای داده و comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Iterableها و iteratorها](https://docs.python.org/3/library/stdtypes.html#iterator-types)
