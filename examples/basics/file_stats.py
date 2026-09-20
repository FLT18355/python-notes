# 文件统计
# 统计指定目录下的文件数量和总大小

import os
from pathlib import Path


def count_files(directory):
    """统计目录下的文件数量和总大小"""
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_files += 1
            total_size += os.path.getsize(file_path)

    return total_files, total_size


def count_files_pathlib(directory):
    """使用 pathlib 统计"""
    total_files = 0
    total_size = 0

    for f in Path(directory).rglob("*"):
        if f.is_file():
            total_files += 1
            total_size += f.stat().st_size

    return total_files, total_size


# 统计当前目录
current_dir = "."
files, size = count_files(current_dir)
print(f"文件总数：{files}")
print(f"总大小：{size / 1024:.2f} KB")
