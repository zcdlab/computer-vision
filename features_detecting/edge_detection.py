# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:37:54 2018

@author: Administrator
"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Laplacian, sobel, canny respectively
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    canny_edge = cv2.Canny(frame, 200, 200)
    
    cv2.imshow('origin', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('canny', canny_edge)

    k = cv2.waitKey(33) & 0xFF
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print (k) # else print its value

cap.release()
cv2.destroyAllWindows()