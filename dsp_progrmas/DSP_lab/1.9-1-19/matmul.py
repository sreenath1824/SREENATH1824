def mul(a,b):
	e=[]
	while (n!=r):
		print ("Matrix multiplication is not possible.")
		break
	if (n==r):
		print ("Matrix multiplication is possible.")
		for i in range (0,m,1):
			d=[]
			for j in range (0,c,1):
				s=0
				for k in range (0,n,1):
					s=s+a[i][k]*b[k][j]
				d.append(s)
			e.append(d)
	return e
a=[]
print ("Enter matrix 1:")
m=input ("Enter no of rows:")
n=input ("Enter no of columns:")
for i in range (0,m,1):
	p=[]
	for j in range (0,n,1):
		p.append(input ("Enter a number:"))
	a.append(p)	
print ("Enter matrix 2:")
r=input ("Enter no of rows:")
c=input ("Enter no of columns:")
b=[]
for i in range (0,r,1):
	q=[]
	for j in range (0,c,1):
		q.append(input ("Enter a number:"))
	b.append(q)
print mul (a,b)
