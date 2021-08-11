import cv2

# function that reads video, image is "imread"
# method to show the image is "imshow"
cap = cv2.VideoCapture(0)
cap.set(3, 1800)
cap.set(4, 1800)
cap.set(10, 5000)

while True:
    success, img = cap.read()
    if (success):
        cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
