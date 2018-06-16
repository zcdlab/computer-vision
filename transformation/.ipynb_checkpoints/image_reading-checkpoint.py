# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:00:47 2018

@author: Administrator
"""

import cv2

IMAGE_DIR = "./images/"
images = ['grid.jpg']
img = []

for index, image in enumerate(images):
    img.append(cv2.imread(IMAGE_DIR + image))
    cv2.imshow(image, img[index])
    
cv2.waitKey(0)
cv2.destroyAllWindows()