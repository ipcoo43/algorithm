print('시저 암호 풀기')

# word = input('word >> ')
# num = input('num >> ')

word, n = 'CAT', 5
AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in word:
	print(AZ[(AZ.find(char)+n)%26], end=' ')
print()

print(''.join([AZ[(AZ.find(char)+n)%26] for char in word]))

print(len(AZ))
print(AZ.find('Z'))
print((AZ.find('Z')+5)%26)
print(ord('A'))
print(chr(65))
print(chr(ord('A')+5))

str2 = ''
for c in word:
	if 91 > ord(c):
		str2 += chr(ord(c)+n)
	else:
		str2 += chr((ord(c)+n)%91+65)
print(str2)
