# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:45:01 2018

@author: Administrator
"""

import cv2

cap = cv2.VideoCapture(0)
fg_bg_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    fg_mask = fg_bg_sub.apply(frame)
    
    cv2.imshow('origin', frame)
    cv2.imshow('fg_mask', fg_mask)

    k = cv2.waitKey(33) & 0xFF
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value

cap.release()
cv2.destroyAllWindows()