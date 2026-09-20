# typing — 类型注解

`typing` 模块提供类型提示支持，提高代码可读性和可维护性。

## 导入

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable
```

## 基本类型

```python
# 容器类型
def get_names() -> List[str]:
    return ["张三", "李四", "王五"]


def get_scores() -> Dict[str, int]:
    return {"张三": 85, "李四": 92}


def get_point() -> Tuple[int, int]:
    return (3, 4)


def get_set() -> Set[int]:
    return {1, 2, 3}
```

## Optional — 可为 None

```python
from typing import Optional


def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "张三"
    return None


user = find_user(2)
if user is not None:
    print(user)
```

## Union — 多种类型

```python
from typing import Union


def process(value: Union[int, str]) -> str:
    return str(value)


print(process(10))     # "10"
print(process("hello")) # "hello"
```

> Python 3.10+ 可用 `int | str` 代替 `Union[int, str]`。

## Any — 任意类型

```python
from typing import Any


def log(value: Any) -> None:
    print(value)


log(10)
log("hello")
log([1, 2, 3])
```

## Callable — 可调用对象

```python
from typing import Callable


def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


def add(a: int, b: int) -> int:
    return a + b


print(apply(add, 10, 20))  # 30
```

## TypedDict — 类型化字典

```python
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int
    city: str


user: User = {"name": "张三", "age": 25, "city": "北京"}
print(user["name"])
```

## Literal — 字面量类型

```python
from typing import Literal


def set_level(level: Literal["low", "medium", "high"]) -> str:
    return f"等级：{level}"


print(set_level("medium"))  # 等级：medium
# set_level("ultra")  # ❌ 类型检查错误
```

## Final — 不可变变量

```python
from typing import Final

MAX_CONNECTIONS: Final = 100
# MAX_CONNECTIONS = 200  # ❌ 类型检查错误
```

## Protocol — 协议（结构类型）

```python
from typing import Protocol


class SupportsWrite(Protocol):
    def write(self, data: bytes) -> int: ...


def save(data: bytes, writer: SupportsWrite) -> None:
    writer.write(data)


class FileWriter:
    def write(self, data: bytes) -> int:
        return len(data)


save(b"hello", FileWriter())
```

## TypeVar — 泛型

```python
from typing import TypeVar, Generic

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


int_box = Box(10)
str_box = Box("hello")
print(int_box.get())  # 10
print(str_box.get())  # hello
```

## 实战示例

```python
from typing import List, Dict, Optional


def find_user(users: List[Dict[str, any]], user_id: int) -> Optional[Dict[str, any]]:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


users = [
    {"id": 1, "name": "张三", "age": 25},
    {"id": 2, "name": "李四", "age": 30},
]

user = find_user(users, 1)
if user:
    print(f"找到用户：{user['name']}")
```
