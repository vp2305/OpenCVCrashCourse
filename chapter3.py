# The x axis is same 
# but the positive y axis is in the down direction.
import cv2

img = cv2.imread("Resource/lambo.png")

# We get (462, 623, 3)
# shape gives us 462 which is height, 623 is width, 3 is BGR
# print(img.shape)

# width first and the height
# imgResize = cv2.resize(img, (1000, 500))


# cv2.imshow("Lambo Image", img)
# cv2.imshow("Lambo Image Resize", imgResize)
# cv2.waitKey(0)

# Here height comes first and then width
imgCropped = img[0:200, 200:600]

cv2.imshow("Image cropper", imgCropped)

cv2.waitKey(0)