i = 0  # 宣告 i 為整數
while i < 5:  # 條件式迴圈，當 i 小於 5 時執行 迴圈
    print(i)
    i += 1  # 1 = i + 1
a = 10
a += 1  # 等同於 a = a + 1
print(a)

a -= 1  # 等同於 a = a - 1

print(a)

a *= 2  # 等同於 a = a * 2
print(a)

a /= 2  # 等同於 a = a / 2
print(a)

a //= 2  # 等同於 a = a // 2
print(a)

a %= 3  # 等同於 a = a % 3
print(a)

a **= 2  # 等同於 a = a**2
print(a)


# break 跳出一層迴圈
i = 1
while i < 6:  # 條件式迴圈，當 i 小於 6 時執行 迴圈
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i 等於 3 時，就跳出一層迴圈
    i += 1

    for j in range(1, 6):  # 這是一個 for 迴圈, j從一到五
        print(j)  # 印出 j
        if j == 3:
            break  # 當 j 等於 3 時，就跳出一層迴圈

    import random  # 引入 random 模組

    print(random.randrange(10))  # 印出隨機一個整數 0 到 9
    print(random.randrange(1, 10))  # 印出隨機一個整數 1 到 9
    print(random.randrange(1, 10, 2))  # 隨機產生1到九的奇數
    # randrange更range一樣,第一個數字為開始,第二個數字為結束,第三個數字為間隔
    # 不會數到結束的數字,randrange(1,10),只會產生1到9隨機一個數字

    print(random.randint(1, 10))  # 印出隨機一個整數 1 到 10
    # randint更randrange一樣,第一個數字為開始,第二個數字為結束
    # 但是randint一定要設定兩個數字爾且會數到結束的數字
