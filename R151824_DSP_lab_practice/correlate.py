import numpy as np
import matplotlib.pyplot as plt
rxx=[]
x=np.array(input('enter seq1='))
l1=len(x)
for l in range(-(l1-l),l1,l):
	s=0
	for n in range(0,l1,l):
		if(n+l>=0 and n+l<l1):
			s=s+x[n+l]*x[n]
		rxx=np.append(rxx,s)
print rxx
n=np.linspace(-(l1-l),l1-l,2*l1-l)
plt.figure(l)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("correlation")
plt.stem(n,rxx)
