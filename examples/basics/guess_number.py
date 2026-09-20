# 猜数字游戏
# 程序随机生成一个 1-100 的数字，用户来猜

import random

target = random.randint(1, 100)
attempts = 0

print("猜数字游戏！我心里想了一个 1-100 的数字，你来猜猜看。")

while True:
    try:
        guess = int(input("请输入你的猜测："))
        attempts += 1

        if guess < target:
            print("太小了，再大一点！")
        elif guess > target:
            print("太大了，再小一点！")
        else:
            print(f"恭喜你猜对了！答案是 {target}")
            print(f"你一共猜了 {attempts} 次")
            break
    except ValueError:
        print("请输入有效数字！")
