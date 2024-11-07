from flask import Flask, request, jsonify, send_file
import os
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import supervision as sv

app = Flask(__name__)

# Load model YOLO
model = YOLO("./model/yolo11m_trained.pt")

# Folder to save processed images
output_folder = "./images"
os.makedirs(output_folder, exist_ok=True)

COLORS = [
    (255, 0, 0),    
    (0, 255, 0),    
    (0, 0, 255),    
    (255, 255, 0),  
    (255, 0, 255)   
]

def create_label(class_id, confidence, class_names):
    return f"{class_names[class_id]} {confidence:0.2f}"

def process_image(image, output_path):
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Model prediction
    results = model(frame)[0]
    
    boxes = results.boxes.xyxy.cpu().numpy()
    confidences = results.boxes.conf.cpu().numpy()
    class_ids = results.boxes.cls.cpu().numpy().astype(int)
    
    detections = sv.Detections(
        xyxy=boxes,
        confidence=confidences,
        class_id=class_ids
    )
    
    labels = [
        create_label(class_id, confidence, model.model.names)
        for class_id, confidence 
        in zip(detections.class_id, detections.confidence)
    ]
    
    annotated_frame = frame.copy()
    for i, (box, label) in enumerate(zip(boxes, labels)):
        x1, y1, x2, y2 = box.astype(int)
        color = COLORS[detections.class_id[i] % len(COLORS)]
        
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
        ((text_w, text_h), _) = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + text_w, y1), color, -1)
        cv2.putText(annotated_frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    
    cv2.imwrite(output_path, annotated_frame)
    return True

@app.route("/process_image", methods=["POST"])
def process_image_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    image = Image.open(file.stream)
    output_path = os.path.join(output_folder, "processed_image.jpg")
    
    if process_image(image, output_path):
        return send_file(output_path, mimetype='image/jpeg')
    else:
        return jsonify({"error": "Failed to process image"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
