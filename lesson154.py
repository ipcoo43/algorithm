print('''게시판 페이징
입력 : 총건수(m), 한 페이지에 보여줄 게시물수(n)
출력 : 총페이지수
(m,n,출력) (0,1,0) (1,1,1) (2,1,2) (1,10,1) (10,10,1) (11,10,2)
법칙을 정해서 예외 처리
''')
data = {0:1, 1:1, 2:1, 1:10, 10:10, 11:10}
def CalcNumberOfPages(m,n):
	if m%n>0:
		return m//n+1
	else:
		return m//n

for m,n in data.items():
	print('{}\t{}\t{}'.format(m,n,CalcNumberOfPages(m,n)))
print()

import math
for m,n in data.items():
	print('{}\t{}\t{}'.format(m,n,math.ceil(m/n)))
print()

def board(m,n):
	page = m // n
	if m%n !=0:
		page += 1
	return page
for m,n in data.items():
	print('{}\t{}\t{}'.format(m,n,board(m,n)))
print()

def page(m,n):
	if m%n>0:
		page = 1
	else:
		page = 0
	page = m/n + page
	return page
for m,n in data.items():
	print('{}\t{}\t{:.0f}'.format(m,n,page(m,n)))
print()
