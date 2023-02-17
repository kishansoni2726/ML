import cv2
import numpy as np

img = cv2.imread("img4.jpg")

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

showImage(img,"Main Image")

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (0,255,255), 1)

showImage(img,"Contours Image")
cv2.destroyAllWindows()