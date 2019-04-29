composites = []
prime = [2]
i = 3
n = 100
while i <= n:
	if i not in composites:
		prime.append(i)
		j = i
		while j <= (n/i) :
			composites.append(i*j)
			j += 1
	i += 2
print(prime)