---
id: python.exercise.conditionals-and-loops
title: تمرین شرط‌ها و حلقه‌ها
content_type: exercise
locale: fa
domain: programming-languages
level: beginner
status: draft
prerequisites:
  - python.conditional-statements
  - python.for-and-while-loops
task: برنامه‌ای بنویسید که اعداد یک تا n را پیمایش کند، زوج‌ها را جمع بزند و تعداد اعداد فرد را نیز بشمارد.
hints:
  - برای پیمایش از range استفاده کنید.
  - با باقیمانده تقسیم بر دو، زوج یا فرد بودن را تشخیص دهید.
  - جمع و شمارنده را پیش از آغاز حلقه مقداردهی کنید.
solution: |
  n = int(input("n: "))
  even_sum = 0
  odd_count = 0
  for number in range(1, n + 1):
      if number % 2 == 0:
          even_sum += number
      else:
          odd_count += 1
  print(even_sum, odd_count)
assessment_criteria:
  - حلقه از یک تا n را بدون حذف کران پایانی طی می‌کند.
  - زوج و فرد بودن با شرط درست تشخیص داده می‌شود.
  - جمع و تعداد به‌درستی به‌روزرسانی می‌شوند.
estimated_minutes: 20
sources:
  - python-docs
---

# تمرین: شرط‌ها و حلقه‌ها

## هدف

ترکیب حلقه و شرط برای پردازش یک بازهٔ عددی را تمرین کنید.

## صورت مسئله

عدد صحیح مثبت `n` را دریافت کنید. اعداد ۱ تا n را پیمایش کنید؛ مجموع اعداد زوج و تعداد اعداد فرد را محاسبه و چاپ کنید.

## مثال

برای `n = 6`، عددهای زوج ۲، ۴ و ۶ هستند؛ مجموع آن‌ها ۱۲ است. عددهای فرد ۱، ۳ و ۵ هستند؛ تعدادشان ۳ است.

## نکات

- در `range(1, n + 1)` کران پایانی را طوری تنظیم کنید که n هم بررسی شود.
- قبل از حلقه، متغیرهای جمع و شمارنده را مقداردهی اولیه کنید.
- در نسخهٔ توسعه‌یافته، مقدار صفر یا ورودی منفی را نیز مدیریت کنید.

## پاسخ پیشنهادی

```python
n = int(input("n: "))
even_sum = 0
odd_count = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_count += 1

print(f"مجموع زوج‌ها: {even_sum}")
print(f"تعداد فردها: {odd_count}")
```

## معیار ارزیابی

کران بازه، شرط زوج‌بودن و به‌روزرسانی شمارنده باید صحیح باشد. راه‌حل باید برای `n = 1` و یک عدد زوج نیز رفتار درست داشته باشد.
