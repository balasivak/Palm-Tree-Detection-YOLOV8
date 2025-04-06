# Palm Tree Detection using YOLOv8 + Roboflow + Flask

This project implements an end-to-end palm tree detection pipeline using the YOLOv8 object detection model, Roboflow for dataset integration, and a Flask web application for user image uploads and visualization of detection results.

The model is trained on an aerial palm tree dataset and optimized for deployment on both low-resource and production environments.

---

## Features

- Custom YOLOv8 training on palm tree aerial images
- Roboflow-powered dataset management and preprocessing
- Real-time object detection through a Flask web app
- Upload image via UI, view bounding box results with counts
- Lightweight deployment with OpenCV and ONNX export support

---

## Project Architecture

User (Web Upload via Flask) │ ▼ Flask Server (app.py) │ ├── Accepts aerial image upload ├── Runs YOLOv8 detection on image └── Returns image with palm boxes + count ▼ Results Display (original + annotated image via HTML)

---

## Dataset

- **Source**: Roboflow Project: [Palm Detection](https://universe.roboflow.com/nur-byq0f/palm-detection-4qh3m)
- **Download Method**: Python SDK using API key
- **Augmentations**:
  - Hue/Saturation tweaks
  - Horizontal flips
  - Slight rotations
  - Mask augmentation for dense tree regions

##Model Accuracy & Performance
This project uses a custom-trained YOLOv8 model for detecting palm trees in aerial imagery. The model was trained on a Roboflow-labeled dataset with advanced augmentations and tuned hyperparameters to optimize detection performance for palm clusters in various environments.

Training Details
Model: YOLOv8s (small variant for a balance of speed and accuracy)

Dataset Source: Roboflow (Aerial Palm Tree Dataset)

Image Size: 512 × 512

Epochs: 20

Batch Size: 6 (optimized for 4GB GPU)

Optimizer: AdamW

Augmentations:

Horizontal Flip

HSV (Hue, Saturation, Value) shifts

Small rotation (up to ±7 degrees)

MixUp and Copy-Paste

Perspective adjustment

Training Framework: Ultralytics YOLOv8

Evaluation Results
After training, the model achieved an accuracy of 89%, validated using a held-out test set and visual inspection of bounding boxes.

