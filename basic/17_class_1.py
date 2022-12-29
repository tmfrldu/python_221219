# 1) 각각의 객체를 만들 때
std1 = {'name': '홍길동', 'kor': 87, 'mat': 98, 'eng': 88}
std2 = {'name': '김길동', 'kor': 87, 'mat': 98, 'eng': 88}
std3 = {'name': '황길동', 'kor': 87, 'mat': 98, 'eng': 88}

# 2) 리스트와 딕셔너리를 이용해서 만들 때
students = [
  {'name': '홍길동', 'kor': 87, 'mat': 98, 'eng': 88},
  {'name': '김길동', 'kor': 87, 'mat': 98, 'eng': 88},
  {'name': '동길동', 'kor': 87, 'mat': 98, 'eng': 88}
]


# 3) 함수를 이용하여 객체를 만들때
def create_std(name, kor, math, eng):
  return {'name': name, 'kor': kor, 'mat': math, 'eng': eng}


print("name", "ttl", "Average", sep="\t")
for std in students:
  # 2번 방식
  tt = std['kor'] + std['mat'] + std['eng']
  avg = tt / 3
  print(f"{std['name']}, {tt:>4d}, {avg:>5.2f}")


# 4) 여러 함수를 이용하여 객체를 만들때
def create_std(name, kor, math, eng):
  return {'name': name, 'kor': kor, 'mat': math, 'eng': eng}


def get_sum(std):
  return std['kor'] + std['eng'] + std['mat']


def get_avg(std):
  return get_sum(std) / 3


def get_std(std):
  return f"{std['name']:3s}, {get_sum(std):>4d}, {get_avg(std):>5.2f}"


students = [
  create_std('홍길동', 87, 98, 88),
  create_std('갓길동', 87, 98, 88),
  create_std('동길동', 87, 98, 88)
]

print("Name", "합", "Average", sep='\t')
for std in students:
  print(get_std(std))


# 5) class 선언하기
class Student:
  def __init__(self, name, kor, mat, eng):  # 생성자
    self.name = name
    self.kor = kor
    self.mat = mat
    self.eng = eng

  def __del__(self, ):  # 소멸자
    # print(f'{self.name}의 인스턴스를 제거하였습니다.')
    pass

  def get_sum(self):
    return self.kor + self.eng + self.mat

  def get_avg(self):
    return self.get_sum() / 3

  def to_string(self):
    return f'{self.name:^4s} {self.get_sum():>4d} {self.get_avg():>6.2f}'

  def __str__(self):  # 객체를 스트링으로 변환해주는 메서드
    return f'{self.name:^4s} {self.get_sum():>4d} {self.get_avg():>6.2f}'

  def __eq__(self, other):  # 다른 객체와 같은지 비교해주는 메서드, 기준은 리턴값으로 넣어주면 된다
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() == other.get_sum()


  def __ne__(self, other):  # not equal
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() != other.get_sum()

  def __gt__(self, other):  # self > other 인지
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() > other.get_sum()

  def __lt__(self, other):  # self < other 인지
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() < other.get_sum()

  def __ge__(self, other):  # self >= other 인지
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() >= other.get_sum()

  def __le__(self, other):  # self <= other 인지
    if not isinstance(other, Student):
      raise TypeError('Student의 인스턴스가 아님')
    return self.get_sum() <= other.get_sum()

students = [
  Student('홍길동', 87, 98, 88),
  Student('동길동', 87, 98, 88),
  Student('감길동', 87, 98, 88),
]

print("Name", "합", "Average", sep='\t')
for std in students:
  print(std)

print(students[0]) # __str__메서드로 인해 ref주소값이 아닌 sting으로 출력
print(students[1])
print(students[0] == students[1])  # 위의 __eq__ 메서드로 객체의 get_sum값이 같은지 판별







