#!/usr/bin/env python
from time import time

prime_list = [2]

def num_primes(number):
	test_num = 3

	while len(prime_list) < number:
		prime = True
		for primes in prime_list:
			if primes*primes > test_num:
				break
			if test_num % primes == 0:
				prime = False
				break
		if prime:
			prime_list.append(test_num)
		test_num += 2

if __name__ =="__main__":
	start = time()

	num_primes(10001)

	print "Answer to Problem 7: ", prime_list[10000] # find 10001 prime start at index 0
	print "Completed in: %f seconds" % (time() - start)