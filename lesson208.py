print('''구글 입사문제
1~10000까지 8이라는 숫자가 총 몇번 나오는가? 
''')

count = 0
for i in range(10000):
	for j in str(i):
		if j == '8':
			count += 1
print(count)

print(str(list(range(10000))).count('8'))

print('''
8*** -> 000 ~ 999 -> 1000
*8** -> 000 ~ 999 -> 1000
**8* -> 000 ~ 999 -> 1000
***8 -> 000 ~ 999 -> 1000
4000개가 답이다.
''')