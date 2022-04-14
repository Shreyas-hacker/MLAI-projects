import cv2
import os
from cv2 import threshold

directory = 'DigitRecog/Digit'
for image in os.listdir(directory):
    image_path = os.path.join(directory, image)
    img = cv2.imread(image_path)
    cv2.imshow('Original',img)
    cv2.waitKey(0)

    img_size = cv2.resize(img,(28,28))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray,(3,3), 0)

    edges = cv2.Canny(image=img_blur, threshold1=100,threshold2=200)
    cv2.imshow('Canny Edge',edges)
    cv2.waitKey(0)

cv2.destroyAllWindows()