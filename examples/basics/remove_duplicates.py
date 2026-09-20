# 列表去重
# 多种方式去除列表中的重复元素

nums = [1, 2, 3, 2, 4, 1, 5, 3]

# 方法一：set（不保序）
unique1 = list(set(nums))
print(f"set 去重：{unique1}")

# 方法二：dict（Python 3.7+ 保序）
unique2 = list(dict.fromkeys(nums))
print(f"dict 去重：{unique2}")

# 方法三：循环（保序）
unique3 = []
for n in nums:
    if n not in unique3:
        unique3.append(n)
print(f"循环去重：{unique3}")
