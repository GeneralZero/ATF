#!/usr/bin/env python
from time import time

if __name__ =="__main__":
	start = time()

	test = pow(2,1000)
	string1 = str(test)

	sum=0
	i=0
	while(i<len(string1)):
		#print int(string1[i])
		sum = sum + int(string1[i])
		i=i+1

	print "Answer to Problem time: ", sum
	print "Completed in: %f seconds" % (time() - start)

