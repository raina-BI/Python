# Pedestrian Detection in Images

This Python program detects pedestrians in an image using **OpenCV's Histogram of Oriented Gradients (HOG)** descriptor and a pretrained Support Vector Machine (SVM) optimized for pedestrian detection.

## Features
- Utilizes OpenCV's HOG descriptor for accurate pedestrian detection.
- Resizes the input image for optimized detection performance.
- Highlights detected pedestrians with bounding boxes on the image.

## How It Works
1. **HOG Descriptor Initialization**: The program initializes a HOG descriptor and loads the default pedestrian detection SVM from OpenCV.
2. **Image Processing**: 
   - Reads the input image.
   - Resizes it for better performance and efficiency.
3. **Detection**: Applies the HOG detector to locate pedestrian regions in the image.
4. **Visualization**: Draws bounding boxes around detected pedestrians and displays the result.

## Prerequisites
To run this program, you need:
- Python 3.x
- The following Python libraries:
  - OpenCV (`cv2`)
  - imutils

## Setup and Installation
1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install opencv-python imutils
