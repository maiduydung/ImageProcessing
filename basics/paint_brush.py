import cv2
import numpy as np

# if left double click, then circle

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,110,0),-1)

# Create a black image, a window and bind the function to window
#512 x 512 arr, each element is an arr of 3 (RGB channel)
img = np.zeros((512,512,3), np.uint8)
print(img)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()