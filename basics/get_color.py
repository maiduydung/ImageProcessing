import cv2 
import numpy as np


img = cv2.imread('../resources/eva.jpg')

#numpy shape method displays in (y,x) with (0,0) at the top left
print(img.shape)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #blue = 1st channel, and so on
        print("cordinates: ", x, " ", y)

        #had to switch y and x or else we'll have a REALLY messy program
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        print("rgb: ", red, ", ", green, ", ", blue)




cv2.imshow('img', img)

cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
