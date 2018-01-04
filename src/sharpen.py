#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/11
@File: sharpen.py
@Project: pattern-recognize
'''
import cv2
import numpy as np
from skimage import filters,color,data
import math
import matplotlib.pyplot as plt

def Roberts(img):
    edges = filters.roberts(img)
    return edges
'''
#manual implement Roberts gradient
    rows,cols=img.shape[:2]
    roberts = []
    #initialize dst
    dst = np.zeros((rows,cols),np.float32)
    img = np.float32(img)
    for i in range(rows)[:-1]:
        for j in range(cols)[:-1]:
            robert_x = abs(img[i,j]-img[i+1,j+1])
            robert_y = abs(img[i+1,j]-img[i,j+1])
            dst[i,j] = robert_x+robert_y
    return dst
'''
def Sobel(img):
    #dst = cv2.Sobel(img,ddepth=-1/cv2.CV_32F/cv2.CV_64F,dx=1,dy=1)
    #dst = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
    dst = filters.sobel(img)
    return dst

def Laplace(img):
    #dst = cv2.Laplacian(img,ddepth=-1/cv2.CV_32F/cv2.CV_64F)
    dst = cv2.Laplacian(img,cv2.CV_64F)
    #dst = filters.laplace(img)
    return dst

def sharpen():
    #img_color = cv2.imread('../images/lena.jpg')
    img_color = data.chelsea()
    #b,g,r = cv2.split(img_color)
    #img = color.rgb2gray(img_color)
    #img = data.camera()
    img = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)
    #Robert_b = Roberts(b)
    #Robert_g = Roberts(g)
    #Robert_r = Roberts(r)
    #Roberts_img = cv2.merge([Robert_r,Robert_g,Robert_b])
    Roberts_img = Roberts(img)
    #Sobel_b = Sobel(b)
    #Sobel_g = Sobel(g)
    #Sobel_r = Sobel(r)
    #Sobel_img = cv2.merge([Sobel_r,Sobel_g,Sobel_b])
    Sobel_img = Sobel(img)
    #Laplacian_b = Laplace(b)
    #Laplacian_g = Laplace(g)
    #Laplacian_r = Laplace(r)
    Laplacian_img = Laplace(img)
    #Laplacian_img = cv2.merge([Laplacian_r,Laplacian_g,Laplacian_b])
    plt.subplot(221),plt.imshow(Roberts_img,cmap='gray')
    plt.title('Roberts')
    plt.subplot(222),plt.imshow(Sobel_img,cmap='gray')
    plt.title('Sobel')
    plt.subplot(223),plt.imshow(Laplacian_img,cmap='gray')
    plt.title('Laplacian')
    plt.show()




