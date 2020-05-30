import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("before", frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV ) 
        cv2.imshow("after", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

