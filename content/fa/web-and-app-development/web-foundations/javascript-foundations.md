---
id: web.foundations.javascript
title: مبانی JavaScript برای توسعهٔ وب
content_type: lesson
locale: fa
domain: web-and-app-development
level: beginner
status: draft
learning_objectives:
  - از const و let برای تعریف متغیر استفاده کنید.
  - نوع‌های پایه و ساختارهای شرط و حلقه را به‌کار ببرید.
  - تابع و آرایه و شیء ساده تعریف کنید.
  - تفاوت JavaScript و HTML/CSS را توضیح دهید.
prerequisites:
  - web.foundations.semantic-html
concepts:
  - javascript.foundations
  - web.browser-scripting
sources:
  - mdn-web-docs
estimated_minutes: 50
---

# مبانی JavaScript برای توسعهٔ وب

## ۱. نقش JavaScript

HTML ساختار و معنا، CSS ظاهر و چیدمان، و JavaScript رفتار و منطق تعاملی صفحه را فراهم می‌کند. JavaScript علاوه بر مرورگر در محیط‌های دیگری نیز اجرا می‌شود.

## ۲. متغیرها

```javascript
const courseName = "Web Basics";
let lessonCount = 5;

lessonCount += 1;
console.log(courseName, lessonCount);
```

برای مقداری که قرار نیست دوباره انتساب شود از `const` و برای متغیر قابل انتساب دوباره از `let` استفاده کنید. استفاده از `var` در کد جدید معمولاً لازم نیست.

## ۳. نوع‌ها و ساختارها

نوع‌های پایه شامل string، number، boolean، null و undefined هستند. آرایه برای فهرست مرتب و object برای دادهٔ کلید-مقدار مناسب است:

```javascript
const topics = ["HTML", "CSS", "JavaScript"];
const learner = { name: "Mina", level: "beginner" };
```

## ۴. شرط و حلقه

```javascript
const score = 17;

if (score >= 10) {
  console.log("Passed");
} else {
  console.log("Try again");
}

for (const topic of topics) {
  console.log(topic);
}
```

از مقایسهٔ سخت‌گیرانه `===` و `!==` استفاده کنید تا تبدیل نوع ضمنی ناخواسته کمتر شود.

## ۵. تابع

```javascript
function square(number) {
  return number * number;
}

const result = square(4);
console.log(result);
```

تابع با ورودی‌های روشن و مسئولیت مشخص، امکان استفادهٔ مجدد و آزمون ساده‌تر را فراهم می‌کند.

## ۶. اتصال فایل به HTML

```html
<script src="app.js" defer></script>
```

ویژگی `defer` اجرای اسکریپت کلاسیک خارجی را تا پس از تجزیهٔ HTML به تعویق می‌اندازد. برای مثال‌های سادهٔ این دوره مناسب است؛ ماژول‌ها قواعد بارگذاری متفاوتی دارند.

## ۷. خطاهای رایج

- تغییر مقدار const با انتساب دوباره.
- اشتباه‌گرفتن `==` و `===`.
- استفاده از متغیر پیش از مقداردهی مناسب.
- فرض اینکه JavaScript همان Java است؛ این دو زبان متفاوت‌اند.
- قراردادن همهٔ منطق برنامه در یک اسکریپت بزرگ.

## ۸. تمرین

۱. تابعی بنویسید که نمره را بگیرد و پیام مناسب برگرداند.
۲. مجموع عددهای یک آرایه را با حلقه محاسبه کنید.
۳. فهرستی از سه شیء کتاب بسازید و عنوان‌های آن‌ها را نمایش دهید.

## منابع

- [MDN: JavaScript first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)
- [MDN: JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
