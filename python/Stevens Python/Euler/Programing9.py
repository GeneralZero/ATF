a=1
while(a<1000):
	b=(1000*(a-500))/(a-1000)
	try:
		c = pow(pow(a,2)+pow(b,2),.5)
		if(len(str(c))<6 and b>0):
			print a,b,c
	except:
		print 'Please enter a valid integer'
		exit(1)
	a=a+1
