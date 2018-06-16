# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:51:36 2018

@author: Administrator
"""

import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

img = cv2.imread('../_images/lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
for(fx, fy, fw, fh) in faces:
    roi_face = gray[fy:fy+fh, fx:fx+fw]
    roi_face_color = img[fy:fy+fh, fx:fx+fw]
    
    cv2.rectangle(img, (fx,fy), (fx+fw, fy+fh), (255, 0, 0), 2)
    cv2.putText(img,'face', (fx, fy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    eyes = eye_cascade.detectMultiScale(roi_face)
    
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        cv2.putText(roi_face_color,'eye', (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
cv2.imshow('img', img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()