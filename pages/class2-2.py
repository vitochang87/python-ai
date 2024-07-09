import streamlit as st

number = st.number_input("輸入一個數字", step=1)
st.markdown(f"你輸入的數字是{number}")

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

st.title("按鈕元件練習")

st.button("點我")

if st.button("氣球"):
    st.balloons()
