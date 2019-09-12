from math import sqrt


def print_graph(arr,length): 
	for i in range(length): 
		for j in range(length): 
			print(arr[i][j],end= " ") 
		print('\n')

def findemptyloc(arr,l,length): 
	for i in range(length): 
		for j in range(length): 
			if(arr[i][j]==0): 
				l[0]=i
				l[1]=j
				return True
	return False
 
def usedinrow(arr,row,num,length): 
	for i in range(length): 
		if(arr[row][i] == num): 
			return True
	return False

def usedincol(arr,col,num,length): 
	for i in range(length): 
		if(arr[i][col] == num): 
			return True
	return False

 
def usedinbox(arr,row,col,num,length): 
	for i in range(int(sqrt(length))): 
		for j in range(int(sqrt(length))): 
			if(arr[i+row][j+col] == num): 
				return True
	return False


def locationissafe(arr,row,col,num,length): 
	
	
	return not usedinrow(arr,row,num,length) and not usedincol(arr,col,num,length) and not usedinbox(arr,row - row % int(sqrt(length)), col - col % int(sqrt(length)),num,length) 


def sudoku_solver(arr,length): 
	l=[0,0] 
	
		 
	if(not findemptyloc(arr,l,length)): 
		return True
	
	
	row=l[0] 
	col=l[1] 
	
	for num in range(1,length+1): 
		if(locationissafe(arr,row,col,num,length)): 
			arr[row][col]=num 
			if(sudoku_solver(arr,length)): 
				return True

			arr[row][col] = 0
			
			 
	return False

if __name__=="__main__": 
	
	size = int(input('enter the number of rows'))
	graph = []
	for i in range(size):
		l = list(map(int,input('enter the numbers per row').split()))		
		graph.append(l)
	print(graph)
	# if success print the grid 
	if(sudoku_solver(graph,size)): 
		print_graph(graph,size) 
	else: 
		print ("solution doesnt exist")



			



