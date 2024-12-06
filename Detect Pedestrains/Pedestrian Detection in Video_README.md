# Pedestrian Detection in Video

This Python program detects pedestrians in a video using **OpenCV's Histogram of Oriented Gradients (HOG)** descriptor along with a pretrained Support Vector Machine (SVM) optimized for pedestrian detection.

## Features
- Real-time pedestrian detection in video streams.
- Draws bounding boxes around detected pedestrians.
- Resizes video frames for faster processing and better performance.

## How It Works
1. **HOG Descriptor Initialization**:
   - Initializes a HOG descriptor and loads OpenCV's default pedestrian detection SVM.
2. **Video Frame Processing**:
   - Reads video frames from a specified file.
   - Resizes frames for efficient detection.
3. **Detection**:
   - Applies the HOG detector to locate pedestrian regions in each frame.
4. **Visualization**:
   - Draws bounding boxes around detected pedestrians and displays the frames.

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
