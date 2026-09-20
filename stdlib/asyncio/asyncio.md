# asyncio — 异步编程

`asyncio` 模块提供异步 I/O 框架，用于编写高并发程序。

## 基本概念

- **协程（coroutine）**：用 `async def` 定义的函数
- **事件循环（event loop）**：调度协程执行
- **Future/Task**：协程的执行句柄

## 基本用法

```python
import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)  # 非阻塞等待
    print("World")


# 运行协程
asyncio.run(hello())
```

## 多个协程

```python
import asyncio


async def task(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return f"{name} 的结果"


async def main():
    # 并发执行
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1.5),
    )
    print(results)


asyncio.run(main())
```

## Task

```python
import asyncio


async def task(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return name


async def main():
    t1 = asyncio.create_task(task("A", 1))
    t2 = asyncio.create_task(task("B", 2))

    result1 = await t1
    result2 = await t2
    print(f"结果：{result1}, {result2}")


asyncio.run(main())
```

## 超时控制

```python
import asyncio


async def slow_task():
    await asyncio.sleep(5)
    return "完成"


async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
    except asyncio.TimeoutError:
        print("任务超时")


asyncio.run(main())
```

## 事件循环

```python
import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
```

## 后台任务

```python
import asyncio


async def background_task():
    for i in range(5):
        print(f"后台任务 {i}")
        await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(background_task())
    print("主任务继续")
    await asyncio.sleep(0.5)
    print("主任务结束")
    await task  # 等待后台任务完成


asyncio.run(main())
```

## 同步代码调用

```python
import asyncio


async def main():
    # 在协程中运行同步代码
    result = await asyncio.to_thread(lambda: sum(range(1000000)))
    print(f"结果：{result}")


asyncio.run(main())
```

## 实战示例

```python
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return url, response.status


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://api.github.com",
        "https://www.python.org",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for url, status in results:
            if isinstance(status, Exception):
                print(f"{url}: 错误 {status}")
            else:
                print(f"{url}: {status}")


asyncio.run(main())
```
