def ntriangle(n):
	i=1
	sum=0
	while(i<n+1):
		sum = i+sum
		i=i+1
	return sum


def factorlist(n):
	list=[]
	i=1
	while(i<pow(n+1,.5)):
		if(n%i==0):
			list.append(i)
			list.append(n/i)
		i=i+1
	return list
n=1
while(n>0):
	a = ntriangle(n)
	l=factorlist(a)
	if(len(l)>500):
		print n,len(l),a, "done"
		break
	print n,len(l),a
	n=n+1
