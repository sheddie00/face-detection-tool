# Streamlit Face Detector

![Face Detection Banner](https://images.unsplash.com/photo-1606223724372-11e69c147c35?ixlib=rb-4.0.3&auto=format&fit=crop&w=1400&q=80)

A **Streamlit web app** for detecting faces in images using the **Viola-Jones algorithm** (Haar Cascades) with **OpenCV**. Users can upload images, adjust detection parameters, choose rectangle colors, and download the processed images.

---

## Features

- Detect faces in images using the Viola-Jones algorithm.
- Upload `.jpg`, `.jpeg`, or `.png` images.
- Adjust detection parameters:
  - `scaleFactor` – controls image scaling for detection.
  - `minNeighbors` – controls detection strictness.
- Choose the color of rectangles around detected faces.
- Download the processed image directly from the app.
- User-friendly interface built with **Streamlit**.

---

## Demo

![Demo Screenshot](https://images.unsplash.com/photo-1581091215365-29b5bcd3c33e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1400&q=80)

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/streamlit-face-detector.git
cd streamlit-face-detector
