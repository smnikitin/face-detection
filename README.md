# Face Detection with Effects (Blur, Glow, Animated Corners)

This project uses OpenCV to detect faces in real-time via webcam and applies several cool effects to the detected faces. The effects include:

- **Face Blur**: Blurs the face for privacy or aesthetic purposes.
- **Glow Border**: Adds a glowing border around the face.
- **Animated Corners**: Creates animated pulsing corner lines around the face.

This project demonstrates how to combine **face detection**, **real-time image processing**, and **animation** with Python and OpenCV.

## Features

- Real-time **face detection** using OpenCV's Haar Cascade Classifier.
- Strong **Gaussian blur** applied to faces to obscure them.
- **Glow effect** around faces with a pulsing animation.
- **Animated corner lines** around detected faces that pulse with time.

## Installation

To use this project, you'll need to install Python 3 and the required libraries. Follow these steps to set it up:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/face-detection-effects.git
    cd face-detection-effects
    ```

2. **Install dependencies**:
    This project requires **OpenCV** and **NumPy**. You can install them using `pip`:
    ```bash
    pip install opencv-python numpy
    ```

## Usage

### Run the program:

1. Make sure your webcam is connected.
2. Run the Python script:
    ```bash
    python face_detection_effects.py
    ```

3. The webcam will open and the program will start detecting faces in real-time, applying the blur, glow, and animated corner effects. Press **`q`** to exit the program.

### Key Controls:
- **Press `q`**: Exit the program.
- **Face Detection**: The program automatically detects faces in the webcam feed and applies the effects to them.
  
## Customization

You can adjust the effects:

- **Change blur intensity**: Modify the `ksize` value in the `blur_face()` function. Larger values will result in stronger blur.
- **Glow effect**: Customize the `base_color`, `max_alpha`, and `layers` in the `draw_glow_border()` function to adjust the glow effect around the face.
- **Animated corners**: Tweak the `max_len` and `progress` in the `draw_animated_corners()` function to adjust the corner animation.

## Example

Here’s an example of how the webcam feed might look with the effects applied:

![Face Detection Example](assets/face-detection-example.png)

## Dependencies

This project requires the following Python packages:

- **OpenCV**: For computer vision tasks (face detection, image processing).
- **NumPy**: For mathematical operations and animations.

You can install these libraries via `pip`:
```bash
pip install opencv-python numpy
# face-detection