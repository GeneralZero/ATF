#!/usr/bin/env python
#from math import abs

text_file = open("test.txt")

list_from_file=[]
list_possoble=[]

n=0
p=0
results=[]

class var():
	def __init__(self):
		self.nums =0


def globalvar():
	global nums
	nums=0

def magic(limit, score):
	temp =score/3
	#print  temp,(score-temp)/2,score-((score-temp)/2)-temp
	if max(temp,(score-temp)/2,score-((score-temp)/2)-temp)>=limit:
		diff= max_diffrence(limit, temp /2, temp-(temp /2))
		if diff==2:
			s.num = s.nums-1
		#print  temp,(score-temp)/2,score-((score-temp)/2)-temp
		return 1
	elif s.nums>0:
		temp = score-limit
		diff= max_diffrence(limit, temp /2, temp-(temp /2))
		if diff==2:
			#print limit, temp /2, temp-(temp /2), "S:", s.nums
			#print s.nums
			s.num = s.nums-1
			#print s.nums
			return 1
		elif diff<2:
			#print limit, temp /2, temp-(temp /2)
			return 1
	return 0
		
		
def max_diffrence(num1, num2, num3):
	if num1<0 or num2<0 or num3<0:
		return 5 
	#print num1,num2,num3
	return max(abs(num1-num2), abs(num3-num2),abs(num1-num3))

for lines in text_file:
	list_from_file.append(lines.split())
	
#print list_from_file
s=var()
for i, scores in enumerate(list_from_file):
	n=int(scores[0])
	s.nums=int(scores[1])
	p=int(scores[2])
	
	results.append(0)
	
	for x in xrange(1,n+1):
		#print "INFO",p, int(scores[2+x]), s.nums
		results[i]+=magic(p, int(scores[2+x]))
		#print "Case %d" % i,results[i], s.nums
			
for j,x in enumerate(results):
	print "Case #%d:" % (j+1) , x
