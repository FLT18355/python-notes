# math — 数学函数

`math` 模块提供数学运算功能，包括三角函数、对数、幂运算等。

## 导入

```python
import math
```

## 常数

```python
math.pi          # → 3.141592653589793（圆周率）
math.e           # → 2.718281828459045（自然常数）
math.tau         # → 6.283185307179586（2π）
math.inf         # → 正无穷
math.nan         # → 非数字
```

## 基本运算

```python
math.ceil(3.2)       # → 4（向上取整）
math.floor(3.8)      # → 3（向下取整）
math.trunc(3.8)      # → 3（截断取整）
round(3.14159, 2)    # → 3.14（四舍五入，内置函数）
math.fabs(-5)        # → 5.0（绝对值）
math.modf(3.14)      # → (0.14000000000000012, 3.0)（小数部分，整数部分）
```

## 幂与对数

```python
math.pow(2, 3)       # → 8.0（幂运算，返回 float）
2 ** 3               # → 8（幂运算，返回 int）

math.sqrt(16)        # → 4.0（平方根）
math.isqrt(10)       # → 3（整数平方根）

math.log(100)        # → 4.605...（自然对数，ln）
math.log10(100)      # → 2.0（以10为底的对数）
math.log2(8)         # → 3.0（以2为底的对数）

math.exp(2)          # → 7.389...（e的x次方）
```

## 三角函数

```python
math.sin(math.pi / 2)  # → 1.0
math.cos(0)            # → 1.0
math.tan(math.pi / 4)  # → 0.999...（接近1）
math.asin(1)           # → 1.570...（arcsin）
math.acos(0)           # → 1.570...（arccos）
math.atan(1)           # → 0.785...（arctan）
math.degrees(math.pi)  # → 180.0（弧度转角度）
math.radians(180)      # → 3.141...（角度转弧度）
```

## 进制转换

```python
math.perm(5, 2)    # → 20（排列 P(5,2)）
math.comb(5, 2)    # → 10（组合 C(5,2)）

math.gcd(12, 18)   # → 6（最大公约数）
math.lcm(4, 6)     # → 12（最小公倍数）
```

## 其他

```python
math.factorial(5)    # → 120（阶乘）
math.dist([0, 0], [3, 4])  # → 5.0（两点距离）
math.prod([1, 2, 3, 4])    # → 24（连乘）
```

## 比较与判断

```python
math.isfinite(100)    # → True
math.isinf(math.inf)  # → True
math.isnan(math.nan)  # → True
math.isclose(0.1 + 0.2, 0.3)  # → True（浮点数比较）
```

## 实战示例

```python
import math

# 计算圆的面积
def circle_area(r):
    return math.pi * r ** 2

print(f"半径为5的圆面积：{circle_area(5):.2f}")  # → 78.54

# 计算两点距离
def distance(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

print(distance(0, 0, 3, 4))  # → 5.0

# 抛硬币
def coin_flip(n):
    heads = sum(1 for _ in range(n) if random.random() < 0.5)
    return heads / n

# 验证正态分布
import random
samples = [random.gauss(0, 1) for _ in range(10000)]
mean = sum(samples) / len(samples)
std = math.sqrt(sum((x - mean) ** 2 for x in samples) / len(samples))
print(f"均值：{mean:.2f}，标准差：{std:.2f}")
```
