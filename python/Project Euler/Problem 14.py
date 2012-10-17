#!/usr/bin/env python
from time import time

table = {}

def find_n(num):
	if not table.get(num):
		count = 0
		test = num
		while test > 1:
			count +=1
			if table.get(test):
				table[num] = table[test] + count
				break
			elif test % 2 == 0:
				test = test/2
			else:
				test = 3*test+1
			if test ==1 :
				table[num] = count
				break
	return table[num]

def run(limit):
	ret = [1,0] #Number, Count
	for x in range(3, limit):
		count = find_n(x)
		if count > ret[1]:
			
			ret = [x, count]
	return ret
				
if __name__ =="__main__":
	start = time()


	print "Answer to Problem 14: ",  run(1000000)
	print "Completed in: %f seconds" % (time() - start)