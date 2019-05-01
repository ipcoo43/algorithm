import math
def radius(a,b,c):
	tol=(a+b+c)/2
	return round(math.sqrt(tol*(tol-a)*(tol-b)*(tol-c))/tol,3)

print(radius(12,12,8))