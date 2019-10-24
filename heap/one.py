def checkheap(arr):
	n = len(arr)
	for i in range((n//2)):
		if (2*i+1) < n and ((2*i)+2)<n:
			if arr[i]<max(arr[2*i+1],arr[(2*i)+2]):
				return False
		elif (2*i+1)<n and ((2*i)+2)>=n:
			if arr[i] < arr[2*i+1]:
				return False
		elif (2*i+1)>=n and ((2*i)+2)<n:
			if arr[i] < arr[(2*i)+2]:
				return False
	return True

if __name__ == "__main__":
	numbers = list(map(int,input('enter the numbers').split()))
	print(checkheap(numbers))





