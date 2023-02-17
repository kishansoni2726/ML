import cv2

img1 = cv2.imread("img3.jpg")

img = cv2.resize(img1,(0,0),fx=0.3,fy=0.3)
img = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("output/new_Image_program2.jpg",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
