class Student:
  @property
  def id(self): return self.__id
  @id.setter
  def id(self, id): self.__id = id
  @id.getter
  def id(self): return self.__id

  @property
  def name(self): return self.__name
  @name.setter
  def name(self, name): self.__name = name
  @name.getter
  def name(self): return self.__name

  @property
  def pw(self): return self.__pw
  @pw.setter
  def pw(self, pw): self.__pw = pw
  @pw.getter
  def pw(self): return self.__pw

  @classmethod    # 클래스메서드
  def from_str(cls, student_from_str) -> 'Student':     # -> 리턴값으로 주겠다
    std_list = student_from_str.split(',')
    print(std_list)
    student = Student();
    student.name = std_list[0];
    student.id = std_list[1]
    student.pw = std_list[2]
    return student


