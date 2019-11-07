coin_index = []
def printcoins(coins,V):
	a = V
	global coin_index
	while a>0:
		print(coins[coin_index[a]],end= " ")
		a = a - coins[coin_index[a]]
	print('\n')



def findamount(coins,n,V):
	global coin_index
	maxsize = float('inf')
	table1 = [0 for x in range(V+1)]
	coin_index = [-1 for _ in range(V+1)]
	table1[0] = 0
	coin_index[0] = 0
	for i in range(1,V+1):
		table1[i]=float('inf')
	for i in range(1,V+1):
		for j in range(n):
			if coins[j]<=i:
				value = table1[i-coins[j]]
				if value!=maxsize and value+1 < table1[i]:
					table1[i] = value + 1
					coin_index[i] = j
	print(table1[V])
	printcoins(coins,V)
	
	
if __name__ == "__main__":
	coins = list(map(int,input('enter the coin denomination').split()))
	n = len(coins)
	V = int(input('enter the value'))
	findamount(coins,n,V)
	
