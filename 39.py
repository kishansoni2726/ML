import cv2
import numpy as np

img = cv2.imread("img2.jpg")

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

def imageKMeans(img,k):
    pixel_vals = img.reshape((-1,3))
    pixel_vals = np.float32(pixel_vals)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

    retval, labels, centers = cv2.kmeans(pixel_vals, k,None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape((img.shape))
    showImage(segmented_image,"k = "+str(k))

showImage(img)
for i in range(2,11):
    imageKMeans(img,i)

cv2.destroyAllWindows()