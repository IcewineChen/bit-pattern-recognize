#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/11
@File: histogram.py
@Project: pattern-recognize
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
path = os.path.join('../images')
if os.path.exists(path):
    files = os.listdir(path)
'''
def histogram():
    #encoding
    img = cv2.imread('../images/non-enough.jpg', 0)
    cv2.imwrite('../images/gray-non-enough.jpg',img)
    #hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    #numpy for histogram: slower than cv2.calcHist
    #hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    hist, bins = np.histogram(img.flatten(),256,[0,256])

    #numpy for normalizing
    cdf = hist.cumsum()     #calculate cumsum of the image
    cdf_normalized = cdf * hist.max()/cdf.max() #normalized
    cdf_min = np.ma.masked_equal(cdf,0)
    cdf_min = (cdf_min - cdf_min.min())*255 / (cdf_min.max()-cdf_min.min())
    cdf = np.ma.filled(cdf_min,0).astype('uint8')
    #dst = cdf[img]

    equ = cv2.equalizeHist(img)
    dst = np.hstack((img, equ))
    cv2.imwrite('../images/after_histogram.jpg',dst)
    #plot

    plt.subplot(211),plt.plot(cdf_normalized, color='b')
    plt.hist(dst.flatten(),256,[0,256],color='r')
    plt.title('histogram')
    #plt.hist(img.flatten(),256,[0,256],color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.subplot(212),plt.imshow(dst,cmap='gray')
    plt.title('after equalization')
    plt.show()
