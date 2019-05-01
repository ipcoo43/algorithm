data = [-1, 1, 3, -2, 2]
alist = []
blist = []
for num in data:
	if num < 0:
		alist.append(num)
	else:
		blist.append(num)
print(alist+blist)