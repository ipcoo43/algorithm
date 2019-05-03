print('''사이냅 소프트 면접 문제''')

data = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이선연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')

name=sorted(list(set(data)))
for i in name:
	if data.count(i) > 1 :
		print('{}씨는 {}번 반복되었습니다.'.format(i,data.count(i)))
	else:
		print('{}씨는 {}번 반복되었습니다.'.format(i,data.count(i)))
	


