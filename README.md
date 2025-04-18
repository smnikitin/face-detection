# ✨ Real-Time Face Effects with OpenCV

This project is a Python application that uses a webcam to detect faces in real-time and apply various effects such as face blur, glowing borders, and animated corners. The application leverages OpenCV for face detection and image processing.

## 🧠 Features

- Real-time face detection using OpenCV's Haar Cascade Classifier
- **Face Blur**: Strong Gaussian blur applied to detected faces
- **Glow Effect**: Multi-layer glowing rectangles around detected faces
- **Animated Corners**: Pulsing corner lines around faces
- Easily customizable effects for a personalized experience


## 📦 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Install the dependencies:

```bash
pip install opencv-python numpy
```

## 🚀 How It Works

1. **Face Detection:**  
   The program uses OpenCV's Haar Cascade Classifier to detect faces in each frame captured by the webcam.

2. **Face Blur:**  
   After detecting a face, the application applies a strong Gaussian blur to obscure the face for privacy or aesthetic purposes.

3. **Glow Effect:**  
   A glowing border is drawn around the detected face using multiple transparent layers to create a soft glowing effect.

4. **Animated Corners:**  
   Pulsing animated corner lines are drawn around the face to add a dynamic visual effect.

---

## 🖥️ Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/Real-Time-Face-Effects-with-OpenCV.git
cd Real-Time-Face-Effects-with-OpenCV
```

2. Run the script:

```bash
python face_detection_effects.py
```

3. The webcam feed will open, and face effects will be applied to any detected faces. Press **`q`** to exit the application.

---

## 📁 File Structure

```
Real-Time-Face-Effects-with-OpenCV/
│
├── face_detection_effects.py   # Main application for face effects
├── README.md                   # Project documentation
└── requirements.txt            # (Optional) Python dependencies
```

---

## 📸 Screenshots

![demo1](https://example.com/demo1.jpg)  <!-- Replace with your own demo image or GIF -->
![demo2](https://example.com/demo2.jpg)  <!-- Replace with your own demo image or GIF -->

<!-- You can also include a demo GIF -->
<!-- ![Demo](demo.gif) -->

---

## 🔧 To-Do & Improvements

- Add the option to toggle between different effects (e.g., blur, glow, animated corners).
- Implement the ability to save the video with effects applied.
- Add GUI elements using Tkinter or PyQt for better control.
- Integrate other filters or face-related effects (e.g., hats, glasses, or emoji masks).

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Credits

Created with 💻 using Python and OpenCV.  
Inspired by tutorials and open-source contributions from the computer vision community.

---

## 🤝 Contributing

Pull requests, feature suggestions, and issues are welcome! Let’s make this project even better together. ✨
