"""
#python program to convert a set of images into a video using 'OPENCV--(VideoWriter)'.
and then also add an audio to the video using 'moviepy' library.
@author: raina
"""

import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip


# Folder containing images
image_folder = 'c:/Users/raina/Desktop/PythonFiles/ImagesINTOVideo-Python'
output_folder = 'c:/Users/raina/Desktop/PythonFiles/ImagesINTOVideo-Python'
video_path = os.path.join(output_folder, 'ItoV.avi')
audio_path = 'C:/Users/raina/Desktop/PythonFiles/ImagesINTOVideo-Python/FROZEN.mp3'  # Your audio file

output_video_with_audio = os.path.join(output_folder, 'video_with_audio.mp4')

# Retrieve and sort images
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])
if not images:
    print("No images found in the specified folder.")
    exit()

# Read the first image to get video dimensions
first_frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = first_frame.shape

# Define the codec and create a VideoWriter object
video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height))

# Add each image to the video
for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    video.write(frame)

# Release the VideoWriter
cv2.destroyAllWindows()
video.release()

print(f"Video saved as {video_path}")

# Get video duration
video_clip = VideoFileClip(video_path)
video_duration = video_clip.duration  # Duration in seconds

# Load and trim audio to video duration
audio_clip = AudioFileClip(audio_path).subclip(0, video_duration)
video_clip_with_audio = video_clip.set_audio(audio_clip)

# Save the final video with audio
video_clip_with_audio.write_videofile(output_video_with_audio, codec="libx264")

print(f"Video with audio saved to: {output_video_with_audio}")

