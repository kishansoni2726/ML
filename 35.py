import cv2

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

img = cv2.imread('document.jpg')
showImage(img,"Main Image")

showImage(cv2.line(img.copy(),(100,100),(300,300),(0,0,255),2),"Line Image")
showImage(cv2.arrowedLine(img.copy(),(300,300),(600,300),(0,255,0),3),"Arrow segment")
showImage(cv2.ellipse(img.copy(),(600,600),(200,50),90,0,270,(255,0,0),-1),"Eclipse")
showImage(cv2.circle(img.copy(),(600,600),100,(0,255,255),3),"Circle")
showImage(cv2.rectangle(img.copy(),(300,300),(600,600),(255,255,0),3),"Rectangle")
showImage(cv2.putText(img,"Hello World!",(400,600),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,4,(255,0,255),3),"Text eleving")

cv2.destroyAllWindows()