import re, sys
for x in re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}' , open('new  5.txt').read()):
	sys.stdout.write(x[4])
