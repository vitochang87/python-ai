import random  # 匯入 random 模組

# 生成1到100之間的隨機數字
number_to_guess = random.randint(1, 100)
guess = None  # 初始化使用者的猜測

print("歡迎來到猜數字遊戲！")  # 顯示歡迎訊息
print("我已經想好了一個1到100之間的數字，快來猜猜看吧！")  # 顯示遊戲說明

# 當猜測不等於隨機數字時
while guess != number_to_guess:
    guess = int(input("請輸入你的猜測："))  # 取得使用者的輸入

    if guess < 0:
        print("只能輸入1到100之間的數字！")
    elif guess > 100:
        print("只能輸入1到100之間的數字！")
    elif guess < number_to_guess:
        print("太小了，再大一點！")  # 猜得太小
    elif guess > number_to_guess:
        print("太大了，再小一點！")  # 猜得太大
    else:
        print("恭喜你，猜對了！")  # 猜對了
