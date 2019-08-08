def search(a,ele):
	start= 0
	end=len(a)-1
	while start<= end:
		mid = ( start + end )/2
		if (ele == a[mid]):
			return 1
		elif (ele > a[mid]):
			start = mid+1
		
		else:
			end = mid - 1
	return -1
f = open('search.txt')
testcases = int(f.readline())
for i in range(0,testcases):
	lis2 = list(f.readline())
	b = int(lis2[2])
	lis3 = list(f.readline())
	lis4 = []
	for i in lis3:
		if(i != ' ' and i != '\n'):
			lis4.append(int(i))
	a = search(lis4 , b)
	print(a)

	
