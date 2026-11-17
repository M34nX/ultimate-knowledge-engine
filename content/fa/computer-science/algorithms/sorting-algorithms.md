---
id: cs.algorithms.sorting
title: آشنایی با الگوریتم‌های مرتب‌سازی
content_type: lesson
locale: fa
domain: computer-science
level: beginner
status: draft
learning_objectives:
  - هدف و خروجی مرتب‌سازی را تعریف کنید.
  - ایدهٔ مرتب‌سازی درجی و ادغامی را توضیح دهید.
  - تفاوت رشد زمانی O(n²) و O(n log n) را بیان کنید.
  - مفهوم پایداری مرتب‌سازی را توضیح دهید.
prerequisites:
  - cs.algorithms.big-o
  - cs.algorithms.search
concepts:
  - cs.algorithms.sorting
sources:
  - mit-ocw-6-006
estimated_minutes: 45
---

# آشنایی با الگوریتم‌های مرتب‌سازی

## ۱. مرتب‌سازی چیست؟

مرتب‌سازی، بازچینی داده‌ها بر اساس یک معیار است؛ مانند ترتیب عددی یا حروف الفبا. دادهٔ مرتب می‌تواند جست‌وجو و گزارش‌گیری را ساده‌تر کند.

## ۲. مرتب‌سازی درجی

در مرتب‌سازی درجی (Insertion sort)، هر عضو به جای درست خود در بخش مرتب‌شدهٔ قبلی وارد می‌شود:

```python
def insertion_sort(items):
    result = items.copy()

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result
```

این پیاده‌سازی فهرست ورودی را تغییر نمی‌دهد. زمان بدترین حالت O(n²) است، اما روی ورودی کوچک یا تقریباً مرتب می‌تواند ساده و کاربردی باشد.

## ۳. مرتب‌سازی ادغامی

مرتب‌سازی ادغامی (Merge sort) مسئله را به بخش‌های کوچک‌تر تقسیم می‌کند، هر بخش را مرتب می‌کند و سپس نتایج را ادغام می‌کند. زمان آن در حالت‌های معمول O(n log n) است و پیاده‌سازی متداول به فضای کمکی نیاز دارد.

```python
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]
```

این قطعه فقط مرحلهٔ ادغام دو فهرست از قبل مرتب‌شده را نشان می‌دهد؛ برای الگوریتم کامل باید مرحلهٔ تقسیم و فراخوانی بازگشتی نیز اضافه شود.

## ۴. پایداری مرتب‌سازی

الگوریتم پایدار ترتیب نسبی عضوهایی را که کلید برابر دارند حفظ می‌کند. این ویژگی در مرتب‌سازی چندمرحله‌ای داده‌ها می‌تواند مهم باشد.

## ۵. انتخاب الگوریتم

برای یادگیری، پیاده‌سازی چند الگوریتم کمک می‌کند مصالحه‌ها را بفهمید. در برنامهٔ واقعی پایتون معمولاً از `sorted()` یا متد `list.sort()` استفاده می‌شود، مگر دلیل مشخصی برای الگوریتم سفارشی وجود داشته باشد.

## ۶. اشتباهات رایج

- اعلام پیچیدگی بدون تعیین بهترین یا بدترین حالت.
- مقایسهٔ الگوریتم‌ها بدون درنظرگرفتن اندازهٔ ورودی و حافظه.
- تصور اینکه قطعهٔ merge به‌تنهایی کل Merge sort است.
- نادیده‌گرفتن پایداری در داده‌های دارای کلید تکراری.

## ۷. تمرین

۱. مرتب‌سازی درجی را روی فهرستی شامل عددهای منفی و مثبت اجرا کنید.
۲. مرحلهٔ ادغام دو فهرست مرتب را با دست دنبال کنید.
۳. توضیح دهید چرا برای برنامهٔ معمول بهتر است ابتدا از sorted استفاده کنید.

## منابع

- [MIT OCW 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [مستندات مرتب‌سازی پایتون](https://docs.python.org/3/howto/sorting.html)
