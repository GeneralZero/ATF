import math
import os

class Prime(object):
    def __init__(self):
        self.testnumber = pow(10,100)
        #pow(2,330)
        self.devisor = 2
        self.test = 0
        self.filename = 'prime'
        self.dir = 'prime_output'
        self.checkDir(self.dir, self.filename)
        
    def checkDir(self, dir, filename):
        try:
                self.primefile = open(dir+'/'+filename+'.txt', 'w') 
        except IOError:
                os.mkdir(dir)
                #print kool
                self.checkDir()
        #except WindowsError:
        #       print "Directory already exists"
    def printToFile(self,input):
        self.primefile.write(str(self.testnumber))
        self.primefile.write("\n")
        
    def printToScreen(self,input):
        print input
            
    def primeFromFile(self):
        line = f.readline() # Reading the whole line
        while len(line) !=0:
                return line

    def primeToFile(self):
            i =0
            while 1:
                self.primeTest2(i)
                i+=1

        
    def prime(self):
        while self.devisor <= self.testnumber:
                self.test = self.testnumber % self.devisor
                if self.test == 0 and self.devisor == 2:
                        self.testnumber += 1
                        self.devisor = 2
                elif self.test == 0:
                        #print self.testnumber, "not"
                        self.testnumber += 2
                        self.devisor = 2
                else:
                        if self.devisor == (self.testnumber - 2):
                                self.printToFile(self.testnumber)
                                self.testnumber += 2
                                self.devisor = 2
                        elif self.devisor == 2:
                                self.devisor = 3
                        else:
                                self.devisor += 2
                                
    def primeTest(self,input):
        while input-2 <= self.devisor:
                self.test = self.testnumber % self.devisor
                if self.test == 0:
                        return false
                else:
                        if self.devisor%2 ==1:
                                self.devisor += 2
                        elif self.devisor%2 ==0:
                                self.devisor +=1
        return true
        
    def primeTest2(self,input):
            for line in self.filename:
                self.devisor = int(self.primefile.readline())
                while input-2 <= self.devisor:
                        self.test = self.testnumber % self.devisor
                        if self.test == 0:
                                return false
            return true
            self.printToFile(input)
            
p=Prime()

p.prime()