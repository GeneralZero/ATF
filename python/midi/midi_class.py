#!/usr/bin/env python
def string_to_num(string):
	ret =0
	for char in string:
		ret = (ret << 8) + ord(char)
	return ret
	
class Midi_File():
	def __init__(self, file_name):
		self.load_file(file_name)
		self.midi_tracks = []
		
		class Midi_Track():
			def __init__(self, size=0, bpm, d_time):
				self.size = size #Seems that its mostly wrong but put it in there so i have it just in case
				self.delta_time
				self.beats_per_mesure = 0
				self.midi_message = []
		
	def load_file(self, file_name):
		midi_file = open(file_name, "rb") # open file in binary mode
		if(midi_file.read(4) != "MThd"): # validate File Header
			raise TypeError("not a valid Midi File")
			
		'''Start Header to Midi File	 '''
		header_size = string_to_num(midi_file.read(4))
		self.midi_type, num_tracks, self.ticks_per_quarternote = [string_to_num(midi_file.read(2)) for x in xrange(0,header_size/2)]
		'''End Header to Midi File '''
		
		#for x in xrange(0, num_tracks):
		'''Start Header to Midi Track '''
		if(midi_file.read(4) != "MTrk"): # validate Track Header
			raise TypeError("not a valid Midi Track")
		'''End Header to Midi Track '''
		
		temp = Midi_Track(size = string_to_num(midi_file.read(4), d_time = string_to_num(midi_file.read(1)))
		if string_to_num(midi_file.read(2)) == 0x00FF:
			header_size = string_to_num(midi_file.read(1))
			if header_size = 0x58:
				temp.beats_per_mesure, temp.beat_note, temp.ticks_per_quarter_note = [string_to_num(midi_file.read(2)) for x in xrange(0,header_size/2)
			elif header_size = 0x59:
				temp.sharp_flat, temp.mode = [string_to_num(midi_file.read(2)) for x in xrange(0,header_size/2)
			else:
				raise TypeError("Unknown Header type")
			self.midi_tracks.append(temp)
		
		
		
if __name__ =="__main__":
	Midi_File("Bass_sample.mid")
