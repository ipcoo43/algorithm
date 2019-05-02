print('버전 비교')
from itertools import zip_longest

def version_cmp(left1,right1):
	left2 = map(int,left1.split('.'))
	right2 = map(int,right1.split('.'))
	for left,right in zip_longest(left2,right2,fillvalue=0):
		if int(left) < int(right):
			return (left1+'<'+right1)
		elif int(left) > int(right):
			return (left1+'>'+right1)
	else:
		return (left1+'='+right1)

print(version_cmp('0.0.2','0.0.1'))
print(version_cmp('1.0.3','1.0.10'))
print(version_cmp('1.2.0','1.1.99'))
print(version_cmp('1.0.1','1.0.1'))