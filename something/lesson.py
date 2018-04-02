# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:12:37 2018

@author: hp
"""

#import numpy as np
#import cv2 as cv
##Load an color image in grayscale
#cv.namedWindow('image', cv.WINDOW_NORMAL)
#img = cv.imread('parrots.jpg',0)
#cv.imshow('image',img)
#cv.waitKey(0)
#cv.destroyAllWindows()
#
#cv.namedWindow('image', cv.WINDOW_NORMAL)
#img = cv.imread('quokka.png',1)
#cv.imshow('image',img)
#cv.waitKey(0)
#cv.destroyAllWindows()

#cv.namedWindow('IMAGE', cv.WINDOW_NORMAL)
#img = cv.imread('parrots.jpg',0)
#cv.imshow('image',img)
#k = cv.waitKey(0)
#if k == 27:         # wait for ESC key to exit
#    cv.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv.imwrite('parrotsgray.jpg',img)
#    cv.destroyAllWindows()
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('quokka.png',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()