


def search(arr , x):
	n = len(arr)
	
	for i in range (n):
		if arr[i] == x:
			return i
	
	return -1
		





arr = [2, 3, 4, 10, 40]

x = 10


result=search(arr , x)

if result == -1:
	print("no result found")
	
else:
	print("value found at " , result , "position")