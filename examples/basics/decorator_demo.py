# 简单的装饰器示例

# 计时装饰器
import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时：{end - start:.4f} 秒")
        return result
    return wrapper


# 日志装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}，参数：{args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回：{result}")
        return result
    return wrapper


# 重试装饰器
def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"第 {attempt + 1} 次尝试失败：{e}")
        return wrapper
    return decorator


@timer
@log
def add(a, b):
    time.sleep(0.1)
    return a + b


result = add(10, 20)
print(f"最终结果：{result}")
