def printsol(d,n):
	for i in range(n):
		for j in range(n):
			print(d[i][j],end = " ")
		print('\n')

def floyd(w,n):
	d = w
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d[i][j]=min(d[i][j],d[i][k]+d[k][j])
	printsol(d,n)
if __name__ == "__main__":
	graph = []	
	n = int(input('Enter the number of nodes'))
	print('enter the input one line at a time')
	for i in range(n):
		lis = list(map(int,input().split()))
		graph.append(lis)
	floyd(graph,n)
