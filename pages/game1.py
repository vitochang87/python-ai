import streamlit as st
import random

# 設置頁面標題
st.title("恐龍獵手")

# 初始化遊戲狀態
if "dinosaur_pos" not in st.session_state:
    st.session_state.dinosaur_pos = [400, 300]
if "prey_pos" not in st.session_state:
    st.session_state.prey_pos = [random.randint(0, 800), random.randint(0, 600)]
if "score" not in st.session_state:
    st.session_state.score = 0

# 顯示恐龍和獵物的位置
st.write(f"恐龍位置: {st.session_state.dinosaur_pos}")
st.write(f"獵物位置: {st.session_state.prey_pos}")
st.write(f"得分: {st.session_state.score}")

# 控制恐龍移動
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("左"):
        st.session_state.dinosaur_pos[0] -= 10
with col2:
    if st.button("上"):
        st.session_state.dinosaur_pos[1] -= 10
with col3:
    if st.button("右"):
        st.session_state.dinosaur_pos[0] += 10
with col2:
    if st.button("下"):
        st.session_state.dinosaur_pos[1] += 10

# 檢查恐龍是否捕獲獵物
if (
    abs(st.session_state.dinosaur_pos[0] - st.session_state.prey_pos[0]) < 20
    and abs(st.session_state.dinosaur_pos[1] - st.session_state.prey_pos[1]) < 20
):
    st.session_state.score += 1
    st.session_state.prey_pos = [random.randint(0, 800), random.randint(0, 600)]
    st.success("捕獲獵物！")

# 顯示遊戲畫面
st.write("使用按鈕來移動恐龍，捕獲獵物來獲得分數。")

# 顯示恐龍和獵物的位置圖
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(
    st.session_state.dinosaur_pos[0],
    st.session_state.dinosaur_pos[1],
    c="green",
    label="恐龍",
)
ax.scatter(
    st.session_state.prey_pos[0], st.session_state.prey_pos[1], c="red", label="獵物"
)
ax.set_xlim(0, 800)
ax.set_ylim(0, 600)
ax.legend()
st.pyplot(fig)
