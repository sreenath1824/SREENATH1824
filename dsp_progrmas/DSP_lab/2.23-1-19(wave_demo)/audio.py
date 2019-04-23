#convert voice to signal
import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read ('/home/rgukt/Desktop/Sai/myvoice.wav')
fs=np.float (fs)
print (fs,len(data),data)
t=np.arrange (0,len(data)/fs,1/fs)
plt.plot (t,data)
plt.show()

