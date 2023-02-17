import cv2
import numpy as np

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)
img_translate = img

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

height,width = img.shape[:2]

quarter_height,quarter_width = height/1.5,width/1.5

T = np.float32([[1,0,quarter_width],
               [0,1,quarter_height]])

translate_image = cv2.warpAffine(img,T,(width,height))

showImage(img,"Main Image")
showImage(translate_image,"Transform Image")

cv2.destroyAllWindows()