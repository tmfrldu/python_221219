class Terran:
  tribe = 'Terran'

class Marine(Terran):
  # 클래스 변수(공통의 속성)
  name = 'Marine'
  __count = 0
  __attack_lv = 6
  __deffence_lv = 0

  # 클래스 메서드
  @classmethod
  def get_count(cls):
    print(cls.__count, '※cls는 마린과 동일')
    # 클래스 메서드는 인스턴트메서드를 땡겨쓸수 없다. why? 파일 읽을 시점에 인스턴스 생성이 안돼있음
  @property
  def hp(self):
    return self.__hp

  def __init__(self):
    self.__hp = 40
    # self.count += 1 # 여기에서 카운팅하면 인스턴스 변수가 되어버림
    Marine.__count += 1
    print('생성되었습니다')
  # 더 사용할 가능성이 없는 데이터일 경우, garbage collecter가 메모리에서 제거
  def __del__(self):
    Marine.__count -= 1
    print('소멸되었습니다')
  def move(self):
    Marine.get_count()
    print(f'{Marine.name}가 이동합니다')

  @hp.setter
  def set_hp(self, hp):  # 속성에 대한 setter
    if hp < 0:
      raise TypeError("양의 정수를 넣으세요")
    self.__hp = hp
  @hp.getter
  def get_hp(self):  # 속성에 대한 getter _ return으로 값을 받음
    return self.__hp

marines = [
  Marine(), Marine(), Marine(), Marine()
]

# print(Marine.__count)
marines[0].move()
Marine.get_count()  # 클래스메서드를 활용하여 클래스이름으로 접근
marines[0].get_count()  # 인스턴스를 활용한 접근
# marines[0].hp = -10
marines[0].__hp = 100
print(marines[0].hp)
print(marines[0].__hp)