from PIL import ImageGrab
import PIL
import Image
import os


extentions = ["JPEG","PNG","PDF","GIF","BMP"]
count=0
file = 'screen%d.' % (count)
file += extentions[count].lower()
try:
	myimage = ImageGrab.grabclipboard()
	#print myimage.format
	while(os.path.isfile(file)):
		count +=1
		file = 'screen%d.' % (count)
		file += extentions[count].lower()
	myimage.save(file, extentions[count]) 
except AttributeError:
	print "Clipboard is not a string"
