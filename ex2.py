import sys
def isWhiteLine(var_string):
	count=0
	flag=False
	for var in var_string:
		if(var==' '):
			count=count+1
		if(var=='\t'):
			count=count+1	
		if(var=='\n'):
			if(count==0):
				flag=True
		
	if(count>=len(var_string)):
		flag=True 	
	return flag


def read_file(filename):
	f=open(filename,"r")
	for line in f:
		if(isWhiteLine(line)==False):
			print(line,end='')
	return

argu=sys.argv[1]
read_file(argu)	
