import math
import multiprocessing
#testnumber = pow(10,100)
#pow(2,330)
primefile = open('prime.txt', 'w')

def PrimeGenerator(startnumber,stopnumber):
	test = 0
	devisor = 2
	end = pow(startnumber,.5)
	while startnumber<= stopnumber:
		test = startnumber % devisor
		if test == 0 and devisor == 2:
			startnumber += 1
		elif test == 0:
			#print startnumber, "not"
			startnumber += 2
			devisor = 2
			
		else:
			if (startnumber == 1 or 3 or 5 or 7):
				writeToFile(startnumber)
				startnumber += 2
				devisor = 2
			elif startnumber == 2:
				writeToFile(startnumber)
				startnumber += 1
				devisor = 2	
			elif devisor >= end:
				writeToFile(startnumber)
				startnumber += 2
				devisor = 2
			elif devisor == 2:
				devisor = 3
			else:
				devisor += 2

def PrimeTester(testnumber):
	devisor = 2
	test = 0
	endnumber = pow(testnumber,.5)
	while devisor < testnumber:
		test = testnumber % devisor
		if test == 0:
			#print testnumber,"is not a Prime number"
			break
		if devisor >= endnumber:
			print testnumber, "is a Prime number"
			break
		elif devisor == 2:
			devisor = 3
		else:
			devisor += 2
def writeToFile(prime):
	primefile.write(str(prime))
	primefile.write("\n")
	print prime
				

	
i=62
while 1:
	PrimeTester(2**i -1)
	PrimeTester(2**i +1)
	print i
	i+=1
