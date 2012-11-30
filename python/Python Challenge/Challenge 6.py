import re, zipfile, urllib
filenum = '90052'
comments =''
zipped = zipfile.ZipFile('..\Downloads\channel.zip')
while True:
	file = zipped.read(filenum+".txt")
	comments += zipped.getinfo(filenum+".txt").comment
	filenum = ''.join(re.findall("[0-9]+", file))
	if filenum == '':
		break
	print filenum
print comments
