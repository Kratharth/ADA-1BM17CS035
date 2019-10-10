def printlist(arr,x,y,length,stri):
	c = 1
	for i in range(x+1):
		for j in range(y+1):
			print(arr[i][j],end= " ")
		print('\n')
	for i in range(1,x+1):
		for j in range(1,y+1):
			if arr[i][j] == c and c <= length :
				print(stri[i-1])
				c = c + 1
				break
		 		
	

def lcs(x,y):
	m = len(x)
	n = len(y)
	arr = [[0]*(n+1)for x in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				arr[i][j]=0
			elif x[i-1] == y[j-1]:
				arr[i][j] = 1 + arr[i-1][j-1]
			else :
				arr[i][j] = max(arr[i-1][j],arr[i][j-1])
	print(arr[m][n])
	printlist(arr,m,n,arr[m][n],x)


if __name__ == "__main__":
	str1 = input('enter the first string').strip()
	str2 = input('enter the second string').strip()
	lcs(str1,str2)
