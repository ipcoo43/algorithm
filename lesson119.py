n=100
composites = []
prime = 2
i = 3

while i <= n :
	if i not in composites:
		print(i,end=',')
		prime = prime + 1
		j = i
		while j <= (n/i) :
			composites.append(i*j)
			j = j + 1
	i = i + 2
print(i,end=',')
print()
