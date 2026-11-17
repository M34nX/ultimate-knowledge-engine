---
id: python.strings-and-formatting
title: رشته‌ها و قالب‌بندی متن در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - رشته بسازید و به نویسه‌ها و بخش‌های آن دسترسی پیدا کنید.
  - متدهای پرکاربرد رشته را انتخاب کنید.
  - متن را با f-string قالب‌بندی کنید.
  - تغییرناپذیری رشته را توضیح دهید.
prerequisites:
  - python.basic-data-types
  - python.for-and-while-loops
concepts:
  - python.strings
  - python.string-formatting
sources:
  - python-docs
estimated_minutes: 35
version_scope:
  minimum: "3.8"
  maximum: null
  notes: "f-string از Python 3.6 معرفی شده؛ این درس حداقل نسخه 3.8 را برای یکسانی محیط آموزشی پیشنهاد می‌کند."
---

# رشته‌ها و قالب‌بندی متن در پایتون

## ۱. ساخت رشته

رشته (`str`) برای نمایش متن استفاده می‌شود. می‌توان آن را با کوتیشن تکی یا دوتایی ساخت:

```python
first_name = "Sara"
message = 'Welcome'
```

برای متن چندخطی می‌توان از سه کوتیشن استفاده کرد. نویسه‌های ویژه مانند خط جدید با escape sequence نمایش داده می‌شوند؛ برای نمونه `\n`.

## ۲. دسترسی و برش‌گیری

رشته دنباله‌ای مرتب و تغییرناپذیر از نویسه‌هاست:

```python
word = "Python"
print(word[0])     # P
print(word[-1])    # n
print(word[1:4])   # yth
```

اندیس‌ها از صفر شروع می‌شوند و انتهای برش شامل نمی‌شود. تغییر مستقیم یک نویسه مجاز نیست؛ برای ساخت متن تازه باید رشته جدید تولید کرد.

## ۳. متدهای پرکاربرد

```python
raw = "  Python Basics  "
clean = raw.strip()
print(clean.lower())
print(clean.upper())
print(clean.replace("Basics", "Course"))
print("a,b,c".split(","))
```

متدهای رشته معمولاً رشته جدید برمی‌گردانند و رشته اولیه را تغییر نمی‌دهند. برای بررسی پیشوند، پسوند یا وجود یک متن از `startswith`، `endswith` و `in` استفاده کنید.

## ۴. قالب‌بندی با f-string

f-string راهی خوانا برای قرار دادن مقدارها در متن است:

```python
name = "Nima"
score = 18.456
print(f"{name} scored {score:.1f}")
```

خروجی:

```text
Nima scored 18.5
```

بخش `:.1f` قالب نمایش عدد را مشخص می‌کند. قالب‌بندی فقط شکل نمایش را تغییر می‌دهد، نه مقدار اصلی متغیر را.

## ۵. متن ورودی و پاک‌سازی

ورودی کاربر را قابل اعتماد فرض نکنید. برای نمونه، فاصله‌های ابتدا و انتها را می‌توان با `strip()` حذف کرد و سپس داده را اعتبارسنجی کرد:

```python
answer = input("نام شما: ").strip()
if not answer:
    print("نام خالی است.")
else:
    print(f"سلام، {answer}")
```

## ۶. خطاهای رایج

- تلاش برای تغییر یک نویسه رشته با اندیس.
- فراموش‌کردن تبدیل عدد به رشته در اتصال دستی متن.
- استفاده از قالب‌بندی متنی برای داده‌ای که باید عددی باقی بماند.
- فرض اینکه `strip()` همه فاصله‌های داخل رشته را حذف می‌کند؛ این متد فقط دو سر رشته را پاک می‌کند.

## ۷. تمرین

۱. یک جمله دریافت کنید و تعداد نویسه‌های آن را با `len()` نمایش دهید.
۲. فاصله ابتدا و انتهای نام را حذف کنید و حرف‌های آن را به حروف کوچک تبدیل کنید.
۳. گزارشی با نام، تعداد و میانگین نمره با f-string بسازید.

## منابع

- [رشته‌ها در آموزش رسمی پایتون](https://docs.python.org/3/tutorial/introduction.html#strings)
- [متدهای رشته](https://docs.python.org/3/library/stdtypes.html#string-methods)
