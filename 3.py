import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

showImage(img,"Image")

img2 = np.copy(img[275:350,350:550])
img[275:350,350:550]=0
showImage(img,"Image")
showImage(img2,"ROI")

cv2.destroyAllWindows()