# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:50:50 2018

@author: Administrator
"""

import cv2

def Image_Reader(filename, to_grey=False):
    img = cv2.imread(filename)

    assert img is not None , "file (%s) is not exist." % (filename)

    if(to_grey is True):
        img= cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    return img
 
def Image_Renderer(img_arr):
    cv2.imshow('image', img_arr)
    
if __name__ is '__main__':
    filename = "../_images/grid.jpg"
    img = Image_Reader(filename)
    Image_Renderer(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    img = Image_Reader(filename, to_grey=True)
    Image_Renderer(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()