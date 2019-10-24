class Node:
	def __init__(self,data,i,j):
		self.data = data
		self.i = i
		self.j = j
		
def heapify(heap,i):
	
	
	
	
	
def findMin(lis,row):
	range1  = float('inf')
	minimum = float('inf')
	maximum = float('-inf')
	heap = []

	for i in range(len(row)):
		t  = Node(lis[i][0],i,1)
		heap.append(t)
		if	


if __name__ == "__main__":
	row = int(input('enter the number of lists'))
	cols = int(input('enter the number of columns'))
	print('enter the lists')
	final_list = []
	for i in range(rows):
		l = list(map(int,input('enter the elements')))
		final_list.append(l)
	findMin(final_list,row)
