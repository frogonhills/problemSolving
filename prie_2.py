#!/usr/bin/env python3



num = 3


if num > 1 :
	for i in range ( 2,num):
		if (num % 2)==0:
			print("not")
			break
	else:
		print('prime')
		
else:
	print('not')