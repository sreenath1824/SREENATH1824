import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x=input("Enter a signal : ")
l=len(x)
N=input("Enter N :")
if(l<N):
	for i in range(N-l):
		x.append(0)
j=cm.sqrt(-1)
k=np.linspace(-2*N,2*N-1,4*N)
X_W=[]
for m in range(-2*N,2*N,1):
	s=0
	for t in range (N):
		s+=(x[t]*np.exp(-2*np.pi*m*j*t/N))
	X_W.append(s)
plt.subplot(221)
plt.stem(x[0:N])
plt.subplot(222)
plt.stem(k,X_W)
plt.subplot(223)
plt.stem(k,np.abs(X_W))
plt.subplot(224)
plt.stem(k,np.angle(X_W))
plt.show()
