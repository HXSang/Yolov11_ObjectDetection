# YOLO Object Detection with OpenCV and Supervision

## Mô tả
Dự án này sử dụng mô hình YOLO để thực hiện phát hiện đối tượng trong ảnh, tạo bounding box xung quanh các đối tượng được phát hiện và thêm nhãn chỉ số độ tin cậy cho từng đối tượng. Mô hình YOLO giúp dự án đạt được độ chính xác và hiệu suất cao, phù hợp cho các ứng dụng phát hiện đối tượng trong thời gian thực.

## Các thư viện sử dụng
- **OpenCV**: Thư viện xử lý ảnh và video mạnh mẽ.
- **YOLO (Ultralytics)**: Mô hình phát hiện đối tượng nhanh và chính xác.
- **Supervision**: Hỗ trợ thêm chú thích (annotations) cho ảnh.

## Cấu trúc dự án
```
├── data/                     # Thư mục chứa ảnh đầu vào cần xử lý
├── images/                   # Thư mục lưu trữ ảnh sau khi đã phát hiện và thêm chú thích
├── yolo11m_trained.pt        # Tệp mô hình YOLO đã huấn luyện
├── main.py                   # Mã nguồn chính
└── README.md                 # Hướng dẫn sử dụng và mô tả dự án
```

## Cài đặt

1. **Clone repository về máy**:
   ```bash
   [git clone https://github.com/HXSang/Yolov11_ObjectDetection.git]
   cd yolo-object-detection
   ```

2. **Cài đặt các thư viện cần thiết**:
   Sử dụng `pip` để cài đặt các thư viện:
   ```bash
   pip install opencv-python-headless ultralytics supervision
   ```

3. **Chuẩn bị mô hình YOLO**:
   - Tải mô hình YOLO đã huấn luyện (`yolo11m_trained.pt`) và đặt vào thư mục dự án.

## Cách sử dụng

- Đặt ảnh đầu vào trong thư mục `data/`.
- Chạy tệp `main.py` để bắt đầu xử lý và lưu ảnh kết quả vào thư mục `images/`.

```bash
python main.py
```

## Chi tiết mã nguồn

- **Tải mô hình YOLO**: Sử dụng mô hình YOLO đã huấn luyện để phát hiện đối tượng.
- **Vẽ bounding box và nhãn**: Sử dụng OpenCV để vẽ bounding box với các màu sắc khác nhau dựa trên lớp đối tượng, và thêm nhãn cho từng đối tượng với chỉ số độ tin cậy.
- **Xử lý hàng loạt**: Duyệt qua từng ảnh trong thư mục đầu vào, xử lý và lưu ảnh sau khi đã thêm chú thích vào thư mục đầu ra.

## Kết quả
Mã sẽ xuất ra các thống kê về số lượng ảnh đã xử lý thành công và số lượng ảnh gặp lỗi trong quá trình phát hiện.

## Đóng góp
Mọi đóng góp đều được chào đón! Vui lòng tạo Pull Request hoặc mở Issue nếu bạn muốn góp ý hoặc thêm chức năng.
