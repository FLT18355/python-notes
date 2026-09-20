# sqlite3 — 轻量级数据库

`sqlite3` 模块提供 SQLite 数据库访问，无需服务器，适合嵌入式场景。

## 连接数据库

```python
import sqlite3

# 连接（文件不存在则创建）
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
```

## 创建表

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")

conn.commit()
conn.close()
```

## 插入数据

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# 单条插入
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("张三", 25, "zhangsan@example.com")
)

# 批量插入
users = [
    ("李四", 30, "lisi@example.com"),
    ("王五", 22, "wangwu@example.com"),
]
cursor.executemany(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    users
)

conn.commit()
conn.close()
```

## 查询数据

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# 查询所有
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 带条件查询
cursor.execute("SELECT name, age FROM users WHERE age > ?", (25,))
for name, age in cursor.fetchall():
    print(f"{name}: {age}")

# 查询单条
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
user = cursor.fetchone()
print(user)

conn.close()
```

## 更新与删除

```python
# 更新
cursor.execute(
    "UPDATE users SET age = ? WHERE name = ?",
    (26, "张三")
)

# 删除
cursor.execute("DELETE FROM users WHERE id = ?", (1,))

conn.commit()
```

## 使用字典行

```python
import sqlite3

conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row  # 返回字典式行

cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
row = cursor.fetchone()

print(row["name"])  # 按列名访问
print(row[1])       # 按索引访问
```

## 事务管理

```python
import sqlite3

conn = sqlite3.connect("app.db")
try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (1, "测试", 20))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"操作失败：{e}")
finally:
    conn.close()
```

## 实战示例

```python
import sqlite3
from pathlib import Path


def init_db(path="app.db"):
    """初始化数据库"""
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn


def add_note(conn, title, content):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    return cursor.lastrowid


def get_notes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, created_at FROM notes ORDER BY created_at DESC")
    return cursor.fetchall()


conn = init_db()
note_id = add_note(conn, "学习笔记", "Python 基础笔记")
for note in get_notes(conn):
    print(f"#{note[0]} {note[1]} ({note[2]})")
conn.close()
```
