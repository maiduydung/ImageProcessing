import cv2
import numpy as np

img = cv2.imread('../resources/man.jpg')
#w, h, and channel
print("shape: ",img.shape)

print("number of pixel: ",img.size)
print("type: ", img.dtype)


ball = img[280:340, 330:390]
print("ball ",ball)
img[273:333, 000:60] = ball



cv2.imshow('image', img)
cv2.waitKey(0)


# 552 292
# 668 405