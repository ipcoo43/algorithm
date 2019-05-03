S=[1,3,4,6,13,17,20]
pairs = list(zip(S[0:], S[1:]))
pairs.sort(key=lambda x:x[1]-x[0])
print(pairs[0])

