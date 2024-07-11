print(1 == 1)  # 這是比較是否相等的運算
print(1 != 1)  # 這是比較是否不相等的運算
print(1 < 1)  # 這是比較是否小於的運算
print(1 <= 1)  # 這是比較是否小於等於的運算
print(1 >= 1)  # 這是比較是否大於等於的運算

print(not True)  # 這是相反的運算
print(not False)  # 這是相反的運算

print(True and True)  # 這是全部要符合條件才是true
print(True and False)  # 這是全部要符合條件才是true
print(False and True)  # 這是全部要符合條件才是true
print(False or False)  # 這是只要有一個條件符合條件就是true

# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. ==, !=, > < >= <=
# 6. not and or
# 7. = += -= *= /= //= %= **=


pwd = input("請輸入密碼：")
if pwd == "123456":
    print("密碼正確！")
else:
    print("密碼錯誤！")

    # 判斷一定要是if開頭,if只能有一個
    # 判斷後面可以有無限個elif,也可以沒有
    # 判斷else只能有一個,也可以沒有
    # elif和else都是選擇性的
