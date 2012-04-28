import os
import time
numFile = 0
f=open('wordlist-' + str(numFile) + '.txt', 'w')

def xselections(items, n):
	if n==0: 
		yield []
	else:
		for i in xrange(len(items)):
			for ss in xselections(items, n-1):
				yield [items[i]]+ss

# Numbers = 48 - 57
# Capital = 65 - 90
# Lower = 97 - 122
allreal =range(33,128)
numb = range(48,58)
cap = range(65,91)
low = range(97,123)
choice = 0
while int(choice) not in range(1,9):
	choice = raw_input('''
	1) Numbers
	2) Capital Letters
	3) Lowercase Letters
	4) Numbers + Capital Letters
	5) Numbers + Lowercase Letters
	6) Numbers + Capital Letters + Lowercase Letters
	7) Capital Letters + Lowercase Letters
	8) ALL Normal keys
	: ''')

choice = int(choice)
poss = []
if choice == 1:
	poss += numb
elif choice == 2:
	poss += cap6
elif choice == 3:
	poss += low
elif choice == 4:
	poss += numb
	poss += cap
elif choice == 5:
	poss += numb
	poss += low
elif choice == 6:
	poss += numb
	poss += cap
	poss += low
elif choice == 7:
	poss += cap
	poss += low
elif choice == 8:
	poss += allreal
	
bigList = []
for i in poss:
	bigList.append(str(chr(i)))

MIN = raw_input("What is the min size of the word? ")
MIN = int(MIN)
MAX = raw_input("What is the max size of the word? ")
MAX = int(MAX)
MAX_SIZE_MB = 100
MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024
HOW_OFTEN_CHECK = 1000
count = 0
START_TIME = time.time()
for i in range(MIN,MAX+1):
	for s in xselections(bigList,i):
		count += 1
		f.write(''.join(s) + '\n')
		if count >= HOW_OFTEN_CHECK:
			size = os.path.getsize('wordlist-' + str(numFile) + '.txt')
			if size > MAX_SIZE_BYTES:
				f.close()
				numFile += 1
				f=open('wordlist-' + str(numFile) + '.txt', 'w')
				count = 0
				print 'New File. Current word: ', ''.join(s)

f.close()
END_TIME = time.time()
print 'Time it took to compute files:', END_TIME - START_TIME, 'seconds'\