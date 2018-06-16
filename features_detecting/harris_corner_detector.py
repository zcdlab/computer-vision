# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:05:37 2018

@author: Administrator
"""

import sys
import cv2
import numpy as np

sys.path.append('../utility/')
import read_image

def corner_detector(img_arr, windows_size=2, k=0.04, reponse_threshold=0):
    new_img_arr = img_arr.copy()
    
    dx, dy = np.gradient(new_img_arr)
    
    """
       E = \sum [dx, dy] [Ixx Ixy] [dx]
                         [Ixy Iyy] [dy]
       
       M = \sum window() * [Ixx Ixy]
                           [Ixy Iyy]
       det M = \sum Ixx * \sum Iyy
       trace M = \sum Ixx + \sum Iyy
       
       R = det M - k * (trace M ** 2)
    """
    Ixx = dx * dx
    Iyy = dy * dy
    Ixy = dx * dy
    
    width = new_img_arr.shape[1]
    height = new_img_arr.shape[0]
    new_rgb_img_arr = cv2.cvtColor(new_img_arr, cv2.COLOR_GRAY2RGB)
    offset = int(windows_size / 2)
    
    corner_points = []
    
    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            S_Ixx = sum(Ixx[x - offset: x + offset + 1, y - offset: y + offset + 1].ravel())
            S_Ixy = sum(Ixy[x - offset: x + offset + 1, y - offset: y + offset + 1].ravel())
            S_Iyy = sum(Iyy[x - offset: x + offset + 1, y - offset: y + offset + 1].ravel())
            #S_Ixx = np.sum(Ixx[x - offset : x + offset, y - offset : y + offset])
            #S_Iyy = np.sum(Iyy[x - offset : x + offset, y - offset : y + offset])
            #S_Ixy = np.sum(Ixy[x - offset : x + offset, y - offset : y + offset])
            
            determinant = (S_Ixx * S_Iyy) - (S_Ixy ** 2)
            trace = S_Ixx + S_Iyy
            
            response = determinant - k * (trace ** 2)

            if(response - reponse_threshold > 0):
                corner_points.append([x, y, response])
                cv2.circle(new_rgb_img_arr, (y, x), 1, (0, 0, 255), -1)
                
    return new_rgb_img_arr, corner_points

if __name__ is '__main__':
    #filename = '../_images/grid.jpg'
    filename = '../_images/checkerboard.png'
    img_arr = read_image.Image_Reader(filename,to_grey=True)
    new_img_arr, corner_list = corner_detector(img_arr)
    read_image.Image_Renderer(new_img_arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()