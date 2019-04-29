print('''1에서 100까지에서 3의 배수이면서 5의 배수인 수 구하기
- 공배수 : 3의 배수이기도하고 5의 배수인 수
''')

i=0
su1=0
su2=0
su3=0
print('3과 5의 공배수 = {', end='')
while i < 100:
	i = i + 1
	su1 = i % 3
	su2 = i % 5
	su3 = su1 + su2
	if su3 == 0:
		print(i,end=',')
print('}')