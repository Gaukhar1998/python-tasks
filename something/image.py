# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:06:23 2018

@author: hp
"""

from PIL import Image
import pytesseract
#import subprocess
#import cv2
#import os

#image = cv2.imread("cisco 2/example.jpg")
#import Image
#from tesseract import image_to_string
#print(os.getcwd())
#print (pytesseract.image_to_string(Image.open('C://Users//hp//Desktop//image.jpg')))
print (pytesseract.image_to_string(Image.open('life.png')))
#print (pytesseract.image_to_string(Image.open('test-english.jpg'), lang='eng'))