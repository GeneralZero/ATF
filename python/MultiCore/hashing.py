# /sbin/python
import hashlib

def hashstring(string, alg):
	try:
		algor = hashlib.algorithms()
	except AttributeError:
		algor = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')	
	if alg in algor:
		print getattr(hashlib,alg)(unicode(string)).hexdigest()
	else:
		raise NameError('Not a valid Hashing algorithm')

