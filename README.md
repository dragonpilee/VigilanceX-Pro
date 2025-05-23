VigilanceX Pro
VigilanceX Pro is a high-performance real-time object detection desktop application powered by YOLOv8m and GPU acceleration. It provides a sleek dark retro-themed GUI for monitoring your webcam feed with configurable detection confidence, live object counting, and snapshot saving.
Features

Real-time detection: Uses YOLOv8m for robust multi-object detection at high FPS.
GPU acceleration: Automatically detects and utilizes CUDA-enabled GPUs (e.g., RTX 2050) for optimal performance.
Interactive GUI: Built with PyQt5 featuring a dark retro theme, large live camera feed, and intuitive controls.
Adjustable confidence threshold: Use a slider to dynamically set detection confidence.
Start/Stop detection: Toggle detection on/off without closing the app.
Save snapshots: Capture and save the current frame with detections.
Live object count: Displays the number of detected objects in real-time.
Detection zones: Highlights a configurable region for focused monitoring.
Lightweight & efficient: Optimized for minimal lag and frame drops.

Requirements

Python 3.8 or newer
NVIDIA GPU with CUDA support (recommended for best performance)
PyTorch with CUDA (see PyTorch Get Started)
OpenCV
PyQt5
ultralytics (YOLOv8)

Installation

Clone or download this repository.
Install dependencies:

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
pip install opencv-python pyqt5 ultralytics


Download the YOLOv8m model weights (yolov8m.pt) or let the app auto-download on first run.

Usage

Run the app with:

python vigilancex_pro.py


Adjust confidence using the slider.
Use the Stop Detection button to pause or resume detection.
Click Save Snapshot to save the current camera frame with bounding boxes.
See live GPU acceleration status in green if CUDA is enabled.
Monitor detected object count below the camera feed.

Troubleshooting

Ensure your webcam is connected and accessible.
Confirm CUDA drivers and PyTorch with CUDA are properly installed for GPU acceleration.
If GPU is unavailable, the app will automatically fallback to CPU, but performance may degrade.

License
MIT License
Acknowledgments

Ultralytics YOLOv8 for the powerful detection model.
PyQt5 for the GUI framework.
OpenCV for video capture and image processing.

VigilanceX Pro — Elevate your real-time object detection experience!
