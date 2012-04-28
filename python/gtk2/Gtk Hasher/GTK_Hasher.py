#!/usr/bin/env python
#GTK_Hasher.py
import pygtk
pygtk.require('2.0')
import gtk
import sys
import Hasher

class GTK_Hasher:
	def __init__(self):
		self.hasher = Hasher.Hasher()
		self.accepted = self.hasher.accepted
	
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", lambda w: gtk.main_quit())
		self.window.set_title("Multi Hasher")
		#Window setup

		self.vbox_label = gtk.VBox(False, 5)
		self.vbox_entry = gtk.VBox(False, 5)
		self.hbox = gtk.HBox(False, 5)
		self.window.add(self.hbox)
		self.window.set_border_width(5)
		#Horozontal and vertical boxes setup

		self.txt_label = gtk.Label("Plain Text:")
		self.txt_label.set_justify(gtk.JUSTIFY_LEFT)
		self.hbox.add(self.txt_label)
		#TXT_BOX label

		self.entry = gtk.Entry(max=0)
		self.hbox.add(self.entry)
		
		self.hash_boxes()
			
		self.window.show_all()
		
	def hash_boxes(self):
		self.hbox.add(self.vbox_label)
		
		for hashalgs in self.accepted:
			self.txt_label = gtk.Label(hashalgs.upper() + ":") 
			self.txt_label.set_justify(gtk.JUSTIFY_LEFT)
			self.vbox_label.add(self.txt_label)
		#Hash Algroithum labels
		
		
		self.h_button = gtk.Button("Hash")
		self.vbox_label.add(self.h_button)
		self.h_button.connect("clicked", self.hash_clicked)
		#Hash Button
		
		self.hbox.add(self.vbox_entry)
		
		self.entries = [gtk.Entry(max=0) for hashalgs in self.accepted]
		for entry in self.entries:
			self.vbox_entry.add(entry)
			#Hash Algroruthum TextBoxes
		
		self.c_button = gtk.Button("Cancel")
		self.c_button.connect_object("clicked", gtk.Widget.destroy, self.window)
		self.vbox_entry.add(self.c_button)
		#Cancel Button
	
	def hash_clicked(self, widget, data=None):
		output = self.hasher.multihash(self.entry.get_text())
		#output is a list of the hashes basied on the input
		
		for entry in self.entries:
			entry.set_text(output.pop(0))
		#sets the entry text equel to 
			
def main():
	gtk.main()
	return 0
# If no arguments display gui
if len(sys.argv) == 1:
	GTK_Hasher()
	main()
#If arguments the first argument is hashed
else:
	h = Hasher.Hasher()
	print "UnHashed text:", sys.argv[1]
	for hashes in h.multihash(sys.argv[1]):
		print h.accepted.pop(0)+'\t', hashes
		
