def lettersInNumber(num):
	stringnum = str(num)
	return (helper(stringnum,1))
	
def helper(stringnum,counter):
	stringnum = str(stringnum)
	if(counter ==1):
		if(stringnum[-counter]=="1"):
			return 3
		if(stringnum[-counter]=="2"):
			return 3
		if(stringnum[-counter]=="3"):
			return 5
		if(stringnum[-counter]=="4"):
			return 4
		if(stringnum[-counter]=="5"):
			return 4
		if(stringnum[-counter]=="6"):
			return 3
		if(stringnum[-counter]=="7"):
			return 5
		if(stringnum[-counter]=="8"):
			return 5
		if(stringnum[-counter]=="9"):
			return 4
		if(stringnum[-counter]=="0"):
			return 0 
	if(counter ==2):
		if(stringnum[-counter]=="1"):
			if(stringnum[-(counter-1)]=="1"):
				return 6
			if(stringnum[-(counter-1)]=="2"):
				return 6
			if(stringnum[-(counter-1)]=="3"):
				return 8
			if(stringnum[-(counter-1)]=="4"):
				return 8
			if(stringnum[-(counter-1)]=="5"):
				return 7
			if(stringnum[-(counter-1)]=="6"):
				return 7
			if(stringnum[-(counter-1)]=="7"):
				return 9
			if(stringnum[-(counter-1)]=="8"):
				return 8
			if(stringnum[-(counter-1)]=="9"):
				return 8
			if(stringnum[-(counter-1)]=="0"):
				return 3
		if(stringnum[-counter]=="2"):
			return 6
		if(stringnum[-counter]=="3"):
			return 5
		if(stringnum[-counter]=="4"):
			return 5
		if(stringnum[-counter]=="5"):
			return 5
		if(stringnum[-counter]=="6"):
			return 5
		if(stringnum[-counter]=="7"):
			return 7
		if(stringnum[-counter]=="8"):
			return 5
		if(stringnum[-counter]=="9"):
			return 4
		if(stringnum[-counter]=="0"):
			return 0 
	if(counter ==3):
		ret=0
		if(stringnum[-counter]=="1"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="2"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="3"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="4"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="5"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="6"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="7"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]=="8"):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]==str(9)):
			ret = helper(stringnum[-counter],counter-2) +7
		if(stringnum[-counter]==str(0)):
			return 0
		if(stringnum[-(counter-1)]=="0" and stringnum[-(counter-2)]=="0"):
			return ret
		else:
			return ret+3
	if(counter==4):
		if(stringnum[-counter]=="1"):
			return helper(stringnum[-counter],counter-3) +8
'''
i=1
sum=0
while(i<1001):
	length = len(str(i))
	while(length!=0):
		sum=sum+ helper(i,length)
		length=length-1
	i=i+1
print sum

'''
i=0
sum=0
while(i<1001):
	length = len(str(i))
	stringi = str(i)
	while(length!=0):
		#print helper(i,length)
		if(length==2 and stringi[-2]=="1"):
			sum=sum+ helper(i,length)
			break
		sum=sum+ helper(i,length)
		length=length-1
	i=i+1
print sum