# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:34:03 2018

@author: hp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('digits.png')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Load the data, converters convert the letter to a number
data= np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',',
                    converters= {0: lambda ch: ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.KNearest()
knn.train(trainData, responses)
ret, result, neighbours, dist = knn.find_nearest(testData, k=5)

# Find an accuracy of model to evaluate 
correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print (accuracy)
