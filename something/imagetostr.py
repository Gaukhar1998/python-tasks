# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:46:37 2018

@author: hp
"""

#import pytesseract
##import cv2 as cv
#from PIL import Image, ImageEnhance, ImageFilter
#
#im = Image.open("opencv_logo.jpg") # the second one 
#im = im.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#im.save('temp2.jpg')
##img = cv.imread('temp2.jpg')
#text = pytesseract.image_to_string(Image.open('C:/Users/hp/Desktop/temp2.jpg'))
#print(text)

from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('another.png'))
print(text)