print('''지뢰찾기
**...  **100
.....  33200
.*...  1*100
''')

M,N=map(int,input('두 숫자(M*N)을 입력하세요 >>> ').split())
matrix = []
for m in range(M):
	matrix.append(list(input('>>> ')))

print(matrix)

lst1 = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for m in range(M):
	for n in range(N):
		if matrix[m][n] == '*':
			continue
		elif matrix[m][n] == '.':
			count = 0
			for x,y in lst1:
				try:
					if (matrix[m+x][n+y] == '*') and m+x >= 0 and n+y >= 0 :
						count += 1
				except Exception as e:
					pass
			matrix[m][n] = str(count)
		else:
			print('[err]데이터가 잘 못 됐습니다.')

for m in matrix:
	print(''.join(m))