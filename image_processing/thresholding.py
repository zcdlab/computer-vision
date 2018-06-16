# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:02:32 2018

@author: Administrator
"""

import cv2

img = cv2.imread('./images/dark_image.jpg')
retval1, threshold_RGB_img = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
retval2, threshold_gray_img = cv2.threshold(gray_img, 12, 255, cv2.THRESH_BINARY)

gaussian_thres = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('origin', img)
cv2.imshow('threshold_RGB_img', threshold_RGB_img)
cv2.imshow('threshold_gray_img', threshold_gray_img)
cv2.imshow('gaussian', gaussian_thres)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()