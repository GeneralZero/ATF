import os, sys
from optparse import OptionParser
#from threading import Thread
#import subprocess
'''
if os==windows:
	
elif os==linux:
	
else:
'''


use = "Usage: %prog [options] argument1 argument2"
parser = OptionParser()		
parser.add_option("Usage: %prog [options] argument1 argument2")
parser.add_option("-p", "--port", dest="port", action="store_true", default=False, help="Specify Port number or range.")
parser.add_option("-f", "--file", dest="read", help="read from IP:PORT FILE")
parser.add_option("-0", "--outfile", dest="write" , help="write output to FILE")
options, args = parser.parse_args()
	
print options.write
print args[0]
print args[1]	
	
	
	'''def __help__(self):
		Ping.help()
		
	def help(self):
		print "Help"
		print "[Source] [Destination] [Arguments]"
		print "Arguments"
		print "/? Help"
		print "/p Port"
		print "/f file of IP:Port or IP"
		print "/o output file"
		
	def pingip(self,ipport):
		
	def threadip(self,ipport,threads):
		if threads == "" or threads == 0:
			threads = 0
		
		
		
	def processip(self,ipport,threads):


num_threads = 4
queue = Queue()
ips = ["10.0.1.1", "10.0.1.3", "10.0.1.11", "10.0.1.51"]
#wraps system ping command
def pinger(i, th):
    """Pings subnet"""
    while True:
        ip = th.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit    
queue.join()"""
