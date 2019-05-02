print('1부터 20사이 어떤 수로 나누어 떨어지는 가장 작은 수')
print('최소 공배수 : 소인수 분해의 집합')

number = int(input('소인수 분해 >>> '))

def soinsu(n):
	lst = []
	while n>1 :
		for i in range(2,n+1):
			if n%i == 0:
				lst.append(i)
				n = n//i
				break
	return lst
print(soinsu(number))
