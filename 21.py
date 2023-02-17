import cv2
import numpy as np

img = cv2.imread("bit1.jpg")

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

showImage(img,"Main Image")

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
cv2.drawContours(img, [cnt], 0, (0,0,255), 2)

showImage(img,"Contours Image")

x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print("Aspect Ration=",aspect_ratio)

area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area
print("Extent = ",extent)

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print("Solidity = ",solidity)

equi_diameter = np.sqrt(4*area/np.pi)
print("Equivalent Diameter = ",equi_diameter)

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
print("Orientation= x y MA ma angle",x,y,MA,ma,angle)

mask = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
print("Mask and Pixel Points",pixelpoints.dtype)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray,mask = mask)
print("Maximum Value, Minimum Value and their locations")
print("Max val:",max_val)
print("Min val:",min_val)
print("Max Loc:",max_loc)
print("Min Loc",min_loc)

mean_val = cv2.mean(img,mask = mask)
print("Mean Color or Mean Intensity",mean_val)

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print("Extreme Points")
print("leftmost",leftmost)
print("rightmost",rightmost)
print("topmost",topmost)
print("bottommost",bottommost)

cv2.destroyAllWindows()