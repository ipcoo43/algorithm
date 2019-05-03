print('''리스트 회전
입력 : 1 10 20 30 40 50 
출력 : 50 10 20 30 40
입력 : 4 가 나 다 라 마 바 사
출력 : 라 마 바 사 가 나 다
입력 : -2 A B C D E F G
출력 : C D E F G A B
입력 : 0 똘기 떵이 호치 새초미
출력 : 똘기 떵이 호치 새초미
''')

arr1 = input('입력 : ').split()
vec,arr2 = int(arr1[0]), arr1[1:]
print(arr2[-vec:] + arr2[:-vec])