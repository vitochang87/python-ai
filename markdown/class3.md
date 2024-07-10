# Python 列表操作技巧筆記

## 列表操作基本技巧

### 1. `append()`

使用 `append()` 方法在列表的末尾添加元素。

```python
l = [1, 2, 3]
l.append(4)
print(l)  # [1, 2, 3, 4]
```

### 2. `remove()`

使用 `remove()` 方法删除列表中的第一个指定元素。

```python
l = ["a", "b", "c", "a"]
l.remove("a")
print(l)  # ['b', 'c', 'a']
```

### 3. `count()`

使用 `count()` 方法计算列表中指定元素的出现次数。

```python
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))  # 2
```

### 4. 循环删除元素

结合 `count()` 和 `remove()`，循环删除列表中的所有指定元素。

```python
L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]
c = L.count(3)
for i in range(c):
    L.remove(3)
print(L)  # [12, 7, 9, 5, 2, 4]
```

### 5. `pop()`

使用 `pop()` 方法通过索引删除列表中的元素。

```python
L.pop(0)  # 删除第一个元素
print(L)  # [7, 9, 5, 2, 4]
```

### 6. `sort()`

使用 `sort()` 方法对列表进行排序。

```python
L.sort()  # 升序排序
print(L)  # [2, 4, 5, 7, 9]
L.sort(reverse=True)  # 降序排序
print(L)  # [9, 7, 5, 4, 2]
```

### 7. `index()`

使用 `index()` 方法获取列表中指定元素的索引。

```python
print(L.index(5))  # 输出 2
```

## Streamlit 元件操作技巧

### 1. 欄位元件

建立两个列，并在每个列中添加按钮和其他元件。

```python
import streamlit as st

st.title("欄位元件")
coli1, coli2 = st.columns(2)
coli1.button("左邊")
coli2.button("右邊")

with coli1:
    st.markdown("這是藍一")
    st.button("左邊1")

with coli2:
    st.markdown("這是藍二")
    st.button("右邊2")
```

### 2. 不同比例的欄位

使用不同的比例创建多个列，并在每个列中添加按钮。

```python
cols = st.columns([1, 5, 1])
cols[0].button("按鈕1", key="button1")
cols[1].button("按鈕2", key="button2")
cols[2].button("按鈕3", key="button3")
```

### 3. 文字輸入元件

创建一个文字输入框，并显示用户输入的内容。

```python
st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"您輸入的文字是：{text}")
```

### 4. `session_state`

使用 `session_state` 来存储和管理状态。

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("session_state.ans按鈕", key="session_state btn"):
    st.session_state.ans += 1
st.markdown(f"{st.session_state.ans}")
```

### 5. 點餐機範例

创建一个简单的点餐系统，通过输入框添加餐点，并可以从购物车中删除餐点。

```python
import streamlit as st

st.title("點餐機")
if "order" not in st.session_state:
    st.session_state.order = []

coli1, coli2 = st.columns(2)

with coli1:
    foodInput = st.text_input("請輸入餐點")

with coli2:
    if st.button("加入", key="add"):
        st.session_state.order.append(foodInput)

st.write("購物籃")
for i in range(len(st.session_state.order)):
    coli1, coli2 = st.columns(2)
    with coli1:
        st.write(st.session_state.order[i])
    with coli2:
        if st.button("刪除", key=i):
            st.session_state.order.pop(i)
            st.rerun()
```

### 6. 重新清理按鈕

创建一个按钮来重新清理状态，并在点击时显示成功信息。

```python
import time

if st.button("重新清理"):
    st.success("準備重新清理")
    time.sleep(3)
    st.rerun()
```
