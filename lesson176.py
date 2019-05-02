print('3이 나타나는 시간')

count=0
for h in range(24):
	for m in range(60):
		if str(h).find('3')!=-1 or str(m).find('3')!=-1:
			count +=60
print(count)

print(len([h for h in range(24) for m in range(60) if str(h).find('3')!=-1 or str(m).find('3')!=-1])*60)