print('''농장 분할
[ 640  400 40 ]
 - 640 소인수 분해 = 2**7, 5**1
 - 400 소인수 분해 = 2**4, 5**2
 - 최대 공약수 2**4 * 5**1 = 80
 - 정사 각형 = 80 * 80 = 1600
 - 640 * 400 / 1600 = 40 
[ 1980 640 3168 ]
''')

def soin(n):
	lst = []
	while n>1 :
		for i in range(2,n+1):
			if n%i == 0:
				lst.append(i)
				n = n//i
				break
	return lst

def gongYak(n1, n2): # 최대 공약수
	set1 = set()
	lst1 = []
	for i in [n1,n2]:
		so = soin(i)
		set1 = set1 | set(so)
		lst1.append(so)
	dict1=dict()
	for i in set1:
		dict1[i] = 1000
		for j in lst1:
			if dict1[i] > j.count(i):
				dict1[i] = j.count(i)
		result =1
		for i in dict1.keys():
			result *= i ** dict1[i]
	return result

n1, n2 = map(int,(input('가로,세로 입력 >>> ').split(',')))
print('최대 공약수 =', gongYak(n1,n2))
print(n1*n2//gongYak(n1,n2)**2)

