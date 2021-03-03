#!/usr/bin/env python3

def countX(lst, x): 
		count = 0
		for ele in lst: 
				if (ele == x): 
						count = count + 1
		return count 


lst = ['Fahim', 'Tamal	', 'Emruz' ,'Emruz' , 'Kamol', 'Fahim','Emruz' , 'Emruz' ,'Fahim' ,'Tamal' ]

for i in range(len(lst)):
	x= lst[i]
	print('{} has revived  {} times'.format(x, countX(lst, x))) 
	
