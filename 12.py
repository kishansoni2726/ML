import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not open")

while cap.isOpened():
    ret, frame = cap.read()
    
    img = cv2.flip(frame,1)
    cv2.imshow("Camera",img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()