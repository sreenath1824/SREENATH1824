import numpy
import matplotlib.pyplot as plt
fs=int(input("Enter a number fs:"))
f=int(input("Enter a number f:"))
n=numpy.asarray(range (0,2000),'float32')
x=numpy.sin (2*3.14*(f/fs)*n)
plt.plot(x)
plt.show()
fs2=int(input("Enter a number:"))
f2=int(input("Enter a number f:"))
n2=numpy.asarray(range (0,2000),'float32')
x2=numpy.sin (2*3.14*(f2/fs2)*n2)
plt.plot(x2)
plt.show()
y=x+x2
print ("y=")
plt.plot(y)
plt.show()
