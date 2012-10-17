#!/usr/bin/env python
from time import time

def gcd(num1, num2):
    return gcd(num2, num1 % num2) if num2 else abs(num1)

def min_muultables(num):
	ret = range(1, num+1)
	for index, list_num in enumerate(ret):
		for y in range(1, len(ret) -index-1):
			if gcd(ret[-(index+1)], ret[y-1]) !=1 :
				#print "gcd(%d, %d) =" % (ret[-(index+1)], ret[y-1]), gcd(ret[-(index+1)], ret[y-1]), ret
				#print ret[y-1], "/", gcd(ret[-(index+1)], ret[y-1])
				ret[y-1] /= gcd(ret[-(index+1)], ret[y-1])
	return ret

def prod(list_num):
	sums=1
	for x in list_num: 
		sums*=x
	return sums

if __name__ =="__main__":
	start = time()
	
	print "Answer to Problem 5: ", prod(min_muultables(20))
	print "Completed in: %f seconds" % (time() - start)