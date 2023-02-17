import cv2

img1 = cv2.imread("bit1.jpg",0)
img2 = cv2.imread("bit2.jpg",0)

def showImage(img,name="image"):
    cv2.imshow(name,cv2.resize(img,(0,0),fx=0.3,fy=0.3))
    cv2.waitKey(0)

showImage(img1,"Image1")

showImage(img2,"Image2")

anding = cv2.bitwise_and(img1,img2)
showImage(anding,"And condition")

orCondintion = cv2.bitwise_or(img1,img2)
showImage(orCondintion,"Or Condintion")

notCondintion = cv2.bitwise_not(img1)
showImage(notCondintion,"Not Condintion")

xorCondintion = cv2.bitwise_xor(img1,img2)
showImage(xorCondintion,"Xor Condintion")

cv2.destroyAllWindows()