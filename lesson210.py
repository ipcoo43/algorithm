a,b = 1,1
while(a !=0 and b != 0):
	a, b = input('두 숫자 입력(띄어쓰기 구분) >>> ').split()
	if not len(a) == len(b):
		# 삼항 연산 a의 입력 숫자가 b 보다 크면 a를 반환 그렇지 않으면 b를 반환
		length = len(a) if len(a) > len(b) else len(b)
		c = length - len(a)
		d = length - len(b)
		a = '0' * c + a
		b = '0' * d + b

	carry = 0
	temp = 0
	for c,d in zip(a[::-1],b[::-1]):
		if 10 <= int(c)+int(d)+temp:
			carry += 1
			temp = 1
		else:
			temp = 0
		print('temp', temp)
	if carry == 0:
		print('No carry operation')
	else:
		print(carry,'carry operation')
