---
id: python.exercise.collections-and-functions
title: تمرین مجموعه‌ها و توابع
content_type: exercise
locale: fa
domain: programming-languages
level: beginner
status: draft
prerequisites:
  - python.functions.basics
  - python.lists-and-tuples
  - python.dictionaries-and-sets
task: تابعی بنویسید که فهرستی از نام‌ها را بگیرد و تعداد تکرار هر نام را در قالب دیکشنری برگرداند.
hints:
  - یک دیکشنری خالی بسازید.
  - روی نام‌ها پیمایش کنید.
  - اگر کلید وجود داشت مقدارش را افزایش دهید وگرنه آن را با یک مقدار آغاز کنید.
solution: |
  def count_names(names):
      counts = {}
      for name in names:
          counts[name] = counts.get(name, 0) + 1
      return counts

  print(count_names(["Ali", "Sara", "Ali"]))
assessment_criteria:
  - تابع نتیجه را return می‌کند.
  - شمارش تکرارها برای نام‌های یکسان درست است.
  - ورودی خالی دیکشنری خالی برمی‌گرداند.
estimated_minutes: 25
sources:
  - python-docs
---

# تمرین: شمارش فراوانی نام‌ها

## هدف

ترکیب تابع، فهرست و دیکشنری را در یک مسئلهٔ کوچک به‌کار ببرید.

## صورت مسئله

تابعی به نام `count_names` بنویسید که فهرستی از نام‌ها را دریافت کند و دیکشنری‌ای برگرداند که کلیدهای آن نام‌ها و مقدارهایش تعداد تکرار هر نام باشند.

## مثال

ورودی:

```python
["Ali", "Sara", "Ali", "Nima", "Sara", "Ali"]
```

خروجی مورد انتظار:

```python
{"Ali": 3, "Sara": 2, "Nima": 1}
```

ترتیب نمایش اعضای دیکشنری در این تمرین معیار ارزیابی نیست.

## پاسخ پیشنهادی

```python
def count_names(names):
    counts = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts

print(count_names(["Ali", "Sara", "Ali"]))
```

## آزمون‌های پیشنهادی

- فهرست خالی باید `{}` برگرداند.
- نامی که فقط یک بار آمده باید مقدار ۱ داشته باشد.
- نام تکراری باید به‌درستی شمرده شود.

## معیار ارزیابی

تابع باید به‌جای چاپ‌کردن نتیجه، آن را بازگرداند؛ برای شمارش از کلید دیکشنری استفاده کند و ورودی خالی را نیز درست پردازش کند.
