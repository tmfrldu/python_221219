from my_util import *

class Parent:
  # 클래스 변수
  inh = 1000    #public
  # _inh = 1000   #protected
  # __inh = 1000  # private

  # 인스턴스 변수
  def __init__(self, age=50):
    self.age = age
    # self._age = age
    # self.__age = age
  def setdata(self, age): self.age = age;

class Child(Parent):
  def setjob(self, job):self.job = job

p1 = Parent(); p2 = Parent();
c1 = Child(); c2 = Child();
# 변수의 선언에 따라 인스턴스변수,클래스변수 2가지
# 클래스 변수는 클래스의 공통된 변수
# 예)법정근로시간은 모든근로자 동일=>클래스변수
# 인스턴스변수는 각각 고유한 값을 가지게 해줌.
# 예)개인의 호봉은 고유한 요소=>인스턴스변수
# 인스턴스변수는 self.변수명 으로 생성
# 클래스변수는 클래스아래 변수명 으로 생성
# 인스턴스변수는 인스턴스에서만 접근 가능
# 클래스변수는 2가지로 접근가능
# ->클래스명.변수(공통값),인스턴스명.변수(고유의값)
# 접근 제어자 __(private), _(protected), public

lines('public일 경우')
print("p1.inh:", p1.inh) #클래스변수접근가능
print("p2.inh:", p2.inh) #클래스변수접근가능
print("p1.age:",p1.age) #변수접근가능
print("p2.age:",p2.age) #변수접근가능
print("Parent.inh:",Parent.inh) #변수접근가능
# print("Parent.age:",Parent.age) #인스턴스변수접근시에러
print("c1.inh:", c1.inh) #변수접근가능
print("c2.inh:", c2.inh) #변수접근가능
print("c1.age:",c1.age) #변수접근가능
print("c2.age:",c2.age) #변수접근가능
print("Child.inh:",Child.inh) #변수접근가능
# print("Child.age:",Child.age) #변수접근시에러

lines('protected일 경우:실제 제약되지 않고 경고')
# print("p1._inh:", p1._inh) #변수접근가능
# print("p2._inh:", p2._inh) #변수접근가능
# print("p1._age:",p1._age) #변수접근가능
# print("p2._age:",p2._age) #변수접근가능
# print("Parent._inh:",Parent._inh) #변수접근가능
# print("Parent._age:",Parent._age) #변수접근시에러
# print("c1._inh:", c1._inh) #변수접근가능
# print("c2._inh:", c2._inh) #변수접근가능
# print("c1._age:",c1._age) #변수접근가능
# print("c2._age:",c2._age) #변수접근가능
# print("Child._inh:",Child._inh) #변수접근가능
# print("Child._age:",Child._age) #변수접근시에러

# Parent._inh = 5 #모든 인스턴스값 변경
# Parent._age = 10 #모든 인스턴스값 변경
# Child._inh = 9 #모든 인스턴스값 변경
# Child._age = 40 #모든 인스턴스값 변경
# p2._inh = 2000 #해당 인스턴스만 변경
# p2._age = 30 #해당 인스턴스만 변경
# c2._inh = 2000 #해당 인스턴스만 변경
# c2._age = 30 #해당 인스턴스만 변경
# print("p1._inh: ", p1._inh) #값 변경후 접근 가능
# print("p1._age: ", p1._age) #값 변경후 접근 가능
# print("p2._inh: ", p2._inh) #값 변경후 접근 가능
# print("p2._age: ", p2._age) #값 변경후 접근 가능
# print("c1._inh: ", c1._inh) #값 변경후 접근 가능
# print("c1._age: ", c1._age) #값 변경후 접근 가능
# print("c2._inh: ", c2._inh) #값 변경후 접근 가능
# print("c2._age: ", c2._age) #값 변경후 접근 가능
# print("Parent._inh: ", Parent._inh) #값 변경후 접근 가능
# print("Parent._age: ", Parent._age) #값 변경후 접근 가능
# print("Child._inh:",Child._inh) #값 변경후 접근 가능
# print("Child._age:",Child._age) #값 변경후 접근 가능

lines('private일 경우')
# print("p1.__inh:", p1.__inh) #변수접근시에러
# print("p2.__inh:", p2.__inh) #변수접근시에러
# print("p1.__age:",p1.__age) #변수접근시에러
# print("p2.__age:",p2.__age) #변수접근시에러
# print("Parent.__inh:",Parent.__inh) #변수접근시에러
# print("Parent.__age:",Parent.__age) #변수접근시에러
# print("c1.__inh:", c1.__inh) #변수접근시에러
# print("c2.__inh:", c2.__inh) #변수접근시에러
# print("c1.__age:",c1.__age) #변수접근시에러
# print("c2.__age:",c2.__age) #변수접근시에러
# print("Child.__inh:",Child.__inh) #변수접근시에러
# print("Child.__age:",Child.__age) #변수접근시에러

# Parent.__inh = 5 #모든 인스턴스값 변경
# Parent.__age = 10 #모든 인스턴스값 변경
# Child.__inh = 9 #모든 인스턴스값 변경
# Child.__age = 40 #모든 인스턴스값 변경
# p2.__inh = 2000 #해당 인스턴스만 변경
# p2.__age = 30 #해당 인스턴스만 변경
# c2.__inh = 2000 #해당 인스턴스만 변경
# c2.__age = 30 #해당 인스턴스만 변경
# print("p1.__inh: ", p1.__inh) #값 변경후 접근 가능
# print("p1.__age: ", p1.__age) #값 변경후 접근 가능
# print("p2.__inh: ", p2.__inh) #값 변경후 접근 가능
# print("p2.__age: ", p2.__age) #값 변경후 접근 가능
# print("c1.__inh: ", c1.__inh) #값 변경후 접근 가능
# print("c1.__age: ", c1.__age) #값 변경후 접근 가능
# print("c2.__inh: ", c2.__inh) #값 변경후 접근 가능
# print("c2.__age: ", c2.__age) #값 변경후 접근 가능
# print("Parent.__inh: ", Parent.__inh) #값 변경후 접근 가능
# print("Parent.__age: ", Parent.__age) #값 변경후 접근 가능
# print("Child.__inh:",Child.__inh) #값 변경후 접근 가능
# print("Child.__age:",Child.__age) #값 변경후 접근 가능

print(type(p1))
print(type(c1))
print(type(p1)==Parent)
print(type(c1)==Child)

print(isinstance(c1, Parent))  # 상속관계를 확인하는 메서드
print(isinstance(c1, Child))