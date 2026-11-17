---
id: python.dictionaries-and-sets
title: دیکشنری‌ها و مجموعه‌ها در پایتون
content_type: lesson
locale: fa
domain: programming-languages
level: beginner
status: draft
learning_objectives:
  - داده‌های کلید-مقدار را با dict ذخیره کنید.
  - مقدار یک کلید را بخوانید و به‌روزرسانی کنید.
  - کاربرد set برای نگهداری عضوهای یکتا را توضیح دهید.
prerequisites:
  - python.basic-data-types
  - python.for-and-while-loops
concepts:
  - python.dictionaries
  - python.sets
sources:
  - python-docs
estimated_minutes: 30
version_scope:
  minimum: "3"
  maximum: null
  notes: "نوع‌های مجموعه‌ای استاندارد پایتون ۳."
---

# دیکشنری‌ها و مجموعه‌ها در پایتون

## ۱. دیکشنری چیست؟

دیکشنری (`dict`) داده‌ها را به شکل جفت‌های کلید و مقدار نگه می‌دارد. کلید برای بازیابی مقدار استفاده می‌شود:

```python
student = {
    "name": "Neda",
    "grade": 18,
    "active": True,
}

print(student["name"])
```

کلیدها باید hashable باشند؛ رشته و عدد معمولاً گزینه‌های رایجی برای کلید هستند.

## ۲. افزودن و به‌روزرسانی

با انتساب به یک کلید می‌توان مقدار را افزود یا جایگزین کرد:

```python
student["grade"] = 19
student["city"] = "Tabriz"
print(student.get("grade"))
print(student.get("age", "نامشخص"))
```

دسترسی با کروشه برای کلید ناموجود `KeyError` ایجاد می‌کند؛ متد `get()` امکان تعیین مقدار پیش‌فرض را فراهم می‌کند.

## ۳. پیمایش دیکشنری

```python
for key, value in student.items():
    print(key, value)
```

متد `items()` جفت‌های کلید و مقدار را برای پیمایش فراهم می‌کند.

## ۴. مجموعه چیست؟

مجموعه (`set`) مجموعه‌ای از عضوهای یکتا است و ترتیب اندیسی ندارد:

```python
tags = {"python", "code", "python"}
print(len(tags))  # 2
```

برای ساخت مجموعه خالی باید از `set()` استفاده کرد؛ `{}` یک دیکشنری خالی می‌سازد.

## ۵. عملیات مجموعه‌ها

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # اجتماع
print(a & b)  # اشتراک
print(a - b)  # تفاضل
```

این عملیات برای حذف تکرارها، یافتن عضوهای مشترک و مقایسه گروه‌ها کاربرد دارند.

## ۶. اشتباهات رایج

- تصور اینکه مجموعه اندیس دارد.
- استفاده از یک کلید ناموجود با کروشه.
- فراموش‌کردن اینکه کلید دیکشنری باید hashable باشد.
- ساخت مجموعه خالی با `{}` به‌جای `set()`.
- فرض اینکه ترتیب پیمایش مجموعه معنای ثابتی دارد.

## ۷. تمرین

۱. دیکشنری‌ای برای مشخصات یک کتاب بسازید و قیمت آن را تغییر دهید.
۲. تعداد واژه‌های یکتای یک فهرست را با تبدیل آن به مجموعه به‌دست آورید.
۳. اشتراک دو مجموعه از علاقه‌مندی‌ها را محاسبه کنید.

## ۸. منابع

- [آموزش رسمی پایتون: دیکشنری‌ها](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [آموزش رسمی پایتون: مجموعه‌ها](https://docs.python.org/3/tutorial/datastructures.html#sets)
