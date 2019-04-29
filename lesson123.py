prime=[]
for i in range(2,101):
	cnt = 0
	for j in range(1,i):
		if i%j == 0:
			cnt += 1
	if cnt < 2:
		prime.append(i)
print(prime)