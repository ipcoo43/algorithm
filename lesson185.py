print('Dash Insert')
data='4546793'

def DashInsert(str1):
	str1=list(map(int,str1))
	str2=[]
	for i in range(len(str1)-1):
		str2.append(str(str1[i]))
		if str1[i]%2==1 and str1[i+1]%2==1:
			str2.append('-')
		if str1[i]%2==0 and str1[i+1]%2==0: 
			str2.append('*')
	str2.append(str(str1[-1]))
	return "".join(str2)
print(DashInsert(data))