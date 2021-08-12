import cv2
import numpy as np
# Detect color
# we can use trackbars to play around with value so that we can find the optimal min and max values of the color


def filterChange(_):
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask Result", imgResult)


path = "Resource/lambo.png"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, filterChange)
cv2.createTrackbar("Hue Max", "TrackBars", 87, 179, filterChange)
cv2.createTrackbar("Sat Min", "TrackBars", 14, 255, filterChange)
cv2.createTrackbar("Sat Max", "TrackBars", 227, 255, filterChange)
cv2.createTrackbar("Val Min", "TrackBars", 161, 255, filterChange)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, filterChange)

img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original image", img)
cv2.imshow("HSV Image", imgHSV)

cv2.waitKey(0)
