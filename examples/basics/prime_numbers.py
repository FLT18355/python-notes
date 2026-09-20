# 质数判断
# 判断一个数是否为质数，并找出范围内的所有质数

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 判断单个数
num = 17
print(f"{num} 是质数吗？{is_prime(num)}")

# 找出 1-100 之间的所有质数
primes = [n for n in range(2, 101) if is_prime(n)]
print(f"1-100 的质数：{primes}")
