#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:17:26 2019

@author: rgukt
"""
#changing our voice speed
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read ('/home/rgukt/Desktop/Sai/myvoice.wav')
fs=np.float (fs)
print (fs,len(data),data)
t=np.arange(0,len(data)/fs,1/fs)
plt.plot (t,data)
plt.show()
wav.write ('my_new_voice1' ,2*fs,data)
