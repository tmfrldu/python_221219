# for


# for i in range(2, 10):
#   for j in range(1, 10):
#     # print(f'{i}*{j}=', i * j)
#     # print("{0}*{1}={2:>2}".format(i,j,i*j))
#     print(f'{i}*{j}={(i*j):>2}')
#   print()

# for i in range(2, 10, 3):  # range의 세번째 공간은 증감을 표현한다
#   for j in range(1, 10):
#     for k in range (0,3):
#       if (i + k) != 10:
#       # print(f'{i}*{j}=', i * j)
#       # print("{0}*{1}={2:>2}".format(i,j,i*j))
#         print(f'{i+k}*{j}={((i+k)*(j)):>2}', end=' ')
#     print()
#   print()
# 반복문을 사용할때는 break를 쓰기보단 다른 방법을 물색해보도록 하자

# for문 숫자가 감소할때
import time

for i in range(10, -1, -1):
  print(i)
  time.sleep(1)