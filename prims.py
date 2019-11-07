def prim(graph,v):
	weight = 0
	vertices = []
	edges = []
	vertices.append(0)
	for i in range(1,v):
		minimum = float('inf')
		index = float('inf')
		start = float('inf')
		for j in vertices:
			for k in range(v):
				if k in vertices:
					continue
				else:
					if graph[j][k] < minimum:
						minimum = graph[j][k]
						start = j
						index = k
		vertices.append(index)
		edges.append((start,index))
		weight+= minimum
	print(edges)
	return weight	

if __name__ == "__main__":
	graph = []
	number = int(input('enter the number of nodes'))
	print('enter the graph one row per line(If an edge doesnt exist,give 999)')
	for i in range(number):
		lis = list(map(int,input().split()))
		graph.append(lis)
	print(prim(graph,number))
