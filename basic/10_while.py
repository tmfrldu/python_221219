# while
# python에서는 do while문이 없다

a = list(range(0, 10))
i = 0

while i < len(a):
  if a[i] % 2 == 0:  print(a[i])
  i += 1

while a:
  tmp = a.pop()
  if not tmp % 2: print(tmp)

# for item in a:
#   if a[item] % 2 == 0:
#     print(a[item])

# break 활용
# while a:
#   if a[i]%2 == 0:
#     print(a[i])
#   if (i < len(a)-1):
#     i += 1
#   else: break

import random

# randNum = random.randrange(1, 101)
# print(randNum)
# cnt = 0
# while True:
#   ans = int(input('New 숫자맞추기_숫자입력하시오'))
#   cnt += 1
#   if ans == randNum:
#     print(f"정답. {cnt}번만에 맞춤")
#     break
#   elif ans > randNum:
#     print("그거보단 작습니다")
#   else:
#     print("그거보단 큽니다")

# python에서 do while처럼 구현하려면
# 실행문
# while 조건문:
#    실행문  초반에 실행문이 두번 되버리는 ....

# while True:
#   실행문
#   if not 조건: break

# while True:
#   실행문
#   if 조건: continue
#   break

# dowhile처럼 구현한 예제
randNum = random.randrange(1, 101)
cnt = 0
while True:
  ans = int(input('숫자입력'))
  cnt += 1
  if (ans > randNum):
    print('큽니다.'); continue
  elif (ans < randNum): print('작습니다'); continue;
  else:
    print(f"정답. {cnt}번만에 맞춤")
  break

