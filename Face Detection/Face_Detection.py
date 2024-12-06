import cv2

img=cv2.imread("C:/Users/raina/Desktop/PythonFiles/IMG_20170402_192520.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


face_cascade=cv2.CascadeClassifier('C:/Users/raina/Desktop/PythonFiles/haarcascade_frontalface_default.xml')

faces=face_cascade.detectMultiScale(gray,1.1,3)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)