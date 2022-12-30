import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from student_management.util import ui_util as tool
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

join = Tk()
join.title("Student Regist")
join.resizable(False, False)
tool.center_win(join,280,250)


id, pw, name, repw = StringVar(), StringVar(), StringVar(), StringVar()


def check_join():

  if str(name.get()) == "":
    messagebox.showinfo("알림", "이름을 확인해주세요")
    ent_name.focus()
    return

  if str(id.get()) == "":
    messagebox.showinfo("알림", "ID를 확인해주세요")
    ent_id.focus()
    return

  if str(pw.get()) == "":
    messagebox.showinfo("알림", "비밀번호를 확인해주세요")
    ent_pw.focus()
    return

  if str(repw.get()) == "":
    messagebox.showinfo("알림", "비밀번호를 다시 한번 입력해주세요")
    ent_repw.focus()
    return

  if str(pw.get()) != str(repw.get()):
    messagebox.showinfo("알림", "비밀번호가 일치하지 않습니다")
    ent_pw.focus()
    ent_pw.delete(0, 'end')
    ent_repw.delete(0, 'end')
    return

def cancel():
  pass

ttk.Label(join, text="이름 : ").grid(row=0, column=0, padx=10, pady=10, sticky= 'e')
ttk.Label(join, text="ID : ").grid(row=1, column=0, padx=10, pady=10, sticky= 'e')
ttk.Label(join, text="비밀번호 : ").grid(row=2, column=0, padx=10, pady=10, sticky= 'e')
ttk.Label(join, text="비밀번호 확인 : ").grid(row=3, column=0, padx=10, pady=10, sticky= 'e')
ent_name = ttk.Entry(join, textvariable=name)
ent_name.grid(row=0, column=1, padx=10, pady=10)
ent_id = ttk.Entry(join, textvariable=id)
ent_id.grid(row=1, column=1, padx=10, pady=10)
ent_pw = ttk.Entry(join, textvariable=pw, show="*")
ent_pw.grid(row=2, column=1, padx=10, pady=10)
ent_repw = ttk.Entry(join, textvariable=repw, show="*")
ent_repw.grid(row=3, column=1, padx=10, pady=10)

ttk.Button(join, text="등록", command=check_join).grid(row=4, column=0, padx=10, pady=10)
ttk.Button(join, text="취소", command=cancel).grid(row=4, column=2, padx=10, pady=10)

join.mainloop()