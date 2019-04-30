import pprint

matrix=[[0]*5 for i in range(5)]
k=0
i=0
while i<5:
	j=0
	while j<5:
		k=k+1
		matrix[i][j]=k
		j=j+1
	i=i+1

pprint.pprint(matrix)