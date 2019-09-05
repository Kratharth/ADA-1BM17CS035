#global variables
rowNbr = [-1,-1,-1,0,0,1,1,1]
colNbr = [-1,0,1,-1,1,-1,0,1]


def isSafe(adj_mat, row, col, visited_mat):
	if row>=0 and row<n and col>=0 and col<n:
		if adj_mat[row][col]==1  and visited_mat[row][col]== 0:
			return True
	else:
		return False

def dfs(adj_mat, i, j, visited_mat):
	global rowNbr
	global colNbr
	visited_mat[i][j] = True
	for k in range(8):
		if isSafe(adj_mat, i+rowNbr[k], j+colNbr[k], visited_mat):
			if( i!= j):
				dfs(adj_mat, i+rowNbr[k], j+colNbr[k], visited_mat)


if __name__ == "__main__":
	adj_mat	= []
	visited_mat = []
	island_count = 0
	rows = 0
	cols = 0
	rows = int(input('enter the number of rows'))
	cols = int(input('enter the number of columns'))
	for _ in range(rows):
		l = list(map(int, input().split()))
		adj_mat.append(l)
	
	for i in range(rows):
		for j in range(len(adj_mat[i])):
			visited_mat[i][j] = 0	

	for i in range(rows):
		for j in range(len(adj_mat[i])):
			if adj_mat[i][j] == 1 and visited_mat[i][j] == False:
				dfs(adj_mat, i, j, visited_mat)
				island_count += 1
	print(island_count)			
