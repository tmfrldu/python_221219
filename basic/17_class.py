# 클래스명은 대문자로 생성한다
class Calculator:
  n3 = 100

  def __init__(self, n1=1, n2=1):  # 객체의 속성을 초기화하는데 사용 _생성자
    self.n1 = n1
    self.n2 = n2

  def setdata(self, n1, n2):  # 자신의 값과 기능을 초기화_ 객체의 본질을 유지(?) _ setter
    if n1 > -1:
      self.n1 = n1
      self.n2 = n2

  def add(self):
    return self.n1 + self.n2

  def add(self):  # 매개변수로 들어가는 n3은 지역변수이므로 클래스에 선언된 n3를 참조할수 없다
    # 메서드가 중복될 경우 마지막 정의가 우선
    return self.n1 + self.n2 + self.n3

  def sub(self):
    return self.n1 - self.n2

  def mul(self):
    return self.n1 * self.n2

  def div(self):
    return self.n1 / self.n2

  def selfish(self):
    print('parent')


c1 = Calculator()
c2 = Calculator()
c3 = Calculator(3, 4)

c3.n3 = 200
print(type(c1))
print(id(c1))
print(id(c2))

Calculator.setdata(c1, 4, 2)
# c1.setdata(4,2)
c2.setdata(2, 1)

print(c1.n1, c1.n2, c1.n3)
print(c2.n1, c2.n2, c2.n3)
print(c3.n1, c3.n2, c3.n3)

print(id(c1.n1))
print(id(c2.n1))

# print(c1.add())
print(c1.add())


class MultiCalc(Calculator):
  n3 = 300
  def setdata(self, n1, n2, n3=200):
    if n1 > -1:
      self.n1 = n1
      self.n2 = n2
      self.n3 = n3

  def selfish(self):  # -> method overriding
    print('child')

# 상속시 중복될 경우 변수, 메서드는 자손값
# 메서드가 호출시 관련된 값도 자손값

m1 = MultiCalc(10, 20)
print(m1.add())
# print('setdata', m1.setdata())
print('n3', m1.n3)

m1.selfish()  # 부모와 자손의 메서드명이 중복되면 자손의 메서드가 출력

m2 = Calculator()
