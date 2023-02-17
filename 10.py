import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

def pixelval(pix,r1,r2,s1,s2):
    if(pix>0 and pix<=r1):
        return 0
    elif(pix > r1 and pix <= r2):
        return ((s2-s1)/(r2-r1)) * (pix-r1) + s1
    else :
        return 0

pix_vactor = np.vectorize(pixelval)
pix_img = pix_vactor(img,70,140,0,255)
showImage(pix_img)

cv2.destroyAllWindows()