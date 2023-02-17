import cv2
import numpy as np

def showImage(img,name="Image"):
    cv2.imshow(name,img)
    cv2.waitKey(0)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not open")

kernelx = np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])
kernely = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])

video = cv2.VideoWriter("Temp.mp4",cv2.VideoWriter_fourcc(*'XVID'),20,(640,480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        img = cv2.flip(frame, 1)

        img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        filter = cv2.GaussianBlur(img2, (3, 3), 0)
        sobelx = cv2.Sobel(filter, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(filter, cv2.CV_64F, 0, 1, ksize=5)
        sobel = sobelx + sobely

        prewittx = cv2.filter2D(filter, -1, kernelx)
        prewitty = cv2.filter2D(filter, -1, kernely)

        canny = cv2.Canny(img2, 150, 255 )
        video.write(img)
        cv2.imshow("Camera", img)
        cv2.imshow("Sobel",sobel)
        cv2.imshow("PrewittX",prewittx)
        cv2.imshow("PrewittY",prewitty)
        cv2.imshow("Canny",canny)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
video.release()


cv2.destroyAllWindows()