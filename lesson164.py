data = [-1, 1, 3, -2, 2]

alist = [i for i in data if i<0]
blist = [i for i in data if i>=0]
print(alist+blist)

print([i for i in data if i<0]+[i for i in data if i>=0])

print(sorted(data,key=lambda x: 1 if x>0 else 0))

