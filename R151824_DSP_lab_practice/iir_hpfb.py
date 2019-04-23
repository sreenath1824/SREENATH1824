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
apf1=1
asf1=asf/apf
dp=0.6
ds=0.1
N=np.ceil(np.log10((ds**-2)-1/(dp**-2)-1)/(2*np.log10(asf1/apf1)))
print ('order=%d'% N)
acf1=(asf1/((ds**-2)-1)**(0.5/N))
print ('acf=%d% acf1)
k=(N/2)
j=mp.sqrt(-1)
bk=2*np.sin((((2*k)-1)*np.pi)/(2*N))
w=np.arange(0.1,np,pi,0.1

z=np.exp(j*w)
s1=(2/t)*((1-z**(-1))/(1+z**(-1)))
s=apf/s1
hs=((acf1)**N)/((s**2)+(bk*acf1*s)+(acf1**2))
plt.figure(1)
plt.xlable('frequency')
plt.ylable('magnitude|H(e**(jw)|')
plt.title('High pass filter')
plt.plot(w,np,abs(hs))
