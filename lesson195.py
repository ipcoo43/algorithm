print('palindrome')

max1 = 0
for i in range(10,100):
	for j in range(10,100):
		ij = i * j
		_ij = list(str(ij))
		_ij.reverse()
		if list(str(ij)) == _ij and max1 < ij:
			max1 = ij

print(max1)
