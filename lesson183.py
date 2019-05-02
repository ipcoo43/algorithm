print('1~1000에서 각 숫자의 개수 구하기')

data = str(list(range(1,101)))
for i in '0123456789':
	print('{} : {}개'.format(i,data.count(i)))

