print('''
1부터 10까지 짝수 합계
''')

i=0
sum=0
while i<10:
	i=i+1
	if i%2==0:
		sum=sum+i
		print('{}\t{}'.format(i,sum))