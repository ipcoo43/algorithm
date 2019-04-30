import pprint

print('행고정 열변화 직각 삼각형 모양')
matrix=[[0]*5 for i in range(5)]
i=0
for row in range(5):
	for col in range(row+1):
		i=i+1
		matrix[row][col]=i
pprint.pprint(matrix)
print()


matrix=[[0]*5 for i in range(5)]
i=0
for row in range(5):
	for col in range(row,5):
		i=i+1
		matrix[row][col]=i
pprint.pprint(matrix)
print()


matrix=[[0]*5 for i in range(5)]
i=0
for row in range(5):
	for col in range(5-row):
		i=i+1
		matrix[row][col]=i
pprint.pprint(matrix)
print()

matrix=[[0]*5 for i in range(5)]
i=0
for row in range(5):
	for col in range(4-row,5):
		i=i+1
		matrix[row][col]=i
pprint.pprint(matrix)
print()