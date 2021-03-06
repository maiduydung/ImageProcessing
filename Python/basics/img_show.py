#load and print image
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../resources/cards.jpg')
plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()