print('Fibonacci Numbers')

def fibo(num):
	a,b=[1,2],3
	while (b<=num):
		a.append(b)
		b=a[-1]+a[-2]
	return a

print(fibo(100))
#print(sum(row for row in fibo(fibo(1000)) if i%2==0))