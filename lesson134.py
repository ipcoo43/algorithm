matrix = [[0]*5 for i in range(25)]

# 출력할 값을 담은 변수

# 0행 2열에서 시작 (0,2)
row=0
col=2

for num in range(1,26):   # 1에서 25까지 입력 숫자
	matrix[row][col] = num

	if num % 5 == 0 :       # num가 5의 배수인지 검사
		row = row + 1         # 5의 배수이면 행만 1증가
	else:
		row = row - 1         # 행 감소
		col = col + 1         # 열 증가
		if row <= 1 : row = 5  # 행이 1보다 작으면 5로 바꿈
		if col >= 5 : col = 1  # 열이 5보다 크면 1로 바꿈

for row in range(5):
	for col in range(5):
		print('%2d'%matrix[row][col], end=' ')
	print()

