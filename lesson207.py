print('''넥슨 입사문제
d(91) = 9+1+91 = 101
n을 d(n) generator라고 한다. 91은 101의 제네레이터 이다.
iterator은 next() 메소드를 이용해 데이터에 순차적 접근 가능한 object
generator은 iterator를 생성해 주는 function
iterable는 member를 하나씩 차례로 반환 가능한 object : list, str, tuple
- for loop, zip([iterable,...]), map(function, iterable) - sequence
''')

def d(n):
	for i in str(n):
		n += int(i)
	return n
# 1~5000
a=set(list(range(1,5000))) # a 집합
b=set() # 제너레이터에 대한 집합
for i in a:
	b.add(d(i))

print(sum(a-b))

print(sum(set(range(1,5000))-set(x+sum([int(a) for a in str(x)]) for x in range(1,5000))))