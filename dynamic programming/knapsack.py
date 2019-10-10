
def printarray(arr,n,w):
	for i in range(n+1):
		for j in range(w+1):
			print(arr[i][j],end= " ")
		print('\n')

def knap(W,wt,val,n):
	arr = [[0 for i in range(W+1)]for x in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i==0  or w ==0:
				arr[i][w]=0
			elif wt[i-1]>w:
				arr[i][w] = arr[i-1][w]
			else :
				arr[i][w] = max(arr[i-1][w],(val[i-1]+arr[i-1][w-wt[i-1]]))
	printarray(arr,n,W)	
	return arr[n][W]

if __name__ == "__main__":
	W = int(input('enter the capacity of the sack'))
	wt = list(map(int,input('enter the weight array').split()))
	val = list(map(int,input('enter the value array').split()))
	n = len(val)
	print("The max value is : " + str(knap(W,wt,val,n)))
