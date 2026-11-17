---
id: db.sql.aggregates-and-group-by
title: توابع تجمیعی و GROUP BY در SQL
content_type: lesson
locale: fa
domain: databases
level: beginner
status: draft
learning_objectives:
  - از COUNT و SUM و AVG و MIN و MAX استفاده کنید.
  - داده‌ها را با GROUP BY گروه‌بندی کنید.
  - تفاوت WHERE و HAVING را بیان کنید.
  - اثر NULL بر توابع تجمیعی را توضیح دهید.
prerequisites:
  - db.sql.select-where-order-by
concepts:
  - db.sql.aggregation
  - db.sql.grouping
sources:
  - postgres-docs
estimated_minutes: 40
---

# توابع تجمیعی و GROUP BY در SQL

## ۱. توابع تجمیعی

توابع تجمیعی چند ردیف را به یک مقدار خلاصه تبدیل می‌کنند:
- `COUNT(*)`: تعداد ردیف‌ها؛
- `SUM(column)`: مجموع مقدارهای غیر NULL؛
- `AVG(column)`: میانگین مقدارهای غیر NULL؛
- `MIN(column)` و `MAX(column)`: کمینه و بیشینه.

```sql
SELECT
    COUNT(*) AS student_count,
    AVG(grade) AS average_grade,
    MIN(grade) AS min_grade,
    MAX(grade) AS max_grade
FROM students;
```

## ۲. گروه‌بندی

```sql
SELECT course_id, COUNT(*) AS enrollment_count
FROM enrollments
GROUP BY course_id;
```

به ازای هر مقدار متفاوت course_id یک گروه ساخته می‌شود. ستون‌هایی که در SELECT استفاده می‌شوند باید با قواعد گروه‌بندی سازگار باشند؛ معمولاً یا در GROUP BY می‌آیند یا داخل تابع تجمیعی قرار می‌گیرند.

## ۳. تفاوت WHERE و HAVING

WHERE ردیف‌ها را پیش از گروه‌بندی فیلتر می‌کند. HAVING گروه‌های ساخته‌شده را بر اساس نتیجهٔ تجمیع فیلتر می‌کند:

```sql
SELECT course_id, COUNT(*) AS enrollment_count
FROM enrollments
WHERE course_id >= 10
GROUP BY course_id
HAVING COUNT(*) >= 5;
```

ابتدا ثبت‌نام‌های درس‌های دارای شناسهٔ حداقل ۱۰ وارد گروه‌بندی می‌شوند، سپس فقط گروه‌های دارای دست‌کم پنج عضو باقی می‌مانند.

## ۴. NULL و COUNT

`COUNT(*)` همهٔ ردیف‌ها را می‌شمارد؛ `COUNT(column)` فقط مقدارهای غیر NULL آن ستون را می‌شمارد. این تفاوت در داده‌های ناقص اهمیت دارد.

## ۵. خطاهای رایج

- استفاده از WHERE برای شرطی که به نتیجهٔ تابع تجمیعی وابسته است.
- انتخاب ستون غیرگروه‌بندی‌شده بدون تابع تجمیعی.
- تصور اینکه COUNT(column) مقدارهای NULL را نیز می‌شمارد.
- نام‌گذاری‌نکردن ستون‌های محاسبه‌شده و دشوارکردن خواندن خروجی.

## ۶. تمرین

۱. تعداد کتاب‌ها را در هر دسته محاسبه کنید.
۲. میانگین نمرهٔ هر درس را به‌دست آورید.
۳. فقط درس‌هایی را نگه دارید که بیش از ۲۰ دانشجو دارند.

## منابع

- [PostgreSQL: توابع تجمیعی](https://www.postgresql.org/docs/current/functions-aggregate.html)
- [PostgreSQL: SELECT و GROUP BY](https://www.postgresql.org/docs/current/sql-select.html)
