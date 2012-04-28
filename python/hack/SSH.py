####
# @Author Jan-Marten de Boer
# @Copyright 2009
# @Description Some program to set up some common SSH tunnels
# @version 1.5
####

import os 
import sys 

## Set some environment variables
tmax = 6 ## Nasty way to tell the number of functions available in the menu
log = './tunnel.log' ## Location of the log file
conf = './tunnel.conf' ## Location of the configuration file

## Functies voorbakken
## It literally stands for "pre-baking functions"
## I'm just creating some common functions to unclutter the code
def init():
	i = 0
	argument = 0
	for arg in sys.argv:
		if(i>0 and arg =="auto"):
			argument = 1
		i += 1
	return argument
			

def clear():
	os.system('clear')

## Pre-bake functions for log entries
def touch(): ## Initialize log
	os.system('touch '+log)
	os.system('chmod 0777 '+log)
	os.system('echo "[-- Session start --]" >> '+log)

def endlog(timestamp):
	os.system('echo "[-- Sessie end ('+str(timestamp)+') --]" >> '+log)

def timestamp():
	os.system('date >> '+log)

def writelog(line):
	os.system('echo "> '+line+'" >> '+log)

def readlog():
	clear()
	print "Read log:: \n\n"
	os.system('tail '+log)
	raw_input()
	clear()

## Pre-bake functions for the configuration
def touchconf():
	os.system('touch '+conf)
	os.system('chmod 0777 '+conf)

def readconf():
	cf = open(conf)
	fileList = cf.readlines()
	cf.close()
	try:
		name = fileList[0]
		name = name[:-1]
	except:
		name = "Not configured"
	return name

def useconf(line):
	cf = open(conf)
	fileList = cf.readlines()
	cf.close()
	try:	
		line = fileList[line]
		line = line[:-1]
	except:
		line = ""
	return line

def flushconf():
	os.system('cat /dev/null > '+conf)

def putconf(content):
	os.system('echo "'+content+'" >> '+conf)


## Create menu
def menu():
	tc = 1
	proxynaam = readconf()
	print "Choose a tunnel type:\n1) AutoProxy ("+proxynaam+")\n2) Configure AutoProxy\n3) Forward port\n4) Set up a SOCKS5 proxy + Forward a port\n5) Read end of log\n6) Quit\n"
	while tc:
		tc2 = 1
		ttype = raw_input("Type [1]: ")
		try:
			ttype = int(ttype)
		except:
			ttype = 0
			tc2 = 0
		ttype = int(ttype)
		
		if(ttype == 0 and tc2):
			functie = 1
			tc = 0
		elif(ttype <= tmax and tc2):
			functie = ttype
			tc = 0

	return functie

## Main functions
def jmxproxy():
	host = useconf(1)
	gebruiker = useconf(2)
	actualport = useconf(3)
	lport = useconf(4)
	clear()
	print "Proxy up!"
	os.system('ssh -nNTx -D '+str(lport)+' '+str(gebruiker)+'@'+str(host)+' -p '+str(actualport)+'')
	clear()
	print "Proxy down!\n\n"

def proxy():
	naam = raw_input("Name: ")
	print "\nLogin settings:"
	host = raw_input("Server: ")
	gebruiker = raw_input("User: ")
	eport = raw_input("Port [22]: ")
	actualport = 22
	if eport != "" and eport != "22": actualport = eport
	writelog("Session=> "+str(gebruiker)+"@"+str(host)+":"+str(actualport))
	print "\nProxy settings:"
	lport = raw_input("Local port: ")
	writelog("Proxy=> ("+str(naam)+") localhost:"+str(lport))
	clear()
	flushconf()
	putconf(naam)
	putconf(host)
	putconf(gebruiker)
	putconf(actualport)
	putconf(lport)
	print "Proxy configured!\n\n"

def forward():
	print "Login settings:"
	host = raw_input("Server: ")
	gebruiker = raw_input("User: ")
	eport = raw_input("Port [22]: ")
	actualport = 22
	if eport != "" and eport != "22": actualport = eport
	writelog("Session=> "+str(gebruiker)+"@"+str(host)+":"+str(actualport))
	cmd = '-nNTx '+str(gebruiker)+'@'+str(host)+' -p '+str(actualport)+''
	print "\nForward:"
	host = raw_input("Host: ")
	eport = raw_input("Port [80]: ")
	print "Forward to: localhost"
	lport = raw_input("Port: ")
	actualport = 80
	if eport != "" and eport != "80": actualport = eport
	writelog("Session=> "+str(lport)+":"+str(host)+":"+str(actualport))
	clear()
	cmd += ' -L '+str(lport)+':'+str(host)+':'+str(actualport)+''
	print "Forward up!"
	os.system('ssh '+cmd)
	clear()
	print "Forward down!\n\n"

def proxyforward():
	print "Login settings:"
	host = raw_input("Server: ")
	gebruiker = raw_input("User: ")
	eport = raw_input("Port [22]: ")
	actualport = 22
	if eport != "" and eport != "22": actualport = eport
	writelog("Session=> "+str(gebruiker)+"@"+str(host)+":"+str(actualport))
	print "\nProxy settings:"
	lport = raw_input("Local port: ")
	writelog("Proxy=> localhost:"+str(lport))
	cmd = '-nNTx -D '+str(lport)+' '+str(gebruiker)+'@'+str(host)+' -p '+str(actualport)+''
	print "\nForward:"
	host = raw_input("Host: ")
	eport = raw_input("Port [80]: ")
	print "Forward to: localhost"
	lport = raw_input("Port: ")
	actualport = 80
	if eport != "" and eport != "80": actualport = eport
	writelog("Session=> "+str(lport)+":"+str(host)+":"+str(actualport))
	clear()
	cmd += ' -L '+str(lport)+':'+str(host)+':'+str(actualport)+''
	print "Proxy+Forward up!"
	os.system('ssh '+cmd)
	clear()
	print "Proxy+Forward down!\n\n"

## Prepare program
clear()
touch()
touchconf()
timestamp()
ts = "+" ## Reserve this for errors

if init():
	writelog("Using AutoProxy")
	try:
		jmxproxy()
	except:
		ts += " - fatal error: jmxproxy()"
else:
	programloop = 1
	while(programloop):
		## Menu aanroepen
		m = menu()
		clear()

		if m == 1:
			writelog("Using AutoProxy")
			try:
				jmxproxy()
			except:
				ts += " - fatal error: jmxproxy()"
		elif m == 2:
			writelog("Setting up AutoProxy")
			try:
				proxy()
			except:
				ts += " - fatale error: proxy()"
		elif m == 3:
			writelog("Use forward")
			try:
				forward()
			except:
				ts += " - fatal error: forward()"
		elif m == 4:
			writelog("Use Proxy+Forward")
			try:
				proxyforward()
			except:
				ts += " - fatal error: proxyforward()"
		elif m == 5:
			writelog("Reading log")
			try:
				readlog()
			except:
				ts += " - fatal error: readlog()"
		elif m == 6:
			programloop = 0

timestamp()
endlog(ts)
