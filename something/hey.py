# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:55:36 2018

@author: hp
"""

import cv2
#import numpy as np

img = cv2.imread("example.jpg")
cv2.imshow("Window",img)
cv2.waitKey(5)