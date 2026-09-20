# 简易 Todo 列表
# 命令行待办事项管理

import json
import os
from pathlib import Path


TODO_FILE = Path("todo.json")


def load_todos():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text(encoding="utf-8"))
    return []


def save_todos(todos):
    TODO_FILE.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def add_todo(title):
    todos = load_todos()
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"已添加：{title}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("暂无待办事项")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        print(f"{i}. [{status}] {todo['title']}")


def complete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print(f"已完成：{todos[index]['title']}")
    else:
        print("无效的序号")


def delete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"已删除：{removed['title']}")
    else:
        print("无效的序号")


# 清理
TODO_FILE.unlink(missing_ok=True)
