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
from skimage import data
import matplotlib.pyplot as plt
# import zigzag functions
from zigzag import *
def encoder():
    block_size = 8
    img = data.chelsea()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('input image', img)
    #cv2.waitKey(0)
    # get size of the image
    [h,w] = img.shape
    # compute number of blocks by diving height and width of image by block size
    h = np.float32(h)
    w = np.float32(w)
    nbh = math.ceil(h/block_size)
    nbh = np.int32(nbh)
    nbw = math.ceil(w/block_size)
    nbw = np.int32(nbw)

    H = block_size * nbh
    W = block_size * nbw

    padded_img = np.zeros((H,W))
    for i in range(h):
            for j in range(w):
                    pixel = img[i,j]
                    padded_img[i,j] = pixel

    #cv2.imshow('input padded image', np.uint8(padded_img))
    for i in range(nbh):
            row_ind_1 = i*block_size
            # Compute end row index of the block
            row_ind_2 = row_ind_1+block_size
            for j in range(nbw):
                col_ind_1 = j*block_size
                col_ind_2 = col_ind_1+block_size
                block = padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ]
                DCT = cv2.dct(block)
                reordered = zigzag(DCT)
                reshaped = np.reshape(reordered, (block_size, block_size))
                padded_img[row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2] = reshaped

    #cv2.imshow('encoded image', np.uint8(padded_img))

    np.savetxt('./encoded.txt',padded_img)
    np.savetxt('./size.txt',[h, w, block_size])
    plt.subplot(211),plt.imshow(img, cmap='gray')
    plt.title('origin')
    plt.subplot(212),plt.imshow(padded_img,cmap='gray')
    plt.title('after padded')
    plt.show()
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()




