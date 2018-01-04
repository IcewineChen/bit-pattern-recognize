#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/11
@File: dft_dct.py
@Project: pattern-recognize
'''
import cv2
import numpy as np
from skimage import data,color
import skimage.filters.rank as sfr
import matplotlib.pyplot as plt

import os
import sys

'''
path = os.path.join('../images')
if os.path.exists(path):
    files = os.listdir(path)
'''
def dft_dct():
    #encoding
    #img = cv2.imread('../images/lena.jpg', 0)
    #img = cv2.resize(img, (240, 360))
    img = data.chelsea()
    img = color.rgb2gray(img)
    #do dft
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum_dft = 20 * np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    #or use numpy:
    #magnitude_spectrum_dft = 20*np.log(np.abs(dft_shift))

    #do dct
    dct = cv2.dct(np.float32(img))
    dct_img = np.log(abs(dct))

    #plot
    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(magnitude_spectrum_dft, cmap='gray')
    plt.title('DFT Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(dct_img, cmap='gray')
    plt.title('DCT result'), plt.xticks([]), plt.yticks([])
    plt.show()
