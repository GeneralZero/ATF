import os
import urllib

counter = 1600
finish = 1602

timeoutini = 0
timeoutfin = 5

image = urllib.URLopener()

while(counter < finish):
	url = "http://questionablecontent.net/comics/%s.png" %counter
	urlos = "http://questionablecontent.net/comics/%s.png" %counter
	saveto = "Y:/torrents/Questionable Content/%s.png" %counter
	savetoos = "Y:\\torrents\\Questionable Content\\%s.png" %counter

	image.retrieve(url,saveto)
	if os.path.exists(savetoos):
		print ("Done Downloading #%s" %counter)
		counter = counter +1
	else:
		print ("Downloading #%s failed" %counter)
		if timeoutini < timeoutfin:
			print ("Retrying #%s" %counter)
			break
		else:
			counter = counter +1
			print("Cannot Download #%s")

	
'''while(counter < finish):
	image = urllib.URLopener()
	image.retrieve("http://questionablecontent.net/comics/%s.png", "%s.png" % (counter))
	counter = counter + 1
	print ("Done Downloading #%s" % (counter))'''