# runtime error, syntax error

print(1)
try:
  print(2)
  f = open('xmen','r')
  print([1,2,3][3])
  print(10/0) # <- runtime error 중 하나
  print(3)
except FileNotFoundError as e:
  pass # 예외 처리 동작이 미정일 경우 pass 처리
except IOError as e:  # 입출력 작업에서 오류 발생시 예외처리 구문
  print('IOError')
# except IndexError as e:  # 인덱스 에러 발생시 예외처리 구문
#   print('index error')
except (ZeroDivisionError,IndexError) as e: # 나눗셈 연산시 0으로 나눌때의 예외처리 구문
  print('4-2')
except Exception as e:  # 포괄적인 에러 발생시의 예외처리 구문으로 가장 마지막에 작성되도록 한다.
  print(4)
finally:
  print(5)
print(6)

input_ans = input('숫자만 입력하시오')
if input_ans.isdigit():
  print(int(input_ans)+100)
else:
  print('정수를 입력하시오')

try:
  print(int(input_ans)+100)
except:
  try:
    print(int(input_ans.strip())+100)
  except:
    print('숫자를 입력하시오')

class Bird:
  def fly(self):
    raise NotImplementedError  # 강제로 구현이 안되는 에러 발생시킴
    # print('훨훨')

class Eagle(Bird):
  def fly(self):
    print('훨훨뤄뤄훠루러ㅜ러루러러')

eagle = Eagle()
eagle.fly()

# 사용자 예외처리 클래스
class MyError(Exception):  # Exception의 상속을 받아서 MyError클래스를 생성
  # pass
  def __str__(self):
    return "허용되지 않은 별명입니다."
def say_nick(nick):
  if nick == '바보':
    raise MyError()
  print(nick)

try:
  say_nick('천사')
  say_nick('바보')
except MyError as e:
  print(e)

class CustomException(Exception):
  def __init__(self):
    Exception.__init__(self)
  def __str__(self):
    return "오류가 발생했어요"

# raise CustomException()

class CustomException2(Exception):
  def __init__(self, message, value):
    Exception.__init__(self)
    self.message = message
    self.value = value
  def __str__(self):
    return "오류가 발생했어요"
  def print(self):
    print("##### 오류정보 #####")
    print("메시지:", self.message)
    print("값:", self.value)

try:
  raise CustomException2("CustomException2",5)
except CustomException2 as e:
  e.print()
