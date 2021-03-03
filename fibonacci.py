#!/usr/bin/env python3




nterms = int(input("how many times: "))

n1 = 0 
n2 = 1
now = 0
count = 0 

if nterms > 0:
	
	while count < nterms:
		print(n1)
		now = n1+n2
		n1 , n2 = n2 , now
		count = count +1