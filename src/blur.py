#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/11
@File: blur.py
@Project: pattern-recognize
'''
from skimage import io,data,filters,color
import numpy as np
import cv2
import matplotlib.pyplot as plt

def PSFestiamte(C,PSF,Fw,beta,noiseLevel):
    F = np.fft.fft2(np.zeros(np.shape(C)))
    Cabs = np.abs(C)
    Gwabs = np.abs(PSF)
    cond0 = (Cabs < noiseLevel)
    cond1 = (Gwabs >= Cabs) & (~cond0)
    cond2 = (Gwabs < Cabs) & (~cond0)
    F[cond0] = Fw[cond0]
    F[cond1] = (1.-beta)*Fw[cond1] + beta*np.divide(C[cond1], PSF[cond1])
    tmp = np.divide((1.-beta), (Fw[cond2] +
                    np.divide(beta*PSF[cond2],C[cond2])))
    F[cond2] = np.divide(1.,tmp)
    return F

def blur():
    #blur
    #img = data.chelsea()
    img = data.chelsea()
    #img = color.rgb2gray(img)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img = color.rgb2gray(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.float32)/16
    #multi method for blur
    #dst = cv2.filter2D(img,-1,kernel)

    dst_color = cv2.GaussianBlur(data.chelsea(),(5,5),0)
    dst = cv2.GaussianBlur(img,(5,5),0) #image after Gaussian Blur
    dst_tmp = dst
    #restore

    pw = cv2.bilateralFilter(img,9,15,15)
    #compare to bilateralFilter used by opencv
    size_psf = 12
    wpsf = np.zeros(np.shape(dst))
    wpsf[0:size_psf,0:size_psf] = 1

    beta = 0.8  #param for iteration
    noiseLevel = 1
    itertime = 40
    fw = dst
    C = np.fft.fft2(dst)
    PSF = np.zeros(np.shape(C))     #PSF=GW

    for i in range(itertime):
        Fw = np.fft.fft2(dst)
    #print Fw
    G = PSFestiamte(C,Fw,PSF,beta,noiseLevel)
    g = np.real(np.fft.ifft2(G))
    gw = g
    #print gw

    for i in range(gw.shape[0]):
        for j in range(gw.shape[1]):
            if gw[i,j] < 0.:
                gw[i,j] = 0
    gw = gw*wpsf
    gw_sum = np.sum(gw)
    gw = gw/gw_sum
    Gw = np.fft.fft2(gw)

    F = PSFestiamte(C,Gw,Fw,beta,noiseLevel)
    f = np.real(np.fft.ifft2(F))
    fw = f
    for i in range(fw.shape[0]):
        for j in range(fw.shape[1]):
            if fw[i,j] < 0.:
                fw[i,j] = 0
    E = np.sum(np.abs(fw)-np.abs(f))
    fw = fw + E/(np.shape(img)[0]*np.shape(img)[1])

    plt.subplot(221),plt.imshow(data.chelsea())
    plt.title('init')
    plt.subplot(222),plt.imshow(dst_color)
    plt.title('GaussianBlur')
    plt.subplot(223),plt.imshow(dst_tmp,cmap='gray')
    plt.title('GaussianBlur_Gray')
    plt.subplot(224),plt.imshow(fw,cmap='gray')
    plt.title('recovery')
    plt.show()