# sys — 系统相关

`sys` 模块提供对解释器相关的变量和函数的访问，常用于处理命令行参数、路径、退出等。

## 导入

```python
import sys
```

## 命令行参数

```python
# 运行：python script.py arg1 arg2
# sys.argv[0] 是脚本名，sys.argv[1:] 是参数列表
print(sys.argv)
# → ['script.py', 'arg1', 'arg2']
```

```python
import sys

if len(sys.argv) < 2:
    print("请提供文件名")
    sys.exit(1)

filename = sys.argv[1]
print(f"处理文件：{filename}")
```

## 路径与模块搜索

```python
sys.path          # 模块搜索路径列表（类似 PYTHONPATH）
sys.path.append("/custom/path")  # 动态添加搜索路径

sys.executable    # → Python 解释器路径
sys.version       # → Python 版本信息
sys.version_info  # → 版本号元组 (3, 11, 4, 'final', 0)
```

## 标准输入输出

```python
sys.stdin   # 标准输入（默认键盘）
sys.stdout  # 标准输出（默认屏幕）
sys.stderr  # 标准错误输出
```

```python
# 读取标准输入
for line in sys.stdin:
    print(line.strip())
```

## 退出程序

```python
sys.exit(0)    # 正常退出（0 表示成功）
sys.exit(1)    # 异常退出（非 0 表示失败）
```

## 获取模块

```python
sys.modules    # 已导入的模块字典
```

## 其他

```python
sys.platform   # → 'linux'、'darwin'、'win32'
sys.maxsize    # → 最大整数值
sys.getrecursionlimit()   # → 默认递归深度（通常 1000）
sys.setrecursionlimit(5000)  # 修改递归深度
```

## 常用实战：进度条

```python
import sys
import time

for i in range(101):
    sys.stdout.write(f"\r进度：{i}%")
    sys.stdout.flush()
    time.sleep(0.05)
print()  # 换行
```

## 常用实战：参数解析

```python
import sys

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("用法：python script.py [选项]")
        print("  --name NAME  设置名称")
        print("  --count N    循环次数")
        return

    name = "world"
    count = 1

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--name" and i + 1 < len(args):
            name = args[i + 1]
            i += 2
        elif args[i] == "--count" and i + 1 < len(args):
            count = int(args[i + 1])
            i += 2
        else:
            i += 1

    for _ in range(count):
        print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
```

> 💡 复杂参数解析推荐使用 `argparse` 模块。
