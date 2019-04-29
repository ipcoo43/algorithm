prm=[2,3]
cnt=2
for p in range(5,101,2):  # 5부터 홀수로 증가 시킴
	for q in range(2,cnt):
		mok = int(p/prm[q])  
		nam = p-(mok*prm[q])
		if nam == 0:
			continue
	cnt = cnt+1
	prm.append(p)
	if cnt == 15:
		break

print(prm)

		