i=1
sum=1
while(i<101):
	sum=sum*i
	i=i+1
	print i
print sum

string1= str(sum)
i=0
sum=0
while(i<len(string1)):
	sum= int(string1[i:i+1])+sum
	i=i+1
	
print sum