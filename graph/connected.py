
def dfs(vertex):
	global size
	global marked
	global graph
	marked[vertex] = 1
	
	print(vertex , end =" ")
	
	for i in range(size):
		if graph[vertex][i] == 1 and marked[i] == 0:
			dfs(i)
graph = []
size = int(input("enter the total number of vertices"))
marked = [0] * size
print("enter the graph in the form of matrix (if there exists an edge , enter 1 else enter 0 ")

for _ in range(size):
	lis = list(map(int,input().split()))
	graph.append(lis)
print('\n')
for ele in range(size):
	if marked[ele] == 0 :
		dfs(ele)
		print('\n')
