print('공백을 제외한 글자수 세기')

strs = [' ', '\n', '\r\n', '\t']
data = '''공백을 제외한
글자수만을 세는 코드 테스트
'''
for char in strs:
	data = data.replace(char,'')
print(len(data))

