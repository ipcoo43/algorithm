names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
print(names)
print()

print([item for item in names if item[0]=='이' or item[0]=='김'])
print(names.count('이재영'))
print(set(names))
print(sorted(set(names)))
