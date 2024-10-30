# YOLO Object Detection with OpenCV and Supervision

## Mô tả
Dự án này sử dụng mô hình YOLO để thực hiện phát hiện đối tượng trong ảnh, tạo bounding box xung quanh các đối tượng được phát hiện và thêm nhãn chỉ số độ tin cậy cho từng đối tượng. Mô hình YOLO giúp dự án đạt được độ chính xác và hiệu suất cao, phù hợp cho các ứng dụng phát hiện đối tượng trong thời gian thực.Kết hợp với bộ dữ liệu được xây dựng nhằm mục đích phát hiện và phân loại các lỗi linh kiện điện tử trong sản xuất và lắp ráp. Bộ dữ liệu bao gồm hình ảnh các bảng mạch với các loại lỗi khác nhau, giúp các kỹ sư và nhà phát triển trong lĩnh vực trí tuệ nhân tạo huấn luyện mô hình phát hiện và chẩn đoán lỗi tự động, góp phần cải thiện hiệu quả và độ chính xác trong quy trình kiểm tra chất lượng sản phẩm.

Nội dung
Bộ dữ liệu này chứa hình ảnh của các bảng mạch điện tử được chụp trong môi trường kiểm tra sản xuất. Các lỗi được chia thành năm loại, cụ thể:

- Lỗi 0 - Vết trầy xước trên bề mặt mạch
- Lỗi 1 - Hỏng hóc hoặc mất một phần linh kiện
- Lỗi 2 - Bám bẩn hoặc oxi hóa trên bề mặt linh kiện
- Lỗi 3 - Sai lệch về vị trí hoặc lắp đặt không chính xác
- Lỗi 4 - Lỗi kết nối, hỏng chân hàn

Định dạng dữ liệu
Hình ảnh: Các hình ảnh chứa bảng mạch điện tử với các vùng lỗi được đánh dấu bằng các hộp giới hạn với màu sắc khác nhau, tượng trưng cho từng loại lỗi.
Tệp chú thích: Các tệp chú thích đi kèm (ở định dạng CSV hoặc JSON) chứa thông tin chi tiết về vị trí và loại lỗi cho từng hình ảnh.

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
