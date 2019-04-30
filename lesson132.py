import pprint
print('''
< 마방진 : 홀수 방진>
- 5*5 : 가로 세로 합 65
- 1행 가운데 3열에서 시작 한다.
- 행 감소(↑), 열 증가(→)
- 0행이 되면 5행으로 변경
- 6열이 되면 1열로 변경
- 5의 배수이면 행만 1증가(↓)
''')

num=5 # 홀수 정방행렬만 가능(3,5,7)
matrix = [[0]*num for i in range(num)] # 배열 생성
row=0               # 시작을 위한 행 설정
col=int(num/2)      # 시작을 위항 열 설정
matrix[row][col]=1  # (0,2) = 1을 넣고 시작

x = 0  # 행 위쪽에 값이 있을 경우 되돌아오기위해 위치를 넣을 변수 생성
y = 0  # 열 오른쪽에 값이 있을 경우 되돌아오기위해 위치를 넣을 변수 생성
for i in range(2,num*num+1):  # 2부터 입력 받은 숫자 변수에 저장 
	x=row           # 행의 위치
	y=col           # 열의 위치
	row = row-1     # 행은 행-1 
	col = col+1     # 열은 열+1
	if row < 0 :    # 행이 0보다 작으면
		row = num - 1 # 행은 입력 받은 숫자 - 1
	if col > num-1: # 열이 입력 받은 숫자-1 보다 크면
		col = 0       # 열은 0이된다.
	if matrix[row][col]==0:  # 배열이 0과 같으면 
		matrix[row][col] = i   # 배열에 i 값을 append한다
	else:                    # 배열이 0이 아니면
		row = x + 1            # 행은 x + 1
		col = y                # 열은 y 
		matrix[row][col] =i    # 배열에 i 값을 append한다

for row in range(0,num):
	for col in range(0,num):
		print('%2d'%matrix[row][col], end=' ')
	print()