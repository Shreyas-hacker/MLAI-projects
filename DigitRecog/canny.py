import cv2
import os
from cv2 import threshold

directory = 'C:/Users/shrey/OneDrive - Nanyang Technological University/Desktop/MLAI projects/DigitRecog/Dataset/trainingSet/trainingSet/0'
count = 1
for image in os.listdir(directory):
    image_path = os.path.join(directory, image)
    img = cv2.imread(image_path)
    cv2.imshow('Original',img)
    cv2.waitKey(0)

    img_size = cv2.resize(img,(28,28))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray,(3,3), 0)

    edges = cv2.Canny(image=img_blur, threshold1=100,threshold2=200)
    file = directory + f'0_img({count})'
    count+=1
    cv2.imread(file,edges)
    cv2.waitKey(0)

cv2.destroyAllWindows()