print('''
1부터 5까지의 합계
i   = 1, 2, 3, 4, 5...  i=i+1 i에 1씩 누적계산
sum = 1, 3, 6, 10,15... sum=sum+i sum에 i를 누적 계산
< 선증가 후처리 >
while i < 5: (i <= 4)
선증가 : i=i+1
후처리 : sum=sum+i
< 선처리 후증가>
while i <= 5: (i < 6)
선처리 : sum=sum+i
후증가 : i=i+1
''')
print('선증가 후처리 i<5')
i=0
sum=0
while i<5:
	i=i+1
	sum=sum+i
	print('{}\t{}'.format(i,sum))
print('선처리 후증가 i<=5')
i=1
sum=0
while i<=5:
	sum=sum+i
	i=i+1
	print('{}\t{}'.format(i,sum))