#!/usr/bin/env python
from time import time

def find_tripplet(sum):
	a=1 
	c=1
	while(a<sum/2 and c< sum):
		b=(sum*(sum/2-a))/(sum-a)
		c = pow(pow(a,2)+pow(b,2), .5)
		if c == int(c) and b>0: # tests to see if c is a whole number
			return a,b,int(c)
		a=a+1

def prod(list_num):
	sums=1
	for x in list_num: 
		sums*=x
	return sums

if __name__ =="__main__":
	start = time()


	print "Answer to Problem time: ", prod(find_tripplet(1000))
	print "Completed in: %f seconds" % (time() - start)
 