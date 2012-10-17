#!/usr/bin/env python
from time import time
import math

def unique_factors(num):    # Stole from Stack Overflow
	return set(reduce(list.__add__, 
				([i, num/i] for i in range(1, int(num**0.5) + 1) if num % i == 0 )))

def factors(num):    # Stole from Stack Overflow
	return reduce(list.__add__, 
				([i, num/i] for i in range(1, int(num**0.5) + 1) if num % i == 0 ))

def triangle_sum():
	triangle_sum = 1
	for x in range(2,50000):
		triangle_sum += x
		if len(unique_factors(triangle_sum)) >= 500:
			return triangle_sum

if __name__ =="__main__":
	start = time()
	print "Answer to Problem 12: ", triangle_sum()
	print "Completed in: %f seconds" % (time() - start)