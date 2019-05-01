print('''Duplicate Numbers
입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인
sample inputs: 0123456789 01234 01234567890 6789012345 012322456789
sample outputs: true false false true false
''')

data = "0123456789 01234 01234567890 6789012345 012322456789"
num = [''.join(sorted(x)) for x in data.split()]
for i in num:
	if i=='0123456789':
		print(True,end=' ')
	else:
		print(False,end=' ')
print()

print(list(map(lambda x:len(set(x))==10 and len(x)==10, data.split())))

for ca in data.split():
	check = [0 for i in range(10)]
	for s in ca:
		check[int(s)] += 1
	print(sum(check) == 10 and all(check), end=' ')
print()

lst = data.split()
for i in lst:
	lst_sorted = sorted(i.replace('',' ').split())
	if lst_sorted == sorted(set('0123456789')):
		print('True',end=' ')
	else:
		print('False',end=' ')
print()


