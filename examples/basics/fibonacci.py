# 斐波那契数列
# 打印前 n 个斐波那契数

# 方法一：循环
def fibonacci_loop(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# 方法二：递归
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 方法三：生成器
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 10
print(f"前 {n} 个斐波那契数（循环）：{fibonacci_loop(n)}")
print(f"第 {n} 个斐波那契数（递归）：{fibonacci_recursive(n)}")
print(f"前 {n} 个斐波那契数（生成器）：{list(fibonacci_generator(n))}")
