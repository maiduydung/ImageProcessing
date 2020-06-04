import cv2
import numpy as np



img = cv2.imread('../../resources/man2.jpg')
img2 = cv2.imread('../../resources/man3.jpg')

#opencv addition = saturated operation
    #I(x,y) = min(max(round(result), 0), 255)
cv_add = cv2.add(img, img2)
weighted = cv2.addWeighted(img, 0.5, img2, 0.5, 50)

#numpy addition
add =  img + img2



cv2.imshow("add", add)
cv2.imshow("cv_add", cv_add)
cv2.imshow("weighted", weighted)



cv2.waitKey(0)
cv2.destroyAllWindows()
