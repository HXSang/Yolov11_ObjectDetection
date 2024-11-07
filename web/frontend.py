# frontend.py
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Bo mạch nhận diện lỗi")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Chọn một ảnh bo mạch")
with col2:
    uploaded_file = st.file_uploader(label ="",type=["jpg", "jpeg", "png"])
# Tạo giao diện với hai cột

col1, col2 = st.columns(2)

with col1:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Ảnh gốc", use_column_width=True)
        find_fault_button = st.button("Tìm lỗi")

# Khi nhấn nút "Tìm lỗi", gửi ảnh tới API để xử lý
if uploaded_file is not None and find_fault_button:
    files = {'file': uploaded_file.getvalue()}
    response = requests.post("http://localhost:5000/process_image", files=files)

    with col2:
        if response.ok:
            processed_image = Image.open(BytesIO(response.content))
            st.image(processed_image, caption="Ảnh sau khi nhận diện lỗi", use_column_width=True)
            st.balloons()
            st.success("Xử lý thành công")
        else:
            st.write("Lỗi:", response.json().get("error", "Không rõ lỗi"))
