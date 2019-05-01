print('''Multiples of 3 and 5
3과 5의 배수의 총합 구하기
3,5,6,9 = 23
''')
lst = [] # 메모리 사용량 증가
for i in range(1,10):   # 0~9까지 숫자
	if (i % 3 == 0) or (i % 5 == 0):      # 3과 5의 배수
		lst.append(i)
print(sum(lst))  # 23

sum1=0
for i in range(1,10):
	if i%3==0 or i%5==0:
		sum1 = sum1 + i
print(sum1)

print(list([x for x in range(1,10) if x%3==0 or x%5==0]))

# if 조건을 for 뒤에 적어주고 이것을 꺼내 올 i를 앞에 적어 준다
print([i for i in range(1,10) if i%3==0 or i%5==0])