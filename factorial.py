#!/usr/bin/env python3



x = abs(int(input("enter a number :")))


factorial = 1

while x > 1:
	factorial = factorial * x
	x = x - 1
	
	
	
print(factorial)