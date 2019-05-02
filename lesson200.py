print('어느 숫자가 중간값을 가지는 숫자일까?')
print('2,5,3=>3  4,6,4=>4')

lst = list(map(int,input('3개의 숫자 ,로 입력 >>> ').split(',')))
lst = sorted(lst)
print(lst[1])

 # print(sorted(list(map(int,input('3개의 숫자를 띄어쓰기와 함께 입력하세요 >>>').split())))[1])


