print('소수')

num = 9
chk = True

for i in range(2,num):
	if num % i == 0:
		chk = False
		break

if chk:
	print(num, 'prime')
else:
	print(num, 'no prime')

