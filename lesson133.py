num = 5
matrix=[[0]*num for i in range(num)]

row=1
col=(num+1)//2
i=1
matrix[row-1][col-1]=i

while i < num*num:
	i = i + 1
	if i % num == 1:
		col = col - 1
	else:
		row = row - 1
		col = col - 1
		if row < 1 : 
			row = num
		if col < 1 : 
			col = num
	matrix[row-1][col-1]=i	

for row in range(0,num):
	for col in range(0,num):
		print('%2d'%matrix[row][col], end=' ')
	print()
