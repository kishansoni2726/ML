import numpy as np
import cv2

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

row, col = img.shape[:2]
bottom = img[row-2:row, 0:col]

bordersize = 20
border = cv2.copyMakeBorder(img,10,20,30,40,cv2.BORDER_CONSTANT,None,[255, 0, 255])

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    
showImage(img,'image')
showImage(border,'border')
cv2.destroyAllWindows()