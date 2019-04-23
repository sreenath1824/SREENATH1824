
# coding: utf-8

# In[2]:


import numpy


# In[14]:


import matplotlib.pyplot as plt


# In[5]:


import math


# In[64]:


f=int(input("Enter a number f:"))
n=numpy.asarray(range (0,200),'float32')
x=numpy.sin (2*3.14*f*n)
plt.plot(x)
plt.show()


# 
# 

# In[57]:


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


# In[40]:


fs=int(input("Enter a number:"))
f=int(input("Enter a number f:"))
n=numpy.asarray(range (0,2000),'float32')
x=numpy.linspace(0,10,30)
x=numpy.sin (2*3.14*(f/fs)*x)
plt.stem(x)
plt.show()

