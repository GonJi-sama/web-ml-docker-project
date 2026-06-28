# Web-ML Sentiment Analysis Dummy Project

โปรเจกต์นี้เป็นการจำลองระบบ Web Application สำหรับ Machine Learning โดยใช้ Docker Compose ประกอบด้วย 2 Containers ที่ทำงานร่วมกัน:
1. **Frontend:** สร้างด้วย Streamlit
2. **Backend:** สร้างด้วย FastAPI

## วิธีการรันโปรเจกต์ (How to run)
1. ติดตั้ง Docker และ Docker Compose บนเครื่องของคุณ
2. Clone repository นี้
3. เปิด Terminal แล้วเข้าไปที่โฟลเดอร์ของโปรเจกต์
4. รันคำสั่งต่อไปนี้:
   ```bash
   docker-compose up -d --build
