import random
import time
def bubble_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				temp = arr[j]
				arr[j]=arr[j+1]
				arr[j+1] =temp
	return arr

def selection_sort(arr):
	for i in range(len(arr)-1):
		pos = i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[pos]:
				pos=j
		temp = arr[pos]
		arr[pos]=arr[i]
		arr[i]=temp
	return arr

arr = []
n = 50000
for i in range(n):
	arr.append(random.randint(0,100))
arr1 = arr

# for bubble

start1 = time.time()
li1 = bubble_sort(arr)
stop1 = time.time()

# for selection

start2 = time.time()
li2 = selection_sort(arr1)
stop2 = time.time()

# subtract

bub = stop1 - start1
sel = stop2 - start2

with open ("graph.txt","a") as f:
	f.write(str(n) + " " + str(bub) + " "+ str(sel) + "\n")
