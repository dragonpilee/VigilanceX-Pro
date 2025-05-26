# VigilanceX Pro

![Python](https://img.shields.io/badge/Language-Python-blue)
![YOLOv8](https://img.shields.io/badge/Detection-YOLOv8m-yellow)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-purple)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-red)
![CUDA](https://img.shields.io/badge/GPU-Acceleration-green)

> **Developed by Alan Cyril Sunny**  
> If you find this project helpful, please consider ⭐ [starring the repository](https://github.com/dragonpilee/VigilanceX-Pro)!

---

## 🛡️ VigilanceX Pro

**VigilanceX Pro** is a state-of-the-art desktop application for real-time object detection, leveraging YOLOv8m and GPU acceleration. Featuring a sleek, dark retro-themed GUI built with PyQt5, it offers intuitive monitoring of webcam feeds with advanced features like configurable detection confidence, live object counting, and snapshot capture.

---

## ✨ Key Features

- **High-Performance Detection**: YOLOv8m for robust, multi-object detection with high FPS.
- **GPU Acceleration**: CUDA-enabled NVIDIA GPU support for optimal performance.
- **Modern GUI**: PyQt5 dark retro theme, large live camera feed, and user-friendly controls.
- **Dynamic Confidence Adjustment**: Real-time detection confidence slider.
- **Flexible Detection Control**: Start/stop detection without closing the app.
- **Snapshot Functionality**: Capture and save annotated frames.
- **Real-Time Object Counting**: Live count of detected objects below the feed.
- **Configurable Detection Zones**: Focus on specific regions with customizable areas.
- **Optimized Performance**: Minimal latency and frame drops.

---

## 🖥️ System Requirements

- **OS**: Windows 10/11 or Linux (Ubuntu 20.04+ recommended)
- **Python**: 3.8 or higher
- **Hardware**: NVIDIA GPU with CUDA (recommended; CPU fallback available)
- **Dependencies**:
  - PyTorch with CUDA ([PyTorch Get Started](https://pytorch.org/get-started/locally/))
  - OpenCV
  - PyQt5
  - ultralytics (YOLOv8)

---

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dragonpilee/VigilanceX-Pro.git
   cd vigilancex-pro
   ```

2. **Install Dependencies**
   ```bash
   pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
   pip install opencv-python pyqt5 ultralytics
   ```

3. **Model Weights**
   - The app auto-downloads YOLOv8m weights (`yolov8m.pt`) on first run.
   - Or, download manually from [Ultralytics](https://github.com/ultralytics/ultralytics) and place in the project directory.

---

## 🕹️ Usage

1. **Launch the Application**
   ```bash
   python vigilancex-pro.py
   ```

2. **Interact with the GUI**
   - **Adjust Confidence**: Use the slider to set detection confidence.
   - **Control Detection**: Toggle detection on/off.
   - **Capture Snapshots**: Save current frame with bounding boxes.
   - **Monitor GPU Status**: Green indicator for CUDA acceleration.
   - **Track Objects**: Live object count below the feed.
   - **Configure Detection Zones**: Set regions for focused monitoring.

---

## 🛠️ Troubleshooting

- **Webcam Issues**: Ensure your webcam is connected and recognized.
- **GPU Acceleration**: Verify CUDA drivers and PyTorch with CUDA are installed. CPU fallback is available but slower.
- **Dependency Errors**: Confirm all packages are installed as above.
- **Performance Lag**: Meet hardware requirements and close unnecessary apps.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request with a detailed description.

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- [OpenCV](https://opencv.org/)

---

## 📬 Contact

For questions, feedback, or support, open an issue on the [GitHub repository](https://github.com/dragonpilee/VigilanceX-Pro) or contact <alan_cyril@yahoo.com>.

---

**VigilanceX Pro — Empowering Precision in Real-Time Object Detection**
