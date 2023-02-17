import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

showImage(img,"Image")

def smoothImage(img,n):
    R = np.ones((n,n),np.float32)/(n*n)
    return cv2.filter2D(img,-1,R)

    cv2.fil

showImage(smoothImage(img,1),"Smooth Image1")
showImage(smoothImage(img,2),"Smooth Image2")
showImage(smoothImage(img,3),"Smooth Image3")
showImage(smoothImage(img,4),"Smooth Image4")
showImage(smoothImage(img,5),"Smooth Image5")

cv2.destroyAllWindows()