print(''' 탭을 공백 문자로 바꾸기''')

data = '''\
sum1=0
for i in range(1,9):
\tif i%3==0 or i%5==0:
\t\tsum1 += i '''

print(data.replace('\t',' '*4))  # 바꿀것과, 바꿀예정인것

f=open('lesson149.py','r',encoding='utf8')
data=f.read()
f.close()
print(data.replace('\t',''*4))
