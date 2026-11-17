---
id: python.iterators-and-generators
title: Iterator و Generator در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: intermediate
status: draft
learning_objectives:
  - پروتکل iterator را با __iter__ و __next__ توصیف کنید.
  - generator function را با yield تعریف کنید.
  - تفاوت تولید تنبل و ساخت فهرست کامل را تحلیل کنید.
  - کاربرد generator را برای داده‌های بزرگ تشخیص دهید.
prerequisites:
  - python.comprehensions-and-iteration
  - python.functions.basics
concepts:
  - python.iterator-protocol
  - python.generators
sources:
  - python-docs
estimated_minutes: 45
version_scope:
  minimum: "3"
  maximum: null
  notes: "پروتکل پیمایش استاندارد پایتون ۳."
---

# Iterator و Generator در پایتون

## ۱. مرور پیمایش

شیء iterable می‌تواند iterator تولید کند. iterator در هر مرحله مقدار بعدی را عرضه می‌کند و وقتی داده‌ای باقی نمانده باشد، `StopIteration` رخ می‌دهد. حلقه for این جزئیات را به شکل خودکار مدیریت می‌کند.

## ۲. ساخت generator با yield

تابعی که از `yield` استفاده می‌کند، generator function است. فراخوانی آن یک generator object برمی‌گرداند؛ بدنه تابع با درخواست مقدار بعدی اجرا می‌شود:

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for item in count_up_to(3):
    print(item)
```

خروجی عددهای ۱، ۲ و ۳ است. پس از هر `yield` وضعیت تابع حفظ می‌شود و اجرای بعدی از همان نقطه ادامه پیدا می‌کند.

## ۳. تولید تنبل

ساخت فهرست همه نتایج را همان ابتدا در حافظه نگه می‌دارد. generator مقدارها را هنگام نیاز تولید می‌کند. این ویژگی برای جریان داده یا مجموعه‌های بزرگ مفید است؛ البته محاسبه همچنان هزینه زمانی دارد و generator را نباید معادل «بدون مصرف حافظه» دانست.

## ۴. generator expression

```python
numbers = (n * n for n in range(1_000_000))
first_three = [next(numbers) for _ in range(3)]
print(first_three)
```

عبارت داخل پرانتز generator می‌سازد. این generator را می‌توان تدریجی مصرف کرد؛ پس از مصرف هر عضو، آن عضو دوباره در دسترس نیست.

## ۵. چه زمانی generator مناسب است؟

- داده‌ها به‌ترتیب و مرحله‌ای پردازش می‌شوند.
- نیازی به دسترسی تصادفی یا پیمایش دوباره نیست.
- حجم داده زیاد است و تولید تدریجی مناسب‌تر است.
- یک زنجیره پردازش می‌خواهید که خروجی هر مرحله ورودی مرحله بعد شود.

اگر نتیجه باید چند بار پیمایش شود یا اندیس‌گذاری لازم است، list مناسب‌تر است.

## ۶. خطاهای رایج

- انتظار پیمایش دوباره generator مصرف‌شده.
- فراموش‌کردن اینکه تابع دارای yield با فراخوانی، مقدار نهایی را فوراً محاسبه نمی‌کند.
- استفاده از generator در جایی که دسترسی تصادفی لازم است.
- تصور اینکه تولید تنبل همیشه سریع‌تر است؛ مزیت آن به الگوی مصرف و اندازه داده بستگی دارد.

## ۷. تمرین

۱. generatorای بنویسید که عددهای زوج تا یک حد را تولید کند.
۲. مجموع مربع اعداد یک فایل بزرگ را به‌صورت خط‌به‌خط و بدون ساخت فهرست کامل محاسبه کنید.
۳. موردی را توضیح دهید که در آن list از generator مناسب‌تر باشد.

## منابع

- [Generatorها در آموزش رسمی پایتون](https://docs.python.org/3/tutorial/classes.html#generators)
- [عبارت‌های generator در مرجع زبان](https://docs.python.org/3/reference/expressions.html#generator-expressions)
