



def partition(arr , low , high):
	povit = arr[high]
	i = low-1
	
	
	for j in range(low , high):
		if arr[j] <= povit :
			i=i+1
			arr[i],arr[j] = arr[j] , arr[i]
			
	arr[i+1],arr[high] = arr[high],arr[i+1]
	
	
	return i+1









def quickSort(arr ,  low , high):
	
	if low < high:
		pi = partition(arr , low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1 , high)





data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)