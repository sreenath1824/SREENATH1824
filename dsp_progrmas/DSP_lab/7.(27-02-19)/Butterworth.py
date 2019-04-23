import numpy as np
from matplotlib import pyplot as plt
dp=np.float(input ("Enter dp value:"))
ds=np.float(input ("Enter ds value:"))
wp=np.float(input ("Enter wp value:"))
ws=np.float(input ("Enter ws value:"))
N=(np.log10 ((1/dp)**2-1)-np.log10 ((1/ds)**2-1))/np.log10 (wp/ws)
N= np.ceil(0.5*N)
z=1/(2*N)
wc=wp/(((1/dp)**2-1))**z
print "The value of N is:",N
print "The value of wc is:",wc
w=np.arange (0,10000,1)
H=1/np.sqrt (1+((w/wc)**(2*N)))
H=np.abs(H)
plt.plot (w,H)
plt.show()
