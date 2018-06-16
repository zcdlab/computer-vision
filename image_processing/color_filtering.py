# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 00:04:27 2018

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
    
    
    cv2.imshow('origin', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    k = cv2.waitKey(33)
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value
    
cv2.destroyAllWindows()
cap.release()