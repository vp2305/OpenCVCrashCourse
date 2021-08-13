import cv2
import numpy as np

licenceCascade = cv2.CascadeClassifier(
    "Resource/haarcascades/haarcascade_russian_plate_number.xml")

img = cv2.imread("Resource/licencePlate.jpg")
imgResize = cv2.resize(img, (1000, 800))
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

licencePlate = licenceCascade.detectMultiScale(imgGray, 1.1, 4)
minArea = 500

for (x, y, w, h) in licencePlate:
    area = w*h
    if area > minArea:
        cv2.rectangle(imgResize, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(imgResize, "Number Plate", (x, y-10),
                    cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
        imgCropped = imgResize[y:y+h, x:x+w]
        cv2.imshow("Cropped Image", imgCropped)
        cv2.imwrite("Resource/Scanned/NoPlate_licencePlate.jpg", imgCropped)


cv2.imshow("Image", imgResize)
cv2.waitKey(0)
