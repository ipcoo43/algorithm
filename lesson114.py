a=1
b=2
s=0

while a<4:
	s=s+(a/b)
	a=a+1
	b=b+1
	print('{}/{}={:.2f}'.format(a,b,s))