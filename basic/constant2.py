class _constant2:
  def __setattr__(self, key, value):
    if key in self.__dict__:
      raise Exception('변수 값 할당 안됨')
    self.__dict__[key] = value

  def __delattr__(self, item):
    if item in self.__dict__:
      raise Exception('변수 삭제 불가')

import sys
sys.modules[__name__] = _constant2()
