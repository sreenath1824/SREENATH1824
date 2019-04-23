import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import math
def cnx(N,x):
	if(x<=1.0):
		c=np.cos(N*np.arccos(x))
	else:
		c=np.cosh(N*np.arccosh(x))
	return c
dp=input("Enter dp : ")
ds=input("Enter ds : ")
wp=input("Enter fp : ")
ws=input("Enter fs : ")
ws=ws*2*np.pi
wp=wp*2*np.pi
eps=math.sqrt(1/(dp*dp)-1)
print eps
y=(1/eps)*math.sqrt(1/(ds*ds)-1)
N=1
while(1):
	r=cnx(N,ws/wp)
	if(r>=y):
		break
	N+=1
print N
w=np.linspace(0,np.pi*2*6000,1000)
h=np.zeros(1000)
for i in range(1000):
	h[i]=1/(1+(eps*cnx(N,w[i]/wp))**2)**0.5
plt.plot(w/(2*np.pi),h)
plt.show()
