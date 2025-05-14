# ✋ Hand Gesture Recognition with MediaPipe

This project uses **MediaPipe** and **OpenCV** to recognize hand gestures in real-time from your webcam feed.

## 🔍 Features

- Detects a single hand using MediaPipe
- Identifies how many fingers are raised
- Classifies gestures from a simple predefined list:
  - **FIST** (0 fingers)
  - **GESTURE ONE** (1 finger)
  - **GESTURE TWO** (2 fingers)
  - **GESTURE THREE** (3 fingers)
  - **GESTURE FOUR** (4 fingers)
  - **GESTURE FIVE** (5 fingers)

## 🛠️ Requirements

Install the dependencies:

```bash
pip install opencv-python mediapipe
```

## 🚀 How to Run

1. Make sure your webcam is connected.  
2. Run the script:
 ```bash
   python model.py
```
A window will open showing the webcam feed with hand gesture recognition labels.

Press Esc to exit.


