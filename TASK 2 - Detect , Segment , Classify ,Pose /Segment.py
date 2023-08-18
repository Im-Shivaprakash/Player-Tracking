#import library
from ultralytics import YOLO
from PIL import Image

#load model
model = YOLO('yolov8n-seg.pt')

#prediction
result = model("/home/shivaprakash/Documents/git/YOLO/TASK 2 - Detect , Segment , Classify ,Pose /walking.jpeg")

for r in result:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
