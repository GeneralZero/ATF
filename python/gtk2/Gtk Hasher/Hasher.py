#!/usr/bin/env python

import hashlib
class Hasher:
	def __init__(self):
		try:
			self.accepted = hashlib.algorithms()
			#Only works in 2.7 and up so default Hashes are included
		except AttributeError:
			self.accepted = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
		#self.accpeted is the list of algorithms

	def singlehash(self,text,algor):		
		if algor in self.accepted:
			return getattr(hashlib,algor)(unicode(text)).hexdigest()
		else:
			raise NameError('Not a valid algorithm')
			
	def multihash(self,text,algors):
		ret = []
		for algor in algors:
			ret.append(self.singlehash(text, algor))
		return ret

#h= hasher()
#print h.multihash('cool',['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'])
