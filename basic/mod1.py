# mod1.py
def add(a, b):
  print("__name__ :",__name__)
  return a + b

def sub(a, b):
  return a - b

# __name__ 내장된 변수 이름

if __name__ == "__main__":  # 여기서 실행될때만 출력하도록 하는 거인듯
  print(add(1,4))
  print(sub(4,2))


# 파이썬에는 기본적으로 상수가 없다.
PI = 3.14
GRAVITY = 9.8
