print('1부터 100까지 소수')
n=100
def isPrime(a):
	if a < 2:
		return False
	for i in range(2,a):
		if a % i == 0:
			return False
	return True

for i in range(n+1):
	if isPrime(i):
		print(i, end=',')
print()