import sys, os, string

class Ping(self):
	def __init__(self):
		
	def help(self):
		print "Help"
		print "[Source] [Destination] [Arguments]"
		print "Arguments"
		print "/? Help"
		print "/f Widescreen"
		print "/o Old iPods Non 640 (Resolution) Compatible"
		print "/d DVD"
		print "/y Automatically Overwrite a file if it already exists"
		print "/w Watch the source video while converting it"
		print "Format"
		print "For DVD support Use /d Arguments and for Source the title"
	def ping(self,ipaddress):
		result = os.popen("ping 192.168.1.1")
		print result.read()