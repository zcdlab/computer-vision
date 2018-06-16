# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:21:37 2018

@author: Administrator
"""

import cv2
import numpy as np

img = cv2.imread('../_images/dark_image.jpg')

mask = np.zeros(img.shape[:2], np.uint8)

bg_model = np.zeros((1, 65), np.float64)
fg_model = np.zeros((1, 65), np.float64)

rect = (0, 0, img.shape[0], img.shape[1])

cv2.grabCut(img, mask, rect, bg_model, fg_model, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
img_ext = img * mask2[:, :, np.newaxis]

cv2.imshow('img', img)
cv2.imshow('img_ext', img_ext)

cv2.waitKey(0)
cv2.destroyAllWindows()