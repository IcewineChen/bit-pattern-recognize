#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/12
@File: huffman_decoder.py
@Project: pattern-recognize
'''
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import io
from zigzag import *
def decoder():
    padded_img = np.loadtxt('./encoded.txt')
    [h, w, block_size] = np.loadtxt('./size.txt')
    [H, W] = padded_img.shape

    nbh = math.ceil(h/block_size)
    nbh = np.int32(nbh)
    nbw = math.ceil(w/block_size)
    nbw = np.int32(nbw)

    for i in range(nbh):
        row_ind_1 = i*int(block_size)
        row_ind_2 = row_ind_1+int(block_size)
        for j in range(nbw):
            col_ind_1 = j*int(block_size)
            col_ind_2 = col_ind_1+int(block_size)
            block = padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ]
            reshaped = np.reshape(block,(int(block_size)*int(block_size)))
            reordered = inverse_zigzag(reshaped, int(block_size), int(block_size))
            IDCT = cv2.idct(reordered)##### your code #####
            padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ] = IDCT

    padded_img = np.uint8(padded_img)
    #cv2.imshow('decoded padded image', padded_img)

    decoded_img = padded_img[0:int(h),0:int(w)]
    #io.imshow(decoded_img)
    #io.show()
    plt.imshow(decoded_img,cmap='gray')
    plt.title('decode')
    plt.show()
    #cv2.imshow('decoded image', decoded_img)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
