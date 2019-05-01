names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
print(names)
print()

print(len([x for x in names if x.startswith('김')]))
print(len([x for x in names if x.startswith('이')]))
print(len([x for x in names if x.startswith('이재영')]))
print(','.join(set(names)))
print(','.join(sorted(set(names))))