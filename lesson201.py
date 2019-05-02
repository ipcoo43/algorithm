print('자릿수를 출력하는 프로그램')

a = int(input('양의 정수를 입력해 주세요 >>> ')) 
if a > 0: 
	print('{} > {} 자리수 '.format(a,len(str(a))))
else:
	print('양의 정수가 아닙니다.')
