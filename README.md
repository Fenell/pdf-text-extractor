# 📄 AI OCR Service - Technology & Deployment

## 🧠 Công nghệ sử dụng

Dự án sử dụng các thành phần chính sau:

### 1. AI Model

* **Vintern-1B-v2**

  * Model AI dùng để nhận dạng và trích xuất văn bản từ ảnh/PDF
  * Phù hợp với bài toán OCR nâng cao (layout phức tạp, nhiều font)

---

### 2. Backend API

* **Flask (Python)**

  * Xây dựng REST API đơn giản
  * Nhận file đầu vào (PDF / Image)
  * Gọi model để xử lý và trả kết quả

---

### 3. Xử lý dữ liệu đầu vào

* **OpenCV**

  * Resize, grayscale, threshold ảnh
  * Tăng chất lượng OCR

* **pdf2image**

  * Convert PDF → ảnh để đưa vào model

---

### 4. Môi trường chạy model

* **Google Colab**

  * Cung cấp GPU miễn phí để load model
  * Phù hợp cho test / demo nhanh

---

### 5. Public API

* **Ngrok**

  * Expose local server (Flask trên Colab) ra internet
  * Cho phép các ứng dụng khác gọi API

---

## 🚀 Cách triển khai

### Bước 1: Khởi tạo môi trường (Colab)

* Cài dependencies Python
* Enable GPU runtime

---

### Bước 2: Load AI Model

* Load model **Vintern-1B-v2** vào bộ nhớ GPU
* Chuẩn bị pipeline inference

---

### Bước 3: Xây dựng API

* Tạo endpoint `/ocr`
* Nhận file upload (multipart/form-data)
* Xử lý:

  * PDF → convert ảnh
  * Image → preprocess
* Gọi model để extract text
* Trả response JSON

---

### Bước 4: Expose API

* Sử dụng Ngrok để tạo public URL
* Map tới Flask server (port 5000)

---

### Bước 5: Tích hợp vào hệ thống

* Client (web/app/backend khác) gọi API qua HTTP
* Nhận kết quả OCR dạng JSON
* Sử dụng cho các nghiệp vụ tiếp theo

---

## ⚠️ Lưu ý triển khai

* Ngrok URL là tạm thời (thay đổi mỗi lần chạy)
* Colab không phù hợp production (timeout, reset session)
* Model load lại mỗi lần restart runtime

---

## 🔥 Hướng triển khai production

* Deploy lên server GPU (AWS EC2, GCP, Azure)
* Dockerize toàn bộ service
* Dùng reverse proxy (Nginx) thay cho Ngrok
* Tách service OCR thành microservice độc lập
* Thêm queue (RabbitMQ / Kafka) nếu xử lý batch

---

👉 Phù hợp cho: POC, demo, nghiên cứu, thử nghiệm pipeline AI OCR
