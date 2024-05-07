
from ultralytics import YOLO
# Load a model

model = YOLO('yolov8n-seg.yaml').load('yolov8n-seg.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='coco8-seg.yaml', epochs=100, imgsz=640)


print('hi')