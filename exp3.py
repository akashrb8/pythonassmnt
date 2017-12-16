def isListOfInts(li):
	flag=False
	for var in li:
		i=0
		if(var[i=i+1].isdigit()):
			if(var.isdecimal()):
				flag=True
		else:
			flag=False
	return flag
#def testlist(var):
#	print(var+"-->"+isListOfInts(var))
print(isListOfInts([1]))
