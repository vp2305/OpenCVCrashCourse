import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier(
    "Resource/haarcascades/haarcascade_frontalface_default.xml")
img = cv.imread("Resource/lena.png")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv.imshow("Lena", img)
cv.waitKey(0)
