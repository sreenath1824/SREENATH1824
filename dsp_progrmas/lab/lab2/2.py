import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2,200)
x=np.sin(2*np.pi*t)
n=np.linspace(0,20,20)
s=np.sin(2*np.pi*(1.0/9.0)*n)
y=[]
p=input("Enter order of MAS : ")
for i in range(20):
	m=0
	c=p
	if(i<p):
		c=i
	for j in range(c+1):
		m=m+s[i-j]
	y.append(m/p)
plt.subplot(221)
plt.plot(t,x)
plt.subplot(222)
plt.stem(n,s)
plt.subplot(223)
plt.stem(n,y)
plt.show()
