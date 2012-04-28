def functionD(number):
	list = listDevisors(number)
	sum = 0
	for num in list:
		sum=num +sum
	return sum
		
def listDevisors(number):
	list = []
	i=1
	while(i<number):
		if(number%i==0):
			list.append(i)
		i=i+1
	#print list
	return list

i=1
sum=0
while(i<10001):
	j=functionD(i)
	if(i==functionD(j) and j!=i):
		print i,j
		sum=sum+i
	i=i+1
print sum