# 1)
print('홍길동씨 평균점수는 ', (80 + 75 + 55) / 3, '입니다')

# 2)
a = 13
# a = int(input("숫자 입력(0은종료)"))
if a % 2:
  print(a, '는 홀수 입니다.')
else:
  print(a, '는 짝수 입니다.')
print(a, '는 홀수' if a else '는 짝수')  # 삼항연산자처럼 한줄로 작성

# 3)
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:14]
print('19' + yyyymmdd)
print(num)

# 4)
print('남자' if pin[7] == '1' else '여성')

# 5)
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6)
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7)
a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print('"' + result + '"')
print('"', end="")
for item in a:
  print(item, end=" ")
print('"')

# 8)
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9)
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'  # list는 key 값이 될수 없다
a[250] = 'python'
for key in a:
  print(key, a[key])

# 10)
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# 11)
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12)
a = b = [1, 2, 3]
a[1] = 4
print(b)
print('a=b는 같은 reference를 갖는 객체로 복제된거이므로 a가 바뀌면 b도 바뀐다')
