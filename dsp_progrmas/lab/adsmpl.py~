import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sgl
[x,y]=sgl.read("/home/rgukt/Desktop/E2S2/DSP/lab/voice.wav")
fs=8000.0
print(fs,len(y),y)
sgl.write("/home/rgukt/Desktop/E2S2/DSP/lab/v2.wav",2*fs,y)
plt.plot(y)
plt.show()
