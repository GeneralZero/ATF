#!/usr/bin/env python
from time import time

def load_file(file_name):
	list_file = open(file_name)
	ret = []

	lists = list_file.readlines()
	for lines in lists:
		ret.append(int(lines))
	return ret

if __name__ =="__main__":
	start = time()

	print "Answer to Problem 13: ", str(sum(load_file('Problem 13.txt')))[:10]
	print "Completed in: %f seconds" % (time() - start)

