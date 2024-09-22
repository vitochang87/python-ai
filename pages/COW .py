import streamlit as st
from langchain_openai import ChatOpenAI  # pip install -U langchain-openai
from langchain_core.messages import HumanMessage, AIMessage  # pip install langchain


col1, col2 = st.columns([4, 1])
with col1:
    openai_key = st.text_input("Password", type="password", key="password")
    if openai_key is None or openai_key == "":
        st.warning("請輸入OpenAI API Key")
        st.stop()

if "history" not in st.session_state:  # 初始化對話紀錄
    st.session_state.history = []  # 對話紀錄

with col2:
    if st.button("🗑️"):  # 清空對話紀錄
        st.session_state.history = []  # 對話紀錄清空
        st.rerun()  # 重新整理頁面

msgs = [
    HumanMessage(
        "並稱呼你為cowAI，稱呼我為小恐龍，陳思瀚是我最好的朋友，張家愷是我的真名"
    )
]  # 對話訊息列表，初始化為一個包含提示訊息的HumanMessage物件
for actor, message in st.session_state.history:  # 透過對話紀錄來初始化對話訊息列表
    if actor == "user":  # 如果是使用者的訊息
        st.chat_message("user", avatar="🦖").write(message)  # 顯示使用者的對話紀錄訊息
        # st.chat_message("user", avatar=st.image("image/蘋果.jpg")).write(message)
        msgs.append(HumanMessage(message))  # 將使用者的訊息加入對話訊息列表
    else:
        st.chat_message("assistant", avatar="🐮").write(
            message
        )  # 顯示AI回傳的對話紀錄訊息
        msgs.append(AIMessage(message))  # 將AI回傳的訊息加入對話訊息列表

chat = ChatOpenAI(model="gpt-4o", temperature=0.2, api_key=openai_key)
prompt = st.chat_input("請輸入想要對話的訊息")  # 顯示對話輸入框
if prompt:  # 如果使用者輸入了訊息
    st.session_state.history.append(["user", prompt])  # 將使用者輸入的訊息加入對話紀錄
    msgs.append(HumanMessage(prompt))  # 將使用者輸入的訊息加入對話訊息列表
    response = chat.invoke(msgs).content  # 使用ChatOpenAI模型進行對話
    st.session_state.history.append(
        ["assistant", response]
    )  # 將ChatOpenAI回傳的訊息加入對話紀錄
    st.rerun()
