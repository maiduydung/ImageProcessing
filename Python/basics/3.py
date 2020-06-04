import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

#Height, Width
img[200:300, 100:512] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

cv2.rectangle(img, (0,0), (350, 350), (0,0,255), 2)

cv2.circle(img, (256,256), 200, (214,110,4),3)

cv2.putText(img, "???", (256,256), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

cv2.imshow("", img)
cv2.waitKey(0)