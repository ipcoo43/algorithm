names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
print(names)
print()

kcnt, lcnt, lee = 0, 0, 0
new_names = []

for name in names:
	if name[0] == '김':
		kcnt += 1
	if name[0] == '이':
		lcnt += 1
	if name == '이재영':
		lee += 1
	if name not in new_names:
		new_names.append(name)

print(kcnt, lcnt, lee)
print(new_names)
new_names.sort()
print(new_names)