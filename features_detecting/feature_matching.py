# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:03:06 2018

@author: Administrator
"""
import sys
import cv2
import numpy as np

sys.path.append('../utility/')
import read_image

if __name__ is '__main__':
    #filename = '../_images/grid.jpg'
    matching_1_a = '../_images/feature_matching_1_a.png'
    matching_1_b = '../_images/feature_matching_1_b.png'
    matching_2_a = '../_images/feature_matching_2_a.jpg'
    matching_2_b = '../_images/feature_matching_2_b.jpg'
    
    matching_1_a_arr = read_image.Image_Reader(matching_1_b, to_grey=True)
    matching_1_b_arr = read_image.Image_Reader(matching_1_b, to_grey=True)
    matching_2_a_arr = read_image.Image_Reader(matching_2_a, to_grey=True)
    matching_2_b_arr = read_image.Image_Reader(matching_2_b, to_grey=True)
    
    orb = cv2.ORB_create()
    
    kp1_a, des1_a = orb.detectAndCompute(matching_1_a_arr, None)
    kp1_b, des1_b = orb.detectAndCompute(matching_1_b_arr, None)
    kp2_a, des2_a = orb.detectAndCompute(matching_2_a_arr, None)
    kp2_b, des2_b = orb.detectAndCompute(matching_2_b_arr, None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    matches_1 = bf.match(des1_a, des1_b)
    matches_2 = bf.match(des2_a, des2_b)
    
    matches_1 = sorted(matches_1, key=lambda x: x.distance)
    matches_2 = sorted(matches_2, key=lambda x: x.distance)
    
    matches_img_1 = cv2.drawMatches(matching_1_a_arr, kp1_a, matching_1_b_arr, kp1_a, matches_1[:30], None, flags=2)
    matches_img_2 = cv2.drawMatches(matching_2_a_arr, kp2_a, matching_2_b_arr, kp2_b, matches_2[:30], None, flags=2)
    
    cv2.imshow('matches_img_1', matches_img_1)
    cv2.imshow('matches_img_2', matches_img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
