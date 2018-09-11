# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:20:27 2018

@author: Administrator
"""

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    
    cv2.imshow('gray_frame', gray_frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) >= 0:  # Break with ESC
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()