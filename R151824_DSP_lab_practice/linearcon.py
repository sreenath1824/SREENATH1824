import numpy as np
import matplotlib.pyplot as plt
y=[]
x=np.array(input('seq1='))
h=np.array(input('seq2='))
l1=len(x)
l2=len(h)
for n in range(0,l1+l2-1,1):
	s=0
	for k in range(0,l1,1):
		if(n-k>=0 and n-k<l1):
			s=s+x[k]*h[n-k]
	y=np.append(y,s)
n=np.linspace(0,l1+l2-1,5)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("linear convolution")
plt.stem(n,y)
