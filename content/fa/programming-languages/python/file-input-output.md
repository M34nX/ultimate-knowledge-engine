---
id: python.file-input-output
title: خواندن و نوشتن فایل در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - فایل متنی را با open باز کنید و محتوای آن را بخوانید.
  - داده را با حالت مناسب در فایل بنویسید.
  - دلیل استفاده از with و تعیین encoding را توضیح دهید.
  - خطاهای متداول مسیر و دسترسی را تشخیص دهید.
prerequisites:
  - python.strings-and-formatting
  - python.exceptions-and-errors
concepts:
  - python.file-io
  - python.context-managers
sources:
  - python-docs
estimated_minutes: 40
version_scope:
  minimum: "3"
  maximum: null
  notes: "مثال‌ها برای فایل متنی UTF-8 نوشته شده‌اند."
---

# خواندن و نوشتن فایل در پایتون

## ۱. چرا فایل؟

متغیرها معمولاً برای نگهداری داده در زمان اجرای برنامه مناسب‌اند. اگر داده باید پس از پایان برنامه باقی بماند، می‌توان آن را در فایل ذخیره کرد. این درس روی فایل‌های متنی تمرکز دارد.

## ۲. خواندن فایل با with

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

تابع `open` فایل را باز می‌کند. حالت `r` برای خواندن است. استفاده از `with` باعث می‌شود فایل پس از خروج از بلوک به‌درستی بسته شود، حتی اگر خطایی رخ دهد.

## ۳. نوشتن و افزودن

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Another line\n")
```

حالت `w` فایل موجود را بازنویسی می‌کند یا فایل تازه می‌سازد. حالت `a` متن را به انتهای فایل می‌افزاید. پیش از استفاده از `w` مطمئن شوید بازنویسی داده موردنظر است.

## ۴. خواندن خط‌به‌خط

برای فایل بزرگ بهتر است از پیمایش خطی استفاده کنید تا کل محتوا یک‌باره در حافظه بارگذاری نشود:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

متد `rstrip()` در این مثال نویسه‌های انتهایی مانند newline را حذف می‌کند.

## ۵. مسیر فایل

مسیر نسبی نسبت به پوشه کاری فعلی تفسیر می‌شود، نه لزوماً پوشه‌ای که فایل پایتون در آن قرار دارد. برای مدیریت قابل‌حمل مسیرها از `pathlib` استفاده کنید:

```python
from pathlib import Path

path = Path("data") / "notes.txt"
path.parent.mkdir(parents=True, exist_ok=True)

path.write_text("سلام\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
```

## ۶. نکات ایمنی و پایداری

- داده مهم را پیش از بازنویسی پشتیبان‌گیری کنید.
- ورودی کاربر را بدون کنترل به مسیر فایل تبدیل نکنید.
- برای متن فارسی، encoding را صریحاً مشخص کنید.
- خطاهای نبود فایل و نداشتن مجوز را در سطح مناسب مدیریت کنید.
- هنگام کار با فایل‌های ناشناس، محتوا را داده تلقی کنید و آن را به‌عنوان کد اجرا نکنید.

## ۷. تمرین

۱. برنامه‌ای بسازید که سه یادداشت را در فایل UTF-8 ذخیره کند.
۲. محتوای فایل را خط‌به‌خط بخواند و تعداد خط‌ها را بشمارد.
۳. تفاوت حالت `w` و `a` را با اجرای مثال روی فایل آزمایشی مشاهده کنید.

## منابع

- [ورودی و خروجی فایل در آموزش رسمی](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [کتابخانه pathlib](https://docs.python.org/3/library/pathlib.html)
