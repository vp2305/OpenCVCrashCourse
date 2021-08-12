import cv2
import numpy as np


def getContors(img):
    contors, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contors:
        area = cv2.contourArea(cnt)
        if (area > 500):
            cv2.drawContours(imgContors, cnt, -1, (210, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContors, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContors, objectType,
                        (x+(w//2) - 10, y+(h//2) - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)


img = cv2.imread("Resource/shapes.png")

imgContors = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContors(imgCanny)

imgBlack = np.zeros_like(img)

cv2.imshow("Image", img)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Contors", imgContors)

cv2.waitKey(0)
