import streamlit as st

st.title("欄位元件")
coli1, coli2 = st.columns(2)
coli1.button("左邊")  # 在coli1中建立一個按鈕
coli2.button("右邊")  # 在coli2中建立一個按鈕

with coli1:
    st.markdown("這是藍一")
    st.button("左邊1")
with coli2:  # 在coli2中任意增加元件
    st.markdown("這是藍二")
    st.button("右邊2")


cols = st.columns([1, 5, 1])  # 3個欄位, list中的數字代表比例: 1:5:1
cols[0].button("按鈕1", key="button1")  # 在地0個欄位中建立一個按鈕
cols[1].button("按鈕2", key="button2")  # 在地1個欄位中建立一個按鈕
cols[2].button("按鈕3", key="button3")  # 在地2個欄位中建立一個按鈕


st.title("文字輸入元件")
text = st.text_input("請輸入文字")  # 建立一個文字輸入框
st.markdown(f"您輸入的文字是：{text}")


if (
    "ans" not in st.session_state
):  # 如果沒有在session_state中存在ans則建立一個名為ans的值
    st.session_state.ans = 1

if st.button("session_state.ans按鈕", key="session_state btn"):
    st.session_state.ans += 1
st.markdown(f"{st.session_state.ans}")
