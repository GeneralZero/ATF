import multiprocessing, math

class Prime(object):
	def __init__(self):
		self.cores = multiprocessing.cpu_count()
		Prime.core_prime_generator(self.startnumber,self.endnumber,self.cores)
		self.primefile = open('prime.txt', 'a')

		self.testnumber = pow(10,100)
		#pow(2,330)
		self.devisor = 2
		self.test = 0
		
	def primetest(self, testnumber):
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
	
	def	multigenerator(self,cores)
		linelist = self.primefile.readlines()
		testnumber = lineList[len(lineList)-1]
		if testnumber == "":
			testnumber == 10
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
					primefile.write(str(testnumber))
					primefile.write("\n")
					print testnumber
					testnumber += 2
					devisor = 2
				elif devisor == 2:
					devisor = 3
					
				else:
					devisor += 2
			

multigenerator(self.cores)	
	'''def core_prime_generator(self,startnumber,endnumber,cores):
		if cores > 1:
			
			if endnumber ==0
				while self.devisor <= self.testnumber:
					self.test = self.testnumber % self.devisor
					if self.test == 0 and self.devisor == 2:
						self.testnumber += 1
						self.devisor = 2
					elif self.test == 0:
						print self.testnumber, "not"
						self.testnumber += 2
						self.devisor = 2
						
					else:
						if self.devisor == (self.testnumber - 2):
							primefile.write(str(self.testnumber))
							primefile.write("\n")
							print self.testnumber
							self.testnumber += 2
							self.devisor = 2
						elif self.devisor == 2:
							self.devisor = 3
							
						else:
							self.devisor += 2
			else:
				while self.testnumber <= endnumber:
					self.test = self.testnumber % self.devisor
					if self.test == 0 and self.devisor == 2:
						self.testnumber += 1
						self.devisor = 2
					elif self.test == 0:
						print self.testnumber, "not"
						self.testnumber += 2
						self.devisor = 2
						
					else:
						if self.devisor == (self.testnumber - 2):
							primefile.write(str(self.testnumber))
							primefile.write("\n")
							print self.testnumber
							self.testnumber += 2
							self.devisor = 2
						elif self.devisor == 2:
							self.devisor = 3
							
						else:
							self.devisor += 2
							'''

