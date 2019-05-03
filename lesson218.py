print(''' 3n+1 Problem
n=22이면 22 11 34 17 52 24 13 40 10 5 16 8 4 2 1
''')

def exam(n):
	n = [n]
	while(n[-1]!=1):
		if n[-1] % 2 == 0 :
			n.append(n[-1]//2)
		else:
			n.append(n[-1]*3+1)
	return n
print(exam(22))