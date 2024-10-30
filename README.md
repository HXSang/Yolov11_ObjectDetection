# YOLO Object Detection with OpenCV and Supervision

# Description
This project utilizes the YOLO model to perform object detection in images, creating bounding boxes around detected objects and adding confidence labels for each object. YOLO's high accuracy and performance make it ideal for real-time object detection applications. Combined with a custom dataset, this project aims to detect and classify defects in electronic components during manufacturing and assembly. The dataset includes images of circuit boards with various defect types, assisting AI engineers and developers in training models for automated defect detection and diagnosis, ultimately enhancing quality control efficiency and accuracy.

Contents
This dataset contains images of electronic circuit boards captured in a production testing environment. Defects are categorized into five distinct types:

- Defect 0 - Surface scratches on the circuit board
- Defect 1 - Scratches on component surfaces
- Defect 2 - Missing components
- Defect 3 - Damaged components
- Defect 4 - Solder joint or pin defects
Data Format
Images: Each image includes circuit boards with defect regions highlighted by bounding boxes in various colors, representing each defect type.
Annotations: Accompanying annotation files (in CSV or JSON format) provide detailed information on the location and type of defect for each image.


## Result example
<table align="center">
  <tr>
    <td align="center">
      <img src="/data/2604_2.png" alt="Input Image" width="500"/>
      <br>Input Image
    </td>
    <td align="center">
      <img src="images/2604_2.png" alt="Output Image" width="500"/>
      <br>Output Image
    </td>
  </tr>
</table>

## Libraries used
- **OpenCV**: Thư viện xử lý ảnh và video mạnh mẽ.
- **YOLO (Ultralytics)**: Mô hình phát hiện đối tượng nhanh và chính xác.
- **Supervision**: Hỗ trợ thêm chú thích (annotations) cho ảnh.

## Cấu trúc dự án
```
├── data/                     # Thư mục chứa ảnh đầu vào cần xử lý
├── images/                   # Thư mục lưu trữ ảnh sau khi đã phát hiện và thêm chú thích
├── yolo11m_trained.pt        # Tệp mô hình YOLO đã huấn luyện
├── main.py                   # Mã nguồn chính
├── requirements              # Thư viện cần dùng
└── README.md                 # Hướng dẫn sử dụng và mô tả dự án
```

## Cài đặt

1. **Clone repository về máy**:
   ```bash
   git clone https://github.com/HXSang/Yolov11_ObjectDetection.git
   cd Yolov11_ObjectDetection
   ```

2. **Cài đặt các thư viện cần thiết**:
   Sử dụng `pip` để cài đặt các thư viện:
   ```bash
   pip install opencv-python ultralytics supervision
   pip install requirements.txt
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
