def issafe(i,j):
	global rows
	global cols
	global marked
	global graph
	if i >= 0 and i < rows and j>=0 and j<cols:
		if graph[i][j] == 1 and marked[i][j] == 0:
			print('Entering'+' '+str(graph[i][j])+' '+'at '+str(i)+' '+str(j))
			marked[i][j]=1
			return True
		else:
			marked[i][j]=1
			return False
	else:
		return False


def des(i,j):
	global marked
	global count
	marked[i][j] = 1
	if issafe(i-1,j-1):
		des(i-1,j-1)
	if issafe(i-1,j):
		des(i-1,j)
	if issafe(i-1,j+1):
		des(i-1,j+1)
	if issafe(i,j-1):
		des(i,j-1)
	if issafe(i,j+1):
		des(i,j+1)
	if issafe(i+1,j-1):	
		des(i+1,j-1)
	if issafe(i+1,j):	
		des(i+1,j)
	if issafe(i+1,j+1):
		des(i+1,j+1)



graph = []
marked = []
rows = int(input('enter the number of rows'))
cols = int(input('enter the number of columns'))
count = 0
# matrix input
print('enter the matrix (one row in one line)')
for i in range(rows):
	lis=list(map(int,input('enter the '+str((i+1))+'row').split()))
	graph.append(lis)

# marking the entire matrix as zero

for i in range(rows):
	lis = [0]*cols
	marked.append(lis)
print(marked)
print(graph)
# checking for number of islands
for i in range(rows):
	for j in range(cols):
		if marked[i][j] == 0:
			if graph[i][j] == 1:
				print("entering" + str(i) + " " + str(j))
				count = count + 1
			des(i,j)
print(count) 		
