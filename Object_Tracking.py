import cv2

# object tracking algorithms: KCF,MOSSE,Medianflow, CSRT
video= cv2.VideoCapture("C:/Users/raina/Desktop/PythonFiles/bb3.mp4")

# load tracker
tracker=cv2.TrackerCSRT_create()
# Read the first frame of the video
returned, img=video.read()
# Select the bounding box(ROI) on the image
bbox=cv2.selectROI("Tracking",img,False)

# initialise tracker
tracker.init(img,bbox)
print(bbox)

def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(80,80), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

while True:
    check, img=video.read()

    #update the tracker on img and the bounding box
    success, bbox=tracker.update(img)

    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"Lost",(80,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    cv2.imshow("result",img)
    key=cv2.waitKey(25)
    if key==32:
        print("stopped")
        break

video.release()
cv2.destroyAllWindows()