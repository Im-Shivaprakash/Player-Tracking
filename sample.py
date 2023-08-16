from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('yolov8n.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Perform object detection
    detections = model.detect(frame)

    # Draw the bounding boxes
    for detection in detections:
        x, y, w, h = detection[0]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the results
    cv2.imshow("Object Detection", frame)

    # Press ESC to quit
    if cv2.waitKey(1) == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()