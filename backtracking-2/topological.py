def topological(graph):
	global jobs
	lis = []
	for j in range(num):
		flag = 0
		for i in range(num):
			if graph[i][j] == 0 :
				flag = 0
				rowval = j
			else :
				flag = 1
				rowval = -1 
				break
		if rowval != -1:
			if rowval !=4 :		
				print(rowval)
		
		if flag == 0 :
			for i in range(num):				
				graph[rowval][i] = 0
	print(1)
	print(0)
if __name__ == "__main__":
	graph = []
	jobs = []
	num = int(input('enter the number of pairs'))
	for i in range(num):
		total = list(map(int,input('enter the pairs one line after another').split()))
		jobs.append(total)
	for i in range(num):
		l = [0] * num
		graph.append(l)
	for pair in jobs:
		graph[pair[1]][pair[0]] = 1
	topological(graph)
