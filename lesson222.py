print('''그 시간 사물실에 몇 명 있었나?
출근시간  퇴근시간
09:12:23  11:14:35
10:34:01  13:23:40
10:34:31  11:20:10
특정시간 : 11:05:20
''')

import pandas as pd
data = [['09:12:23', '11:14:35'],
				['10:34:01', '13:23:40'],
				['10:34:31', '11:20:10']]

input1 = pd.to_datetime('11:05:20')
count=0
for s,e in data:
	s = pd.to_datetime(s)
	e = pd.to_datetime(e)
	if input1 >= s and e >= input1:
		count +=1
print(count)