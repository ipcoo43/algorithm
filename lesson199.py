print('''
- 1부터 20까지의 어떤 수로도 나누어지는 수는 1부터 20까지의 최소공배수 입니다.
- 이 수를 인수분해했을 때
- 2의 지수는 4 (16)
- 3의 지수는 2 (9,18)
- 나머지는 (5,7,11,13,17,19)의 지수는 1입니다.
- 따라서 2^4 * 3^2 * 5 * 7 * 11 * 17 * 19 = 232792560
''')

def soinsu(n):  # 소인수 분해 함수
	lst = []
	while n>1 :
		for i in range(2,n+1):
			if n%i == 0:
				lst.append(i)
				n = n//i
				break
	return lst

set1 = set()  # set을 사용해 모든 원소의 고유한 값을 구하고
lst2 = []     # lst2를 사용해서는 전체 리스트를 반환 받는다.
for i in range(2,20+1):
	so = soinsu(i)
	set1=set1 | set(so)
	lst2.append(so)
print('원소의 고유한 값 =',set1)
print('전체 리스트 = ',lst2)

# lis2의 count 함수를 사용해 모든 원소의 최대값을 찾고
# dict를 사용해 이를 정리 한다.
dict1 = dict()  
for i in set1:
	dict1[i] = 0
	for j in lst2:
		if dict1[i] < j.count(i):
			dict1[i] = j.count(i)
print('원소의 최대값 = ',dict1)

# 모든 소인수분해를 종합한 데이터를 연산한다
result = 1
for i in dict1.keys():
	result *= i ** dict1[i]
print('결과 값 = ',result)