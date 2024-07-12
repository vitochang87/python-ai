import streamlit as st
from openai import OpenAI  # pip install openai

openai_key = st.text_input("Password", type="password", key="password")
if openai_key is None or openai_key == "":
    st.warning("請輸入OpenAI API Key")
    st.stop()

prompt_text = st.text_area("Prompt", "A cute baby sea otter")
if st.button("開始生成圖片"):
    client = OpenAI(api_key=openai_key)
    generatedImage = client.images.generate(
        model="dall-e-3",
        prompt=prompt_text,
        n=1,
        size="1024x1024",
    )
    image_url = generatedImage.data[0].url
    st.image(image_url)
