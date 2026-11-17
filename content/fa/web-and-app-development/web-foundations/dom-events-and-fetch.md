---
id: web.foundations.dom-events-fetch
title: کار با DOM، رویدادها و Fetch API
content_type: lesson
locale: fa
domain: web-and-app-development
level: beginner
status: draft
learning_objectives:
  - یک عنصر DOM را با selector پیدا کنید.
  - برای یک عنصر رویداد ثبت کنید.
  - دادهٔ JSON را با Fetch API دریافت و پردازش کنید.
  - خطاهای شبکه و پاسخ ناموفق HTTP را مدیریت کنید.
prerequisites:
  - web.foundations.javascript
  - web.foundations.http
concepts:
  - web.dom
  - web.events
  - web.fetch
sources:
  - mdn-web-docs
estimated_minutes: 45
---

# کار با DOM، رویدادها و Fetch API

## ۱. DOM چیست؟

مرورگر HTML را به ساختار درختی‌ای به نام Document Object Model تبدیل می‌کند. JavaScript می‌تواند با DOM عنصرها را پیدا کند، متن یا ویژگی‌های آن‌ها را تغییر دهد و به رویدادها واکنش نشان دهد.

## ۲. انتخاب عنصر

```html
<p id="message">سلام</p>
<button id="change-button" type="button">تغییر متن</button>
<script src="app.js" defer></script>
```

```javascript
const message = document.querySelector("#message");
const button = document.querySelector("#change-button");
```

اگر selector عنصری پیدا نکند، نتیجه null است؛ پیش از استفاده باید وجود عنصر بررسی شود.

## ۳. رویدادها

```javascript
button.addEventListener("click", () => {
  message.textContent = "متن به‌روزرسانی شد";
});
```

به‌جای قرار دادن کد اجرایی داخل ویژگی‌های HTML، معمولاً ثبت رویداد در فایل JavaScript خواناتر و نگهداری‌پذیرتر است. برای تغییر متن از `textContent` استفاده کنید؛ قرار دادن متن غیرقابل اعتماد با `innerHTML` می‌تواند خطر تزریق HTML ایجاد کند.

## ۴. دریافت داده با Fetch

```javascript
async function loadUsers() {
  try {
    const response = await fetch("/api/users");

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const users = await response.json();
    console.log(users);
  } catch (error) {
    console.error("Could not load users:", error);
  }
}
```

Fetch برای درخواست شبکه استفاده می‌شود. پاسخ HTTP با وضعیت 404 یا 500 لزوماً باعث reject شدن Promise نمی‌شود؛ بنابراین باید `response.ok` را هم بررسی کنید.

## ۵. async و await

`async` تابعی می‌سازد که Promise برمی‌گرداند و `await` نتیجهٔ Promise را درون تابع async منتظر می‌ماند. این دستورها نوشتن کد ناهمگام را خواناتر می‌کنند؛ اما عملیات شبکه همچنان ممکن است شکست بخورد یا زمان ببرد.

## ۶. خطاهای رایج

- فرض اینکه fetch برای همهٔ کدهای وضعیت ناموفق exception ایجاد می‌کند.
- استفاده از selector بدون بررسی null.
- درج دادهٔ بیرونی با innerHTML.
- فراموش‌کردن نمایش وضعیت بارگذاری و خطا برای کاربر.
- درخواست از دامنهٔ دیگر بدون درنظرگرفتن سیاست CORS.

## ۷. تمرین

۱. دکمه‌ای بسازید که متن یک پاراگراف را تغییر دهد.
۲. JSON ساختگی را از یک فایل محلی یا endpoint تمرینی بخوانید.
۳. وضعیت HTTP ناموفق و خطای شبکه را جداگانه نمایش دهید.

## منابع

- [MDN: Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [MDN: Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
- [MDN: Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
