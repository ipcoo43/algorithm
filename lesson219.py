print(''' 3n+1 Problem
1 10 => 20
100 200 => 125
201 210 => 89
900 1000 => 174
''')

def exam(n):
	n = [n]
	while(n[-1]!=1):
		if n[-1] % 2 == 0 :
			n.append(n[-1]//2)
		else:
			n.append(n[-1]*3+1)
	return len(n)

i,j = map(int,input('i, j (공백사용 두 숫자 입력) >>>').split())
print(max([exam(n) for n in range(i,j)]))