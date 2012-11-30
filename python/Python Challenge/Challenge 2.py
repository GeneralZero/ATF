import re
f = open('new  4.txt')
print re.sub('[^a-z]', '' , f.read())
