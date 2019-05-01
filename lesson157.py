names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
print(names)
print()

print('1. 김씨와 이씨는 각각 몇 명 인가요?')
a=[i[0] for i in names]
print(a)
print('김씨 : {}명, 이씨 : {}명'.format(a.count('김'), a.count('이')))
print()

print('2. "이재영"이란 이름이 몇 번 반복되나요?')
print('이재영은 {}번 반복 됩니다.'.format(names.count('이재영')))
print()

print('3. 중복을 제거한 이름을 출력하세요.')
uniq_names = list(set(names))
print(uniq_names)
print()

print('4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.')
uniq_names.sort()
print(uniq_names)