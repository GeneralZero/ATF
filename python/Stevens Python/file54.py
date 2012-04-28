import os 
import shutil

name = []
animename = ""
filenumber = 0
ext = ".mp3"
com = ''

def ensure_dir(f):
	if not os.path.exists(f):
		os.makedirs(f)
def movedirs(inf,outf):
	os.system("mv -f -R " + inf + " " + outf)
	

for f in os.listdir("/srv/uploads/music/"):
	(pdb, extension) = os.path.splitext(f)
	name.append(pdb)

for files in name:
	placenumber = name[filenumber].find('_-_')
	#print placenumber
	#print files[:placenumber]
	if placenumber >= 0:
		print ("/srv/uploads/music/" + files[:placenumber])
		ensure_dir(("/srv/uploads/music/" + files[:placenumber]))
		src = ("/srv/uploads/music/" + name[filenumber] + ext)
		com =("mv " + src + " /srv/uploads/music/" +files[:placenumber] + "/" + name[filenumber] + ext)
		print com
		os.system(com)
		ensure_dir("/srv/animemusic/" + files[:placenumber])
		movedirs("/srv/uploads/music/" + files[:placenumber],"/srv/animemusic/" + files[:placenumber])
	filenumber+= 1

