import re
num = input('>>> ')
regex = re.compile('\d+')
number = regex.search(num)

def sum_digit(number):
	# return sum([int(i) for i in str(number.group())])
	return sum(map(int,str(number.group())))

print(sum_digit(number))