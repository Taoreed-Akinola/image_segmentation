#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:24:31 2022

@author: treed
"""

import glob
import matplotlib.pyplot as plt
import cv2

pathImg = '/raid/credit/tarry/xDB/joplin-tornado/images/*'
pathMask = '/raid/credit/tarry/xDB/joplin-tornado/masks/*'
img_list =sorted(glob.glob(pathImg))
mask_list =sorted(glob.glob(pathMask))

im = cv2.imread(mask_list[-51])
cv2.imshow('image', im)