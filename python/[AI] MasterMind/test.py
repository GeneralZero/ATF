import re
import argparse

limit = 5

def get_numbers():
	test = raw_input('Test:')
	test = re.findall(r'\d', re.sub(r'[^\d]', '', test)[:limit])
	while len(test) != limit:
		print "Wrong input string %d" % len(test)
		test = raw_input('Test:')
		test = re.findall(r'\d', re.sub(r'[^\d]', '', test)[:limit])

	print test

parser = argparse.ArgumentParser(description='Mastermind for the Console')
parser.add_argument('-c','--custom_game', help='Define rules of the custom game', required=False, default='yes')
parser.add_argument('-a','--ai', help='Turns AI on', required=False, choices=['on', 'off'], default='off')
parser.add_argument('-g','--gui', help='Uses pygame to run a GUI version', required=False, default='off')
args = vars(parser.parse_args())

if args['custom_game'] != None:
	custom_rules()
if ''.lower(args['ai']) in ('yes','true', 'on'):
	print "AI on"
