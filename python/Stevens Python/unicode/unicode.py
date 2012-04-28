import codecs

somefile = codecs.open('unicode.txt', 'wb', "utf-8")
for i in range(1000):
	somefile.write(unichr(i))
	somefile.write("\t %d\n" %i)
