import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
x=np.array(input('enter seq1='))
N=input('enter point dft value')
y=[]
j=mp.sqrt(-1)
for k in range(0,N,1):
	s=0
	for n in range(0,len(x),1):
		p=np.exp((-j*n*k*2*np.pi)/N)
		s=s+x[n]*p
		y=np.append(y,s)

w=np.linspace(0,N-1,N)
plt.figure(1)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("magnitude plot")
plt.stem(w,(np.abs(y)))
plt.figure(2)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("angle plot")
plt.stem(w,np.angle(y))
def idft(X):
X=np.asarray(X)
N=X.size
x=np.xeros(N,dtype=complex)
for n in range(0,N,1):
	su=0
	for k in range(0,N,1):
		product=(2*np.pi)/N
		su=su+X[k]*np.exp(j*product*n*k)
	x[n]=su
x=x/N
return(x)

x=dft(X)
x=np.real(x)
print"IDFT:",x
