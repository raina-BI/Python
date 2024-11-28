"""
# python program to detect pedestrians on a video using OpenCV's Histogram of Oriented Gradients (HOG) descriptor 
  along with a pretrained Support Vector Machine (SVM) specifically optimized for pedestrian detection.
@author: raina

"""
import cv2
import imutils

# Initialize the video capture
video_path = "c:/Users/raina/Desktop/PythonFiles/walking.avi"  # Replace with your video path
vid = cv2.VideoCapture(video_path)

if not vid.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize the HOG descriptor with the pretrained SVM for pedestrian detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Process video frames
while True:
    ret, frame = vid.read()
    if not ret:
        break  # End of video

    # Resize the frame for faster processing (optional)
    frame = imutils.resize(frame, width=min(600, frame.shape[1]))

    # Detect pedestrians in the frame
    (regions, _) = hog.detectMultiScale(frame, 
                                        winStride=(4, 4),
                                        padding=(8, 8),
                                        scale=1.05)
    
    # Draw bounding boxes around detected pedestrians
    for (x, y, w, h) in regions:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detections
    cv2.imshow("Pedestrian Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video and close all OpenCV windows
vid.release()
cv2.destroyAllWindows()
