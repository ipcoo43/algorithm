print('Duplicate Numbers')

datas = '0123456789 01234 01234567890 6789012345 012322456789'.split()

def is_not_duplicate(str1):
	return set(str1) == set('0123456789') and len(str1)==10

for data in datas:
	print(is_not_duplicate(data), end=",")
print()