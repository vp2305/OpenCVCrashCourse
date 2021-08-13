import cv2
import numpy as np


frameWidth = 680
frameHeight = 780
camFeed = cv2.VideoCapture(0)
camFeed.set(2, frameWidth)
camFeed.set(3, frameHeight)
camFeed.set(10, 150)


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
    cv2.imshow("Mask Result", mask)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask Result", imgResult)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, filterChange)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, filterChange)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, filterChange)
cv2.createTrackbar("Sat Max", "TrackBars", 225, 255, filterChange)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, filterChange)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, filterChange)

while True:
    success, img = camFeed.read()
    if (success):
        filterChange(img)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("Cam Feed", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
