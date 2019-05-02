print('Fibonacci numbers')

x,y=[0,1]
s=0
while y<=100:
	x += y
	y,x=x,y
	if y%2==0:
		s += y
print(s)