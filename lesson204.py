a,b=tuple(map(int,input('가로,세로 입력 >> ').split(',')))
c = a*b
while a:
	a,b = max(a,b) % min(a,b), min(a,b)  # n = gcd(a,b)=b
print(c/b**2) # result = a/gcd(a,b) * b/gcd(a,b) = a*b / gcd(a,b)**2


