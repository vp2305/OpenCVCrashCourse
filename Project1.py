import cv2
import numpy as np

# function that reads video, image is "imread"
# method to show the image is "imshow"
frameWidth = 640
frameHeight = 780

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Red, green and orange
myColors = [
    [0, 0, 146, 104, 81, 255],
    [0, 87, 0, 77, 146, 77],
    [0, 0, 156, 80, 94, 255]
]
# BGR
myColorValues = [
    [0, 0, 255],
    [0, 255, 0],
    [0, 128, 255]
]

# 3 values x, y, colorId per index
myPoints = []


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img, lower, upper)
        x, y = getContors(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[4]), mask)
    return newPoints


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]),
                   10, myColorValues[point[2]], cv2.FILLED)


def getContors(img):
    contors, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contors:
        area = cv2.contourArea(cnt)
        if (area > 500):
            # cv2.drawContours(imgResult, cnt, -1, (210, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y


while True:
    success, img = cap.read()
    if (success):
        imgResult = img.copy()
        newPoints = findColor(img, myColors, myColorValues)
        if (len(newPoints) != 0):
            for newP in newPoints:
                myPoints.append(newP)

        if (len(myPoints) != 0):
            drawOnCanvas(myPoints, myColorValues)
        cv2.imshow("Cam Feed", imgResult)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
