import numpy as n
import matplotlib.pyplot as plt
f=input ("Enter frequency:")
t=n.linspace (0,10,2000)
x=n.sin (2*n.pi*f*t)
plt.plot(t,x)
plt.show()
