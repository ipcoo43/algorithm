print('행고정 열변화')
for row in range(1,6):   # 행
	for col in range(1,6): # 열
		print('({},{})'.format(row,col), end=' ')
	print()
print()

print('열고정 행변화')
for row in range(1,6):   # 행
	for col in range(1,6): # 열
		print('({},{})'.format(col,row), end=' ')
	print()
print()