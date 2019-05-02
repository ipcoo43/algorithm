print('완전수 구하기')

num = int(input('num >> '))

def is_perfectNumber(M):
	sub_multiple = []
	for i in range(1,M):
		if M % i == 0:
			sub_multiple.append(i)
	if sum(sub_multiple)==M:
		return True
	else:
		return False

for j in range(1,num+1):
	if is_perfectNumber(j):
		print(j,end=' ')
print()