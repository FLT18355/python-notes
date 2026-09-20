# os — 操作系统接口

`os` 模块提供了与操作系统交互的功能，用于处理文件、目录、环境变量等。

## 导入

```python
import os
```

## 目录操作

```python
# 当前工作目录
os.getcwd()                        # → '/home/user/project'
os.chdir("/tmp")                    # 切换目录

# 列出目录内容
os.listdir(".")                     # → ['file.txt', 'src']
os.listdir("/home/user")            # 列出指定目录

# 创建目录
os.mkdir("new_dir")                 # 创建单级目录
os.makedirs("a/b/c", exist_ok=True) # 递归创建，已存在不报错

# 删除目录
os.rmdir("empty_dir")               # 只能删除空目录
os.removedirs("a/b/c")              # 递归删除空目录

# 删除文件
os.remove("file.txt")               # 删除文件
```

## 路径操作

```python
os.path.join("data", "users.json")       # → 'data/users.json'（跨平台）
os.path.abspath("file.txt")              # → 绝对路径
os.path.exists("file.txt")               # 是否存在
os.path.isfile("file.txt")               # 是否是文件
os.path.isdir("data")                    # 是否是目录
os.path.getsize("file.txt")              # 文件大小（字节）

# 路径拆分
os.path.basename("/a/b/c.txt")  # → 'c.txt'（文件名）
os.path.dirname("/a/b/c.txt")   # → '/a/b'（目录部分）
os.path.splitext("c.txt")       # → ('c', '.txt')（分离后缀）
```

## 文件与目录操作

```python
# 重命名 / 移动
os.rename("old.txt", "new.txt")

# 遍历目录树
for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))
```

## 环境变量

```python
os.environ                    # 所有环境变量（dict-like）
os.environ["HOME"]            # 获取
os.environ.get("EDITOR", "vim")  # 获取，不存在返回默认值
os.getenv("PATH")             # 等价写法
```

## 执行系统命令

```python
os.system("ls -la")           # 执行 shell 命令
os.system("echo hello")       # → 输出 hello
```

```python
# 更推荐的方式
import subprocess
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
```

## 其他

```python
os.name          # → 'posix' (Linux/Mac) 或 'nt' (Windows)
os.sep           # → '/' (路径分隔符)
os.linesep       # → '\n' (换行符)
os.urandom(8)    # → 8 个随机字节
os.cpu_count()   # → CPU 核心数
os.getpid()      # → 当前进程 ID
```
