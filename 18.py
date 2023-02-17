import cv2
import numpy as np

img = cv2.imread("bin.png",0)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

kernel = np.ones((3,3),np.uint8)
dilate = cv2.dilate(img,kernel,iterations=16)
Erosion  = cv2.erode(img,kernel,3)

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

showImage(img,"Main Image")
showImage(dilate,"Dilation image")

cv2.destroyAllWindows()