# conditionals.py
# 条件判断示例

# if-elif-else
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数：{score}，等级：{grade}")  # 良好

# 三元表达式
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(f"年龄：{age}，状态：{status}")  # 成年人

# match-case（Python 3.10+）
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

print(f"状态码 200: {http_status(200)}")  # OK
print(f"状态码 404: {http_status(404)}")  # Not Found
