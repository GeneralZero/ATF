#!/usr/bin/env python
from time import time

prime_list = [2]

def primes(number):
	test_num = 3

	while test_num <= number:
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

	primes(2000000)

	print "Answer to Problem time: ", sum(prime_list)
	print "Completed in: %f seconds" % (time() - start)