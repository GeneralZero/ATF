import urllib, re
current = '12345'
while True:
	text = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % current).read()
	test = re.findall('[0-9]+', text)
	print test
	if test == []: 
		if re.findall('Divide', text):	current = str(int(current)/2)
		else:	break
	for x in test:
		current = x
print text
