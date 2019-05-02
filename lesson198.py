print('1부터 20사이 어떤 수로 나누어 떨어지는 가장 작은 수')
print('최소 공배수 : 소인수 분해의 집합')

def soinsu(n):
	lst = []
	while n>1 :
		for i in range(2,n+1):
			if n%i == 0:
				lst.append(i)
				n = n//i
				break
	return lst

set1 = set()
lst2 = []
for i in range(2,10+1):
	so = soinsu(i)
	set1=set1 | set(so)
	lst2.append(so)
print(set1)
print(lst2)

dict1 = dict()
for i in set1:
	dict1[i] = 0
	for j in lst2:
		if dict1[i] < j.count(i):
			dict1[i] = j.count(i)
print(dict1)

result = 1
for i in dict1.keys():
	result *= i ** dict1[i]
print(result)