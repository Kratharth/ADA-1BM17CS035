def printlist(arr):
	for ele in arr:
		print(ele , end = " ")

def quick(arr,l,h):
	if l < h :
		p = partition(arr,l,h)
		quick(arr , l , p-1)
		quick(arr , p+1 , h)

quick_count = 0
def partition(arr,l,h):
	pos = l
	i = l + 1
	for j in range (l+1,h+1):
		global quick_count
		quick_count += 1
		if arr[j] < arr[pos]:
			arr[i],arr[j] = arr[j],arr[i]
			i+=1
	arr[pos],arr[i-1] = arr[i-1],arr[pos]
	return i - 1

arr = list(map(int , input('enter the elements').split()))
quick(arr,0,len(arr)-1)
print("The sorted array is :")
printlist(arr)
print('\n')
print("the total number of elements in quick sort is " + str(quick_count))

