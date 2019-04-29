print('''
< 소수(prime number)의 개념 >
- 1보다 큰 양의 정수 중에서 1과 자기 자신만으로 나누어 떨어지는 수
- 1과 자신 이외는 약수가 없는 수
- 2의 약수 : 1,2    (o)
- 3의 약수 : 1,3    (o)
- 4의 약수 : 1,2,4  (x)
- 5의 약수 : 1,5    (o)
''')

j = 1
num = 7
while j < num :
	j=j+1
	if num%j == 0:
		if num == j:
			print('{}은 소수 입니다.'.format(num) )
		else:
			print('{}은 소수가 아닙니다'.format(num))
			break