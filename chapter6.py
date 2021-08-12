import cv2
import numpy as np

# Both of them have to have some number of channels

img = cv2.imread("Resource/lena.png")

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)
