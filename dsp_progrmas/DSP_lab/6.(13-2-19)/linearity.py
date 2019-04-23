#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:48:48 2019

@author: apiiit-rkv
"""
from DFT_func import dft
import numpy as np
import cmath as c
from matplotlib import pyplot as plt
x=input ("Enter x:")
y=input ("Enter y:")
xy=np.add (x,y)
x1=dft (x)
y1=dft (y)
r=np.add (x1,y1)
r=np.abs(r)
re=dft (xy)
re=np.abs(re)
plt.subplot (211)
plt.stem (r)
plt.subplot (212)
plt.stem (re)
    
    