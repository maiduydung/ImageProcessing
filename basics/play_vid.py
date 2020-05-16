import numpy as np
import cv2

cap = cv2.VideoCapture('test_vid.mkv')

while(cap.isOpened()):
    ret, frame = cap.read()
    #grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()