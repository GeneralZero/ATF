import math

i=0

a1=65
b1=72


a=a1*pow(a1,i)
b=b1*pow(a1,i)
c=int(math.sqrt(a*a+b*b))
while(a+b+c<1001):
	a=a1*pow(2,i)
	b=b1*pow(2,i)
	c=int(math.sqrt(a*a+b*b))
	print a,b,c, a+c+b
	if(a+b+c==1000):
		print a,b,c
	i=i+1