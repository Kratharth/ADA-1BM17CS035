def merge(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
	# divide the array into 2 halves
		l = arr[:mid]
		r = arr[mid:]
	# merge sort the divided arrays
		merge(l)
		merge(r)
		i,j,k = 0,0,0
		while ( i < len(l) and j < len(r)):
			if (l[i]<r[j]):
				arr[k] = l[i]
				i = i + 1
			else:
				arr[k] = r[j]
				j = j + 1
			k = k + 1 
		if ( i == len(l)):
			while ( j < len(r)):
				arr[k] = r[j]
				j = j + 1
				k = k + 1
		elif ( j == len(r)):
			while ( i < len(l)):
				arr[k] = l[i]
				k = k + 1 
				i = i + 1
def printlist(arr):
	print("the sorted order is : ")
	for ele in arr:
		print(ele , end = " ")
	print("\n")

arr = list(map(int , input('enter the numbers').split()))
merge(arr)
printlist(arr)

