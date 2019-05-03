print('''파일찾기
A라는 디렉토리 하위에 있는 텍스트 파일 (*.txt)중에서
LIFE IS TOO SHORT라는 문자열을 포함하고 있는
파일들을 모두 찾을 수 있는 프로그램 작성
단, 하위 디렉토리도 포함해서 검색해야 한다.
''')

import os
A = './data'
for root, dirs, files in os.walk(A):
	for file in files:
		file_name = root + '/' + file
		with open(file_name, 'r', encoding ='UTF-8') as fp:
			if fp.read().find('LIFE IS TOO SHORT') != -1:
				print(file_name)
