from ultralytics import YOLO 

# load a model

model = YOLO("yolov8n.yaml") # training from strach

# use the model
results = model.train(data="data.yaml", epochs=5) # train the model

