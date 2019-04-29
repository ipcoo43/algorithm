print(''' 팩토리얼 수열의 합계
5! = 5*4*3*2*1 (=1*2*3*4*5)
i = 1!, 2!, 3!,  4!,  5!   i=i+1
f = 1, 1*2, 2*3, 6*4, 24*5 f=f*i
s = 1, 2,   6,   24,  120  s=s+f
1! = 1*1 = 1
2! = 2*1 = 2
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 =120
''')

n=1
f=1
sum=1

while n < 5:
	n = n+1
	f = f*n
	sum=sum+f
	print('{}\t{}\t{}'.format(n,f,sum))
print()

f=1
sum=0
for i in range(1,6):
	f = f * i
	sum=sum+f
	print('{}\t{}\t{}'.format(i,f,sum))
print()

