# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:00:47 2018

@author: Administrator
"""

import cv2
import numpy as np

IMAGE_DIR = "./images/"
image = 'grid.jpg'

img = cv2.imread(IMAGE_DIR + image)
width, height, ch = img.shape

# Aad circle points
cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)

ptsl = np.float32([[83, 90], [447,90], [83, 472]])
pts2 = np.float32([[30, 90], [447,90], [83, 472]])

affined_matrix = cv2.getAffineTransform(ptsl, pts2)
affined_img = cv2.warpAffine(img, affined_matrix, (height, width))

cv2.imshow(image, img)
cv2.imshow((image+" affine"), affined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()