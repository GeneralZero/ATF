import math
import os

class Prime(object):
    def __init__(self):
        self.testnumber = 10#pow(10,100)
        #pow(2,330)
        self.devisor = 2
        self.test = 0
        self.filename = 'prime'
        self.dir = 'prime_output'
        self.primearray=[]
        self.checkDir(self.dir, self.filename)
        
    def checkDir(self, dir, filename):
        try:
                self.primefile = open(dir+'/'+filename+'.txt', 'r+') 
        except IOError:
                os.mkdir(dir)
                #print kool
                self.checkDir()
        #except WindowsError:
        #       print "Directory already exists"
        
    def printToFile(self,input):
        self.primefile.write(str(input))
        self.primefile.write("\n")
        #self.printToScreen(input)
        
    def printToScreen(self,input):
        print input
                                
    def primeTest(self,input):
        foo = 0
        self.devisor=2
        while input-2 >= self.devisor and foo!=1:
                self.test = input % self.devisor
                if self.test == 0:
                        foo = 1
                else:
                        if self.devisor%2 ==1:
                                self.devisor += 2
                        elif self.devisor%2 ==0:
                                self.devisor +=1
        if foo==0:
                self.printToScreen(input)
                
    def primeArrayTest(self):
        x=1
        for primes in self.primefile:
                if len(primes)!=0 and primes !='\n':
                        self.primearray.append(primes[:-1])
                        x=primes[0:primes.find('\n')]
        return x
        
    def primeTest2(self,input):
                testing=0
            #if input == 1 or input == 2 or input == 3:
                #self.printToFile(input)
            #else:
                for primes in self.primefile:
                        print primes
                        if len(primes)!=0 and primes !='\n':
                                x=primes[0:primes.find('\n')]
                                self.test = input % int(x)
                                print "Test:",self.test,'Input:',input,'X:',x
                                if self.test == 0:
                                        testing = 1
                                        break
                if testing !=1:
                        self.printToFile(input)

    def primeTestArray(self,input):
            testing=0
            if input == 1 or input == 2 or input == 3:
                self.primearray.append(input)
                self.printToFile(input)
            else:
                for primes in self.primearray:
                        #print primes
                        if (primes !=1):
                                test = input % primes
                                if test == 0:
                                        testing = 1
                if testing !=1:
                        self.primearray.append(input)
                        self.printToFile(input)

p=Prime()
kool= int(p.primeArrayTest())
kool+=1
while kool<100:
        p.primeTest2(kool)
        kool+=1