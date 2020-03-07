# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:41:10 2018

@author: hp
"""

import pytesseract
#from pytesseract import image_to_string
import cv2
import numpy as np
import os
from PIL import Image

img = cv2.imread('thres.jpg', 0)
img = cv2.imread(os.path.normcase(os.path.join(os.getcwd(), 'thres.jpg')),0)
#cv2.imshow('image',img)
print(os.path.normcase(os.path.join(os.getcwd(), 'thres.jpg')))
cv2.waitKey(0)
img = cv2.resize(img, (80, 30))
img = img.transpose(1, 0)
img = img.reshape((80 * 30))
img = np.multiply(img, 1/255.0)

cv2.destroyAllWindows()
#print(np.fromstring(img.getvalue(), dtype='uint8'))
#print(pytesseract.image_to_string(img))
#print(os.getcwd())

#Path to image folder    
src_path = "C:\\Users\\hp\\Desktop\\"

#Run OCR on image    
#text = pytesseract.image_to_string(Image.open(src_path + "thres.jpg"))

#Print OCR result
#print (text)
from PIL import Image
import pytesseract
tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
TESSDATA_PREFIX= 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata'
tessdata_dir_config = 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata\\configs'
words = pytesseract.image_to_string( Image.open('C:\\Users\\hp\\Desktop\\power.png'), lang='eng', config=tessdata_dir_config)
f = open('helloworld.txt','w',encoding='utf-8')
f.write(words)
f.close()
print(words)
