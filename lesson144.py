print('1/2+2/3+3/4+4/5 합계')

i=0
s=0

while i<5:
	i=i+1
	s=s+i/(i+1)
print('{:.2f}'.format(s))