class Parent:
  def __init__(self):
    self.value = '부모'
    print('Parent class의 __init__호출 되었습니다.')
  def test(self):
    self.power = False
    print("Parent class test 호출")
class Child(Parent):
  def __init__(self):
    Parent.__init__(self)
    # Parent의 생성자가 생성한 인스턴스변수에 접근
    print('Child class의 __init__호출 되었습니다.')

child = Child()
child.test()
print(child.value)
print(child.power) # 생성자가 아닌 인스턴스 변수 접근가능
