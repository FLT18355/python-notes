# lists.py
# 列表操作示例

# 创建列表
nums = [1, 2, 3, 4, 5]
print(f"原列表：{nums}")

# 新增
nums.append(6)
nums.insert(0, 0)
nums.extend([7, 8])
print(f"新增后：{nums}")

# 删除
nums.remove(3)
last = nums.pop()
del nums[0]
print(f"删除后：{nums}")

# 修改
nums[0] = 100
print(f"修改后：{nums}")

# 查询
print(f"索引2的值：{nums[2]}")
print(f"100的索引：{nums.index(100)}")
print(f"4出现次数：{nums.count(4)}")

# 切片
print(f"前3个：{nums[:3]}")
print(f"后3个：{nums[-3:]}")
print(f"反转：{nums[::-1]}")

# 排序
nums.sort()
print(f"升序：{nums}")
nums.sort(reverse=True)
print(f"降序：{nums}")

# 统计
print(f"长度：{len(nums)}")
print(f"最大值：{max(nums)}")
print(f"最小值：{min(nums)}")
print(f"总和：{sum(nums)}")

# 列表推导式
squares = [x ** 2 for x in range(5)]
print(f"平方列表：{squares}")

# 遍历
for i, n in enumerate(nums):
    print(f"索引 {i}: 值 {n}")
