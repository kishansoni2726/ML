import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.imwrite("output/program10"+name+".jpg",img)
    cv2.waitKey(0)

showImage(img)

pUp = cv2.pyrUp(img)
showImage(pUp,"Pyramid Up/ Laplacian Pyramid")

pDown = cv2.pyrDown(img)
showImage(pDown,'Pyramid Down / Gaussian Pyramid')

cv2.destroyAllWindows()