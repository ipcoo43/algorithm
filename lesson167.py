print('''
The Knights Of The Round Table
- 삼각형의 세 변의 길이를 나타내는 실수 세 개(a,b,c)가 입력된다.
- su = (a+b+c)/2
- heron = (su*(su-a)*(su-b)*(su-c))**0.5
- result = heron / su
- Sample Input : 12.0 12.0 8.0
- Sample Output : 2.828
''')

data = '''12.0,12.0,8.0
7.0,8.0,14.0
4.0,5.0,6.0'''

print('a\tb\tc\tresult')
triangles = data.split('\n')
for triangle in triangles:
	a,b,c = map(float,triangle.split(','))
	su=(a+b+c)/2
	heron=(su*(su-a)*(su-b)*(su-c))**0.5
	result = heron/su
	print('{}\t{}\t{}\t{}'.format(a,b,c,round(result,3)))