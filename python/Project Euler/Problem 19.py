#!/usr/bin/env python
from time import time

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def run():
	day=2
	count=0
	for i in range(1901,2001):
		for j in range(1,13):
			if i%4==0 and i%100!=0 or i%400==0:
				day = day+29
			else:
				day = day+month[j]
			if day%7==0:
					count=count+1
	return count

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 19:", run()
	print "Completed in: %f seconds" % (time() - start)