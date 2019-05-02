a,b=tuple(map(int,input('가로,세로 입력 >> ').split(',')))

from math import gcd
print(a*b//gcd(a,b)**2)