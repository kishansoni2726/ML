import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r"C:\\Users\\91898\\anaconda3\\Lib\site-packages\\cv2\data\\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\\Users\\91898\\anaconda3\\Lib\site-packages\\cv2\data\\haarcascade_smile.xml")

img = cv2.resize(cv2.imread("img4.jpg"),(0,0),fx=0.5,fy=0.5)

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

faces = face_cascade.detectMultiScale(img,1.3,5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color = img[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(img,1.8,20)

    for(sx,sy,sw,sh) in smiles:
        img = cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    
showImage(img)

cv2.destroyAllWindows()