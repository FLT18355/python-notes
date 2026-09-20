# modules_demo.py
# 模块导入示例

# 导入整个模块
import math
print(f"圆周率：{math.pi}")
print(f"平方根：{math.sqrt(16)}")

# 导入特定内容
from datetime import datetime, timedelta
now = datetime.now()
print(f"当前时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")

# 重命名导入
import random as rnd
print(f"随机数：{rnd.randint(1, 100)}")

# 导入所有内容（不推荐）
from os import *
print(f"当前目录：{getcwd()}")

# 条件导入
try:
    import numpy as np
    print(f"NumPy 版本：{np.__version__}")
except ImportError:
    print("NumPy 未安装")

# 自定义模块示例
# 假设有一个 utils.py 文件：
# def greet(name):
#     return f"Hello, {name}!"
#
# 导入方式：
# import utils
# print(utils.greet("World"))
#
# 或：
# from utils import greet
# print(greet("World"))

# __name__ 使用
def main():
    print("这是主程序")


if __name__ == "__main__":
    main()
else:
    print("这是被导入的模块")
