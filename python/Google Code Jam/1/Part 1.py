#!/usr/bin/env python

az=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'];

text_file = open("A-small-attempt0.in")
i=0

output=''

for lines in text_file:
	if i!=0:
		output += "Case #%d " % i
	i+=1
	for letters in lines:
		base=ord(letters)-ord('a')
		if(base>=0 and base<=25):
			output += az[base]
		else:
			output += " "

	output += "\n"
	
print output
