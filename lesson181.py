print('''Printing OXs
000001(1),000011(3),000111(7),001111(15),011111(31),111111(63) 
''')

length = int(input(">>> "))
sum1=1
for i in range(length):
	sum1 = sum1 | 2**i
	char = bin(sum1).count('1')
	print(((length-char)*'o')+(char*'x'))
print()

sum1=1
for i in range(length):
	sum1 = sum1 | 2**i
	char = bin(sum1).count('1')
	print(((length-char)*'x')+(char*'o'))
print()

for i in range(1,length+1):
	print('o'*(length-i)+('x'*i))
print()


