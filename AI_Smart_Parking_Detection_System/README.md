# AI Smart Parking Occupancy Detection System
# 🅿️ AI Smart Parking Occupancy Detection System

An AI-powered smart parking detection system built using Python, OpenCV, and YOLOv8.

This project detects vehicles in a live video stream and determines whether predefined parking slots are occupied or free. It provides real-time parking statistics and visual slot classification.


Designed for:
- Smart city applications
- Intelligent transportation systems
- AI & Computer Vision learning
- Engineering mini/major projects
- Hackathons

---

## 🚀 Features

- Real-time vehicle detection
- Detects: car, truck, bus, motorcycle
- Parking slot occupancy detection
- Free vs Occupied classification
- Live parking statistics display
- Webcam or video input support
- Lightweight YOLOv8 nano model

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy

---

## 📂 Project Structure

AI_Smart_Parking_Detection_System/
│
├── main.py
├── detector.py
├── config.py
├── requirements.txt
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to the project directory:

   cd AI_Smart_Parking_Detection_System

4. Install dependencies:

   pip install -r requirements.txt

5. Run the system:

   python main.py

The YOLOv8 model will automatically download on first execution.

---

## 📊 How It Works

1. Video stream is captured from webcam or file.
2. YOLOv8 detects vehicles in each frame.
3. Predefined parking slot regions are checked for vehicle overlap.
4. Each slot is classified as:
   - 🟢 Free
   - 🔴 Occupied
5. Live statistics are displayed:
   - Total spots
   - Occupied spots
   - Free spots

---

## ⚠️ Configuration

Parking slots are manually defined in `config.py`:

```python
PARKING_SPOTS = [
    (x1, y1, x2, y2),
    ...
]

AI-based smart parking detection system using YOLOv8 and OpenCV.

## Features
- Real-time vehicle detection
- Parking spot occupancy detection
- Free vs Occupied classification
- Live parking statistics display
- Webcam or video input support

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

Modify PARKING_SPOTS in config.py to match your camera view.
YOLO model auto-downloads on first run.
