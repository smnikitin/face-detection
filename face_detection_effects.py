# Import required libraries
import cv2               # OpenCV for image/video processing
import numpy as np       # NumPy for math and animations
import time              # For animation timing

# === Function: Blur Face Region ===
def blur_face(img, x, y, w, h, ksize=(101, 101)):
    """
    Blurs a rectangular region (the face) within the image.
    ksize defines how strong the blur is — higher means more blur.
    """
    face_region = img[y:y+h, x:x+w]                        # Crop face area from image
    blurred_face = cv2.GaussianBlur(face_region, ksize, 0)  # Apply strong Gaussian blur
    img[y:y+h, x:x+w] = blurred_face                       # Replace original face with blurred version

# === Function: Glow Border Effect ===
def draw_glow_border(img, x, y, w, h, base_color=(0, 255, 255), max_alpha=0.3, layers=5):
    """
    Draws a glowing effect around the detected face using semi-transparent rectangles.
    """
    overlay = img.copy()                    # Create a copy of the frame for drawing glow
    alpha_step = max_alpha / layers         # Gradually reduce transparency with each layer
    thickness_step = 8 // layers            # Thickness increases per layer

    for i in range(layers):
        thickness = 2 + i * thickness_step  # Layer thickness
        color = tuple(int(c) for c in base_color)  # Convert color to BGR
        # Draw glow rectangle
        cv2.rectangle(overlay, (x, y), (x + w, y + h), color, thickness)
        alpha = alpha_step * (layers - i)   # Layer alpha fades out
        # Blend the overlay with the original image
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

# === Function: Animated Corner Lines ===
def draw_animated_corners(img, x, y, w, h, progress, color=(0, 255, 0), thickness=2, max_len=30):
    """
    Draws animated pulsing corner lines around the face.
    Progress controls the animation (value between 0 and 1).
    """
    length = int(progress * max_len)  # Calculate current line length based on animation

    # Top-left corner
    cv2.line(img, (x, y), (x + length, y), color, thickness)
    cv2.line(img, (x, y), (x, y + length), color, thickness)

    # Top-right corner
    cv2.line(img, (x + w, y), (x + w - length, y), color, thickness)
    cv2.line(img, (x + w, y), (x + w, y + length), color, thickness)

    # Bottom-left corner
    cv2.line(img, (x, y + h), (x + length, y + h), color, thickness)
    cv2.line(img, (x, y + h), (x, y + h - length), color, thickness)

    # Bottom-right corner
    cv2.line(img, (x + w, y + h), (x + w - length, y + h), color, thickness)
    cv2.line(img, (x + w, y + h), (x + w, y + h - length), color, thickness)

# === Load Haar Cascade for Face Detection ===
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

# Store initial time for animations
start_time = time.time()

# === Main Loop ===
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break                # Stop if there's an issue with the webcam

    # Convert frame to grayscale (face detection works on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Calculate animation progress using sine wave (pulsing effect)
    t = time.time() - start_time
    pulse = (np.sin(t * 2) + 1) / 2  # Value between 0 and 1

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        blur_face(frame, x, y, w, h)                          # Step 1: Blur the face
        draw_glow_border(frame, x, y, w, h)                   # Step 2: Draw glow border
        draw_animated_corners(frame, x, y, w, h, pulse)       # Step 3: Add animated corners

    # Show the processed video frame
    cv2.imshow("🕶️ Face Blur + Glow + Animation", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === Cleanup ===
cap.release()              # Release the webcam
cv2.destroyAllWindows()    # Close all OpenCV windows
