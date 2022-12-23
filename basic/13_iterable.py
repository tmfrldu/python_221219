# Iterable은 차례로 요소를 접근할 수 있는 객체(리스트, 딕셔너리, 튜플)
# Iterator은 객체에 접근하기 위한 객체, 원본 영향 없음
# iterator는 순서 유무에 상관없이 객체에 접근가능

a = [1, 2, 3, 4, 15, 6, 7, 8, 9]

s = set([1, 2, 3])
sitr = iter(s)  # set s에 접근하기 위한 객체
for item in sitr: print(item)

sitr = iter(s)
i = 0
while i < len(s):
  print(next(sitr))
  i += 1

# 1) 일반적인 접근 방법
i = 0
for item in a:  # list를 활용함 변수 선언해줘야함
  print(f'{i}:{item}')
  i += 1
print()

# 2) range를 이용한 방법
for i in range(len(a)):  # range를 활용해서 list:a의 인덱스: value 출력 변수 따로 선언 안해도됨
  print(f'{i}:{a[i]}')
print()

# 3) enumerate를 이용한 접근
for i, item in enumerate(a):  # enumerate(): 리스트내 요소와 인덱스를 한번에 출력
  print(f'{i}:{item}')
print()

a.reverse()  # return값이 없는 method
print(a)

print('++++iterator++++')
# iterator를 이용한 접근 방법
itr = reversed(a)  # 이때 iterator 타입으로 변환
print(itr)
print(list(itr))  # reversed()된 a를 list로 출력하기 위해선 형변환을 시켜야함
# list_reverseiterator' has no len()
# print('iterator len: ',len(a)) # error

itr = reversed(a)  # interator 한번쓰면 초기화되기 때문에 다시 reversed()해줌
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

itr = iter(a)
for i in itr:
  print(i, end=' ')
print()

itr = iter(a)
i = 0
while i < len(a):
  print(next(itr), end=' ')
  i += 1
print()

if (2 > 1):
 print('첫번째 줄 \
       두번째 줄\
       세번째 줄')

if (2 > 1):
 print('''첫번째 줄
       두번째 줄
       세번째 줄''')

if (2 > 1):
   print('''첫번째 줄\n두번째 줄\n세번째 줄''')

str = ("첫번째 줄 \n"
       "두번째 줄 \n"
       "세번째 줄") # tuple 아님, 그냥 문자형임
print(type(str))

if (2 > 1):
 print("str: ", str)

if (2 > 1):
 print("".join(["첫번째 줄 \n", "두번째 줄 \n", "세번째 줄"]))


