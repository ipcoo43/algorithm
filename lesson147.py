print('소수')

num = 5
j=2
while True:
	if num % j ==0:
		break
	j = j + 1
if num==j:
	print('prime')
else:
	print('no prime')
