import random
import time
def bubble_sort(arr):
	bub_count = 0
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			bub_count += 1
			if arr[j]>arr[j+1]:
				temp = arr[j]
				arr[j]=arr[j+1]
				arr[j+1] =temp
	return bub_count

def selection_sort(arr):
	sel_count = 0
	for i in range(len(arr)-1):
		pos = i
		for j in range(i+1,len(arr)):
			sel_count += 1
			if arr[j]<arr[pos]:
				pos=j
		temp = arr[pos]
		arr[pos]=arr[i]
		arr[i]=temp
	return sel_count
merge_count = 0
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
			global merge_count
			merge_count += 1
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
arr = []
arr1 = []
arr2 = []
n = 100
for i in range(n):
	arr.append(random.randint(0,100))
arr1 = arr
arr2 = arr
merge(arr2)
print("the total number of comparisons in bubble sort is : " + str(bubble_sort(arr)))
print("the total number of comparisons in selection sort is : " + str(selection_sort(arr1)))
print("the total number of comparisons in merge sort is : " + str(merge_count))



