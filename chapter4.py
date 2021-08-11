# have text or rectangle
import cv2
import numpy as np

img = np.zeros((512, 512, 3),np.uint8)

# Adding color
# img[:] = 200,15,20

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0, 255, 255), 3)

# cv2.FILLED fills the thing
cv2.rectangle(img, (0, 0), (250, 350), (0,0,255), 2)

cv2.circle(img, (450, 20), 20, (15,225,15), 5)

cv2.putText(img, "Hello World!", (165,256), cv2.FONT_HERSHEY_DUPLEX, 1, (0,150,0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)