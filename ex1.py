def ruler(num):	
	for var in range(1,num+1):
		if(var%10==0):
			print(0,end='')
		else:
			print(end=' ')
	print()

	for var in range(1,num+1):
		print((var%10),end='')


number = 50
ruler(number)	
print()		
