print('Printing OXs')

num=6
for i in range(1,num+1):
	print('o'*(num-i)+('x'*i))


print('\n'.join(['o'*(6-i-1)+'x'*(i+1) for i in range(6)]))
print((lambda n:'\n'.join('o'*(n-i)+'x'*i for i in range(1,n+1)))(int(input('>>> '))))


try:
	line=int(input('>>> '))
except IOError as err:
	print(str(err))

for i in range(1, line+1):
	print('o'*(line-i)+('x'*i))