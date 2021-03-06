print('''
2에서 100까지 정수 중 소수 15개 구하기
< 에라토스테네스의 체 >
- 2부터 100까지의 수를 나열 한다.
- 자기 자신을 제외한 2의 배수를 모두 지운다
- 남아있는 수 가운데 3은 소수이미로 오른쪽에 3을 쓴다
- 자기 자신을 제외한 3의 배수를 모두 지운다
- 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
''')

n = 100
a = [False, False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
	if a[i]:
		primes.append(i)
		for j in range(2*i, n+1, i):
			a[j] = False
print(primes)