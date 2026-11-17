---
id: python.basic-data-types
title: نوع‌های داده پایه در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - نوع‌های int و float و str و bool را معرفی کنید.
  - تبدیل نوع صریح را با مثال انجام دهید.
  - تفاوت تبدیل نوع و تغییر مقدار را توضیح دهید.
prerequisites:
  - python.variables-and-values
concepts:
  - python.types
  - python.type-conversion
sources:
  - python-docs
estimated_minutes: 25
version_scope:
  minimum: "3"
  maximum: null
  notes: "مناسب برای پایتون ۳."
---

# نوع‌های داده پایه در پایتون

## ۱. چرا نوع داده مهم است؟

نوع داده مشخص می‌کند یک مقدار چه ماهیتی دارد و چه عملیاتی روی آن قابل انجام است. برای نمونه، جمع دو عدد با کنار هم قرار دادن دو رشته یکسان نیست.

## ۲. عدد صحیح و اعشاری

`int` برای عددهای صحیح و `float` برای عددهای ممیز شناور به‌کار می‌رود:

```python
students = 28
average = 18.75

print(students + 2)       # 30
print(average * 2)        # 37.5
```

عددهای ممیز شناور نمایش دودویی تقریبی دارند؛ بنابراین بعضی محاسبات اعشاری ممکن است دقیقاً برابر مقدار ده‌دهی مورد انتظار نباشند.

## ۳. رشته‌ها

رشته (`str`) دنباله‌ای از نویسه‌هاست:

```python
first = "Ali"
last = "Ahmadi"
full_name = first + " " + last
print(full_name)
```

برای قرار دادن مقدار متغیر در متن، رشته قالب‌بندی‌شده مناسب است:

```python
age = 17
print(f"Age: {age}")
```

## ۴. مقدارهای بولی

نوع `bool` دو مقدار دارد: `True` و `False`. این مقدارها معمولاً نتیجه مقایسه‌ها هستند:

```python
temperature = 22
is_warm = temperature > 20
print(is_warm)  # True
```

## ۵. تبدیل نوع

تبدیل نوع را می‌توان با سازنده‌هایی مانند `int()`، `float()` و `str()` به‌صورت صریح انجام داد:

```python
raw_number = "42"
number = int(raw_number)
print(number + 8)  # 50
```

هر رشته‌ای قابل تبدیل به عدد نیست؛ برای نمونه `int("hello")` خطای `ValueError` ایجاد می‌کند. هنگام دریافت ورودی کاربر باید احتمال ورودی نامعتبر را در نظر گرفت.

## ۶. اشتباهات رایج

- جمع‌کردن رشته و عدد بدون تبدیل مناسب.
- فرض اینکه `input()` عدد برمی‌گرداند؛ خروجی آن رشته است.
- مقایسه مستقیم عدد ممیز شناور با مقدار دقیق، بدون توجه به خطای نمایش.
- فراموش‌کردن اینکه تبدیل ممکن است خطا ایجاد کند.

## ۷. تمرین

۱. دو عدد را از کاربر با `input()` بگیرید و مجموع آن‌ها را چاپ کنید.
۲. یک مقدار بولی بسازید که مشخص کند نمره از ۱۰ بیشتر است.
۳. بررسی کنید تبدیل رشته `"12.5"` به `int` چه نتیجه‌ای دارد و چرا.

## ۸. منابع

- [مستندات رسمی نوع‌های داخلی](https://docs.python.org/3/library/stdtypes.html)
- [آموزش رسمی پایتون: رشته‌ها](https://docs.python.org/3/tutorial/introduction.html#strings)
