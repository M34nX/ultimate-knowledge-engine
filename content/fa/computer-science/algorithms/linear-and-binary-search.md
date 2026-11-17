---
id: cs.algorithms.search
title: جست‌وجوی خطی و دودویی
content_type: lesson
locale: fa
domain: computer-science
level: beginner
status: draft
learning_objectives:
  - جست‌وجوی خطی را پیاده‌سازی و تحلیل کنید.
  - پیش‌شرط مرتب‌بودن داده برای جست‌وجوی دودویی را توضیح دهید.
  - جست‌وجوی دودویی تکراری را بدون خطای مرزی بنویسید.
prerequisites:
  - cs.algorithms.big-o
concepts:
  - cs.algorithms.linear-search
  - cs.algorithms.binary-search
sources:
  - mit-ocw-6-006
estimated_minutes: 35
---

# جست‌وجوی خطی و دودویی

## ۱. جست‌وجوی خطی

جست‌وجوی خطی اعضا را از ابتدا تا انتها بررسی می‌کند و با یافتن هدف، مکان آن را برمی‌گرداند:

```python
def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
```

این روش به مرتب‌بودن فهرست نیاز ندارد. در بدترین حالت همهٔ n عضو بررسی می‌شوند؛ پیچیدگی زمانی O(n) و فضای کمکی این نسخه O(1) است.

## ۲. ایدهٔ جست‌وجوی دودویی

اگر داده مرتب باشد، می‌توان هر بار نیمه‌ای از بازهٔ جست‌وجو را کنار گذاشت. ابتدا عضو میانی بررسی می‌شود:
- اگر برابر هدف بود، مکان پیدا شده است.
- اگر هدف کوچک‌تر بود، نیمهٔ راست حذف می‌شود.
- اگر هدف بزرگ‌تر بود، نیمهٔ چپ حذف می‌شود.

این کار تا یافتن هدف یا خالی‌شدن بازه ادامه دارد.

## ۳. پیاده‌سازی تکراری

```python
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = (left + right) // 2
        value = items[middle]

        if value == target:
            return middle
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

این تابع به ورودی مرتب‌شده نیاز دارد. برای فهرست n عضوی، تعداد مراحل در حدود log₂(n) رشد می‌کند؛ زمان O(log n) و فضای کمکی این نسخه O(1) است.

## ۴. درستی و فرض‌ها

اگر فهرست مرتب نباشد، حذف نیمهٔ بازه تضمین نمی‌کند که هدف از دست نرود؛ در این حالت نتیجه ممکن است غلط باشد. پیش‌شرط تابع باید در مستندات نوشته شود یا ورودی پیش از جست‌وجو مرتب شود.

## ۵. خطاهای رایج

- اجرای جست‌وجوی دودویی روی دادهٔ نامرتب.
- استفاده از `left < right` به‌جای شرط متناسب با قرارداد بازه.
- فراموش‌کردن `+ 1` یا `- 1` پس از بررسی عضو میانی.
- اشتباه گرفتن اندیس با مقدار عضو.

## ۶. تمرین

۱. هر دو تابع را روی فهرست خالی، تک‌عضوی و چندعضوی آزمایش کنید.
۲. جست‌وجوی دودویی را روی فهرست مرتب با هدف موجود و ناموجود اجرا کنید.
۳. توضیح دهید چرا برای n بزرگ، log₂(n) معمولاً بسیار کمتر از n است.

## منابع

- [MIT OCW 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
