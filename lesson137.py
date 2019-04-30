print('1에서 10까지 짝수 합계 %함수 이용')
i=0
s=0
while i<10:
	i=i+1
	if i%2==0:
		s=s+i
print(s)

s=0
for i in range(11):
	if i%2==0:
		s=s+i
print(s)