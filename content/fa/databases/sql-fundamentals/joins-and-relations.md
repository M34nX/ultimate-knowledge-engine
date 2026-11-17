---
id: db.sql.joins-and-relations
title: پیوند جدول‌ها با JOIN در SQL
content_type: lesson
locale: fa
domain: databases
level: beginner
status: draft
learning_objectives:
  - رابطهٔ کلید اصلی و خارجی را در JOIN به‌کار ببرید.
  - تفاوت INNER JOIN و LEFT JOIN را توضیح دهید.
  - از نام مستعار برای خوانایی query استفاده کنید.
  - علت ایجاد ردیف‌های تکراری در join را تحلیل کنید.
prerequisites:
  - db.relational-model-and-keys
  - db.sql.select-where-order-by
concepts:
  - db.sql.joins
sources:
  - postgres-docs
estimated_minutes: 40
---

# پیوند جدول‌ها با JOIN در SQL

## ۱. چرا JOIN؟

داده‌ها برای کاهش تکرار معمولاً در چند جدول مرتبط نگهداری می‌شوند. JOIN ردیف‌های جدول‌ها را بر اساس شرط ارتباط ترکیب می‌کند.

## ۲. INNER JOIN

```sql
SELECT students.name, enrollments.course_id
FROM students
INNER JOIN enrollments
    ON students.student_id = enrollments.student_id;
```

INNER JOIN فقط ردیف‌هایی را نگه می‌دارد که شرط اتصال در هر دو طرف برقرار باشد.

## ۳. LEFT JOIN

```sql
SELECT students.name, enrollments.course_id
FROM students
LEFT JOIN enrollments
    ON students.student_id = enrollments.student_id;
```

LEFT JOIN تمام ردیف‌های جدول سمت چپ را حفظ می‌کند. اگر تطبیقی وجود نداشته باشد، ستون‌های جدول سمت راست مقدار NULL خواهند داشت.

## ۴. نام مستعار

نام مستعار کوتاه، query را خواناتر می‌کند:

```sql
SELECT s.name, e.course_id
FROM students AS s
JOIN enrollments AS e
  ON e.student_id = s.student_id;
```

استفاده از نام مستعار به‌ویژه هنگامی مفید است که دو جدول ستون‌های هم‌نام دارند.

## ۵. چند نکته دربارهٔ تعداد ردیف‌ها

اگر یک دانشجو در چند درس ثبت‌نام کرده باشد، اتصال دانشجو به ثبت‌نام‌ها چند ردیف برای او تولید می‌کند. این رفتار خطا نیست؛ نتیجهٔ رابطهٔ یک‌به‌چند است. برای حذف تکرارهای ناخواسته، ابتدا علت چندگانگی را بررسی کنید؛ استفادهٔ کور از DISTINCT ممکن است مسئلهٔ طراحی query را پنهان کند.

## ۶. اشتباهات رایج

- فراموش‌کردن شرط ON و ایجاد حاصل‌ضرب دکارتی.
- قراردادن شرط جدول سمت راست در WHERE پس از LEFT JOIN و ناخواسته حذف‌کردن ردیف‌های NULL.
- تصور اینکه JOIN همیشه تعداد ردیف‌ها را کاهش می‌دهد.
- اتصال ستون‌های نامرتبط یا با معنای متفاوت.

## ۷. تمرین

۱. نام دانشجو و عنوان درس ثبت‌نام‌شده را نمایش دهید.
۲. همهٔ دانشجویان، حتی افراد بدون ثبت‌نام را با LEFT JOIN نمایش دهید.
۳. توضیح دهید چرا یک دانشجو ممکن است در خروجی چند بار دیده شود.

## منابع

- [PostgreSQL: Table Expressions و JOIN](https://www.postgresql.org/docs/current/queries-table-expressions.html)
