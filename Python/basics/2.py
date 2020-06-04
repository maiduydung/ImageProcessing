import cv2
import numpy as np

img = cv2.imread("resources/eva.jpg")
print('shape ',img.shape)
imgResize = cv2.resize(img, (400*3, 525*3))




cv2.imshow("", imgResize)
cv2.waitKey(0)