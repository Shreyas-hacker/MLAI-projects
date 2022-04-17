import cv2
import os
import PIL
import numpy as np
from PIL import Image
from cv2 import threshold

for i in range(0,10):
    directory = f'C:/Users/shrey/OneDrive - Nanyang Technological University/Desktop/MLAI projects/DigitRecog/Dataset/testSet/{i}'
    new_direc = 'C:/Users/shrey/OneDrive - Nanyang Technological University/Desktop/MLAI projects/DigitRecog/Dataset/testSet/testSet/'
    count = 1
    for image in os.listdir(directory):
        image_path = os.path.join(directory, image)
        img = cv2.imread(image_path)

        img_size = cv2.resize(img,(28,28))
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray,(3,3), 0)

        edges = cv2.Canny(image=img_blur, threshold1=100,threshold2=200)
        file = new_direc + f'{i}_img({count}).jpeg'
        count+=1
        image_tosave = Image.fromarray(edges.astype(np.uint8))
        image_tosave.save(file, 'JPEG')

cv2.destroyAllWindows()