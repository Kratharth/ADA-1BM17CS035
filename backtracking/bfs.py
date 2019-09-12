def bfs(vis,numnodes,grap,j):
	qu = []	
	vis[j] = 1
	qu.append(j)
	while len(qu) > 0 :
		s = qu.pop(0)
		print( s, end = " ")
		for i in range(numnodes):
			if graph[s][i] == 1 and not vis[i]:
				vis[i] = 1
				qu.append(i)




num_nodes = int(input('enter the number of nodes'))

visited = [0] * num_nodes

graph = []

for i in range(num_nodes):
	l = list(map(int,input('enter the elements one row after another').split()))
	graph.append(l)

for i in range(num_nodes):
	if not visited[i] :
		bfs(visited,num_nodes,graph,i)

