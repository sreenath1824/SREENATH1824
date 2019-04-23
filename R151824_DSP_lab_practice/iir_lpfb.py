import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
wp=0.35*np.pi
ws=0.7*np.pi
t=0.1
apf=2*np.tan(wp/2)/t
asf=2*np.tan(ws/2)/t
print ("apf=%d"%apf)
print ("asf=%d"%asf)
dp=0.6
ds=o.1
N=np.ceil(np.log10((ds**-2)-1/(dp**-2)-1)/(2*np.log10(asf/apf)))
print ('order=%d'% acf)
k=(N/2)
j=mp.sqrt(-1)
bk=2*np.sin((((2*k)-1)*np.pi)/(2*N))
w=np.arange(0,np,pi,0.1)
z=np.exp(j*w)
s=(2/t)*((1-z**(-1))/(1+z**-1)))
hs=((acf)**N)/((s**2)+(bk*acf*s)+(acf**2))
plt.figure(1)
plt.xlabel('frequency')
plt.ylabel('magnitude|H(e**(jw)|')
plt.title('Low pass filter')
plt.plot(w,np,abs(hs))
