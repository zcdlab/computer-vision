# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:49:50 2018

@author: Administrator
"""

import sys
import cv2
import numpy as np

sys.path.append('../utility/')
import read_image

if __name__ is '__main__':
    #filename = '../_images/grid.jpg'
    filename = '../_images/checkerboard.png'
    img_arr = read_image.Image_Reader(filename, to_grey=True)
    corners = cv2.goodFeaturesToTrack(img_arr, 50, 0.01, 10)
    corners = np.int0(corners)
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_GRAY2RGB)
    
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img_arr, (x, y), 3, (0, 0, 255), -1)
    
    read_image.Image_Renderer(img_arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()