#!/usr/bin/env python
from time import time

def gen_fib_list(limit):
	fib_list =[1,2]
	while fib_list[-1] < limit:
		fib_list.append(fib_list[-1] + fib_list[-2])
	return fib_list

if __name__ =="__main__":
	start = time()

	fib = gen_fib_list(4000000)
	num = sum([x for x in fib if x%2==0])

	print "Answer to Problem 2: ", num
	print "Completed in: %f seconds" % (time() - start)