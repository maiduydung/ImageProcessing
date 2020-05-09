import cv2
import numpy as np

img = cv2.imread('resources/luna.jpg')
imgHor = np.hstack((img, img))
imgVer = np.vstack((imgHor, imgHor))



cv2.imshow("Image", imgVer)


cv2.waitKey(0)