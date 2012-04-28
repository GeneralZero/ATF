from PIL import ImageGrab
import PIL
import Image
import os


class picToFile(object):
	def __init__(self):
		self.extentions = ["JPEG","PNG","PDF","GIF","BMP"]
		self.count=0
		self.array=0
		self.file = 'screen%d.' % (self.array)
		self.file += self.extentions[self.array].lower()
	
		self.myimage = ImageGrab.grabclipboard()
	def clipToFile(self):
		while(os.path.isfile(self.file)):
			self.count +=1
			self.file = 'screen%d.' % (self.count)
			self.file += self.extentions[self.array].lower()
		self.myimage.save(self.file, self.extentions[self.array]) 
	
	def retclip(self):
		try:
			myimage = ImageGrab.grabclipboard()
		except AttributeError:
			print "Clipboard is not a string"
		return myimage
	def isEquel(self):
		myimage = self.retclip()
		#print myimage
		#print self.myimage
		if(self.myimage!= myimage):
			self.myimage = myimage
			return 0
		else:
			return 1

pic = picToFile()
pic.retclip()