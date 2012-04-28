import os 
import shutil
import eyeD3

name = []
animename = ""
filenumber = 0
ext = ".mp3"
com = ''

def ensure_dir(f):
	if not os.path.exists(f):
		os.makedirs(f)
		
def movedirs(inf,outf):
	os.system("cp -f -r " + inf + " " + outf)
	os.system("rm -f -r " + inf)
	

for f in os.listdir("/mnt/server/uploads/music/"):
	(pdb, extension) = os.path.splitext(f)
	name.append(pdb)

for files in name:
	placenumber = name[filenumber].find(' - ')
	#print placenumber
	#print files[:placenumber]
	if placenumber >= 0:
		print ("/mnt/server/Music/" + files[:placenumber])
		ensure_dir(("/mnt/server/Music/" + files[:placenumber]))
		src = ("/mnt/server/Music/" + name[filenumber] + ext)
		com =("mv " + src + " /mnt/server/Music/" +files[:placenumber] + "/" + name[filenumber] + ext)
		print com
		os.system(com)
		ensure_dir("/mnt/server/Music/" + files[:placenumber])
		movedirs("/mnt/server/Music/" + files[:placenumber],"/mnt/server/Music/" + files[:placenumber])
	filenumber+= 1

