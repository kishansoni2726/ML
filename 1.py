
import cv2

img1 = cv2.imread("img3.jpg",0)
img2 = cv2.imread("img3.jpg",1)

img = cv2.resize(img1,(0,0),fx=0.5,fy=0.5)
cv2.imshow("output/new_Image_program1.jpg",img)
cv2.waitKey(0)

img = cv2.resize(img2,(0,0),fx=0.5,fy=0.5)
cv2.imshow("output/new_Image_program1_2.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
