print('''그 시간 사물실에 몇 명 있었나?
출근시간  퇴근시간
09:12:23  11:14:35
10:34:01  13:23:40
10:34:31  11:20:10
특정시간 : 11:05:20
''')

data = [['09:12:23', '11:14:35'],
				['10:34:01', '13:23:40'],
				['10:34:31', '11:20:10']]

input1 = list(map(int,'11:05:20'.split(':')))
input1 = (input1[0]*60+input1[1])*60+input1[2]

count=0
for s,e in data:
	s=list(map(int,s.split(':')))
	e=list(map(int,e.split(':')))
	s = (s[0]*60+s[1])*60+s[2]
	e = (e[0]*60+e[1])*60+e[2]

	if input1 >= s and input1 <= e:
		count += 1

print(count)