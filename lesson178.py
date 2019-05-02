print('CamelCase를 Pothole_case로 바꾸기')

def camelToPotholeFor(str1):
	str2=''
	for char in str1:
		if char.isdigit() or char.isupper():
			str2 += '_'
		str2 += char
	return str2.lower()

import re
def camelToPotholeRe(str1):
	pat = re.compile('([A-Z0-9])')
	return pat.sub('_\g<1>', str1).lower()


str1='codingDojang'
str2='numGoat30'
print(camelToPotholeFor(str1))
print(camelToPotholeRe(str1))
print(camelToPotholeFor(str2))
print(camelToPotholeRe(str2))

pc=lambda src: re.sub('([A-Z0-9])', lambda m:'_'+m.group().lower(), src)
print(pc(str1))
print(pc(str2))