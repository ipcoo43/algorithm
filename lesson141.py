print('1+2+4+7+11+16 합계')
print('a:증가치, i: 각 항, s:합계')

a=0
i=1
s=1

while a<5:
	a=a+1
	i=i+a
	s=s+i
print(s)

i=1
s=0
for a in range(6):
	i=i+a
	s=s+i
print(s)