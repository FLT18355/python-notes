# argparse — 命令行参数解析

`argparse` 模块用于解析命令行参数，编写友好的命令行工具。

## 基本用法

```python
import argparse

parser = argparse.ArgumentParser(description="示例程序")
parser.add_argument("name", help="姓名")
parser.add_argument("--age", type=int, default=18, help="年龄")
parser.add_argument("--city", default="未知", help="城市")
args = parser.parse_args()

print(f"姓名：{args.name}")
print(f"年龄：{args.age}")
print(f"城市：{args.city}")
```

运行：
```bash
python script.py 张三 --age 25 --city 北京
```

## 参数类型

```python
import argparse

parser = argparse.ArgumentParser()

# 位置参数
parser.add_argument("input", help="输入文件")
parser.add_argument("output", help="输出文件")

# 可选参数
parser.add_argument("-n", "--count", type=int, default=1, help="重复次数")
parser.add_argument("--flag", action="store_true", help="布尔标志")
parser.add_argument("--choices", choices=["a", "b", "c"], default="a")
parser.add_argument("--items", nargs="+", help="多个值")
parser.add_argument("--levels", nargs="*", help="0个或多个值")
parser.add_argument("-v", "--verbose", action="count", default=0)

args = parser.parse_args()
```

### 常用 action

| action | 说明 |
|--------|------|
| `store` | 默认，存储值 |
| `store_true` | 存储 True |
| `store_false` | 存储 False |
| `append` | 追加到列表 |
| `count` | 计数出现次数 |
| `version` | 显示版本 |

## 子命令

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# 子命令：add
add_parser = subparsers.add_parser("add", help="添加")
add_parser.add_argument("items", nargs="+")

# 子命令：remove
remove_parser = subparsers.add_parser("remove", help="删除")
remove_parser.add_argument("items", nargs="+")

args = parser.parse_args()

if args.command == "add":
    print(f"添加：{args.items}")
elif args.command == "remove":
    print(f"删除：{args.items}")
```

## 实战示例

```python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="JSON 配置工具")
    parser.add_argument("config", help="配置文件路径")
    parser.add_argument("--key", help="查询键")
    parser.add_argument("--value", help="设置值")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    if args.key and args.value:
        config[args.key] = args.value
        with open(args.config, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        if args.verbose:
            print(f"已设置 {args.key} = {args.value}")
    elif args.key:
        print(f"{args.key}: {config.get(args.key, '未找到')}")


if __name__ == "__main__":
    main()
```
