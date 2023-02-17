import cv2

img1 = cv2.imread("img2.jpg")
img2 = cv2.imread("img3.jpg")


def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

def resizeImage(img):
    x = img.shape[0]
    y = img.shape[1]
    #print(x , y)
    resize_image = cv2.resize(img,(562,375),fx=1,fy=1)
    return resize_image

img1 = resizeImage(img1)
img2 = resizeImage(img2)

showImage(img1,"Image1")
showImage(img2,"Image2")

img3 = img1-img2
showImage(img3,"Subtraction two images1")

img4 = img2-img1
showImage(img4,"Subtraction two images2")

cv2.destroyAllWindows()