"""
# python program to capture video from a webcam or a specified video file path and displays it
@author: raina
"""

import cv2

# Load Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start video capture from the default webcam
vid = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = vid.read()

    # Convert frame to grayscale (Haar cascades work better on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw rectangle around each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0),1)

        # Get the region of interest (ROI) for eye detection within the face rectangle
        face_roi_gray = gray[y:y + h, x:x + w]
        face_roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))

        for (ex, ey, ew, eh) in eyes:
            # Draw rectangle around each eye within the face ROI
            cv2.rectangle(face_roi_color, (ex, ey), (ex + ew, ey + eh), (0, 250, 0), 1)

    # Display the output frame with face and eye detection
    cv2.imshow("Live Face and Eye Detection", frame)

    # Press space bar to exit the live feed
    if cv2.waitKey(25)==32:
        break

# Release the webcam and close all OpenCV windows
vid.release()
cv2.destroyAllWindows()
