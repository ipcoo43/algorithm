print('''
1부터 20까지의 5의 배수
i = range(1,21) 
몫(m) = int(i/5)
나머지(r) = i - 몫(m) * 5
< i 값이 9일 때 >
m = int(9/5)           # 1
r = 9(값) - 1(몫) * 5  # 4
< i 값이 10일 때 >
m = int(10/5)           # 2
r = 10(값) - 2(몫) * 5  # 0
''')

cnt=0
sum=0
print('i\tcnt\tsum')
for i in range(1,21):
	m = int(i/5)
	r = i - m * 5
	if r == 0:
		cnt = cnt +1
		sum = sum + i
		print('{}\t{}\t{}'.format(i, cnt, sum))