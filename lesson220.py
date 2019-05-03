print('''사이냅 소프트 면접 문제''')

data = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이선연,박영서,박민호, 전경헌,송정환,김재성,이유덕,전경헌'.split(',')

print('이씨는 {}명 입니다'.format(len(list(d for d in data if d[0]=='이'))))
print('김씨는 {}명 입니다'.format(len(list(d for d in data if d[0]=='김'))))
print('이재영씨는 이름이 {}번 반복됩니다.'.format(data.count('이재영')))
print('중복을 제거 이름 =',sorted(list(set(data))))
