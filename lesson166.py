data = '''12,12,8
7,8,14
4,5,6'''

def radius(triangles):
	triangles = triangles.split('\n')
	for triangle in triangles:
		a,b,c=map(int,triangle.split(','))
		su = (a+b+c)/2
		r = (su*(su-a)*(su-b)*(su-c))**0.5/su
		print('The radius of the round tabe is: ', round(r,3))

radius(data)