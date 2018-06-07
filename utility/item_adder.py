# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:21:06 2018

@author: Administrator
"""

import cv2
import read_image

def Set_Items(image=None, items=[]):
    new_img = image.copy()
    
    for index, item in enumerate(items):
        print(item)
        new_img.itemset((item[1], item[0], index), item[2])

    return new_img

if __name__ is '__main__':
    filename = "../_images/grid.jpg"
    img = read_image.Image_Reader(filename)
    read_image.Image_Renderer(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    item_list = [[1, 2, 100], [1, 3, 100], [1, 4, 100], [1, 5, 100]]
    new_img = Set_Items(img, item_list)
    read_image.Image_Renderer(new_img)
    print(new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
