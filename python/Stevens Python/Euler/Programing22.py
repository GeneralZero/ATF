
def nameToNum(string1):
	sum=0
	i=0
	while(i<len(string1)):
		sum=sum+lettersToNumbers(string1[i])
		i=i+1
	return int(sum)
	
def lettersToNumbers(char):
	if(char == "A"):
		return 1
	elif(char == "B"):
		return 2
	elif(char == "C"):
		return 3
	elif(char == "D"):
		return 4
	elif(char == "E"):
		return 5
	elif(char == "F"):
		return 6
	elif(char == "G"):
		return 7
	elif(char == "H"):
		return 8
	elif(char == "I"):
		return 9
	elif(char == "J"):
		return 10
	elif(char == "K"):
		return 11
	elif(char == "L"):
		return 12
	elif(char == "M"):
		return 13
	elif(char == "N"):
		return 14
	elif(char == "O"):
		return 15
	elif(char == "P"):
		return 16
	elif(char == "Q"):
		return 17
	elif(char == "R"):
		return 18
	elif(char == "S"):
		return 19
	elif(char == "T"):
		return 20
	elif(char == "U"):
		return 21
	elif(char == "V"):
		return 22
	elif(char == "W"):
		return 23
	elif(char == "X"):
		return 24
	elif(char == "Y"):
		return 25
	elif(char == "Z"):
		return 26
	else:
		return 0
		
def sortlist(filename):
	namefile = open(filename)
	lists= namefile.readline().replace('\"','').split(',')
	sortedlist = sorted(lists,key=str.upper)
	return sortedlist
		
lists = sortlist("names.txt")
print lists
i=1
sum=0
for name in lists:
	a=i*nameToNum(name)
	sum=sum+a
	print nameToNum(name), i, name,a
	i=i+1
print sum