import os, sys
from optparse import OptionParser
#from threading import Thread
#import subprocess
'''
if os==windows:
	
elif os==linux:
	
else:
'''

parser = OptionParser()		
parser.add_option("-p", "--port", dest="port", action="store_true", default=False, help="Specify Port number or range.")
parser.add_option("-f", "--portfile", dest="portfile", help="read from IP:PORT FILE")
parser.add_option("-0", "--outfile", dest="outfile" , help="write output to FILE")
options, args = parser.parse_args()

arguments = parser.parse_args()

for i in arguments:
    if arguments[i] == "portfile":
        print argument[i]
    elif arguments[i] == "outfile":
        print arguments[i]
    elif arguments[i] == "port":
        print arguments[i]
    else:
        print "end"
    

print arguments[0]
print arguments[1]	
	
	