print('디지털 시계에 하루동안 3이 표시되는 시간을 초로 환산하면 총 몇 초?')

second=0
for hour in range(24):
	for minute in range(60):
		if '3' in str(hour) or '3' in str(minute):
			second += 60
print(second)

second = 0
for hour in range(24):
	if '3' in str(hour):
		second += (60*60)
	else:
		for minute in range(60):
			if '3' in str(minute):
				second += 60
print(second)

print(60*len([hour for hour in range(24) for minute in range(60) if str(hour).find('3') !=-1 or str(minute).find('3') !=-1]))

print(sum('3' in str(h)+str(m) for h in range(24) for m in range(60))*60)

print(sum(60 for m in range(60) for h in range(24) if '3' in f'{h}:{m}'))

print(sum([60 for h in range(24) for m in range(60) if '3' in str(h)+str(m)]))

print(60*len([0 for h in range(24) for m in range(60) if '3' in str(h)+str(m)]))
