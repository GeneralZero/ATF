#!/usr/bin/env python
from time import time

table = {}

def rec_findpaths(length, width): #(x, y)
	if length==0 or width==0:
		return 1
	elif table.get((length, width)) == None:
		table[(length, width)] = rec_findpaths(length-1, width) + rec_findpaths(length, width-1)
	return table[(length, width)]

if __name__ =="__main__":
	start = time()
	print "Answer to Problem 15: ", rec_findpaths(20,20)
	print "Completed in: %f seconds" % (time() - start)