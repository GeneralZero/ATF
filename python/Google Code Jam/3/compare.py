#!/usr/bin/env python
import re

fake = open("fake.txt")
real = open("real.txt")

reallist= []
fakelist= []

i=0
for lines in real:
	lines = re.sub(r'\[', '', lines)
	lines = re.sub(r'\]', '', lines)
	lines = re.sub(r'\,', '', lines)
	reallist.append(lines.split())
	
for lines in fake:
	lines = re.sub(r"\[", '', lines)
	lines = re.sub(r"\]", '', lines)
	lines = re.sub(r"\,", '', lines)
	fakelist.append(lines.split())
	
for lines in fakelist:
	if lines in reallist or [lines[1], lines[0]] in reallist:
		pass#print lines, [lines[1], lines[0]]
	else:
		i+=1
		print lines
		
print i

