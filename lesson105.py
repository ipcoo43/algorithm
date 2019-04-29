print('''
홀수와 짝수 개수 구하기
even : 짝수 
odd : 홀수
''')

evencnt=0
oddcnt=0
for i in range(1,11):
	if i % 2 == 0:
		evencnt = evencnt+1
	else:
		oddcnt = oddcnt+1

print('enencnt = {}, oddcnt = {}'.format(evencnt, oddcnt))

i=1
even=0
odd=0
while i<=10:
	if i % 2 == 0:
		even = even + 1
	else:
		odd = odd +1
	i = i +1
print('enencnt = {}, oddcnt = {}'.format(evencnt, oddcnt))
