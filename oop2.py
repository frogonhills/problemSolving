#!/usr/bin/env python3


class Employee:
	
	
	
	
	rise_ammount= 1.04
	def __init__(self ,  first , last , pay):
		
		self.first = first
		self.last = last 
		self.pay = pay
		self.email = first + "." + last + "@company.com"
		
		
		
	def fullName(self):
		
		return '{} {}'.format(self.first, self.last)
	
	
	
	def apply_raise(self):
		
		self.pay = int(self.pay * self.rise_ammount)




			
	
	@classmethod
	
	def set_rise_ammount(cls, ammount):
		cls.rise_ammount = ammount
		
		
	
	
	
	
emp1 = Employee("shifat", "Ahmed", 80000)
print(emp1.email)


print(Employee.fullName(emp1))
print(emp1.fullName())



print(emp1.pay)
emp1.rise_ammount = 2.3
emp1.apply_raise()
print(emp1.pay)


		