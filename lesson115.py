print('''
[ 스위치 변수 ]
1/2 - 2/3 + 3/4 - 4/5 + 5/6
''')

k=1
s=0
sw=0

while k < 5 :
	if sw == 0:
		s = s + (k/(k+1))
		sw = 1
	else:
		s = s - (k/(k+1))
		sw = 0
	print('{}/{}\t{:.2f}'.format(k,k+1,s))
	k=k+1