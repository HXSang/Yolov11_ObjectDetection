import cv2
import os
from ultralytics import YOLO
import supervision as sv

# Tải model YOLO
model = YOLO("./model/yolo11m_trained.pt")

COLORS = [
    (255, 0, 0),    
    (0, 255, 0),    
    (0, 0, 255),    
    (255, 255, 0),  
    (255, 0, 255)   
]

def create_label(class_id, confidence, class_names):
    return f"{class_names[class_id]} {confidence:0.2f}"

def process_image(image_path, output_path):
    # Đọc ảnh
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Không thể đọc ảnh: {image_path}")
        return False
    
    results = model(frame)[0]
    
    boxes = results.boxes.xyxy.cpu().numpy()
    confidences = results.boxes.conf.cpu().numpy()
    class_ids = results.boxes.cls.cpu().numpy().astype(int)
    
    detections = sv.Detections(
        xyxy=boxes,
        confidence=confidences,
        class_id=class_ids
    )
    
    if len(detections) == 0:
        print(f"Không phát hiện đối tượng nào trong ảnh: {image_path}")
        cv2.imwrite(output_path, frame)
        return True
    
    # Tạo labels
    labels = [
        create_label(class_id, confidence, model.model.names)
        for class_id, confidence 
        in zip(detections.class_id, detections.confidence)
    ]
    
    # Sao chép ảnh và vẽ bounding box, label box với cùng màu
    annotated_frame = frame.copy()
    
    for i, (box, label) in enumerate(zip(boxes, labels)):
        x1, y1, x2, y2 = box.astype(int)
        color = COLORS[detections.class_id[i] % len(COLORS)]
        
        # Vẽ bounding box với màu tương ứng
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
        
        # Vẽ label box và text với cùng màu
        ((text_w, text_h), _) = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + text_w, y1), color, -1)
        cv2.putText(annotated_frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    
    try:
        cv2.imwrite(output_path, annotated_frame)
        print(f"Đã xử lý và lưu ảnh: {output_path}")
        return True
    except Exception as e:
        print(f"Lỗi khi lưu ảnh {output_path}: {str(e)}")
        return False

output_folder = "./images"
os.makedirs(output_folder, exist_ok=True)

input_folder = "./data"
processed_count = 0
error_count = 0

for image_name in os.listdir(input_folder):
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, image_name)
        try:
            if process_image(image_path, output_path):
                processed_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"Lỗi khi xử lý ảnh {image_name}: {str(e)}")
            error_count += 1

print(f"\nKết quả xử lý:")
print(f"- Số ảnh đã xử lý thành công: {processed_count}")
print(f"- Số ảnh bị lỗi: {error_count}")
print(f"- Tổng số ảnh: {processed_count + error_count}")
