#!/usr/bin/env python
import os

lamedir = 'lame'
searchdir = "/var/test"
name = []

for f in os.listdir(searchdir):
	name.append(f)

for files in name:
	iswav = files.find('.wav')
	#print files, iswav
	if(iswav >0):
		print lamedir + ' -h -V 6 ' + searchdir + files + ' ' + searchdir + files[:iswav]+'.mp3'
		os.system(lamedir + ' -h -V 6 ' + searchdir + files + " " + searchdir +  files[:iswav]+".mp3")
