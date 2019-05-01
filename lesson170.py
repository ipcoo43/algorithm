print('''메모리공간을 동적으로 사용하여 데이터 관리하기''')

total=0
num = int(input('입력 할 수 >> '))
for i in range(num):
	data = int(input('{} 번 점수 ? '.format(i+1)))
	total += data
print('총점 = {}, 평균 = {}'.format(total, total//num))