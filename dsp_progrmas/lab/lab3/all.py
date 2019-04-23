import numpy as np
import matplotlib.pyplot as plt
def conv(x,h):
	m=len(x)
	n=len(h)
	y=np.zeros(m+n-1)
	for i in range(m):
		for j in range(n):
			y[i+j]=y[i+j]+x[i]*h[j]
	t=np.linspace(0,m+n-2,m+n-1)
	return [y,t]
x=input("Enter first signal : ")
h=input("Enter second signal : ")
m=len(x)
n=len(h)
for i in range(m-1):
	h.append(0)
for j in range(n-1):
	x.append(0)
auto=[]
t=[]
[auto,t]=conv(x,x[::-1])
plt.subplot(311)
plt.stem(t,x)
plt.subplot(312)
plt.stem(t,h)
plt.subplot(313)
plt.stem(t,y)
plt.show()
