#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/12
@File: gui.py
@Project: pattern-recognize
'''
from Tkinter import *
import cv2
import matplotlib.pyplot as plt
import numpy as np
import dft_dct as df
import histogram as hg
import sharpen
import blur
import huffman_compute
import huffman_encoder as he
import huffman_decoder as hd
#from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
#import test

def dftButton():
    df.dft_dct()
def histButton():
    hg.histogram()
def sharpenButton():
    sharpen.sharpen()
def blurButton():
    blur.blur()
def Huffman_encoder():
    he.encoder()
def Huffman_decoder():
    hd.decoder()
def Huffman_compute():
    entropy_result, average_length = huffman_compute.huffman_result()
    w = Label(root,text=str(entropy_result)+'\n'+str(average_length))
    w.pack()

root = Tk()
root.title('pattern-recognize')
root.geometry('320x480')

button1 = Button(root,text='dft_dct',command=dftButton)
button2 = Button(root,text='histogram',command=histButton)
button3 = Button(root,text='sharpen',command=sharpenButton)
button4 = Button(root,text='blur',command=blurButton)
button5 = Button(root,text='huffman_encode',command=Huffman_encoder)
button6 = Button(root,text='huffman_decode',command=Huffman_decoder)
button7 = Button(root,text='huffman_compute',command=Huffman_compute)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
mainloop()

