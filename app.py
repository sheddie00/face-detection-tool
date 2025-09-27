import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Streamlit app title
st.title("Face Detection App using Viola-Jones Algorithm")

# Instructions
st.write("""
**Instructions:**
1. Upload an image containing faces.
2. Adjust the `scaleFactor` and `minNeighbors` sliders to optimize face detection.
3. Choose the color of the rectangles that will be drawn around detected faces.
4. Click the 'Save Image' button to download the image with detected faces.
""")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    original_img = img.copy()
    
    # Adjust parameters
    scaleFactor = st.slider("Scale Factor", 1.01, 2.0, 1.1, step=0.01)
    minNeighbors = st.slider("Min Neighbors", 1, 10, 5, step=1)
    
    # Choose rectangle color
    rect_color = st.color_picker("Choose rectangle color", "#FF0000")
    
    # Convert hex color to BGR for OpenCV
    rect_color_bgr = tuple(int(rect_color.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    
    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), rect_color_bgr, 2)
    
    # Convert back to RGB for displaying in Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption='Detected Faces', use_column_width=True)
    
    # Button to save the image
    if st.button("Save Image"):
        save_path = "detected_faces.png"
        cv2.imwrite(save_path, img)
        st.success(f"Image saved as {save_path}")
