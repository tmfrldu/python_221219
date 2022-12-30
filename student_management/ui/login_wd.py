import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from student_management.util import ui_util as tool
from student_management.dao.dao_student import StudentDao
from student_management.vo.student_vo import Student

login = Tk()
id, pw = StringVar(), StringVar()
dao = StudentDao


def check_login():
  if str(id.get()) == "":
    messagebox.showinfo("알림", "ID를 확인해주세요")
    ent_id.focus()
    return

  if str(pw.get()) == "":
    messagebox.showinfo("알림", "Password를 확인해주세요")
    ent_pw.focus()
    return

  s = Student()
  s.id = id.get()
  s.pw = pw.get()
  result = dao.login_check(s)
  print(result)

  # else:
  #   dao = StudentDao()
  #   students = dao.get_all()
  #
  #   # std = StudentDao(id=id.get(), pw=pw.get())
  #   login_result = dao.login_check(id.get())
  #
  #   if login_result is None:
  #     messagebox.showinfo("알림", "ID가 존재하지 않습니다")
  #     print('login_result' ,login_result)
  #     print('dao.get_all()', dao.get_all())
  #     print('id.get()', id.get())
  #     # ask user to try again
  #   else:
  #     messagebox.showinfo("알림", "로그인 성공")
  #     # allow user to proceed


def go_join():
  pass


ttk.Label(login, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(login, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
ent_id = Entry(login, textvariable=id)
ent_id.grid(row=0, column=1, padx=10, pady=10)
ent_pw = ttk.Entry(login, textvariable=pw, show="*")
ent_pw.grid(row=1, column=1, padx=10, pady=10)

ttk.Button(login, text="Login", command=check_login).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(login, text="Join", command=go_join).grid(row=2, column=2, padx=10, pady=10)

ent_id.focus()
tool.center_win(login, 270, 150)
login.mainloop()
