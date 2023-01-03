from tkinter import messagebox



class MainController:
  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, "_instance"):  # Foo 클래스 객체에 _instance 속성이 없다면
      print("__new__ is called\n")
      cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
    return cls._instance  # Foo._instance를 리턴


  def __init__(self, data):
    cls = type(self)
    if not hasattr(cls, "_init"):  # Foo 클래스 객체에 _init 속성이 없다면
      print("__init__ is called\n")
      self.data = data
      cls._init = True

  @classmethod
  def forwardingControl(cls, cmd=None):
    print("cmd", cmd)

    if cmd == 'Login':

      from student_management.ui.login_wd import LoginWindow
      LoginWindow()
    elif cmd == 'Join':
      from student_management.ui.join_wd import JoinWindow
      JoinWindow()
      pass
    elif cmd == 'List':
      from student_management.ui.list_wd import ListWindow
      ListWindow()

    elif cmd == 'Info':
      from student_management.ui.info_wd import UserInfo
      UserInfo()

    else:
      messagebox.showwarning("알림", "없는 명령입니다.")

  # def __init__(self):
  #   self.forwardingControl('Login')

