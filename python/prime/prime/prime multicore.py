import math
#import threading
import multiprocessing

#import Queue
#testnumber = pow(10,100)
#pow(2,330)

def PrimeGenerator(startnumber,stopnumber):
	primefile = open('prime.txt', 'w')
	test = 0
	devisor = 2
	while startnumber<= stopnumber:
		if startnumber == 3:
			primefile.write(str(startnumber))
			primefile.write("\n")
			print startnumber
			startnumber += 2
			devisor = 2
		test = startnumber % devisor
		if test == 0 and devisor == 2:
			startnumber += 1
		elif test == 0:
			#print startnumber, "not"
			startnumber += 2
			devisor = 2
			
		else:
			#if startnumber < 10 and  not(devisor == (startnumber - 2)):
			if startnumber == 1 or 3 or 5 or 7:
				primefile.write(str(startnumber))
				primefile.write("\n")
				print startnumber
				startnumber += 2
				devisor = 2
			elif startnumber == 2:
				primefile.write(str(startnumber))
				primefile.write("\n")
				print startnumber
				startnumber += 1
				devisor = 2	
			if devisor == (startnumber - 2):
				primefile.write(str(startnumber))
				primefile.write("\n")
				print startnumber
				startnumber += 2
				devisor = 2
			elif devisor == 2:
				devisor = 3
				#startnumber += 1
				
			else:
				devisor += 2
				#startnumber += 1

def PrimeTester(testnumber):
	devisor = 2
	test = 0
	while devisor < testnumber:
		test = testnumber % devisor
		if test == 0:
			#return testnumber,"is not a Prime number"
			print testnumber,"is not a Prime number"
			break
		if devisor == (testnumber - 2):
			#primefile.write(str(testnumber))
			#primefile.write("\n")
			#return testnumber, "is a Prime number"
			print testnumber, "is a Prime number"
			break
		elif devisor == 2:
			devisor = 3
		else:
			devisor += 2
				




def MultiCoreGenerator(startnumber,stopnumber,cores):		
	processing = (Process(target=PrimeGenerator, args=(startnumber,stopnumber,)) for a in range(cores))
	for p in processing:
		p.start()
	for p in processing:
		p.join()
		

#PrimeGenerator(0,2**9)
#PrimeTester(3**9000+1)
MultiCoreGenerator(0,2**200,4)
