from ultralytics import YOLO
from PIL import Image

model = YOLO('runs/detect/train4/weights/best.pt')

result = model("/home/shivaprakash/Documents/git/YOLO/Gls.jpeg")

for r in result:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
