# 함수: def_define function
# 기능들의 묶음이다.

def dline():
  print("==" * 12)


def lines(str):
  print(f"{str :=^20}")


from typing import Iterable


def printIterable(obj):
  # if hasattr(obj, "__iter__"):   # hasattr()속성을 확인해 주는 메서드
  if isinstance(obj, Iterable):  # iterable한 속성인지 확인해주는 typing내의 메서드인듯....
    for item in obj:
      print(f'{item}', end=' ')
    print()
  else:
    print(obj)


lines('printIterable 사용')
a = [1, 2, 3, 4, 5]
printIterable(a)
printIterable('hello world')
printIterable(123)
print(printIterable(111))  # None 출력_ 해당 함수 내에 리턴값이 존재하지 않음


def add(a, b):
  return a + b


add(1, 1)
print(add(1, 1))  # 해당 함수내에 리턴값이 존재함_ 출력 가능

# print(add(1)) # error, add()는 입력으로 2개의 값을 받기때문에 에러남
# print(add(1,2,3)) # error, 입력 자리 안맞음 에러남

lines("가변 매개변수")


def add(n, *values):  # *value 입력값을 여러개 받을 때
  for i in range(n):
    for val in values:
      print(val, end=' ')
    print()


add(3, 1, 2, 3, 4, 5)
dline()


def sums(*values):
  for val in values:
    print(val, end=' ')
  print()


sums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # print
sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # print

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # sum()에 리턴값이 있으므로 출력 가능
print(sums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # <- 함수내 리턴값이 없으므로 출력되지 않음

lines("기본 매개변수")


# 기본 매개변수는 맨 뒤에 놓을 것
def defaultPrint(n1, n2=10):  # default 매개변수를 활용
  return n1 * n2


print(defaultPrint(10))

lines("매개변수 지정하여 호출")


# 기본 매개변수는 맨 뒤에 놓을 것
def defaultPrint(n1, n2=10):  # default 매개변수를 활용
  return n1 - n2


print(defaultPrint(n2=2, n1=1))

lines("응용1) 다양한 매개변수 호출")


def test(a, b=10, c=20):
  print(a + b + c)


test(1, 2, 3)  # 기본 대입 형태
test(a=1, c=4, b=5)  # 매개변수 지정형태
test(10, c=20)

lines("응용2) 자료없이 리턴")


def test_condition(sw):
  if (sw):
    print('a')
    return "a"  # 리턴이 있을 때_ 리턴값은 오직 하나
  else:
    return  # 리턴 없을 때: 함수에 진행 끝

  print('b')


print(test_condition(1))
# 출력값은 a가 두개 나오는데 함수내 print()와 print(t_con())에서 리턴값 a가 한번더 출력되는 형태

lines("응용3) 매개변수와 리턴 응용")


def sum_all(start=0, end=100, step=1):
  output = 0
  for i in range(start, end + 1, step):
    output += i
  return output


print("1. ", sum_all(0, 100, 10))
print("1. ", sum_all(end=100))
print("1. ", sum_all(end=100, step=2))

lines("매개변수의 Scope")
# 함수 내부의 변수는 할당이 되면 지역변수이다.
a = 1
def vartest(a):
  a += 1
  return a

print(vartest(a))
print(a)    # 전역변수로 있는 a의 변경된 값이 출력
vartest(a)
a= vartest(a) # vartest 리턴값으로 초기화
print(a)  # 변수 a가 전역변수로 선언되었기 때문에 출력 가능

def vartest2():
  global a   # 함수 안에서 함수 밖의 변수를 변경할때 사용
  # 함수 내부에서는 외부에 선언된 변수는 참조만 가능
  # 함수 내부에서 외부와 같은 이름 할당하면 연산 가능 <- 지역변수
  # 함수 내부의 global 변수는 함수 실행하면 사용가능 <- 외부 변수의 값이 변경됨
  a += 1
  return a
vartest2()
print(a)  # 전역변수의 값이 바뀐것을 확인할수 있음

def vartest(b):
  b = b + 1
  print(b)

vartest(3)
# print(b) # 함수 내에 선언된 지역변수임으로 호출 불가, error 발생

