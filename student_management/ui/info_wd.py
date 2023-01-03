import tkinter.ttk
from student_management.dao.dao_student import StudentDao
from tkinter import *
from tkinter import messagebox
from student_management.vo.student_vo import Student
from student_management.util import ui_util as tool
# from student_management.ui.list_wd import ListWindow

class UserInfo:
  def __init__(self, std):
    print('std:', std)
    print('std.id', std.id)
    print('std.name', std.name)
    print('std.pw', std.pw)
    print('std.stdno', std.stdno)
    self.dao = StudentDao()  # 생성자로 초기화 안하면 메서드 사용못함.

    self.info = Tk()
    self.info.title("User Information")
    self.info.resizable(False, False)
    tool.center_win(self.info, 280, 250)

    self.name, self.id, self.pw, self.repw, self.stdno = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()


    tkinter.Label(self.info, text="User Information_std.no: "+std.stdno) \
      .grid(row=0, columnspan=3)

    Label(self.info, text="이름 : ", anchor=W) \
      .grid(row=1, column=0, padx=10, pady=10)
    Label(self.info, text="ID : ") \
      .grid(row=2, column=0, padx=10, pady=10)
    Label(self.info, text="비밀번호 : ") \
      .grid(row=3, column=0, padx=10, pady=10)
    Label(self.info, text="비밀번호 확인 : ") \
      .grid(row=4, column=0, padx=10, pady=10)

    self.ent_name = Entry(self.info, textvariable=self.name)
    self.ent_name.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    self.ent_name.insert(0, std.name)

    self.ent_id = Entry(self.info, textvariable=self.id)
    self.ent_id.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    self.ent_id.insert(0, std.id)
    self.ent_id.configure(state="readonly")

    self.ent_pw = Entry(self.info, textvariable=self.pw, show="*")
    self.ent_pw.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
    self.ent_pw.insert(0, std.pw)

    self.ent_repw = Entry(self.info, textvariable=self.repw, show="*")
    self.ent_repw.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    Button(self.info, text="수정", width=7, command=self.edit_check) \
      .grid(row=5, column=0, padx=5, pady=5, sticky='')
    Button(self.info, text="삭제", width=7, command=self.delete) \
      .grid(row=5, column=1, padx=5, pady=5, sticky='')
    Button(self.info, text="취소", width=7, command=self.cancel) \
      .grid(row=5, column=2, padx=5, pady=5, sticky='')

    self.ent_name.focus()
    self.info.mainloop()

  def edit_check(self):
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
      messagebox.showinfo("알림", "비밀번호를 다시한번 입력해주세요")
      self.ent_repw.focus()
      return

    if str(self.pw.get()) != str(self.repw.get()):
      messagebox.showinfo("알림", "비밀번호가 일치하지 않습니다.")
      self.ent_pw.setvar("");
      self.ent_repw.setvar("")
      self.ent_pw.focus()
      return
    tmp = f'{self.name.get()},{self.id.get()},{self.pw.get()},{self.stdno.get()}'
    print(tmp)
    std = Student.from_str(tmp)
    try:
      if self.dao.update_one(std) > 0:
        messagebox.showinfo("알림", "수정되었습니다.")
        self.name.set('');
        self.id.set('');
        self.pw.set('');
        self.repw.set('')
        self.stdno.set('')
        self.info.destroy()
      else:
        messagebox.showerror("알림", "수정에 실패하였습니다.")
        self.info.destroy()
    except Exception as e:
      print(e)

  def delete(self):
    if str(self.pw.get()) == "":
      messagebox.showinfo("알림", "비밀번호를 확인해주세요")
      self.ent_pw.focus()
      return
    if str(self.repw.get()) == "":
      messagebox.showinfo("알림", "비밀번호를 다시한번 입력해주세요")
      self.ent_repw.focus()
      return

    if str(self.pw.get()) != str(self.repw.get()):
      messagebox.showinfo("알림", "비밀번호가 일치하지 않습니다.")
      self.ent_pw.setvar("");
      self.ent_repw.setvar("")
      self.ent_pw.focus()
      return

    s = Student()
    s.id = self.id.get()
    s.pw = self.pw.get()
    result = self.dao.login_check(s)
    print(':::')
    if result == None:
      messagebox.showwarning("알림", "비밀번호가 일치하지 않아 삭제할수 없습니다.")
      self.pw.set('');
      self.ent_pw.focus()
    else:
      try:
        if self.dao.delete_one(s) > 0:
          messagebox.showinfo("알림", "삭제되었습니다.")
          self.name.set('');
          self.id.set('');
          self.pw.set('');
          self.repw.set('')
          self.stdno.set('')
          self.info.destroy()
        else:
          messagebox.showerror("알림", "삭제에 실패하였습니다.")
          self.info.destroy()
      except Exception as e:
        print(e)

  def cancel(self):
    self.info.destroy()
    # from student_management.controller import MainController
    # MainController.forwardingControl('Login')



