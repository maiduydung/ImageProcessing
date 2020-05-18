import cv2 
import numpy as np



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + " " + str(y)
        font = cv2.FONT_HERSHEY_PLAIN
        print(strXY)
        cv2.putText(img, strXY, (x,y), font, 1, (0, 0, 0), 1)
        cv2.imshow('img', img)

img = cv2.imread('../resources/man.jpg')
print(img.shape)
cv2.imshow('img', img)

cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 275 225
# 349 261