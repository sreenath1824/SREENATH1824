import numpy
import matplotlib.pyplot as plt
fs=int(input("Enter a number:"))
f=int(input("Enter a number f:"))
n=numpy.asarray(range (0,2000),'float32')
x=numpy.linspace(0,10,30)
x=numpy.sin (2*3.14*(f/fs)*x)
plt.stem(x)
plt.show()
