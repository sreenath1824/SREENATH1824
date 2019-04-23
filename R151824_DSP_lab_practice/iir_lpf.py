import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
def dtfx(x):
	j=mp.sqrt(-1);
	w.np.linespace(-3.14,3.14,1000)
	l=x.size
	X=np.zeros(len(w),dtype=complex)
	for i in range (1000):
		su=0
		for n in range (0,1,1,)
			su=su+x[n]*np.exp(-j*w[i]*n)
		X[i]=(su)
	return X
n=np.arnge(-17,17,1)
hd=(0.25)*np.sinc(0.25*n)

M=31
n=np.arnge(0,M)
#Rectangular window
plt.title ("rectangular window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.stem(n,Wr)
						#triangular window
Wt=np.zeros(M)
for i in range(0,M,1):
	pro=float(2*np.abs(i-((M-1)/2)))
	Wt[i]=1-(pro/(M-1))
plt.subplot(3,3,2)
plt.title ("triangular window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.stem(n,Wt)

			#hanning window
Whan=np.zeros(M)
for i in range(0,M,1):
	pro=(2*np.pi*i)/(M-1)
	Whan[i]=0.5-(0.5*np.cos(pro))
plt.subplot(3,2,3)
plt.title ("hanning window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.stem(n,Whan)

	#hamming window
	
Wham=np.zeros(M)
for i in range(0,M,1):
	pro=(2*np.pi*i)/(M-1)
	Wham[i]=0.54-(0.46*np.cos(pro))
plt.subplot(3,2,4)
plt.title ("hamming window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.stem(n,Wham)

	#blackman window

Wbla=np.zeros(M)
for i in range(0,M,1):
	pro=(2*np.pi*i)/(M-1)
	Wbla[i]=0.42-(0.5*np.cos(pro))+0.08*np.cos(2*pro)
plt.subplot(3,2,5)
plt.title ("blackman window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.show()
sincw=[]   

#Digital LPF using rectangular window


for i in range(0,31,1):
	pro=Wr[i]*hd[i]
	sincw=np.append(sincw,pro)
digrec=np.abs(dtft(sincw))
w=np.linespace(-3.14,3.14,1000)
plt.subplot(3,2,1)
plt.title ("Digital LPF using rectangular window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.plot(w,digrec)
sincw=[]	

#Digital LPF using triangular window

for i in range(0,31,1):
	pro=Wt[i]*hd[i]
	sincw=np.append(sincw,pro)
digtri=np.abs(dtft(sincw))
plt.subplot(3,2,2)
plt.title ("Digital LPF using traingular window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.plot(w,digtri)
sincw=[]	

#Digital LPF using hanning window

for i in range(0,31,1):
	pro=Whan[i]*hd[i]
	sincw=np.append(sincw,pro)
dighan=np.abs(dtft(sincw))
plt.subplot(3,2,3)
plt.title ("Digital LPF using hanning window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.plot(w,dighan)
sincw=[]	

#Digital LPF using hamming window

for i in range(0,31,1):
	pro=Wham[i]*hd[i]
	sincw=np.append(sincw,pro)
digham=np.abs(dtft(sincw))
plt.subplot(3,2,4)
plt.title ("Digital LPF using hamming window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.plot(w,digham)
sincw=[]	

#Digital LPF using black man window

for i in range(0,31,1):
	pro=Wbla[i]*hd[i]
	sincw=np.append(sincw,pro)
digbla=np.abs(dtft(sincw))
plt.subplot(3,2,5)
plt.title ("Digital LPF using blackman window")
plt.ylabel("Magnitude")
plt.xlabel("frequency")
plt.plot(w,digbla)
plt.show()

