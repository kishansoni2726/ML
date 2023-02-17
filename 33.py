import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r"C:\\Users\\91898\\anaconda3\\Lib\site-packages\\cv2\data\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\\Users\\91898\\anaconda3\\Lib\site-packages\\cv2\data\\haarcascade_eye.xml")

img = cv2.resize(cv2.imread("img4.jpg"),(0,0),fx=0.5,fy=0.5)

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

faces = face_cascade.detectMultiScale(img,1.3,5)
for (x,y,w,h) in faces:
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(img)

    for(ex,ey,ew,eh) in eyes:
        img = cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
showImage(img)

cv2.destroyAllWindows()