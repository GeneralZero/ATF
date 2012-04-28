import os 
import shutil

class AnimeFile(object):
	def __init__(self):
		self.dir = "/srv/uploads/music/"
		self.name = []
		self.animename = ""
		self.filenumber = 0
		self.ext = ".mp3"
		self.com = ''

	def ensure_dir(self, f):
		if not os.path.exists(f):
			os.makedirs(f)
	def movedirs(self, inf, outf):
		os.system("mv -f -R " + inf + " " + outf)
	
	def run(self):
		for f in os.listdir(self.dir):
			(pdb, extension) = os.path.splitext(f)
			self.name.append(pdb)

		for files in self.name:
			self.placenumber = self.name[self.filenumber].find('_-_')
			#print self.placenumber
			#print self.files[:placenumber]
			if self.placenumber >= 0:
				print (self.dir + self.files[:self.placenumber])
				self.ensure_dir((self.dir + self.files[:self.placenumber]))
				self.src = (self.dir + self.name[self.filenumber] + self.ext)
				self.com =("mv " + self.src + self.dir +self.files[:self.placenumber] + "/" + self.name[self.filenumber] + self.ext)
				print self.com
				os.system(self.com)
				self.ensure_dir("/srv/animemusic/" + self.files[:self.placenumber])
				self.movedirs(self.dir + self.files[:self.placenumber],self.dir + self.files[:self.placenumber])
			filenumber+= 1

file=AnimeFile()

file.run()