import cv2
import numpy as np

img = cv2.imread("Resource/lena.png")
kernel = np.ones((5,5), np.uint8)

# Gray Image
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image", imgGray)


# Blur the image

# imgBlur = cv2.GaussianBlur(img, (9,9), 0)
# cv2.imshow("Clear Image", img)
# cv2.imshow("Blur Image", imgBlur)

# To determine the edges.

imgCanny = cv2.Canny(img, 100 , 200)
# cv2.imshow("Canny Image", imgCanny)

# Does not detect if the edge has gap between each other it 
# doesn't get detected so we use dilate
# Increases the thickness of the edge

imgDilate = cv2.dilate(imgCanny, kernel,iterations=1 )
# cv2.imshow("Image Dilation", imgDilate)

# Decrease the thickness of the edge
imgEroded = cv2.erode(imgDilate, kernel, iterations= 1)
cv2.imshow("Image Erroded", imgEroded)

cv2.waitKey(0)