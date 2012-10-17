#!/usr/bin/env python

from time import time

def permutations(iterable, r=None):
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	if r > n:
		return
	indices = range(n)
	cycles = range(n, n-r, -1)
	yield tuple(pool[i] for i in indices[:r])
	while n:
		for i in reversed(range(r)):
			cycles[i] -= 1
			if cycles[i] == 0:
				indices[i:] = indices[i+1:] + indices[i:i+1]
				cycles[i] = n - i
			else:
				j = cycles[i]
				indices[i], indices[-j] = indices[-j], indices[i]
				yield tuple(pool[i] for i in indices[:r])
				break
		else:
			return
def run():
	lst =  [ x for x in permutations(range(10))]
	ans = ''
	for x in lst[999999]: #Starts at INDEX 0 so 1000000-1
		ans += x
	return ans
if __name__ == '__main__':
	start = time()


	print "Answer to Problem 24: ",  run()
	print "Completed in: %f seconds" % (time() - start)  
