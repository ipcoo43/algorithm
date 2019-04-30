print('1-2+3-4+5-6+7-8+9-10 합계')
i=0
s=0

while i<10:
	i=i+1
	if i%2==1:
		s=s+i
	else:
		s=s-i
print(s)

s=0
for i in range(11):
	if i%2==1:
		s=s+i
	else:
		s=s-i
print(s)

i=0
s=0
sw=0
while i<10:
	i=i+1
	if sw==0:
		s=s+i
		sw=1
	else:
		s=s-i
		sw=0
print(s)