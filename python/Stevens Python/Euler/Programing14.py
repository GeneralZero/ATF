import math

i=1
n=3

finaln=0
finali=0

startn=3
while(startn<1000000):
	i=1
	n=startn
	#print "startn = "+str(startn)
	while(n>1):
		#print n
		if(n%2==0):
			n=n/2
		elif(n%2==1):
			n=(3*n)+1
		i=i+1
	#print "i="+str(i)
	if(i>finali):
		finaln=startn
		finali=i
		#print finaln,finali
	startn=startn+1
print finaln,finali