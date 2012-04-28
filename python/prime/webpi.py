import time

s= time.time()

for x in range(1,1000001):
	print x

e = time.time()


sx= time.time()

for x in xrange(1,1000001):
	print x

ex = time.time()
print 'xrange time ',str(ex-sx)
print "range time",str(e-s)
