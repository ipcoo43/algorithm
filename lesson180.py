print('''가성비 최대화
원래 기계의 가격 : 10
원래 기계의 성능 : 150  (150/10=15)
추가 부품의 가격 : 3
추가 부품의 성능 : 각각 30, 70, 15, 40, 65
''')

import numpy as np

org_ppp = 150/10 # 원래 기계의 가성비 성능/가격 15
prod = np.array([30, 70, 15, 40, 65]) # 각 기계 성능
prod_ppp = prod//3 # 각 기계의 가성비

print('추가 부품의 성능 =',prod)
print("각 기계의 가성비 =",prod_ppp)  
print("기준 보다 성능이 높음 =",prod[prod_ppp > org_ppp]) 
print("마스킹 =",prod_ppp > org_ppp) 
print("각 부품의 성능 차이 =",prod_ppp-org_ppp) 