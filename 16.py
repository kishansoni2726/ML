import cv2
import numpy as np

img1 = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

showImage(img1,"Image")

showImage(255-img1,"Image Nagation")

c =100
showImage(np.array(c*np.log(1+img1),dtype=("uint8")),"Log Transformation")

gamma = 0.04
showImage(np.array((255*(img1/255)**gamma),dtype=("uint8")),"Gamma Images")

imgs = [255*((img1 &(1<<i))>>i) for i in range(8)]

for i in range(8):
    showImage(imgs[i],"Bit Image"+str(i))

def pixelval(pix,r1,r2,s1,s2):
    if(pix>0 and pix<=r1):
        return ((s1)/(r1)) * (pix-r1) + s1
    elif(pix > r1 and pix <= r2):
        return ((s2-s1)/(r2-r1)) * (pix-r1) + s1
    else :
        return ((s2)/(r2)) * (pix-r2) + s2

pix_vactor = np.vectorize(pixelval)
pix_img = pix_vactor(img1,70,140,0,255)
showImage(pix_img,"Constrast Stratching")


cv2.destroyAllWindows()