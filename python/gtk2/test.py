#PyGTKtest.py

import pygtk
pygtk.require('2.0')
import gtk
import hashlib
import os

class HelloWorld:
	def hello(self,widget, event,data=None):
		print "Hello World"
		
	def calculateSHA1(self, widget,event,data = None):
		sha = hashlib.sha1(self.string)
		print sha.hexdigest()
	
	def destroy(self,widget, data=None):
		print "destroy event occured"
		gtk.main_quit()
		
	def __init__(self):
		self.string  = "Hello World"
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_border_width(10)
		#button
		self.SHA1Button = gtk.Button("Calculate SHA-1")
		self.EXITButton = gtk.Button("Exit")
		self.SHA1Button.connect("clicked",self.calculateSHA1,None) 
		self.EXITButton.connect_object("clicked",gtk.Widget.destroy,self.window)
	
		#self.window.add(self.EXITButton)
		self.window.add(self.SHA1Button)
		
		self.SHA1Button.show()
		self.EXITButton.show()
		
		self.window.show()
		
	def main(self):
		gtk.main()
	
if __name__ == "__main__":
	hello = HelloWorld()
	hello.main()