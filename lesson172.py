print('''가성비 최대화
원래 기계의 가격 : 10
원래 기계의 성능 : 150
추가 부품의 가격 : 3
추가 부품의 성능 : 각각 30, 70, 15, 40, 65
추가 부품을 장착하여 얻을 수 있는 최대 가성비 : 17.81... → 17
(성능이 70과 65인 부품을 장착하면 됨)
''')
orp=10
org=150
adp=3
adg=[30, 70, 15, 40, 65]
adg.sort(reverse=True)
for i in adg:
	if org/orp > (org+i)/(orp+adp):
		break
	else:
		org += i 
		orp += adp
	print('{}의 가성비 : {}'.format(i,org//orp))
print()

orp=10
org=150
adp=3
adg=[30, 70, 15, 40, 65]
adg.sort(reverse=True)
for i in adg:
	print('{}의 가성비 : {}'.format(i, (org+i)//orp+adp))