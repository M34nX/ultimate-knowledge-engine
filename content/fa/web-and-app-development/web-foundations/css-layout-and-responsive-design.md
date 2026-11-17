---
id: web.foundations.css-layout
title: مبانی CSS، مدل جعبه‌ای و طراحی واکنش‌گرا
content_type: lesson
locale: fa
domain: web-and-app-development
level: beginner
status: draft
learning_objectives:
  - CSS را به HTML متصل کنید.
  - selector و property را از هم تشخیص دهید.
  - مدل جعبه‌ای را شرح دهید.
  - با Flexbox و media query چیدمان ساده بسازید.
prerequisites:
  - web.foundations.semantic-html
concepts:
  - web.css
  - web.box-model
  - web.responsive-design
sources:
  - mdn-web-docs
  - csswg-specs
estimated_minutes: 45
---

# مبانی CSS، مدل جعبه‌ای و طراحی واکنش‌گرا

## ۱. CSS چه می‌کند؟

CSS ظاهر و چیدمان سند HTML را کنترل می‌کند. قانون CSS معمولاً یک selector و مجموعه‌ای از declarationها شامل property و value دارد:

```css
h1 {
  color: navy;
  font-size: 2rem;
}
```

## ۲. اتصال CSS به HTML

در پروژهٔ معمول، CSS را در فایل جدا نگه دارید:

```html
<link rel="stylesheet" href="styles.css">
```

این جداسازی نگهداری، استفادهٔ مجدد و خوانایی را بهتر می‌کند.

## ۳. مدل جعبه‌ای

هر عنصر بلوکی را می‌توان با اجزای اصلی مدل جعبه‌ای درک کرد:
- content: محتوای عنصر؛
- padding: فاصلهٔ داخلی؛
- border: کادر؛
- margin: فاصلهٔ بیرونی.

```css
.card {
  box-sizing: border-box;
  width: 100%;
  max-width: 32rem;
  padding: 1rem;
  border: 1px solid #999;
  margin: 1rem auto;
}
```

استفادهٔ عمومی از `box-sizing: border-box` باعث می‌شود عرض اعلام‌شده padding و border را نیز دربر بگیرد.

## ۴. Flexbox

Flexbox برای چیدمان یک‌بعدی در ردیف یا ستون مناسب است:

```css
.navigation {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}
```

برای چیدمان دوبعدی پیچیده‌تر، CSS Grid نیز گزینهٔ مناسبی است.

## ۵. طراحی واکنش‌گرا

طراحی واکنش‌گرا محتوا را با عرض صفحه و شرایط نمایش سازگار می‌کند. به‌جای ساخت صفحه برای یک اندازهٔ خاص، از اندازه‌های منعطف، محدودیت عرض، Flexbox/Grid و media query استفاده کنید:

```css
@media (max-width: 40rem) {
  .layout {
    display: block;
  }
}
```

نقطهٔ شکست باید بر اساس نیاز محتوا انتخاب شود، نه صرفاً نام دستگاه.

## ۶. خوانایی و دسترس‌پذیری

کنتراست متن، اندازهٔ قابل خواندن، حالت focus، ترجیح کاهش حرکت و بزرگ‌نمایی مرورگر را در طراحی در نظر بگیرید. از رنگ به‌تنهایی برای انتقال معنا استفاده نکنید.

## ۷. اشتباهات رایج

- ثابت‌کردن عرض بزرگ و ایجاد اسکرول افقی.
- استفاده از margin برای همهٔ فاصله‌ها بدون فهم مدل جعبه‌ای.
- حذف focus outline.
- طراحی صرفاً برای نمایشگر خود توسعه‌دهنده.
- استفادهٔ بیش از حد از `!important` به‌جای اصلاح cascade.

## ۸. تمرین

۱. یک کارت با حداکثر عرض، padding و border بسازید.
۲. ناوبری با Flexbox ایجاد کنید.
۳. در عرض کوچک، چیدمان را از ردیف به ستون تغییر دهید.

## منابع

- [MDN: CSS first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)
- [MDN: CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout)
- [CSS Specifications](https://www.w3.org/Style/CSS/)
