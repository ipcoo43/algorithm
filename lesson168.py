sample = '''12.0,12.0,8.0
7.0,8.0,14.0
4.0,5.0,6.0'''

datas = sample.split('\n')
for data in datas:
	a,b,c=map(float,data.split(','))
	su=(a+b+c)/2
	heron=(su*(su-a)*(su-b)*(su-c))**0.5
	result=heron/su
	print(a,b,c,round(result,3))