# logging — 日志

`logging` 模块提供灵活的日志系统，用于记录程序运行信息。

## 基础配置

```python
import logging

# 基本配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("调试信息")    # 不显示（级别低于 INFO）
logging.info("程序启动")
logging.warning("警告信息")
logging.error("错误信息")
logging.critical("严重错误")
```

## 日志级别

| 级别 | 数值 | 说明 |
|------|------|------|
| CRITICAL | 50 | 严重错误 |
| ERROR | 40 | 错误 |
| WARNING | 30 | 警告 |
| INFO | 20 | 信息 |
| DEBUG | 10 | 调试 |

## 输出到文件

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.info("写入文件")
```

## 同时输出到文件和屏幕

```python
import logging

# 创建 logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# 文件处理器
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)

# 屏幕处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 格式化
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("信息")
logger.debug("调试")
```

## 日志轮转

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "app.log",
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,               # 保留5个备份
    encoding="utf-8"
)
```

## 上下文变量

```python
import logging

logger = logging.getLogger("app")

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user = getattr(self, "user", "unknown")
        return True


logger.addFilter(ContextFilter())

# 动态设置
for f in logger.filters:
    if isinstance(f, ContextFilter):
        f.user = "张三"
        break

logger.info("用户操作")
```

## 异常捕获

```python
import logging

logger = logging.getLogger("app")

try:
    1 / 0
except Exception:
    logger.exception("发生异常")  # 自动记录堆栈跟踪
```

## 实战示例

```python
import logging
import sys

# 配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("app")

# 使用
def process_file(path):
    logger.info(f"开始处理文件：{path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info(f"文件读取成功，共 {len(content)} 字符")
        return content
    except FileNotFoundError:
        logger.error(f"文件不存在：{path}")
        return None
    except Exception as e:
        logger.exception(f"处理失败：{e}")
        return None


process_file("data.txt")
process_file("nonexistent.txt")
```
