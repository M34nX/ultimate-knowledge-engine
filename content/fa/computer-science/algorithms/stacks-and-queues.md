---
id: cs.data-structures.stacks-and-queues
title: پشته و صف؛ دو ساختمان دادهٔ پایه
content_type: lesson
locale: fa
domain: computer-science
level: beginner
status: draft
learning_objectives:
  - سیاست LIFO و FIFO را توضیح دهید.
  - عملیات اصلی پشته و صف را پیاده‌سازی کنید.
  - برای صف در پایتون از deque استفاده کنید.
  - کاربرد هر ساختار را با یک مسئله تطبیق دهید.
prerequisites:
  - cs.algorithms.big-o
concepts:
  - cs.data-structures.stack
  - cs.data-structures.queue
sources:
  - mit-ocw-6-006
estimated_minutes: 40
---

# پشته و صف؛ دو ساختمان دادهٔ پایه

## ۱. پشته (Stack)

پشته از سیاست LIFO پیروی می‌کند: آخرین عضو واردشده، نخستین عضوی است که خارج می‌شود. عملیات رایج آن push برای افزودن، pop برای برداشتن و peek برای مشاهدهٔ عضو بالاست.

```python
stack = []
stack.append("A")  # push
stack.append("B")
top = stack[-1]    # peek
removed = stack.pop()
```

فهرست پایتون برای پشته‌ای با افزودن و حذف از انتها مناسب است.

## ۲. صف (Queue)

صف از سیاست FIFO پیروی می‌کند: نخستین عضو واردشده، نخستین عضو خارج می‌شود. افزودن معمولاً enqueue و حذف dequeue نام دارد.

برای صفی که از ابتدا و انتهای آن عملیات انجام می‌شود، `collections.deque` انتخاب مناسبی است:

```python
from collections import deque

queue = deque()
queue.append("first")
queue.append("second")
served = queue.popleft()
```

استفاده از `pop(0)` در فهرست برای صف بزرگ مناسب نیست؛ حذف از ابتدای فهرست باعث جابه‌جایی عضوهای بعدی می‌شود.

## ۳. کاربردها

- پشته: تاریخچهٔ بازگشت، undo، بررسی پرانتزهای متوازن و پیمایش عمقی.
- صف: مدیریت درخواست‌ها، صف چاپ و پیمایش سطحی گراف.

ساختار داده را بر اساس عملیاتی که زیاد انجام می‌شود انتخاب کنید، نه فقط ظاهر داده.

## ۴. هزینهٔ عملیات

افزودن و حذف از انتهای list معمولاً هزینهٔ سرشکن ثابت دارد؛ deque عملیات افزودن و حذف از دو سر را کارآمد انجام می‌دهد. برای تحلیل دقیق، مستندات و مدل پیاده‌سازی را در نظر بگیرید.

## ۵. خطاهای رایج

- استفاده از `pop(0)` برای صف بزرگ بدون توجه به هزینه.
- حذف از پشتهٔ خالی.
- سردرگمی میان LIFO و FIFO.
- انتخاب ساختمان داده بدون توجه به الگوی دسترسی.

## ۶. تمرین

۱. با پشته، وارونگی ترتیب نویسه‌های یک رشته را پیاده‌سازی کنید.
۲. با deque صفی از کارهای ساختگی بسازید و آن‌ها را به‌ترتیب انجام دهید.
۳. برای بررسی توازن پرانتزها، از پشته استفاده کنید.

## منابع

- [MIT OCW 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [مستندات collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
