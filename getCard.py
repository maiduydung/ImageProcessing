import cv2
import numpy as np

img = cv2.imread('resources/cards.jpg')

#maintaining 2.5/3.5 ratio
width, height = 250, 350

#original img
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

#cropped
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOut)

cv2.waitKey(0)

