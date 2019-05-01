import numpy as np

org_ppp= 150/10 # 원래 기계의 가성비 퍼포먼스/프라이스
prod = np.array([30, 70, 15, 40, 65]) # 각 기계의 성능
prod_ppp = prod // 3 # 각 기계의 가성비
print(prod_ppp)
print(prod[prod_ppp > org_ppp]) # 어떤 성능을 사용해야 기존 것보다 효율적인가
print(prod_ppp > org_ppp) # 가성비의 효율성이 높으면 True 낮으면 False
print(prod_ppp - org_ppp) # 가성비가 얼마나 차이가 나느냐