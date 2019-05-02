print('100까지의 자연수의 합의 제곱과 제곱의 합의 차이')

import numpy as np

arr1 = np.arange(11)
print('제곱의 합 =',sum(arr1**2))
print('합의 제곱 =',sum(arr1)**2)
print('합의 제곱 - 제곱의 합 =',sum(arr1)**2 - sum(arr1**2))

sum1=0
sum2=0
for i in range(1,11):
	sum1 += i
	sum2 += i**2
print(sum1*sum1-sum2)

print(abs(sum(range(1,11))**2 - sum(x**2 for x in range(1,11))))