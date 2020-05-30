import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

# if(not capture.isOpened()):
#     print("Error opening")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()