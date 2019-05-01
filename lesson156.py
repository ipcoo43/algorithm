page = lambda x,y: x/y if x%y==0 else x/y+1
x,y=map(int,input('두 수 ,로 구분 입력 >>>').split(','))
print(x,y)