from tkinter import messagebox

class MainController:
  def __init__(self):
    self.cmd = 'Login'
  @classmethod
  def forwardingControl(cls, cmd = None):
    if cmd == 'Login':
      from student_management.ui.login_wd import LoginWindow
      login = LoginWindow()
    elif cmd == 'Join':
      from student_management.ui.join_wd import JoinWindow
      join = JoinWindow()
    elif cmd == 'List':
      from student_management.ui.list_wd import ListWindow
      list = ListWindow()

    else:
      messagebox.showwarning("알림", "없는 명령입니다.")

MainController.forwardingControl('Login')

