#!/usr/bin/env python
from time import time

if __name__ =="__main__":
	start = time()

	numb=600851475143
	i=1
	while(i<numb):
		if(numb%i==0):
			numb=numb/i
			#print numb,i
		i=i+1

	print "Answer to Problem 3: ", numb
	print "Completed in: %f seconds" % (time() - start)