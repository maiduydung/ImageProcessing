import cv2

def empty(num):
    pass


path = 'resources/ocean.jpeg'
cv2.namedWindow("Track_bars")
cv2.resizeWindow("Track_bars", 640, 240)
cv2.createTrackbar("Hue Min", "Track_bars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track_bars", 179, 179, empty)

cv2.createTrackbar("Sat Min", "Track_bars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Track_bars", 255, 255, empty)

cv2.createTrackbar("Val Min", "Track_bars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Track_bars", 255, 255, empty)




img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos("Hue Max", "Track_bars")
    h_max = cv2.getTrackbarPos("Hue Min", "Track_bars")
    s_min = cv2.getTrackbarPos("Sat Max", "Track_bars")
    s_max = cv2.getTrackbarPos("Sat Min", "Track_bars")
    val_min = cv2.getTrackbarPos("Val Max", "Track_bars")
    val_max = cv2.getTrackbarPos("Val Min", "Track_bars")

    print(h_min, h_max, s_min, s_max, val_min, val_max)

    cv2.imshow('Original', img)
    cv2.imshow('HSV', imgHSV)
    cv2.waitKey(1)