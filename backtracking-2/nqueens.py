def nqueen(queennumber,totalqueens):
	global graph
	for i in range(0,totalqueens):
		if place(queennumber,i):
			graph[queennumber] = i
			if queennumber == totalqueens -1:
				printarray()
			else:
				nqueen(queennumber+1 , totalqueens)

def place(queennumber,position):
	global graph
	global number_of_queens
	for j in range(queennumber):
		if graph[j] == position or (abs(graph[j] - position) == abs(j-queennumber) ):
			return False
	return True

def printarray():
	global number_of_queens
	global graph
	board = []
	for i in range(number_of_queens):
		total = [0] * number_of_queens
		board.append(total)
	for i in range(number_of_queens):
		board[i][graph[i]] = 1
	print(board)


if __name__ == "__main__":
	graph = []	
	number_of_queens = int(input('enter the numnber of queens'))
	if number_of_queens < 4 : 
		print('Solutions doesnt exist')
	else :
		graph = [0] * (number_of_queens)
		nqueen(0,number_of_queens)					
