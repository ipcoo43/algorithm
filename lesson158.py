import re

names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(",")
print(names)
print()

countNm = 0
for name in names:
	m = re.search('(이|김).*',name)
	if m:
		countNm = countNm + 1

print('1. 김씨와 이씨는 각각 몇 명 인가요? => ',countNm)
print('2. "이재영"이란 이름이 몇 번 반복되나요? =>',names.count('이재영'))
result=list(set(names))
print('3. 중복을 제거한 이름을 출력하세요. =>',','.join(result))
result.sort()
print('4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요 =>',','.join(result))