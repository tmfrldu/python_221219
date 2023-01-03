from tkinter import *
from tkinter import messagebox
from student_management.util import ui_util as tool
from student_management.dao.dao_student import StudentDao
from student_management.vo.student_vo import Student


class LoginWindow:
  def __init__(self):
    self.login = Tk()
    self.id, self.pw = StringVar(), StringVar()
    self.dao = StudentDao()

    Label(self.login, text="ID : ") \
      .grid(row=0, column=0, padx=10, pady=10)
    Label(self.login, text="Password : ") \
      .grid(row=1, column=0, padx=10, pady=10)

    self.ent_id = Entry(self.login, textvariable=self.id)
    self.ent_id.grid(row=0, column=1, padx=10, pady=10)

    self.ent_pw = Entry(self.login, textvariable=self.pw, show="*")
    self.ent_pw.grid(row=1, column=1, padx=10, pady=10)

    Button(self.login, text="Login", width=10, command=self.check_login) \
      .grid(row=2, column=0, padx=10, pady=10, sticky='e')
    Button(self.login, text="Join", width=10, command=self.go_join) \
      .grid(row=2, column=1, padx=10, pady=10, sticky='')

    self.ent_id.focus()
    tool.center_win(self.login, 270, 150)

    self.login.mainloop()

  def check_login(self):
    if str(self.id.get()) == "":
      messagebox.showinfo("알림", "ID를 확인해주세요")
      self.ent_id.focus()
      return

    if str(self.pw.get()) == "":
      messagebox.showinfo("알림", "비밀번호를 확인해주세요")
      self.ent_pw.focus()
      return

    s = Student()
    s.id = self.id.get()
    s.pw = self.pw.get()
    result = self.dao.login_check(s)
    print(':::')
    if result == None:
      messagebox.showwarning("알림", "없는 계정입니다.")
      self.id.set('');
      self.pw.set('');
      self.ent_id.focus()
    else:
      self.login.destroy()
      from student_management.controller import MainController
      MainController.forwardingControl('List')
      # ListWindow()

  def go_join(self):
    self.login.destroy()
    from student_management.controller import MainController
    MainController.forwardingControl('Join')

LoginWindow()