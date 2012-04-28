import math

class prime():
	def __init__(self):
		self.primefile = open('prime.txt', 'w')
		self.testnumber = pow(10,100) #pow(2,330)
		self.devisor = 2
		self.test = 0
		self.prime = 1
	def prime_generator(self,start,stop)
		while start <= stop:
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
					self.primefile.write(str(self.testnumber))
					self.primefile.write("\n")
					print testnumber
					self.testnumber += 2
					self.devisor = 2
				elif self.devisor == 2:
					self.devisor = 3
					
				else:
					self.devisor += 2
	
	def prime_tester(self,test)
		if test > 0:
			while self.testnumber <= test:
				self.test = self.testnumber % self.devisor
				if self.test == 0 and self.devisor == 2:
					self.testnumber += 1
					self.devisor = 2
					self.prime = 0
				elif self.test == 0:
					self.testnumber += 2
					self.devisor = 2
		else:
			print "Input number is either negitive or Zero"

	def clear_varables(self)
		self.test = 0
		self.testnumber = 0
		self.prime = 1
		self.devisor = 2