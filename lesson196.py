a=[1,2,3,4]
a.reverse()
print(a)

b=[1,2,3,4]
b[::-1]
print(b)

max1 = 0
for i in range(10,100):
	for j in range(10,100):
		ij = i * j
		if str(ij) == str(ij)[::-1] and max1 < ij:
			max1 = ij
print(max1)