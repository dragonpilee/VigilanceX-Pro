import sys
import cv2
import torch
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout,
    QSlider, QPushButton, QHBoxLayout, QFileDialog
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from ultralytics import YOLO

class VigilanceXProApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VigilanceX Pro — Real-Time Object Detection")
        self.setGeometry(100, 100, 960, 760)

        # Load YOLOv8m model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = YOLO("yolov8m.pt")
        self.model.to(self.device)

        # Setup webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Cannot open webcam")

        # GUI Components
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(900, 600)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(90)
        self.slider.setValue(40)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.update_confidence)

        self.save_button = QPushButton("Save Snapshot")
        self.save_button.clicked.connect(self.save_snapshot)

        self.toggle_button = QPushButton("Stop Detection")
        self.toggle_button.clicked.connect(self.toggle_detection)

        self.count_label = QLabel("Objects Detected: 0")
        self.count_label.setAlignment(Qt.AlignCenter)

        self.gpu_label = QLabel()
        self.gpu_label.setAlignment(Qt.AlignCenter)
        self.gpu_label.setStyleSheet("color: #00FF00; font-weight: bold;")  # green text
        self.update_gpu_label()

        # Dark retro theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
                color: #e0e0e0;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                background-color: #333333;
                color: #e0e0e0;
                border: none;
                padding: 8px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #333333;
            }
            QSlider::handle:horizontal {
                background: #777777;
                border: 1px solid #444444;
                width: 14px;
                margin: -5px 0;
                border-radius: 7px;
            }
        """)

        # Layout setup
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(QLabel("Confidence:"))
        slider_layout.addWidget(self.slider)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.toggle_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(slider_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.count_label)
        main_layout.addWidget(self.gpu_label)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Timer for webcam
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(25)  # ~40 FPS target

        # Detection settings
        self.conf_threshold = 0.4
        self.detection_enabled = True
        self.current_frame = None

    def update_confidence(self):
        self.conf_threshold = self.slider.value() / 100

    def toggle_detection(self):
        self.detection_enabled = not self.detection_enabled
        self.toggle_button.setText("Start Detection" if not self.detection_enabled else "Stop Detection")

    def save_snapshot(self):
        if self.current_frame is not None:
            filename = QFileDialog.getSaveFileName(self, "Save Snapshot",
                        datetime.now().strftime("snapshot_%Y%m%d_%H%M%S.jpg"),
                        "Images (*.png *.xpm *.jpg)")[0]
            if filename:
                cv2.imwrite(filename, self.current_frame)

    def update_gpu_label(self):
        if self.device == "cuda":
            gpu_name = torch.cuda.get_device_name(torch.cuda.current_device())
            self.gpu_label.setText(f"GPU Acceleration: Enabled ({gpu_name})")
        else:
            self.gpu_label.setText("GPU Acceleration: Disabled (Using CPU)")

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        self.current_frame = frame.copy()

        if self.detection_enabled:
            results = self.model.predict(frame, device=self.device, conf=self.conf_threshold, verbose=False)
            frame = results[0].plot()

            object_count = len(results[0].boxes)
            self.count_label.setText(f"Objects Detected: {object_count}")
        else:
            self.count_label.setText("Detection Paused")

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio
        ))

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigilanceXProApp()
    window.show()
    sys.exit(app.exec_())
