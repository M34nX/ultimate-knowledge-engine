---
id: cs.algorithms.graphs-and-bfs
title: گراف و پیمایش جست‌وجوی سطحی
content_type: lesson
locale: fa
domain: computer-science
level: beginner
status: draft
learning_objectives:
  - رأس و یال را تعریف کنید.
  - گراف را با فهرست مجاورت نمایش دهید.
  - الگوریتم BFS را با صف پیاده‌سازی کنید.
  - شرط‌های استفاده از BFS برای کوتاه‌ترین مسیر را بیان کنید.
prerequisites:
  - cs.data-structures.stacks-and-queues
  - cs.algorithms.big-o
concepts:
  - cs.graphs
  - cs.algorithms.breadth-first-search
sources:
  - mit-ocw-6-006
estimated_minutes: 45
---

# گراف و پیمایش جست‌وجوی سطحی (BFS)

## ۱. گراف چیست؟

گراف از رأس‌ها (Vertices) و یال‌ها (Edges) تشکیل می‌شود. رأس می‌تواند یک شهر یا کاربر و یال رابطهٔ میان دو رأس باشد. گراف ممکن است جهت‌دار یا بدون‌جهت و وزن‌دار یا بدون‌وزن باشد.

## ۲. نمایش با فهرست مجاورت

برای گراف کوچک، دیکشنری‌ای که هر رأس را به همسایه‌هایش نگاشت می‌کند، روشی روشن است:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}
```

این نمونه گراف بدون‌جهت است؛ هر یال در فهرست مجاورت هر دو سر ثبت شده است.

## ۳. پیمایش سطحی

BFS (Breadth-First Search) رأس‌ها را بر حسب فاصلهٔ تعداد یال از مبدأ بررسی می‌کند. برای صف از deque استفاده می‌کنیم:

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
```

ثبت رأس در visited هنگام افزودن به صف مانع افزودن تکراری آن می‌شود.

## ۴. کوتاه‌ترین مسیر چه زمانی؟

در گراف بدون‌وزن، BFS می‌تواند فاصلهٔ کمینه از مبدأ را بر حسب تعداد یال پیدا کند. در گراف وزن‌دار، BFS لزوماً کوتاه‌ترین مسیر بر اساس مجموع وزن را نمی‌دهد؛ برای آن به الگوریتم مناسب مانند Dijkstra با شرایط لازم نیاز است.

## ۵. پیچیدگی

با نمایش فهرست مجاورت، BFS هر رأس و هر یال را حداکثر تعداد محدودی بار بررسی می‌کند؛ زمان O(V + E) است، که V تعداد رأس‌ها و E تعداد یال‌هاست.

## ۶. خطاهای رایج

- علامت‌گذاری visited فقط هنگام خارج‌کردن از صف.
- فرض اینکه BFS در هر گراف وزن‌دار کوتاه‌ترین مسیر را می‌دهد.
- فراموش‌کردن رأس‌هایی که به مبدأ دسترسی ندارند.
- فرض مرتب‌بودن ترتیب خروجی بدون تعریف ترتیب همسایه‌ها.

## ۷. تمرین

۱. تابع BFS را روی گراف بالا اجرا کنید و ترتیب پیمایش را بنویسید.
۲. تابع را طوری توسعه دهید که فاصلهٔ هر رأس از مبدأ را برگرداند.
۳. حالت گراف خالی و مبدأ ناشناخته را تعریف و مدیریت کنید.

## منابع

- [MIT OCW 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
