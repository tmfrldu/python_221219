import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from tkinter import *
from tkinter import messagebox
from student_management.vo.student_vo import Student
from student_management.util import ui_util as tool


class JoinWindow:
  def __init__(self):
    self.dao = StudentDao()  # 생성자로 초기화 안하면 메서드 사용못함.

    self.join = Tk()
    self.join.title("Student Regist")
    self.join.resizable(False, False)
    tool.center_win(self.join, 280, 250)

    self.name, self.id, self.pw, self.repw, self.stdno = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

    tkinter.Label(self.join, text="Student Join") \
      .grid(row=0, columnspan=2)

    Label(self.join, text="이름 : ", anchor=W) \
      .grid(row=1, column=0, padx=10, pady=10)
    Label(self.join, text="ID : ") \
      .grid(row=2, column=0, padx=10, pady=10)
    Label(self.join, text="비밀번호 : ") \
      .grid(row=3, column=0, padx=10, pady=10)
    Label(self.join, text="비밀번호 확인 : ") \
      .grid(row=4, column=0, padx=10, pady=10)

    self.ent_name = Entry(self.join, textvariable=self.name)
    self.ent_name.grid(row=1, column=1, padx=10, pady=10)

    self.ent_id = Entry(self.join, textvariable=self.id)
    self.ent_id.grid(row=2, column=1, padx=10, pady=10)

    self.ent_pw = Entry(self.join, textvariable=self.pw, show="*")
    self.ent_pw.grid(row=3, column=1, padx=10, pady=10)

    self.ent_repw = Entry(self.join, textvariable=self.repw, show="*")
    self.ent_repw.grid(row=4, column=1, padx=10, pady=10)

    Button(self.join, text="등록", width=10, command=self.check_join) \
      .grid(row=5, column=0, padx=10, pady=10, sticky=E)
    Button(self.join, text="취소", width=10, command=self.cancel) \
      .grid(row=5, column=1, padx=10, pady=10, sticky='')

    self.ent_name.focus()
    self.join.mainloop()

  def check_join(self):
    if str(self.name.get()) == "":
      messagebox.showinfo("알림", "이름을 확인해주세요")
      self.ent_name.focus()
      return
    if str(self.id.get()) == "":
      messagebox.showinfo("알림", "ID를 확인해주세요")
      self.ent_id.focus()
      return

    if str(self.pw.get()) == "":
      messagebox.showinfo("알림", "비밀번호를 확인해주세요")
      self.ent_pw.focus()
      return
    if str(self.repw.get()) == "":
      messagebox.showinfo("알림", "비밀번호 확인을 확인해주세요")
      self.ent_repw.focus()
      return

    if str(self.pw.get()) != str(self.repw.get()):
      messagebox.showinfo("알림", "비밀번호가 맞지 않습니다.")
      self.ent_pw.setvar("");
      self.ent_repw.setvar("")
      self.ent_pw.focus()
      return
    tmp = f'{self.name.get()},{self.id.get()},{self.pw.get()},{self.stdno.get()}'
    print(tmp)
    std = Student.from_str(tmp)
    try:
      if self.dao.insert_one(std) > 0:
        messagebox.showinfo("알림", "등록되었습니다.")
        self.name.set('');
        self.id.set('');
        self.pw.set('');
        self.repw.set('')
        self.join.destroy()
      else:
        messagebox.showerror("알림", "등록이 실패하였습니다.")
        self.join.destroy()
    except Exception as e:
      print(e)
  def cancel(self):
    self.join.destroy()
    # from student_management.controller import MainController
    # MainController.forwardingControl('Login')

