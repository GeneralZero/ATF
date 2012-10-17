#!/usr/bin/env python
from time import time

def is_palindrome(string):
	for x in range(len(string)/2):
		if not string[x] == string[-(x+1)]:
			return False
	return True

def main():
	max = 0
	for x in reversed(range(100, 999)):
		for y in reversed(range(x, 999)):
			if is_palindrome(str(x*y)) and x*y > max:
				max = x*y
	return max

if __name__ =="__main__":
	start = time()

	print "Answer to Problem 4: ", main()
	print "Completed in: %f seconds" % (time() - start)
