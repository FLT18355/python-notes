# concurrent.futures — 并发执行

`concurrent.futures` 模块提供高级接口，用于异步执行调用。

## ThreadPoolExecutor — 线程池

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def task(n):
    time.sleep(1)
    return n * n


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]

    for future in as_completed(futures):
        print(f"结果：{future.result()}")
```

## ProcessPoolExecutor — 进程池

```python
from concurrent.futures import ProcessPoolExecutor


def cpu_task(n):
    return sum(i * i for i in range(n))


with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_task, [10000, 20000, 30000]))
    print(results)
```

## map 方法

```python
from concurrent.futures import ThreadPoolExecutor


def square(n):
    return n * n


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])
    for result in results:
        print(result)
# → 1, 4, 9, 16, 25
```

## 超时处理

```python
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def slow_task():
    import time
    time.sleep(5)
    return "完成"


with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(slow_task)
    try:
        result = future.result(timeout=2)
    except TimeoutError:
        print("任务超时")
```

## 回调函数

```python
from concurrent.futures import ThreadPoolExecutor


def task(n):
    return n * n


def callback(future):
    print(f"任务完成，结果：{future.result()}")


with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(task, 5)
    future.add_done_callback(callback)
```

## 实战示例

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


def fetch_url(url):
    try:
        resp = requests.get(url, timeout=5)
        return url, resp.status_code
    except Exception as e:
        return url, str(e)


urls = [
    "https://httpbin.org/get",
    "https://api.github.com",
    "https://www.python.org",
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(fetch_url, url): url for url in urls}
    for future in as_completed(futures):
        url, status = future.result()
        print(f"{url}: {status}")
```
