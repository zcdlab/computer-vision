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

    k = cv2.waitKey(33)
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value
    
cap.release()
out.release()
cv2.destroyAllWindows()