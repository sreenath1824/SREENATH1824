import numpy as np
import matplotlib.pyplot as plt
f=input("Enter frequecy of signal : ")
t=np.linspace(0,0.001,1000)
x=np.sin(2*np.pi*f*t)
n=np.random.rand(x.shape[0])
c=[]
for i in range(1000):
	c.append(x[i]+n[i])
y=[]
p=input("Enter order of MAS : ")
for i in range(1000):
	m=0
	d=p
	if(i<p):
		d=i
	for j in range(d+1):
		m=m+c[i-j]
	y.append(m/p)
plt.subplot(411)
plt.plot(t,x)
plt.subplot(412)
plt.plot(t,n)
plt.subplot(413)
plt.plot(t,c)
plt.subplot(414)
plt.plot(t,y)
plt.show()
