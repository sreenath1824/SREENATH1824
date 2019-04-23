#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:29:44 2019

@author: rgukt
"""

import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read ('/home/rgukt/Desktop/Sai/myvoice.wav')
fs,data=wav.read ('/home/rgukt/Desktop/Sai/my_new_voice.wav')
fs=np.float (fs)
fs1=np.float (fs1)
print (fs,len(data),data)
t=np.arange(0,len(data)/fs,1/fs)
plt.plot (t,data)
plt.show()
wav.write ('my_new_voice1' ,2*fs,data)