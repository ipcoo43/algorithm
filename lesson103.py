print('''
1부터 10까지 짝수 합계
i=i+2
sum=sum+i
''')
print('선증가')
i=0
sum=0
while i<10:
	i=i+2
	sum=sum+i
	print('{}\t{}'.format(i,sum))
print()

print('선처리')
i=2
sum=0
while i<=10:
	sum=sum+i
	i=i+2
	print('{}\t{}'.format(i,sum))

