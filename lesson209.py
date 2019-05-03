print('''Arimary Arithmetic
한 자리 올림이 몇 번 발생하는가
123 + 456 = No carry
555 + 555 = 3 carry
123 + 594 = 1 carry
''')

a,b = input('숫자를 띄어쓰기로 두 숫자 입력 >>').split()
print(a,b)

carry = 0
temp=0 # 숫자 올림있을 때 위에 쓰는 숫자
for c,d in zip(a[::-1],b[::-1]):
	if 10 <= int(c) + int(d) + temp:
		carry += 1
		temp = 1
	else :
		temp = 0
	print('temp: ', temp)

print('carry :', carry)
print()

a='1234'
for i in a[::-1]:
	print(i)