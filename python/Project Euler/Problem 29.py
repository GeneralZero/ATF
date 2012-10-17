#!/usr/bin/env python
from time import time

def power(base, exp):
	ret = 1
	for x in range(exp):
		ret *= base
	return ret

if __name__ =="__main__":
	start = time()

	power_list = []
	for base in range(2,101):
		for exp in range(2,101):
			temp = power(base, exp)
			if not temp in power_list:
				power_list.append(temp)

	print "Answer to Problem 29: ", len(power_list)
	print "Completed in: %f seconds" % (time() - start) 