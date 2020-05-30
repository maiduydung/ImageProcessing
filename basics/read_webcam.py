import cv2 
import numpy as np

capture = cv2.VideoCapture(0)

# if(not capture.isOpened()):
#     print("Error opening")

while(capture.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()