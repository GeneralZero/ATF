import math

primefile = open('prime.txt', 'w')

testnumber = 6745231
#pow(2,330)
devisor = 2
test = 0


while devisor <= testnumber:
	test = testnumber % devisor
	if test == 0 and devisor == 2:
		testnumber += 1
		devisor = 2
	elif test == 0:
		print testnumber, "not"
		testnumber += 2
		devisor = 2
		
	else:
		if devisor == (testnumber - 2):
			#primefile.write(str(testnumber))
			#primefile.write("\n")
			print testnumber
			testnumber += 2
			devisor = 2
		elif devisor == 2:
			devisor = 3
			
		else:
			devisor += 2
			
