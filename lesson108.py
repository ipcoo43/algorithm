print('''배수 판별하면 배수 구하기.
배수 = 그 수를 나눠 떨어지는 수
15는 3의 배수 = 15/3 = 5로 나눠떨어짐 3의 배수
2의 배수 => 15 % 2 = 0
3의 배수 => 15 % 3 = 0
4의 배수 => 15 % 4 = 3
5의 배수 => 15 % 5 = 0
< 1부터 20까지의 수 중에서 5의 배수 구하기 >
''')

cnt=0
sum=0
for i in range(1,11):
	if i % 5 == 0:
		cnt = cnt + 1
		sum = sum + i
		print('{}\t{}\t{}'.format(i,cnt,sum))
print()