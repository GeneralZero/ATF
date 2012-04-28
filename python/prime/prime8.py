import math
primefile = open('prime.txt', 'w')

testnumber = pow(10,100) +1
devisor = testnumber - 1
test = 0


while devisor <= testnumber:
	for num in range(1, 100):
		if testnumber % 2 == 0:
			testnumber += 1
			devisor = testnumber -1
		elif testnumber % 3 == 0:
			testnumber += 1
			devisor = testnumber -1
		elif testnumber % 5 == 0:
			testnumber += 1
			devisor = testnumber -1
		elif testnumber % 7 == 0:
			testnumber += 1
			devisor = testnumber -1
		elif testnumber % 11 == 0:
			testnumber += 1
			devisor = testnumber -1
		else:
			test = testnumber % devisor
			if test == 0:
				testnumber += 1
				devisor = testnumber -1
				
			else:
				if devisor == 2:
					primefile.write(str(testnumber))
					primefile.write( "\n")
					print testnumber
					testnumber += 1
					devisor = testnumber -1
				else:
					devisor -= 1