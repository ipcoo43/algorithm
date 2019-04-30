print('행고정 열변화')
import pprint
matrix = [[0]*5 for i in range(5)]
i=0
for row in range(5):
	for col in range(5):
		i=i+1
		matrix[row][col]=i

pprint.pprint(matrix)