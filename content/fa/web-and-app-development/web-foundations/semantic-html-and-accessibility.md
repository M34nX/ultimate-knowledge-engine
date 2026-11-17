---
id: web.foundations.semantic-html
title: HTML معنایی و دسترس‌پذیری پایه
content_type: lesson
locale: fa
domain: web-and-app-development
level: beginner
status: draft
learning_objectives:
  - ساختار پایهٔ سند HTML را بنویسید.
  - عنصر معنایی مناسب را برای بخش‌های صفحه انتخاب کنید.
  - برای تصویر و فرم، متن و برچسب مناسب فراهم کنید.
  - اهمیت ساختار عنوان‌ها و پیمایش با صفحه‌کلید را توضیح دهید.
prerequisites:
  - web.foundations.http
concepts:
  - web.html
  - web.semantic-html
  - web.accessibility
sources:
  - mdn-web-docs
  - whatwg-html
estimated_minutes: 40
---

# HTML معنایی و دسترس‌پذیری پایه

## ۱. HTML چیست؟

HTML زبان نشانه‌گذاری برای توصیف ساختار و معنای محتوای صفحهٔ وب است. مرورگر عناصر HTML را به ساختار قابل نمایش و قابل پیمایش تبدیل می‌کند.

## ۲. سند پایه

```html
<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>صفحهٔ نمونه</title>
</head>
<body>
  <header>
    <h1>عنوان اصلی</h1>
  </header>
  <main>
    <p>متن اصلی صفحه.</p>
  </main>
  <footer>اطلاعات تکمیلی</footer>
</body>
</html>
```

ویژگی `lang` زبان اصلی محتوا و `dir` جهت نوشتار را مشخص می‌کند. برای صفحهٔ فارسی، جهت راست‌به‌چپ را به‌صورت صریح تعیین کنید.

## ۳. عنصر معنایی

عنصرها فقط برای ظاهر نیستند؛ معنای محتوا را نیز منتقل می‌کنند:
- `header` برای سرصفحه؛
- `nav` برای مجموعهٔ پیوندهای ناوبری؛
- `main` برای محتوای اصلی؛
- `article` برای محتوای مستقل؛
- `section` برای بخش موضوعی؛
- `footer` برای پاصفحه.

از عنصر مناسب به‌جای استفادهٔ بی‌رویه از `div` استفاده کنید. برای عنوان‌ها ترتیب منطقی ایجاد کنید و سطح عنوان را فقط برای اندازهٔ ظاهری انتخاب نکنید.

## ۴. متن جایگزین تصویر

تصویر معنادار باید متن جایگزین توصیفی داشته باشد. اگر تصویر صرفاً تزئینی است، متن جایگزین خالی `alt=""` می‌تواند مناسب باشد تا فناوری کمکی آن را نادیده بگیرد. متن جایگزین نباید فهرست بی‌هدف از کلمات کلیدی باشد.

## ۵. فرم و برچسب

```html
<label for="email">رایانامه</label>
<input id="email" name="email" type="email" autocomplete="email">
<button type="submit">ارسال</button>
```

هر ورودی باید نام قابل درکی داشته باشد. placeholder به‌تنهایی جایگزین label نیست. خطاهای فرم نیز باید به‌صورت قابل دسترس اعلام شوند.

## ۶. صفحه‌کلید و دسترس‌پذیری

همهٔ عملیات اصلی باید بدون ماوس نیز قابل استفاده باشند. ترتیب تمرکز باید منطقی باشد و نشانگر focus قابل مشاهده بماند. از عنصرهای تعاملی بومی مانند button و a برای رفتارهای استاندارد استفاده کنید.

## ۷. اشتباهات رایج

- استفاده از عنصر صرفاً برای ظاهر، بدون توجه به معنا.
- پرش بی‌دلیل از h1 به h4.
- تصویر مهم بدون متن جایگزین.
- ورودی بدون label.
- حذف outline تمرکز صفحه‌کلید بدون جایگزین واضح.

## ۸. تمرین

۱. یک صفحهٔ فارسی با header، nav، main و footer بسازید.
۲. برای تصویر تزئینی و تصویر اطلاعاتی alt مناسب تعیین کنید.
۳. فرم تماس کوتاه بسازید و مطمئن شوید هر ورودی label دارد.

## منابع

- [MDN: HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [WHATWG HTML Living Standard](https://html.spec.whatwg.org/)
- [WAI: Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
