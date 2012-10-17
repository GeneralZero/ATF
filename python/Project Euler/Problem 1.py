#!/usr/bin/env python
from time import time

if __name__ =="__main__":
	start = time()
	num=0

	for x in range(1, 1000):
		if x%3==0 or x%5 ==0:
			num+=x

	print "Answer to Problem 1: ", num
	print "Completed in: %f seconds" % (time() - start)