i=2
lis = [2,3,5]
while(i<2000001):
	if(not((i%2==0 or i%3==0) or i%5==0)):
		print i
		lis.append(i)
	if(i==2):
		i=i+1
	else:
		i=i+2
print "done"
i=0
for num in lis:
	i=1
	while(i<len(lis)):
		if((lis[i]%num==0) and num!=lis[i]):
			print lis[i]
			lis.remove(lis[i])
		i=i+1

i=0
sum=0
while(i<len(lis)):
	sum=lis[i]+sum
	i=i+1
print sum 