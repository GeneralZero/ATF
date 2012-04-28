def nextFib(curentfib,prevfib):
	return curentfib+prevfib

fib1=1
fib2=1
fib3=0
i=2
while(len(str(fib1))<1000):
	fib3=fib2
	fib2=fib1
	fib1=nextFib(fib2,fib3)
	i=i+1
	if(len(str(fib1))>999):
		print i
		break
	
print fib1
print i