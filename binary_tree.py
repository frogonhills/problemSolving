#!/usr/bin/env python3

class Node:
	
	def __init__(self , key):
		
		self.left = None
		self.right = None 
		slef.key = key 
		
		
		
	def preorder(self):
		print(self.key , end="")
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()
			
			
			
		
		
		
		
root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)



print("pre order")
root.preorder()
print("inorder")
root.inorder()
print("post order")
root.postorder()