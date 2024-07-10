import streamlit as st

st.title("點餐機")
if "order" not in st.session_state:
    st.session_state.order = []  # 新增一個購物車的列表


coli1, coli2 = st.columns(2)  # 2欄

with coli1:
    foodInput = st.text_input("請輸入餐點")  # 建立一個文字輸入框


with coli2:
    if st.button("加入", key="add"):  # 如果按鈕被按下
        st.session_state.order.append(foodInput)  # 將輸入的餐點加入購物車

st.write(f"購物籃")
for i in range(len(st.session_state.order)):  # 　index來取得購物車中的餐點
    coli1, coli2 = st.columns(2)  # 2欄
    with coli1:
        st.write(st.session_state.order[i])  # 顯示餐點

    with coli2:
        if st.button("刪除", key=i):  # 如果按鈕被按下,key是index
            st.session_state.order.pop(i)
            # 把購物車中的餐點刪除,這時不能用remove,因為remove 是用元素來刪除,因為可能會刪除錯誤的餐點
            st.rerun()

import time

if st.button("重新清理"):
    st.success("準備重新清理")
    time.sleep(3)
    st.rerun()
