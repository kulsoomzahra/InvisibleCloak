import cv2
import numpy as np

# Reading from video(input)
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, back = cap.read()
    if ret:
        img = cv2.imread('image.png', 0)
# Refining the mask corresponding to the detected red color
# removing noises
        kernel = np.ones( (32,32), np.uint8)

        erosion = cv2.erode(img, kernel, iterations=1)

        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# Mapping
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.png', back)
            break
cap.release()
cv2.destroyAllWindows()