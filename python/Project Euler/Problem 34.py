#!/usr/bin/env python
from time import time

factor = {0:1, 1:1, 2:2, 3:6}

def factorial(number):
	if number not in factor:
		factor[number] = number * factorial(number -1)
	return factor[number]

if __name__ == '__main__':
	start = time()
	total_sum=[]
	for nums in range(3, 100000):
		sums =0
		for digits in str(nums):
			sums += factorial(int(digits))
			#print digits, factorial(int(digits))
		if sums == nums:
			#print nums
			total_sum.append(nums)

	print "Answer to Problem 34: ", sum(total_sum)
	print "Completed in: %f seconds" % (time() - start)  