from roboflow import Roboflow
rf = Roboflow(api_key="lW2M9R50ueexTc1dQW0m")
project = rf.workspace("infinitrix").project("obj-det.")
dataset = project.version(2).download("yolov8")


from ultralytics import YOLO
model = YOLO('yolov8n.yaml')
results = model.train(data= '/home/shivaprakash/Documents/git/YOLO/Obj-Det.-2/data.yaml', epochs=10, imgsz=640)