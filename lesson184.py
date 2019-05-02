print('10~100까지 각 숫자 분해')

sum1=0
for row in range(10,1001):
	map_row = map(int,str(row))
	num = 1
	for col in map_row:
		num *= col
	sum1 += num
print(sum1)