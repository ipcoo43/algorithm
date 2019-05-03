print(''' 다음 입사문제
1차원 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력
단 점들의 배열은 모두 정렬되어 있다고 가정
S={1,3,4,6,13,17,20}이 주어 졌다면 {3,4}
''')

S=[1,3,4,6,13,17,20]
min1=100000
result = 0,0
for i in range(len(S)-1):
	if min1 > S[i+1] - S[i]:
		min1 = S[i+1] - S[i]
		result = S[i], S[i+1]
print(result)
