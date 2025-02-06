from ultralytics import YOLO
from utils import get_device

if __name__ == "__main__":

    # 0. There are a lot of requirements to create/use OpenCV projects. I used the following video to get started
    # https://youtu.be/WgPbbWmnXJ8

    # If you want to train your own model, follow the steps below. Otherwise, use the pre-trained best.pt model

    # 1. Download the dataset specified in config.yaml
    # 2. Put the downloaded folders into your project and change absolute paths in config.yaml
    # 3. Change the following text to the correct relative paths for your project
    # 4. Run this
    # 5. Go to runs/detect/train/weights and use that best.pt as the model while running shot_detector.py

    # Select device for training
    device = get_device()

    # If there is no pre-trained model, use YOLO's default
    PRE_TRAINED_MODEL = 'Yolo-Weights/yolov8n.pt'

    # Load a model
    model = YOLO(PRE_TRAINED_MODEL)

    # Train the model
    results = model.train(data='config.yaml', epochs=100, imgsz=640, device=device)
