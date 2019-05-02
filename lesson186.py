import re

def DashInsert(str1):
	return re.sub('([1,3,5,7,9]{2,})|([2,4,6,8]{2,})',lambda x:'-'.join(x.group(1)) if x.group(1) else '*'.join(x.group(2)), str1)  

print(DashInsert('4546793'))