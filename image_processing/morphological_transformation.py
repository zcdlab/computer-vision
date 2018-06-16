# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:26:25 2018

@author: Administrator
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([50, 50, 50])
    upper_red = np.array([255, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('origin', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    k = cv2.waitKey(33)
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value
    
cv2.destroyAllWindows()
cap.release()