import numpy as np
import matplotlib.pyplot as plt
import cmath as mp

def dtft(x):
 j=mp.sqrt(-1)
 w=np.linspace(0,6.28,1000)
 l=x.size
 X=np.zeros(len(w),dtype=complex)
 for i in range(1000):
	su=0 n
	for n in range(0,1,1):
		su=su+x[n]*np.exp(-j*w[i]*n)
		X[i]=su
 return X
x=np.array(input("enter:"))
X=dtft(x)
mag=np.abs(X)
phase=np.angle(X)
print mag

plt.plot(w,mag)
plt.plot(w,phase)
plt.show()
