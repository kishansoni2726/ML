import cv2

img = cv2.resize(cv2.imread("img3.jpg"),(0,0),fx=0.1,fy=0.1)

def showImage(img,name="image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)


def manHattenDistance(x1,y1,x2,y2):
    return (abs(x1-x2)+abs(y1-y2))

def euclidianDistance(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5

showImage(cv2.line(img, (100,200), (300,400), (0,0,255), 1),"Distance")

print("Manhatten Distance",manHattenDistance(100,200,300,400))

print("Euclidian Distance",euclidianDistance(100,200,300,400))

cv2.destroyAllWindows()