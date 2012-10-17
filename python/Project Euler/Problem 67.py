#!/usr/bin/env python
from time import time

def load_file(file_name):
	list_file = open(file_name)
	ret = []

	lists = list_file.readlines()
	for lines in lists:
		ret.append(lines.split())
	return ret
def run(num_list):
	while len(num_list)> 1:
		for x in range(len(num_list[-2])):
			num_list[-2][x] = max(int(num_list[-2][x]) + int(num_list[-1][x]) , int(num_list[-2][x]) + int(num_list[-1][x+1]))
		del num_list[-1]
	return num_list[0][0]

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 67: ", run(load_file('Problem 67.txt'))
	print "Completed in: %f seconds" % (time() - start)