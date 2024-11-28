"""
# python program to capture video from a specified video file path and displays it
@author: raina
"""

import cv2

#vid=cv2.VideoCapture(0)

vid=cv2.VideoCapture("D:/Photo/VIDEOS BKP/InShot_20210718_220337309.mp4")

if(vid.isOpened()==False):
    print("unable to read the feed")

height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps= int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):
    ret,frame=vid.read()
    cv2.imshow("video display", frame)
    if cv2.waitKey(20)==32:  # 32 is ASCII code of space key
     break

cv2.destroyAllWindows()