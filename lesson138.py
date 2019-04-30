print('1에서 10까지 홀수 제곱')

i=0
s=0

while i<10:
	i=i+1
	if i%2==1:
		s = s+i*i
print(s)

s=0
for i in range(11):
	if i%2==1:
		s=s+i*i
print(s)