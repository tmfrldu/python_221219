# import my_util -> my_util.lines()로 호출
# import my_util as util  -> util.lines()로 호출

from my_util import lines  # import * 로 해주면 my_util내 있는 함수 이름으로 다 땡겨쓸수 있음

lines("재귀함수")


# 재귀함수 Recursive Call
# n! = n * (n-1)*(n-2)*(n-3)

# factorial을 for문으로 구현
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


def factr(n):
  if n == 1:
    return 1
  else:
    return n * factr(n - 1)


print(factorial(5))
print(factr(5))

lines("콜백 함수")


def call_10_times(arg):
  for i in range(5):
    arg()


def my_hello():
  print('hello')


call_10_times(my_hello)


def power(item):
  return item * item


def under_3(item):
  return item < 3


l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = map(power, l1)
print(list(l2))  # l2는 map object라 바로 출력 안됨

l3 = filter(under_3, l1)
print(list(l3))

lines("람다 (lambda)")
# 함수를 생성할 때 사용하는 예약어_ def와 동일한 역할

power = lambda x: x * x
under_3 = lambda x: x < 3

l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = map(power, l1)
print(list(l2))
l3 = filter(under_3, l1)
print(list(l3))

l2 = map(lambda x: x * x, l1)   # <- 괄호 내에 lambda 함수 생성해서 사용가능
print(list(l2))
l3 = filter(lambda x: x < 3, l1)
print(list(l3))
