import streamlit as st
import os

folderpath = "markdown"  # 這是相對路徑
files = os.listdir(folderpath)  # 取得資料夾中的所有檔案
print(files)  # 印出所有的檔案
files_name = []
for f in files:
    if f.endswith(".md"):
        files_name.append(f)

for f in files_name:  # 逐一讀取files_name中的檔案
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:  # 開啟檔案
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 建立一個擴充元件將檔案名稱作為標題
        st.markdown(content)  # 將檔案內容顯示在擴充元件
