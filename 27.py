import cv2
import numpy as np

img = cv2.imread("object.jpg")

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

showImage(img)

img2 = img.copy()

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray2 = np.float32(gray)
dst = cv2.cornerHarris(gray2,2,3,0.04)
dst = cv2.dilate(dst,None)
img2[dst>0.01*dst.max()]=[0,0,255]
showImage(img2,"Harris Corner")

img3 = img.copy()
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img3,(x,y),3,255,-1)
showImage(img3,"Shi-Thomasi corner")

img4 = img.copy()
sift = cv2.SIFT_create()
kp = sift.detect(gray,None)
img4=cv2.drawKeypoints(gray,kp,img4)
img4=cv2.drawKeypoints(gray,kp,img4,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
showImage(img4,"SIFT")

# img5 = img.copy()
# surf = cv2.xfeatures2d.SURF_create(400)
# kp, des = surf.detectAndCompute(gray,None)
# surf.setHessianThreshold(50000)
# img6 = cv2.drawKeypoints(gray,kp,None,(255,0,0),4)
# showImage(img6,"SURF")

cv2.destroyAllWindows()