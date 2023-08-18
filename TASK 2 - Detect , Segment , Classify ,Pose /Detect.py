from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")

results = model.predict('/home/shivaprakash/Documents/git/YOLO/TASK 1 - Inference/dog.jpeg')

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image