import streamlit as st

with st.expander("class1課程筆記"):
    st.markdown(
        """
# Streamlit 程式技巧筆記

## 1. `import streamlit as st`

這行代碼導入了 Streamlit 庫，並使用 `st` 作為縮寫來引用它。

## 2. `st.title("這是標題")`

用來顯示應用程式的標題。

```python
st.title("這是標題")
```

## 3. `st.write()`

用來顯示多種格式的內容，包括字串、數字、Markdown、數據框等。

```python
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
```

## 4. `st.text()`

用來顯示純文字字串，只能顯示純文字，不支持其他格式。

```python
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
```

## 5. `st.markdown()`

用來顯示支持 Markdown 語法的字串，可以處理 Markdown 格式的內容。

```python
    st.markdown(
        '''
    這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
    例如：
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊：
    ```python
    print("Hello, Streamlit!")
    ```

    '''
    )

```

### 示例代碼

```python
    import streamlit as st

    st.title("這是標題")
    st.write(
        "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
    )
    st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
    st.markdown(
        '''
    這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
    例如：
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊：
    ```python
    print("Hello, Streamlit!")
    ```

    '''
    )

```

### 使用技巧總結

- `st.title` 用於顯示標題
- `st.write` 用於顯示多種格式的內容
- `st.text` 用於顯示純文字
- `st.markdown` 用於顯示支持 Markdown 語法的內容

    """
    )
with st.expander("class2課程筆記"):
    st.markdown(
        """
    # 程式技巧筆記

## 比較運算符

### 相等與不相等的運算

```python
print(1 == 1)  # 這是比較是否相等的運算
print(1 != 1)  # 這是比較是否不相等的運算
```

### 大小比較運算

```python
print(1 < 1)    # 這是比較是否小於的運算
print(1 <= 1)   # 這是比較是否小於等於的運算
print(1 >= 1)   # 這是比較是否大於等於的運算
```

## 邏輯運算符

### 取反運算

```python
print(not True)   # 這是相反的運算
print(not False)  # 這是相反的運算
```

### 邏輯與、或運算

```python
print(True and True)   # 這是全部要符合條件才是true
print(True and False)  # 這是全部要符合條件才是true
print(False and True)  # 這是全部要符合條件才是true
print(False or False)  # 這是只要有一個條件符合條件就是true
```

## 運算符優先順序

1. `()` - 圓括號
2. `**` - 指數
3. `*`, `/`, `//`, `%` - 乘法、除法、整數除法、取餘
4. `+`, `-` - 加法、減法
5. `==`, `!=`, `>`, `<`, `>=`, `<=` - 比較運算
6. `not`, `and`, `or` - 邏輯運算

## 控制流 - 條件判斷

### 基本的if條件判斷

```python
pwd = input("請輸入密碼：")
if pwd == "123456":
    print("密碼正確！")
else:
    print("密碼錯誤！")
```

- `if` 開頭
- `if` 只能有一個
- 可以有無限個 `elif`
- `elif` 和 `else` 都是選擇性的
- `else` 只能有一個

## 使用 Streamlit 建立互動應用

### 簡單數字輸入

```python
import streamlit as st

number = st.number_input("輸入一個數字", step=1)
st.markdown(f"你輸入的數字是{number}")
```

### 標題與條件判斷

```python
st.title("練習")

n = st.number_input("輸入你的分數", step=1, min_value=0, max_value=100)
if n >= 90 and n <= 100:
    st.markdown("A")
elif n >= 80 and n <= 89:
    st.markdown("B")
elif n >= 70 and n <= 79:
    st.markdown("C")
elif n >= 60 and n <= 69:
    st.markdown("D")
else:
    st.markdown("F")
```

### 按鈕和特效

```python
st.title("按鈕元件練習")

st.button("點我")

if st.button("氣球"):
    st.balloons()
```

## 迴圈 - for

### 基本for迴圈

```python
for i in range(10):  # i是迴圈的變數, range(10)適從0到9的數字
    print(i)  # i  每次只從range(10)中取出一個數字,從0到9
```

### 帶有範圍的for迴圈

```python
for i in range(2, 100):  # range(2,100)適從2到99的數字
    print(i)  # i  每次只從range(2,100)中取出一個數字,從2到99
```

### 帶有步長的for迴圈

```python
for i in range(2, 100, 2):  # range(2,100,2)適從2到99的偶數
    print(i)  # i  每次只從range(2,100,2)中取出一個數字,從2到99的偶數
```

### 反向迴圈

```python
for j in range(100, 3, -2):  # range(100,3,-2)適從100到4的數字,每次取出的數字是偶數
    print(j)  # j  每次只從range(100,3,-2)中取出一個數字,從100到4的偶數
```

## 利用Streamlit製作金字塔

### 數字金字塔

```python
import streamlit as st

st.title("數字金字塔")
number = st.number_input("輸入一個整數(1到9)", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔")
for i in range(1, number + 1):
    st.markdown(str(i) * i)
```

### 箭頭金字塔

```python
st.title("箭頭金字塔")
number = st.number_input("請輸入箭頭的層數", step=1, min_value=1)
allow = ""
for i in range(1, number * 2, 2):
    allow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(number):
    allow += " " * (number - 1) + "*" + "\n"
st.markdown(f"```\n箭頭金字塔\n{allow}\n```")
```

## List操作

### 創建list

```python
print([])  # 這是一個空的list
print(["蘋果"])  # 這是一個有一個元素的list
print(["a", "b"])  # 這是一個有兩個元素的list
print([1, 2, 3])  # 這是一個有三個元素的list
```

### 訪問list元素

```python
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(L[0])  # 取出L中的第一個元素, 元素編號(index)是從0開始
print(L[1])  # 取出L中的第二個元素
print(L[2])  # 取出L中的第三個元素
```

### 迭代list

```python
for index in range(len(L)):
    print(L[index])  # 取出L中的第index個元素

for element in L:
    print(element)  # 取出L中的每個元素
```

### 修改list元素

```python
L[0] = "moo"  # 將L中的第一個元素改成"moo"
```
"""
    )
