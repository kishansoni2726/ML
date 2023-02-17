import cv2 
import numpy as np
 
img = cv2.imread('img3.jpg',0)   #gray
img = cv2.resize(img,(300,300))
equ = cv2.equalizeHist(img)
after = np.hstack((img,equ))      #double quate
# cv2.imwrite('after.jpg',after)
cv2.imshow('input',img)
cv2.imshow('output',after)

cv2.waitKey(0)
cv2.destroyAllWindows()