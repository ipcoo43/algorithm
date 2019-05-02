print('2진법으로 자연수 나타내기')
print('73=64(2**6)+8(2**3)+1(2**0)')

number = int(input('어떤 자연수 >> '))
print(str(bin(number))[2:])

str2 = ''

i=0
while (number > 2**i):
	i += 1
i -= 1

while i>-1:
	if  number >= (2**i):
		number -= 2**i
		str2 += '1'
	else:
		str2 += '0'
	i -= 1

print(str2)