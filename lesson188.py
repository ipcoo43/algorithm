print('완전수 구하기')
num = int(input('>>> '))
print([row for row in range(1,num+1) if row==sum(col for col in range(1,row) if row%col==0)])

print([row for row in range(1,num+1) if sum([col for col in range(1,row) if row%col==0])==row])