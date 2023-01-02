import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from student_management.util import ui_util as tool
from student_management.vo.student_vo import Student
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class JoinWindow:
  def __init__(self):
    self.dao = StudentDao()
    self.join = Tk()
    self.join.title("Student Regist")
    self.join.resizable(False, False)
    tool.center_win(self.join,280,250)

    self.id, self.pw, self.name, self.repw = StringVar(), StringVar(), StringVar(), StringVar()

    ttk.Label(self.join, text="이름 : ").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(self.join, text="ID : ").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(self.join, text="비밀번호 : ").grid(row=2, column=0, padx=10, pady=10, sticky='e')
    ttk.Label(self.join, text="비밀번호 확인 : ").grid(row=3, column=0, padx=10, pady=10, sticky='e')
    self.ent_name = ttk.Entry(self.join, textvariable=self.name)
    self.ent_name.grid(row=0, column=1, padx=10, pady=10)
    self.ent_id = ttk.Entry(self.join, textvariable=self.id)
    self.ent_id.grid(row=1, column=1, padx=10, pady=10)
    self.ent_pw = ttk.Entry(self.join, textvariable=self.pw, show="*")
    self.ent_pw.grid(row=2, column=1, padx=10, pady=10)
    self.ent_repw = ttk.Entry(self.join, textvariable=self.repw, show="*")
    self.ent_repw.grid(row=3, column=1, padx=10, pady=10)

    ttk.Button(self.join, text="등록", command=self.check_join).grid(row=4, column=0, padx=10, pady=10)
    ttk.Button(self.join, text="취소", command=self.cancel).grid(row=4, column=1, padx=10, pady=10)

    self.join.mainloop()


  def check_join(self):
    print(f'id: {self.id.get()}, pw: {self.pw.get()}, name: {self.name.get()}, repw: {self.repw.get()}')

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
      messagebox.showinfo("알림", "비밀번호를 다시 한번 입력해주세요")
      self.ent_repw.focus()
      return

    if str(self.pw.get()) != str(self.repw.get()):
      messagebox.showinfo("알림", "비밀번호가 일치하지 않습니다")
      self.ent_pw.focus()
      self.ent_pw.delete(0, 'end')
      self.ent_repw.delete(0, 'end')
      return

    tmp = f'{self.name.get()},{self.id.get()},{self.pw.get()}'
    print(tmp)
    std = Student.from_str(tmp)
    if self.dao.insert_one(std)>0 :
      messagebox.showinfo("알림", "등록되었습니다")
      self.name.set(''); self.id.set(''); self.pw.set(''); self.repw.set('')
      self.ent_name.focus()
    else:
      messagebox.showerror("알림", "등록이 실패하였습니다")


  def cancel(self):
    self.join.destroy()

# JoinWindow()