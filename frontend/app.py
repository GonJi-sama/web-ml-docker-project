import streamlit as st
import requests

st.title("Web-ML: Text Sentiment Analysis")
st.write("แอปพลิเคชันจำลองการวิเคราะห์ความรู้สึกของข้อความ")

user_input = st.text_input("พิมพ์ข้อความของคุณที่นี่ (ลองพิมพ์คำว่า 'ดี'):")

if st.button("วิเคราะห์ผล"):
    if user_input:
        # เรียก API จาก Backend Container (ใช้ชื่อ service 'backend')
        response = requests.post("http://backend:8000/predict", json={"text": user_input})
        if response.status_code == 200:
            result = response.json()
            st.success(f"ผลการวิเคราะห์: {result['prediction']}")
        else:
            st.error("เกิดข้อผิดพลาดในการเชื่อมต่อ Backend")
    else:
        st.warning("กรุณาพิมพ์ข้อความก่อน")
