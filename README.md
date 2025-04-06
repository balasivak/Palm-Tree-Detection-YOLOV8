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

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/palm-tree-detection.git
cd palm-tree-detection
