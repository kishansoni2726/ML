import cv2
import numpy as np

img = cv2.imread("hand.png")

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

showImage(img)

print("Moments")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print("cx : ",int(M['m10']/M['m00'])) 
print("cy :",int(M['m01']/M['m00']))

print("Contour Area")
area = cv2.contourArea(cnt)
print("Area : ",area)

print("Contour Perimeter")
perimeter = cv2.arcLength(cnt,True)
print("Perimeter : ",perimeter)

for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (0,255,255), 2)
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img, [approx], 0, (0,0,255), 2)
showImage(img,"Contour Approximation")

for cnt in contours:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], 0, (255,0,0), 2)
showImage(img,"Convex Hull")

k = cv2.isContourConvex(cnt)
print(k)

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
showImage(img,"Straight Bounding Rectangle")

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (255,0,255), 2)
showImage(img,"Rotated Rectangle")

for cnt in contours:
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,150,255),2)
showImage(img,"Minimum Enclosing Circle")

for cnt in contours:
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img,ellipse,(200,200,200),2)
showImage(img,"Fitting an Ellipse")

for cnt in contours:
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(255,255,0),2)
showImage(img,"Fitting a Line")
cv2.destroyAllWindows()