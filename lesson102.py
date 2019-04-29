print('''선처리 후증가 초기 값
i=1
sum=1''')
i=1
sum=1
while i<5:
	i=i+1
	sum=sum+i
	print('{}\t{}'.format(i,sum))
print()

print('''선증가 후처리 초기 값
i=2
sum=1''')
i=2
sum=1
while i<=5:
	sum=sum+i
	i=i+1
	print('{}\t{}'.format(i,sum))
print()

print('for i in range(1,6)')
sum=0
for i in range(1,6):
	sum=sum+i
	print('{}\t{}'.format(i,sum))