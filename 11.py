import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)
bck = cv2.resize(cv2.imread("img3.jpg",0),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

bitAnd = cv2.bitwise_and(img,hsv, mask= mask)
bitNot = cv2.bitwise_not(img,hsv, mask= mask)
bitOr = cv2.bitwise_or(img,hsv, mask= mask)
bitXor = cv2.bitwise_xor(img,hsv, mask= mask)

showImage(img,"Main Image")
showImage(mask,'mask')
showImage(bitAnd,'Bitwise And')
showImage(bitOr,'Bitwise Or')
showImage(bitNot,'Bitwise Not')
showImage(bitXor,'Bitwise Xor')

cv2.destroyAllWindows()