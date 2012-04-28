def binfix(bin,n):
	while(len(bin)<n+1):
		bin="0"+bin
	return bin


num=40

i=0
count =0
binarystring = binfix(bin(count).replace("b",''),num)
while(1):
	if(binarystring.count("1") == (num)/2):
		i=i+1
		print binarystring,i
	if(len(binarystring)>num+1):
		break
	#if(i%100 ==0):
		#print binarystring,i
	count=count+1
	binarystring = binfix(bin(count).replace("b",''),num)
print i
