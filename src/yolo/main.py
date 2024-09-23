from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("Path to yolo model")


    model.to('cuda')

    model.train(data="Path to dataset folder/", epochs=100, imgsz=80)
