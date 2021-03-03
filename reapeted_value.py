#!/usr/bin/env python3

arr = ['Fahim', 'Tamal	', 'Emruz' ,'Emruz' , 'Kamol', 'Fahim','Emruz' , 'Emruz' ,'Fahim' ,'Tamal' ]


c = 1
for i in range(0, len(arr)):
	for j in range(i +1 , len(arr)):
		if arr[i] == arr[j]:
			
			print(arr[i] , end=" ")
			

