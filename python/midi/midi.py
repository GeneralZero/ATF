#!/usr/bin/env python
def open_midi_file(file_name):
	''' This function opens the file and checks the headder to make sure that it is a midi file '''
	try:
		midi_file = open(file_name, "rb") # open file in binary mode
		if(midi_file.read(4) == "MThd"):
			return midi_file
		else:
			return None
	except:
		print "Error Reading MIDI file %s" % (file_name)



"""Extra File functions"""
def string_to_num(string):
	ret =0
	for char in string:
		ret = (ret << 8) + ord(char)
	return ret
	

