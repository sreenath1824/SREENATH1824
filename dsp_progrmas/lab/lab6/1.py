import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import math
dp=input("Enter dp : ")
ds=input("Enter ds : ")
wp=input("Enter wp : ")
ws=input("Enter ws : ")
ws=ws*2*np.pi
wp=wp*2*np.pi
N=math.ceil(0.5*math.log((1.0/(dp*dp)-1)/(1.0/(ds*ds)-1))/math.log(wp/ws))
wc=wp/((1.0/(dp*dp)-1)**(0.5/N))
print wc
print N
w=np.linspace(0,np.pi*2*2000,1000)
H=-10*np.log10(1+(w/wc)**(2*N))
h=1/(1+(w/wc)**(2*N))**0.5
plt.subplot(211)
plt.plot(w,h)
plt.subplot(212)
plt.plot(w,H)
plt.show()
