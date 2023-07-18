# Real-Time AI Basketball Shot Detection with YOLOv8 and OpenCV

## Introduction

Welcome to the real-time basketball shot detection/tracker project! This project utilizes a custom-trained machine learning model, YOLOv8 (You Only Look Once), and OpenCV for processing video feed. The program is designed to detect and analyze shots during a live basketball game, offering an immersive playing experience and valuable insights for players and coaches. With capability to process a video stream in real-time, this project can be used with live camera feed such as from a webcam or streamed from an iPhone.

https://github.com/avishah3/AI-Basketball-Shot-Detector-Tracker/assets/115107522/3f50e1e2-313c-401a-b8a7-f425c1250f16

## Model Training

The model training leverages the ultralytics YOLO implementation, with the model undergoing 100 epochs of training on a custom dataset specified in the 'config.yaml' file. The weights of the best-performing model during training are saved in the 'runs/detect/train/weights' directory as 'best.pt'. This model consists of two objects (basketball and basketball hoop) and worked with decent consistency for me. However, it is not perfect and a different dataset or training method might be better for your project.

## Algorithm

The core of this project is an algorithm that uses the trained YOLOv8 model to detect basketballs and hoops in each frame. It then analyzes the motion and position of the basketball relative to the hoop to determine if a shot has been made.

To enhance the accuracy of the shot detection, the algorithm not only tracks the ball's position over time but also applies data cleaning techniques to both the ball and hoop positions. The algorithm is designed to filter out inaccurate data points, remove points beyond a certain frame limit and prevent jumping from one object to another to maintain the accuracy of the detection.

A linear regression is used to predict the ball's trajectory based on its positions. If the projected trajectory intersects with the hoop, the algorithm registers it as a successful shot.

## How to Use This Code

1. Clone this repository to your local machine.
2. Download the dataset specified in 'config.yaml' and adjust the paths in the configuration file to match your local setup.
3. Follow the instructions in 'main.py' to train the model and prepare for shot detection.
4. Run 'shot_detector.py' through your webcam or iPhone for real-time shot detection. Or input a video for shot detection analysis.

Please ensure you have the required Python packages installed, including OpenCV, numpy, and ultralytics' YOLO. Contributions to this project are welcome - submit a pull request. For issues or suggestions, open an issue in this repository.

**Disclaimer:** The model's performance can vary based on factors such as the quality of the video feed, lighting conditions, and the clarity of the basketball and hoop in the video. Furthermore, this program will not work well if there are multiple basketballs and hoops in frame.
