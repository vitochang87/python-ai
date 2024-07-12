import streamlit as st
import time
import os

# 設計products字典，每個字典，每個商品有價格price,庫存(stock),圖片(image)三個屬性
# image可以讀取存放在images資料夾內的圖片
# 讀取圖片清單

image_folder = "image"
image_files = os.listdir(image_folder)

if "products" not in st.session_state:
    st.session_state.products = {}

for image_file in image_files:
    product_name = image_file[:-4]
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }
# products範例
# products = {"蘋果": {"price": 10, "stock": 10, "image": "image/apple.jpeg"},
#             "香蕉": {"price": 10, "stock": 10, "image": "image/banana.jpeg"},
#             "橘子": {"price": 10, "stock": 10, "image": "image/orange.jpeg"},
#             "葡萄": {"price": 10, "stock": 10, "image": "image/grape.jpeg"},
#             "芒果": {"price": 10, "stock": 10, "image": "image/mango.jpeg"},
# }

# 顯示商品
st.title("購物平台")
col_num = st.number_input("欄數", min_value=1, step=1, value=2)
cols = st.columns(col_num)
i = 0
for product_name, details in st.session_state.products.items():
    with cols[i % col_num]:
        st.image(details["image"], use_column_width=True)
        st.markdown(f"###{product_name}")
        st.markdown(f"價格：${details['price']}")
        st.markdown(f"庫存：{details['stock']}")

        if st.button(f"購買 {product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                st.session_state.products[product_name]["stock"] -= 1
                st.success(f"購買{product_name}成功")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"庫存不足")
    i += 1

# 新增商絣存庫區塊
st.title("新增商品庫存")
product_names = list(st.session_state.products.keys())
coli1, coli2 = st.columns(2)
with coli1:
    selected_product = st.selectbox("選擇商品", product_names)
with coli2:
    new_stock = st.number_input("新增庫存", min_value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += new_stock
    st.success(f"{selected_product}的庫存已新增{new_stock}件")
    time.sleep(1)
    st.rerun()

    # 重新顯示商品已反應更新後的庫存
    st.markdown("目前商品庫存:")
    for product_name, details in st.session_state.products.items():
        st.markdown(f"{product_name}：{details['stock']}件")
