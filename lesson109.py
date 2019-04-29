for x in range(2,11):
	print(x,end='은(는) ')
	for y in range(2,10):
		if x%y==0:
			print(y,end='의 배수, ')
	print()
print()

basu=2
while basu < 10:
	print('%s의 배수 = {'%(basu), end='')
	for i in range(1,21):
		if i%basu == 0:
			print(i,end=',')
	print('}')
	basu = basu + 1