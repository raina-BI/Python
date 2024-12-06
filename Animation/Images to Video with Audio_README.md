# Images to Video with Audio

## Overview

This Python program converts a sequence of images into a video using OpenCV and adds an audio track to the generated video using the `moviepy` library. It is designed to take images from a specified folder, combine them into a video, and synchronize the video with an audio file.

## Features

- Converts a set of images into a video.
- Supports video encoding with OpenCV's `VideoWriter`.
- Adds an audio track to the video using the `moviepy` library.
- Ensures the audio duration matches the video length.

## Requirements

- Python 3.x
- Required Libraries:
  - OpenCV (`cv2`)
  - MoviePy

### Install Dependencies

Install the required libraries using pip:
```bash
pip install opencv-python
pip install moviepy
