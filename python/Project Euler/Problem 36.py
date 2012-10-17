#!/usr/bin/env pthon
from time import time
def is_palandrome(string):
	for x in range(len(string)/2):
		if not string[x] == string[-(x+1)]:
			return False
	return True

if __name__ == '__main__':
	start = time()
	pal = []
	for x in range(1, 1000001):
		if is_palandrome(str(x)) and is_palandrome(bin(x)[2:]):
			pal.append(x)

	print "Answer to Problem 36: ", sum(pal)
	print "Completed in: %f seconds" % (time() - start)