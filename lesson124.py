nat = list(range(2,101))
prime=[]
while nat:
	n=nat.pop(0)
	prime.append(n)
	nat = [x for x in nat if x % n > 0]
print(prime)