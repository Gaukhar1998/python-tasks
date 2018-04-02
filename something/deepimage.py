# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:23:50 2018

@author: hp
"""

#import sys
#import os
import cv2 as cv
import pytesseract
import numpy as np
from PIL import Image

src_path = 'C:/Users/hp/Desktop/'

def get_string(img_path):
    img = cv.imread(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = np.ones((1,1), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)
    img = cv.erode(img, kernel, iterations=1)
    
    cv.imwrite(src_path+"removed_noise.jpg", img)
    img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)
    cv.imwrite(src_path+"thres.jpg",img)
    result = pytesseract.image_to_string(Image.open(src_path + "opencv_logo.jpg"))
    return result

#def main():
#    print('\nDeeptextdetection.py')
#    print('       A demo script of text box alogorithm of the paper:')
#    print('       * Minghui Liao et al.: TextBoxes: A Fast Text Detector with a Single Deep Neural Network https://arxiv.org/abs/1611.06779\n')
#
#    if (len(sys.argv) < 2):
#        print(' (ERROR) You must call this script with an argument (path_to_image_to_be_processed)\n')
#        quit()
#
#    if not os.path.isfile('TextBoxes_icdar13.caffemodel') or not os.path.isfile('textbox.prototxt'):
#        print (" Model files not found in current directory. Aborting")
#        print (" See the documentation of text::TextDetectorCNN class to get download links.")
#        quit()

    #img = cv.imread(str(sys.argv[1]))
print ('--- Start recognize text from image ---')
print (get_string(src_path + "opencv_logo.jpg"))
#    img = cv.imread('C:/Users/hp/Desktop/opencv_logo.jpg')
#    textSpotter = cv.text.TextDetectorCNN_create("textbox.prototxt", "TextBoxes_icdar13.caffemodel")
#    rects, outProbs = textSpotter.detect(img);
#    
#    vis = img.copy()
#    thres = 0.6
#
#    for r in range(np.shape(rects)[0]):
#        if outProbs[r] > thres:
#            rect = rects[r]
#            cv.rectangle(vis, (rect[0],rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 2)
#
#    cv.imshow("Text detection result", vis)
#    cv.waitKey()
#    
#    import goslate
#    gs = goslate.Goslate()
#    print(gs.translate('hello world', 'fr'))
#
#if __name__ == "__main__":
#    main()