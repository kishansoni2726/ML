import cv2

img = cv2.imread("img2.jpg")

cv2.imshow("Full Size Image",img)
cv2.waitKey(0)

img = cv2.resize(img,(0,0),fx=0.2,fy=0.2)
cv2.imshow("Resize Image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()