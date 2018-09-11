# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:19:12 2018

@author: Administrator
"""

import cv2
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description='Convert image sequences into a video',
                             epilog='Example: python image_sequence_to_video.py  -d D:/_videos/MOT2017/train/MOT17-09-FRCNN/img1 -e .jpg -o D:/output.mp4')
ap.add_argument("-d", "--dir", required=False, default="./", help="image location. Default: ./ ")
ap.add_argument("-e", "--extension", required=False, default="png", help="extension name. Default '.png'")
ap.add_argument("-o", "--output", required=False, default="output.mp4", help="output video file. Default: output.mp4")
args = vars(ap.parse_args())

# Arguments
dir_path = args["dir"]
ext = args["extension"]
output = args["output"]

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)
    print('working on', image_path)
    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))