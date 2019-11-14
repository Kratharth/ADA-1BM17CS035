def printsolution(previous,n,distance,graph):
	for i in range(n):
		w = []
		for j in range(n):
			w.append(distance[j])
		p = []
		for k in range(n):
			p.append(previous[k])
		flag = 0
		print("For : "+str(i) +" :",end=" ")
		if w[i] == 0:
			print("0")
		else:
			while w[i] > 0:
				if p[i] == 0 :
					print(str(p[i]) , end= " ")
					flag = 1
					break
				else:
					if graph[p[i]][i] != 999 :
						w[i] = w[i] - graph[p[i]][i]
						print(str(p[i]),end= " ")
						p[i] = p[p[i]]
					elif graph[i][p[i]] != 999 :
						w[i] = w[i] - graph[i][p[i]]
						print(str(p[i]),end= " ")
						p[i] = p[p[i]]
					else:
						w[i] = w[i] - graph[p[i]][i]
						print(str(p[i]),end= " ")
						p[i] = p[p[i]]
			if flag == 0 :
				print("0")
			print('\n') 
					


def printsol(d,n):
	print('\n')
	for i in range(n):
		print(d[i],end=" ")
	print('\n')


def findmin(distance,n,visited):
	mini = 999
	pos = 0
	for i in range(0,n):
		if distance[i] < mini and i not in visited and distance[i]!=0:
			mini = distance[i]
			pos = i
	return pos

def solvedij(visited,n,graph,distance,previous):
	d = findmin(distance,n,visited)
	visited.append(d)
	for i in range(n):
		if graph[d][i] != 0 and graph[d][i]!= 999 and i not in visited :
			if distance[i] > graph[d][i] + distance[d] :
				previous[i] = d
			distance[i] = min(distance[i] ,graph[d][i]+distance[d])
	if len(visited) < n:
		solvedij(visited,n,graph,distance,previous)
	else:
		printsol(distance,n)
		printsol(previous,n)
		printsolution(previous,n,distance,graph)

def dij(node,n,visited,distance,graph,previous):
	for i in range(n):
		distance.append(999)
		previous.append(999)
	distance[0] = 0
	previous[0] = 0
	solvedij(visited,n,graph,distance,previous)

if __name__ == "__main__":
	graph = []
	distance = []
	visited = []
	previous = []	
	n = int(input('Enter the number of nodes'))
	print('enter the input one line at a time')
	for i in range(n):
		lis = list(map(int,input().split()))
		graph.append(lis)
	dij(0,n,visited,distance,graph,previous)

