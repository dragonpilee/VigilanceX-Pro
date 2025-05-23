# VigilanceX Pro

**VigilanceX Pro** is a state-of-the-art desktop application designed for real-time object detection, leveraging the power of YOLOv8m and GPU acceleration. Featuring a sleek, dark retro-themed graphical user interface (GUI) built with PyQt5, it offers an intuitive and efficient solution for monitoring webcam feeds with advanced features like configurable detection confidence, live object counting, and snapshot capture.

## Key Features

- **High-Performance Detection**: Utilizes YOLOv8m for robust, multi-object detection with high frames-per-second (FPS) processing.
- **GPU Acceleration**: Seamlessly integrates with CUDA-enabled NVIDIA GPUs (e.g., RTX 2050) for optimal performance.
- **Modern GUI**: Crafted with PyQt5, featuring a dark retro aesthetic, large live camera feed, and user-friendly controls.
- **Dynamic Confidence Adjustment**: Adjust detection confidence in real-time using an intuitive slider.
- **Flexible Detection Control**: Start or stop detection without closing the application.
- **Snapshot Functionality**: Capture and save frames with annotated bounding boxes for later analysis.
- **Real-Time Object Counting**: Displays the number of detected objects directly below the camera feed.
- **Configurable Detection Zones**: Focus monitoring on specific regions with customizable detection areas.
- **Optimized Performance**: Engineered for minimal latency and frame drops, ensuring a smooth user experience.

## System Requirements

- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+ recommended)
- **Python**: Version 3.8 or higher
- **Hardware**: NVIDIA GPU with CUDA support (recommended for optimal performance; CPU fallback available)
- **Dependencies**:
  - PyTorch with CUDA support (refer to [PyTorch Get Started](https://pytorch.org/get-started/locally/))
  - OpenCV
  - PyQt5
  - ultralytics (YOLOv8)

## Installation

Follow these steps to set up VigilanceX Pro:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-repo>/vigilancex-pro.git
   cd vigilancex pro
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
   pip install opencv-python pyqt5 ultralytics
   ```

3. **Model Weights**:
   The application will automatically download the YOLOv8m model weights (`yolov8m.pt`) on first run. Alternatively, manually download the weights from [Ultralytics](https://github.com/ultralytics/ultralytics) and place them in the project directory.

## Usage

1. **Launch the Application**:
   ```bash
   python vigilancex pro.py
   ```

2. **Interact with the GUI**:
   - **Adjust Confidence**: Use the slider to fine-tune the detection confidence threshold.
   - **Control Detection**: Toggle the **Stop Detection** button to pause or resume object detection.
   - **Capture Snapshots**: Click **Save Snapshot** to save the current frame with bounding box annotations.
   - **Monitor GPU Status**: A green indicator confirms CUDA-enabled GPU acceleration.
   - **Track Objects**: View the live count of detected objects below the camera feed.
   - **Configure Detection Zones**: Set specific regions for focused monitoring via the GUI.

## Troubleshooting

- **Webcam Issues**: Ensure your webcam is properly connected and recognized by your system.
- **GPU Acceleration**: Verify that CUDA drivers and PyTorch with CUDA support are correctly installed. Without a compatible GPU, the application will fallback to CPU mode, which may impact performance.
- **Dependency Errors**: Confirm all required packages are installed using the provided `pip` commands.
- **Performance Lag**: For optimal performance, ensure your system meets the recommended hardware requirements and close unnecessary applications.

## Contributing

We welcome contributions to enhance VigilanceX Pro. To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description of your changes.

Please adhere to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the cutting-edge object detection model.
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) for the robust GUI framework.
- [OpenCV](https://opencv.org/) for efficient video capture and image processing.

## Contact

For questions, feedback, or support, please open an issue on the [GitHub repository](https://github.com/dragonpilee/VigilanceX-Pro) or contact the development team at <alan_cyril@yahoo.com>.

**VigilanceX Pro — Empowering Precision in Real-Time Object Detection**
