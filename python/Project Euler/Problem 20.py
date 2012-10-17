#!/usr/bin/env python
from time import time

def sums(num):
	string_num = str(num)
	summ =0
	for x in string_num:
		summ += int(x)
	return summ

def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)	

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 20: ", sums(factorial(100))
	print "Completed in: %f seconds" % (time() - start)