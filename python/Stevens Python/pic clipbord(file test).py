'''import os

filename = 'prime'
dir = 'prime_output'
try:
	primefile = open(dir+'/'+filename+'.txt', 'w') 
except IOError:
	os.mkdir(dir)
	print kool
except WindowsError:
	print "Directory already exists"
	'''
class WavSet:
     def __init__(self):
         print 'Init'
     def open(self):
         print 'Open'
     def close(self):
         print 'Close'
     def play(self,wav_id):
         print 'Play %d'%(wav_id,)

w=WavSet()
print w.open()
print w.close()
