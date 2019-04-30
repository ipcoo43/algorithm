print('1에서 10까지 홀수/짝수')

i=0
s=0

while i<10:
	i=i+2
	s=s+i
print(s)

s=0
for i in range(0,11,2):
	s=s+i
print(s)
