# 程式技巧筆記

## 宣告變數

```python
i = 0  # 宣告 i 為整數
```

## 條件式迴圈

```python
while i < 5:  # 當 i 小於 5 時執行迴圈
    print(i)
    i += 1  # 等同於 i = i + 1
```

## 賦值運算

```python
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
```

## 使用 `break` 跳出迴圈

```python
i = 1
while i < 6:  # 當 i 小於 6 時執行迴圈
    print(i)
    if i == 3:
        break  # 當 i 等於 3 時，跳出迴圈
    i += 1

for j in range(1, 6):  # j 從 1 到 5
    print(j)
    if j == 3:
        break  # 當 j 等於 3 時，跳出迴圈
```

## 隨機數字生成

```python
import random  # 引入 random 模組

print(random.randrange(10))  # 隨機生成 0 到 9 之間的整數
print(random.randrange(1, 10))  # 隨機生成 1 到 9 之間的整數
print(random.randrange(1, 10, 2))  # 隨機生成 1 到 9 之間的奇數
print(random.randint(1, 10))  # 隨機生成 1 到 10 之間的整數
```

## 猜數字遊戲

```python
import random  # 引入 random 模組

number_to_guess = random.randint(1, 100)
guess = None

print("歡迎來到猜數字遊戲！")
print("我已經想好了一個1到100之間的數字，快來猜猜看吧！")

while guess != number_to_guess:
    guess = int(input("請輸入你的猜測："))

    if guess < 0 or guess > 100:
        print("只能輸入1到100之間的數字！")
    elif guess < number_to_guess:
        print("太小了，再大一點！")
    elif guess > number_to_guess:
        print("太大了，再小一點！")
    else:
        print("恭喜你，猜對了！")
```

## 字典操作

```python
# 建立字典
d = {"星期一": "蘋果", "星期二": "香蕉"}

# 讀取字典
print(d["星期一"])  # 蘋果

# 字典走訪
for key in d:  # 獲得所有 key
    print(key)

for key in d.keys():  # 獲得所有 key
    print(key)

for value in d.values():  # 獲得所有 value
    print(value)

for key, value in d.items():  # 獲得所有 key 和 value
    print(f"key={key}, value={value}")

# 新增或修改元素
d["星期一"] = "橘子"
d["星期三"] = "蘋果"
print(d)

# 檢查 key 是否存在
print("星期一" in d)  # True
print("星期三" in d)  # False
print("蘋果" in d.values())  # True

# 刪除元素
d.pop("星期一")  # 刪除 key 是 "星期一" 的元素
print(d)
d.pop("星期三", "找不到")  # 若 key 不存在，返回 "找不到"
print(d)
```

## Streamlit 應用

```python
import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾內所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)  # 根據使用者輸入的大小調整寬度

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)  # 使用欄寬度
```
