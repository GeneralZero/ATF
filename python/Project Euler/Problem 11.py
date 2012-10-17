#!/usr/bin/env python
from time import time

def load_file(file_name):
	list_file = open(file_name)
	ret = []

	lists = list_file.readlines()
	for lines in lists:
		ret.append(lines.split())
	return ret

def prod(list_num):
	sums=1
	for x in list_num: 
		sums *= int(x)
	return sums

def largest_box(x, y, size): #size is (Width, Length)
	current_max = [1,1,1,1] 
	for i in range(0,17): # Y axis Down
		for j in range(0,20):
			test_max = [c[i+x][j] for x in range(0,4)]
			if prod(test_max) > prod(current_max): 
				current_max = test_max
	for i in range(0,20): # X axis Right
		for j in range(0,17):
			test_max = [c[i][j+x] for x in range(0,4)]
			if prod(test_max) > prod(current_max): 
				current_max = test_max
	for i in range(0,17): # Back Slash
		for j in range(0,17):
			test_max = [c[i+x][j+x] for x in range(0,4)]
			if prod(test_max) > prod(current_max): 
				current_max = test_max
	for i in range(0,17): # Foward Slash
		for j in range(3,20):
			test_max = [c[i+x][j-x] for x in range(0,4)]
			if prod(test_max) > prod(current_max): 
				current_max = test_max
	return current_max

c = load_file("Problem 11.txt")
if __name__ =="__main__":
	start = time()
	
	print "Answer to Problem 11: ", prod(largest_box(20, 20, (4,4)))
	print "Completed in: %f seconds" % (time() - start)