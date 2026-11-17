---
id: db.sql.select-where-order-by
title: پرس‌وجوی SQL با SELECT و WHERE
content_type: lesson
locale: fa
domain: databases
level: beginner
status: draft
learning_objectives:
  - ستون‌های موردنیاز را با SELECT انتخاب کنید.
  - ردیف‌ها را با WHERE فیلتر کنید.
  - نتیجه را با ORDER BY مرتب کنید.
  - از NULL و شرط‌های منطقی آگاهانه استفاده کنید.
prerequisites:
  - db.relational-model-and-keys
concepts:
  - db.sql.select
  - db.sql.filtering
sources:
  - postgres-docs
estimated_minutes: 35
---

# پرس‌وجوی SQL با SELECT و WHERE

## ۱. انتخاب داده

دستور SELECT ستون‌هایی را که می‌خواهید از جدول بخوانید مشخص می‌کند:

```sql
SELECT student_id, name
FROM students;
```

در نمونه‌های آموزشی از `SELECT *` می‌توان برای دیدن همهٔ ستون‌ها استفاده کرد؛ در برنامهٔ واقعی بهتر است ستون‌های موردنیاز را صریح بنویسید تا وابستگی غیرضروری به ساختار جدول ایجاد نشود.

## ۲. فیلتر با WHERE

```sql
SELECT name, grade
FROM students
WHERE grade >= 17;
```

عملگرهای مقایسه مانند `=`، `<>`، `<`، `<=`، `>` و `>=` قابل استفاده‌اند. شرط‌ها را می‌توان با `AND`، `OR` و `NOT` ترکیب کرد. برای گروه‌بندی شرط‌ها از پرانتز استفاده کنید.

## ۳. مرتب‌سازی

```sql
SELECT name, grade
FROM students
ORDER BY grade DESC, name ASC;
```

`ASC` صعودی و `DESC` نزولی است. بدون ORDER BY نباید ترتیب خروجی را تضمین‌شده فرض کنید.

## ۴. محدودکردن نتیجه

در PostgreSQL می‌توان با `LIMIT` تعداد ردیف‌ها را محدود کرد:

```sql
SELECT name
FROM students
ORDER BY student_id
LIMIT 10;
```

برای پیمایش صفحه‌ای داده‌ها، ترتیب یکتا و پایدار مهم است؛ استفاده از LIMIT بدون ORDER BY ممکن است نتایج ناپایدار بدهد.

## ۵. مقدار NULL

`NULL` نشان‌دهندهٔ نبود یا نامعلوم‌بودن مقدار است و با صفر یا رشتهٔ خالی برابر نیست. برای بررسی آن باید از `IS NULL` یا `IS NOT NULL` استفاده کرد:

```sql
SELECT name
FROM students
WHERE grade IS NULL;
```

مقایسهٔ `grade = NULL` روش صحیح بررسی مقدار تهی نیست، زیرا منطق SQL سه‌حالته است.

## ۶. اشتباهات رایج

- فراموش‌کردن شرط اتصال در queryهای چندجدولی.
- فرض ثابت‌بودن ترتیب بدون ORDER BY.
- استفاده از `= NULL`.
- قراردادن مقدار ورودی کاربر با الحاق رشته به SQL؛ در برنامه‌ها از query پارامتری استفاده کنید.

## ۷. تمرین

۱. دانشجویان با نمرهٔ بالاتر یا مساوی ۱۵ را انتخاب کنید.
۲. نتیجه را بر اساس نمرهٔ نزولی و سپس نام مرتب کنید.
۳. ردیف‌هایی را پیدا کنید که نمره ندارند.

## منابع

- [PostgreSQL: SELECT](https://www.postgresql.org/docs/current/sql-select.html)
- [PostgreSQL: مقدارهای NULL](https://www.postgresql.org/docs/current/functions-comparison.html)
