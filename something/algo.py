# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:23:10 2018

@author: hp
"""
from PIL import Image
import pytesseract
import cv2
import numpy as np

src_path = 'C:/Users/hp/Desktop/'

def get_string(img_path):
    img = cv2.imread(img_path,0)
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    
    cv2.imwrite(src_path+"without_noise.jpg", img)
    result = src_path + "without_noise.jpg"
    return result

image = 'words.jpg'
tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
TESSDATA_PREFIX= 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata'
tessdata_dir_config = 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata\\configs'
words = pytesseract.image_to_string( Image.open(get_string(src_path+image)), lang='eng', config=tessdata_dir_config)
print(src_path+image)
print(words)