su=2
print('num\tsu\tmok\tnmg')
while su<5:
	for num in range(2,11):
		mok = int(num/su)
		nmg = num - mok*su
		if nmg == 0: 
			print('{}\t{}\t{}\t{}'.format(num,su,mok,nmg))
	su = su + 1