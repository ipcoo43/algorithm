i=0
s=0
sw=0

while i<10:
	i=i+1
	if sw==0:
		s=s+i*i
		sw=1
	else:
		sw=0
print(s)