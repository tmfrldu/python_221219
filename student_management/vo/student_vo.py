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


