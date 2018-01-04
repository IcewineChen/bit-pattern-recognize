#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@author: Jackie Chen
@Time: 17/12/11
@File: huffman_compute.py
@Project: pattern-recognize
'''

from __future__ import division

from skimage import io,data,color
import numpy as np
import pickle
import matplotlib.pyplot as plt
import cv2
import math

class Node:
    def __init__(self,left=None,right=None,parent=None,weight=0,code=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code

def createnode(count_list):
    nodelist = []
    for i in range(len(count_list)):
        nodelist.append(Node(weight=count_list[i][1],code=str(count_list[i][0])))
    return nodelist

def sort_by_weight(listnode):   #sort the
    listnode = sorted(listnode,key=lambda node:node.weight)
    return listnode

def huffmantree(listnode):  #create huffman tree
    while len(listnode) != 1:
        low_node0,low_node1 = listnode[0],listnode[1]   #get the minimize code
        new_change_node = Node()
        new_change_node.weight = low_node0.weight + low_node1.weight
        new_change_node.left = low_node0
        new_change_node.right = low_node1
        low_node0.parent = new_change_node
        low_node1.parent = new_change_node
        listnode.remove(low_node0)
        listnode.remove(low_node1)
        listnode.append(new_change_node)
        listnode = sort_by_weight(listnode)
    return listnode

def huffman_compute(img): #compute for entropy and average_length
    assert len(img.shape) == 2,("not gray map")
    info = {}       #create a empty dictionary
    m = img.shape[0]
    n = img.shape[1]
    img_temp = img
    img = np.transpose(img)
    f = dict(zip(*np.unique(img, return_counts=True)))  #count for all value
    if '0' in f.keys():
        f.pop(0)  #remove 0 element
    tmp = dict()
    tmp = sorted(f.items(), lambda x, y: cmp(x[1], y[1]),reverse=False)
    #tmp.keys for pixel value
    #tmp.values for pixel frequency
    frequency_sum = 0

    list_tmp = []
    count_list = []
    for item in tmp:
        list_tmp.append(list(item))
        count_list.append(list(item))
    for item in list_tmp:
        frequency_sum = frequency_sum + item[1]
    for item in list_tmp:
        item[1] = item[1]/frequency_sum
    entropy_result = entropy(list_tmp)  #compute for entropy

    treelist = createnode(tmp)
    head = huffmantree(treelist)[0]
    codinglist = {}
    average_length = 0
    for item in treelist:
        new_change_node = item
        codinglist.setdefault(item.code, "")
        while new_change_node != head:
            if new_change_node.parent.left == new_change_node:
                codinglist[item.code] = "1" + codinglist[item.code]
            else:
                codinglist[item.code] = "0" + codinglist[item.code]
            new_change_node = new_change_node.parent

    list_probability = 1/len(codinglist)
    for key in codinglist.keys():
        #print ("point after huffman:" + codinglist[key] + " " + str(key))
        average_length = average_length + list_probability*len(codinglist[key])

    return entropy_result,average_length

def huffman_decode(img):
    assert len(img.shape) == 2, ("not gray map")

def entropy(sorted):
    assert type(sorted) == list, ("input type not matching")
    img_entropy = 0
    for item in sorted:
        img_entropy = img_entropy+item[1]*math.exp(item[1])
    return img_entropy

def huffman_result():
    img = data.chelsea()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    entropy_result,average_length = huffman_compute(img)
    return entropy_result,average_length
    #print entropy_result,average_length

