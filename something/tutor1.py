# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:08:43 2018

@author: hp
"""
# Import numpy and OpenCV
import numpy as np
import cv2 
 # Load a color image in BGR
img = cv2.imread('words.jpg',1)
 # Find the number of rows in the image
print("imgRows = ",img.shape[0])
 # Find the number of columns in the image
print("imgCols = ",img.shape[1])
 # Find the number of channels in the image
print(img.shape[2])
cropped = img[200:600,200:500]

#cv2.imread(cropped)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()