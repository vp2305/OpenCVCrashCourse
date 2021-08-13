"""
Title: Document Scanner
"""
import cv2
import numpy as np

width = 640
height = 780


def preProcessing(img):
    imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDilate, kernel, iterations=1)
    return imgThreshold


def getContors(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    maxCnt = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > maxArea):
            maxArea = area
            maxCnt = cnt
    peri = cv2.arcLength(maxCnt, True)
    approx = cv2.approxPolyDP(maxCnt, 0.02*peri, True)
    if (len(approx) == 4):
        cv2.drawContours(imgContors, maxCnt, -1, (0, 255, 0), 3)
        cv2.drawContours(imgContors, approx, -1, (0, 255, 0), 15)
    return approx


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    sumValues = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(sumValues)]
    myPointsNew[3] = myPoints[np.argmax(sumValues)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img, biggest_approx):
    biggest_approx = reorder(biggest_approx)
    pts1 = np.float32(biggest_approx)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    finalImg = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    finalImageCropped = cv2.resize(finalImg, (width, height))
    return finalImageCropped


img = cv2.imread("Resource/1.jpg")
imgResize = cv2.resize(img, (width, height))
imgContors = imgResize.copy()
imgThreshold = preProcessing(imgResize)
biggest_approx = getContors(imgThreshold)
cv2.imshow("Contors", imgContors)
if biggest_approx.size != 0:
    imgOutput = getWarp(imgResize, biggest_approx)
    # cv2.imshow("Original Image", imgThreshold)
    cv2.imshow("Image Output", imgOutput)
cv2.waitKey(0)
