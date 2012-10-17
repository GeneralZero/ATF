#!/usr/bin/env python
from time import time

def sum_square(limit): #1^2 + 2^2 + ... + 10^2 
	sum = 0
	for x in range(limit+1):
		sum += x*x
	return sum

def square_sum(limit):# (1 + 2 + ... + 10)^2 
	ret = sum(range(limit+1))
	return ret*ret

def diff_square_sums(limit):
	sum = 0
	for x in range(limit):
		sum+= square_sum(x) - sum_square(x)
	return sum

if __name__ =="__main__":
	start = time()

	limit = 100

	print "Answer to Problem 6: ", square_sum(limit) - sum_square(limit)
	print "Completed in: %f seconds" % (time() - start)