a=0
i=1
j=1
sosu=[]
while i<=100:
	while j<=i:
		if i%j==0:
			a += 1
		j += 1
	if a==2:
		sosu.append(i)
	i += 1
	j=1
	a=0
print(sosu,end=',')
print()