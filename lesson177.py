print('메모리 공간 동적으로 데이터 관리')

num = int(input('몇 개의 정수 >> '))
count = num
sum1=0
while count:
	count -= 1
	sum1 += int(input('정수 입력 >> '))

print('합계 : {}, 평균 : {}'.format(sum1, sum1/num))