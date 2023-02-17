import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

filter = cv2.GaussianBlur(img2,(3,3),0)

sobelx = cv2.Sobel(filter,cv2.CV_64F,1,0,ksize=5,)
sobely = cv2.Sobel(filter,cv2.CV_64F,0,1,ksize=5)
sobel = sobelx + sobely

kernelx = np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])
kernely = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])
prewittx = cv2.filter2D(filter, -1, kernelx)
prewitty = cv2.filter2D(filter, -1, kernely)

canny = cv2.Canny(img2,150,255,)

showImage(img,"Main Image")
showImage(filter,"Filter")

showImage(sobel,'Sobel')
showImage(prewittx,'Prewittx')
showImage(prewitty,'Prewitty')
showImage(canny,'Canny')

cv2.destroyAllWindows()