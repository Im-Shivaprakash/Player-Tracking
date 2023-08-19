#TRACKING WITHOUT OPENCV

from ultralytics import YOLO

model = YOLO('yolov8n.pt') 

# Perform tracking with the model
results = model.track(source="https://www.youtube.com/watch?v=Y1jTEyb3wiI", show=True)

